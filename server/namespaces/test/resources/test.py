from flask_restplus import Resource
from server.namespaces.test import test_ns
from server.namespaces.test.models import *


@test_ns.route('/')
class Test(Resource):
    @test_ns.marshal_with(test_get_model)
    @test_ns.doc(description='GET 메소드를 테스트하기 위한 리소스입니다.')
    def get(self):
        return {
            'test': True
        }

    @test_ns.expect(test_form_model, validate=True)
    @test_ns.marshal_with(test_post_model)
    @test_ns.doc(
        responses={200: '성공', 400: '`query` 없음'},
        description='POST 메소드를 테스트하기 위한 리소스입니다. JSON으로 `query`를 받아 다시 반환합니다.')
    def post(self):
        return {
            'test': True,
            'query': test_ns.payload['query']
        }
