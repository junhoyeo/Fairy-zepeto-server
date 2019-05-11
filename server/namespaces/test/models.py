from flask_restplus import Namespace, Resource, fields
from server.namespaces.test import test_ns

test_get_model = test_ns.model('TestGetModel', {
    'test': fields.Boolean(required=True)
})

test_post_model = test_ns.model('TestPostModel', {
    'test': fields.Boolean(required=True),
    'query': fields.String(required=True)
})

test_form_model = test_ns.model('TestFormModel', {
    'query': fields.String(required=True)
})
