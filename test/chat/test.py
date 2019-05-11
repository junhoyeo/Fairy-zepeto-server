import json
import requests

def get_token(user):
    res = requests.post('http://localhost:5000/auth/', json=user)
    return json.loads(res.text)['token']

user1 = {
    'name': 'junhoyeo0704',
    'password': '2019seoul'
}

user1['token'] = get_token(user1)

user2 = {
    'name': 'string',
    'password': 'string'
}

user2['token'] = get_token(user2) 
# 얘는 쿼리 보내기 귀찮아서 이름이랑 패스워드를 string으로 지은 것임
