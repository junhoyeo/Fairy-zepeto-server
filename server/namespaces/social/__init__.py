from flask_restplus import Namespace
from server.namespaces import extend_namespace

social_ns = Namespace('social', description='**[SOCIAL]** 사용자 간 커뮤니케이션')
extend_namespace(social_ns)

social_ns.add_resources('add_friend', 'friends')
