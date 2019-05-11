from flask_restplus import Resource
from server.namespaces.user import user_ns
from server.namespaces.user.models import user_model

from flask import jsonify, request
from server import mongo


@user_ns.route('/all')
class UserAll(Resource):
    @user_ns.marshal_list_with(user_model)
    @user_ns.doc(description='전체 사용자 목록을 가져옵니다(페이징).')
    def get(self):
        limit = request.args.get('limit', 100, type=int)
        skip = request.args.get('skip', 0, type=int)
        # cursor = mongo.db.users.find().limit(limit).skip(skip)
        # return list(cursor)
        cursor = mongo.db.users.find().limit(limit).skip(skip)
        users = list(cursor)
        for idx, user in enumerate(users):
            users[idx]['_id'] = str(user['_id'])
        return users
