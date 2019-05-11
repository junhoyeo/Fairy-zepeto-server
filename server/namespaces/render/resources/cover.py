from flask import send_file
from flask_restplus import Resource
from server.namespaces.render import render_ns
from server.utils import get_zepeto_cover


@render_ns.route('/cover/<string:user_id>')
class Cover(Resource):
    @render_ns.doc(description='`user_id`를 가지는 제페토 전신이 나오는 랜덤 포즈 이미지를 반환합니다.')
    @render_ns.produces(['image/png'])
    def get(self, user_id):
        filename = get_zepeto_cover(user_id, f'server/static/covers/{user_id}.png')        
        return send_file(filename)
