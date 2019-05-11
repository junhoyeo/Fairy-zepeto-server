from flask_restplus import Resource
from server.namespaces.social import social_ns

from bson import ObjectId
from server import mongo

@social_ns.route('/friends/<ObjectId:user_id>/add/<ObjectId:friend_id>')
class AddFriend(Resource):
    @social_ns.doc(description='`user_id`를 가지는 사용자가 `friend_id`의 사용자를 친구에 추가합니다.')
    def get(self, user_id, friend_id):
        user = mongo.db.users.find_one_or_404({'_id': user_id})
        user['_id'] = str(user['_id'])
        user['friends'].append(friend_id)
        mongo.db.users.update_one({ '_id': user_id }, {
          '$set': { 'friends': user['friends'] }
        })
        return {}, 200
