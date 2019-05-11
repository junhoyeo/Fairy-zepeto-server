from flask_restplus import Namespace, Resource, fields
from server.namespaces.user import user_ns

# DB에 들어가는 모델
user_model = user_ns.model('UserModel', {
    '_id': fields.String(),
    # 'email': fields.String(),
    'name': fields.String(),
    'password': fields.String(),
    'zepeto_id': fields.String(),
    'location': fields.String(),
    'friends': fields.List(fields.String) # 친구 목록: 친구들의 _id (string)의 리스트
})

# 사용자가 입력하는 모델
user_form_model = user_ns.model('UserFormModel', {
    # 'email': fields.String(required=True, min_length=1),
    'name': fields.String(required=True, min_length=1),
    'password': fields.String(required=True, min_length=1),
    'zepeto_id': fields.String(required=True, min_length=5),
    'location': fields.String(required=True)
})
