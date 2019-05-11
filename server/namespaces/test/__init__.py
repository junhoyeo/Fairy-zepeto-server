from flask_restplus import Namespace
from server.namespaces import extend_namespace

test_ns = Namespace('test', description='[DEFAULT] API test')
extend_namespace(test_ns)

test_ns.add_resources('test')
