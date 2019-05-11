from flask_restplus import Resource
from server.namespaces.render import render_ns


@render_ns.route('/<string:user_id>/front')
class FontFace(Resource):
    @render_ns.doc(description='`user_id`를 가지는 사용자 제페토의 면상 정면을 반환합니다.')
    def get(self, zepeto_id):
        return {
            'render': True
        }
