from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from server.namespaces.auth import auth_ns
from server.namespaces.auth.models import auth_form_model, auth_token_model
from server import mongo


@auth_ns.route('/test')
@auth_ns.header('Authorization', 'JWT Token (with Bearer)', required=True)
@auth_ns.param('Authorization', 'JWT Token (with Bearer)', 'header')
class AuthTest(Resource):
    @jwt_required
    def get(self):
        return {
            'test': True
        }
