import base64
import hashlib
import types
from functools import wraps
from flask_restplus import Api


def extend_namespace(ns):
    def add_resources(ns, *resources):
        for resource in resources:
            __import__(
                'server.namespaces.{}.resources.{}'.format(
                    ns.name, resource))
    ns.add_resources = types.MethodType(add_resources, ns)

    def validate(ns, key, validator):
        def real_decorator(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                if not validator(ns.payload[key]):
                    return { 'message': "'{}' field validation failed".format(key) }, 400
                return function(*args, **kwargs)
            return wrapper
        return real_decorator
    ns.validate = types.MethodType(validate, ns)

def hash_password(password):
    return base64.b64encode(hashlib.sha512(
        password.encode('UTF-8')
    ).digest()).decode()


api = Api(
    title='Fairy',
    version='1.0',
    description='Powered by JFlask; Video and Chat server is running separately with Socket.IO',
)

from server.namespaces.test import test_ns
api.add_namespace(test_ns, path='/test')

from server.namespaces.user import user_ns
api.add_namespace(user_ns, path='/user')

from server.namespaces.auth import auth_ns
api.add_namespace(auth_ns, path='/auth')

from server.namespaces.render import render_ns
api.add_namespace(render_ns, path='/render')

from server.namespaces.social import social_ns
api.add_namespace(social_ns, path='/social')
