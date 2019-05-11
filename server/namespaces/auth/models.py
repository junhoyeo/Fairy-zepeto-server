from flask_restplus import Namespace, Resource, fields
from server.namespaces.auth import auth_ns

auth_form_model = auth_ns.model('AuthFormModel', {
    'name': fields.String(required=True, min_length=1),
    'password': fields.String(required=True, min_length=1)
})

auth_token_model = auth_ns.model('AuthTokenModel', {
    'token': fields.String(),
    'refresh_token': fields.String(),
})
