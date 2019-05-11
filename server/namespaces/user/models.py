from flask_restplus import Namespace, Resource, fields
from server.namespaces.user import user_ns

user_model = user_ns.model('UserModel', {
    '_id': fields.String(),
    'email': fields.String(),
    'name': fields.String(),
    'password': fields.String()
})

user_form_model = user_ns.model('UserFormModel', {
    'email': fields.String(required=True, min_length=1),
    'name': fields.String(required=True, min_length=1),
    'password': fields.String(required=True, min_length=1)
})
