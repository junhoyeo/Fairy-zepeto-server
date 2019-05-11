from flask_restplus import Namespace
from server.namespaces import extend_namespace

render_ns = Namespace('render', description='[ZEPETO] 사용자 ID를 받아서 제페토 이미지를 렌더링합니다.')
extend_namespace(render_ns)

render_ns.add_resources('profile', 'front_face')
