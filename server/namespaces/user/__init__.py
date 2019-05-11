from flask_restplus import Namespace
from server.namespaces import extend_namespace

user_ns = Namespace('user', description='[DEFAULT] User resources')
extend_namespace(user_ns)

user_ns.add_resources('user', 'user_all', 'register')
