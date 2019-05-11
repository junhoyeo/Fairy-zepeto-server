from flask import send_file
from flask_restplus import Resource
from server.namespaces.render import render_ns
from server.utils import get_zepeto_profile


@render_ns.route('/<string:user_id>')
class Profile(Resource):
    @render_ns.doc(description='`user_id`를 가지는 얼굴이 제대로 드러나는 ~~랜덤 포즈를 가지는~~ 프로필 이미지를 반환합니다. 랜덤포즈 할지 말진 잘 모르겠음.')
    @render_ns.produces(['image/png'])
    def get(self, user_id):
        filename = get_zepeto_profile(user_id, f'server/static/profiles/{user_id}.png')
        # print(filename)
        return send_file(filename)
