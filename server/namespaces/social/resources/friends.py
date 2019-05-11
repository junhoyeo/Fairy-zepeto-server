from flask_restplus import Resource
from server.namespaces.social import social_ns
from server.namespaces.user.models import user_model

from bson import ObjectId
from server import mongo

@social_ns.route('/friends/<ObjectId:user_id>')
class AddFriend(Resource):
    @social_ns.marshal_list_with(user_model)
    @social_ns.doc(description='`user_id`를 가지는 사용자의 친구 목록을 구합니다.')
    def get(self, user_id):
        friend_list = []
        user = mongo.db.users.find_one_or_404({'_id': user_id})
        user['_id'] = str(user['_id'])
        friends = user['friends']
        for friend_id in friends:
            friend = mongo.db.users.find_one_or_404({'_id': friend_id})
            friend['_id'] = str(friend['_id'])
            friend_list.append(friend)
        return friend_list
