from flask_restplus import Resource
from server.namespaces.user import user_ns
from server.namespaces.user.models import user_form_model

from functools import wraps
# import validators
from flask import jsonify, request
from server import mongo
from server.namespaces import hash_password

def location_validator(location):
    if location in ['korea', 'english']:
        return True
    return False

@user_ns.route('/register')
class Register(Resource):
    @user_ns.expect(user_form_model, validate=True)
    @user_ns.doc(
        responses={200: '성공', 400: '잘못된 요청', 500: 'Unacknowledged'},
        description='*사용자 이름, 비밀번호, 제페토 ID, 국적*을 받아 새로운 사용자를 추가합니다.')
    @user_ns.validate('location', location_validator)
    def post(self):
        user = user_ns.payload
        user['password'] = hash_password(user['password'])
        result = mongo.db.users.insert_one(user)
        if not result.acknowledged:
            return {}, 500
        return {}, 200
