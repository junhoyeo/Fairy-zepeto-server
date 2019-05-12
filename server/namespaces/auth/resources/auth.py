from flask import request
from flask_restplus import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from server.namespaces import hash_password
from server.namespaces.auth import auth_ns
from server.namespaces.auth.models import auth_form_model, auth_token_model
from server import mongo


@auth_ns.route('/')
class Auth(Resource):
    # @auth_ns.marshal_with(auth_token_model)
    @auth_ns.expect(auth_form_model, validate=True)
    @auth_ns.doc(description='검증 후 사용자 토큰 생성(로그인)')
    def post(self):
        user = mongo.db.users.find_one_or_404({
            'name': auth_ns.payload['name'],
            'password': hash_password(auth_ns.payload['password'])
        })
        user['_id'] = str(user['_id'])
        for idx, friend in enumerate(user['friends']):
            user['friends'][idx] = str(friend)
        print(user)
        token = create_access_token(identity=str(user['_id']))
        refresh_token = create_refresh_token(identity=str(user['_id']))
        return {
            'user': user,
            'token': token,
            'refresh_token': refresh_token
        }
