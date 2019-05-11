import random
from bson import ObjectId
from server import mongo
from server.socket import socketio
# from flask import request
from flask_jwt_extended import decode_token

CHATS = [] # 현재 서버에 존재하는 chat 오브젝트
USERS = [] # 현재 서버에 존재하는 user 중 chat에 소속 x -> user _id로 구성

# chat_object = {
#     'users': [], # user _id
#     'qustions': [] # 나왔던 질문 id?
# }

def update_users():
    global CHATS, USERS
    if len(USERS) >= 2: # 2명 이상이라 매칭 가능
        pairs = []
        # print(USERS)
        for pair in range(len(USERS) // 2):
            pairs.append([
                USERS.pop(random.randrange(len(USERS))), 
                USERS.pop(random.randrange(len(USERS)))
            ])
        # print(pairs)
        # 최대한 랜덤으로 짝을 만들어 CHAT을 생성한다.

        for pair in pairs:
            chat = { 'users': [] } # 새로운 chat 오브젝트 (하나의 room으로 고쳐야 함)
            for idx, user in enumerate(pair):
                # chat에 짝의 각 사람들을 추가하고 
                chat['users'].append(user)
                # 그 다음에 각각의 사람들에게 emit함
                # NOTE: 처음에 match할때 자기 id로 된 room에 join시킴. 개인 룸임.

                # paired를 보내고 다른 사용자 id (pair[int(not idx)])에 해당하는 유저의 정보를 보낸다.
                # 다른 사용자의 정보에는 _id, username, zepeto_id, 국적

                # NOTE: 제페토 프사는 zepeto_id 가지고 프엔이 알아서 쿼리하셈!!!
                other_user = mongo.db.users.find_one({'_id': ObjectId(pair[int(not idx)])})
                other_user['_id'] = str(other_user['_id'])
                other_user.pop('password', None) # 해싱된 패스워드는 양심적으로 빼서 보내야겠다.
                print(other_user)

                socketio.emit('paired', other_user, room=user) # 해당 유저에게 상대방 정보를 보낸다.

            CHATS.append(chat) # 채팅방 목록에 추가
        print('after update:', CHATS, USERS)
    else:
        print('not enough users')

@socketio.on('match')
def match(token): # 랜덤 매칭?
    global CHATS, USERS
    print('before match:', CHATS, USERS)
    # 먼저 data에는, 사용자의 인증 정보(토큰)이 있음 -> 토큰이 유효한지 확인하고, 해당 토큰에서 제페토 아이디 같은 정보를 extract 해야 함
    # 유효하지 않으면 에러 던짐
    # 이거 일단 나중에 생각

    identity = decode_token(token) # 유효하지 않다면 여기서 에러 뜸
    user_id = identity['identity'] # 사용자 id를 토큰을 통해 구함
    socketio.join_room(user_id) # 자기 id로 룸을 만든다.
    # FIXME: 이거 근데 이미 자기 room에 join한 상황에서 다시 실행되면 어캐되는거임?

    # 그 다음에는 해당 사용자가 채팅 중인지(chats에 있는지) 확인함
    for idx, chat in enumerate(CHATS):
        if user_id in chat['users']: 
            # 채팅 중이면 상대가 싫다던가 해서 다시 매칭하려는 거니까 chats에서 users로 옮김
            users_to_move = chat['users']
            del CHATS[idx] # chat을 지우고
            for user in users_to_move:
                USERS.append(user)
            break
    
    # chats에 없으면 users에 추가해준다 (이미 users에 있으면 상관없겠지)
    if user_id not in USERS:
        USERS.append(user_id)

    # users가 업데이트될 때마다 update_users 같은 걸 실행해주자
    print('before update:', CHATS, USERS)
    update_users()
    # update_users는 users에서 최대한 많이 랜덤 짝을 만들어서 걔네한테 이벤트를 emit해준다.

@socketio.on('talk')
def talk(data):
    # data = token, target, message
    token = data['token']
    identity = decode_token(token) # 유효하지 않다면 여기서 에러 뜸
    user_id = identity['identity'] # 사용자 id를 토큰을 통해 구함

    target = data['target'] # 메세지 수신자의 id
    message = data['message'] # 메세지 내용
    
    # target이라는 user_id로 message라는 데이터를 보내는 게 들어옴.
    # 그러면 target의 room으로 message 담은 received를 emit해주면 되겠지?
    socketio.emit('received', message, room=target) # 해당 유저에게 상대방 정보를 보낸다.
