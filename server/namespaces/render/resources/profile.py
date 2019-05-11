from flask_restplus import Resource
from server.namespaces.render import render_ns


@render_ns.route('/<string:user_id>')
class Profile(Resource):
    @render_ns.doc(description='`user_id`를 가지는 얼굴이 제대로 드러나는 랜덤 포즈를 가지는 프로필 이미지를 반환합니다.')
    def get(self, user_id):
        return {
            'render': True
        }
