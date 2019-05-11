from server.socket import socketio
from flask_jwt_extended import decode_token

CHATS = [] # 현재 서버에 존재하는 chat 오브젝트
USERS = [] # 현재 서버에 존재하는 user 중 chat에 소속 x -> user _id로 구성

chat_object = {
    'users': [], # user _id
    'qustions': [] # 나왔던 질문 id?
} # copy this to use

def update_users():
    print(CHATS, USERS)

@socketio.on('match')
def match(token): # 랜덤 매칭?
    print(CHATS, USERS)
    # 먼저 data에는, 사용자의 인증 정보(토큰)이 있음 -> 토큰이 유효한지 확인하고, 해당 토큰에서 제페토 아이디 같은 정보를 extract 해야 함
    # 유효하지 않으면 에러 던짐
    # 이거 일단 나중에 생각

    identity = decode_token(token) # 유효하지 않다면 여기서 에러 뜸
    user_id = identity['identity'] # 사용자 id를 토큰을 통해 구함

    # 그 다음에는 해당 사용자가 채팅 중인지(chats에 있는지) 확인함
    for idx, chat in enumerate(CHATS):
        if user_id in chat.users: 
            # 채팅 중이면 상대가 싫다던가 해서 다시 매칭하려는 거니까 chats에서 users로 옮김
            users_to_move = chat.users
            del CHATS[idx] # chat을 지우고
            for user in users_to_move:
                USERS.append(user)
            break
    
    # chats에 없으면 users에 추가해준다 (이미 users에 있으면 상관없겠지)
    if user_id not in USERS:
        USERS.append(user_id)

    # users가 업데이트될 때마다 update_users 같은 걸 실행해주자
    update_users()
    # update_users는 users에서 최대한 많이 랜덤 짝을 만들어서 걔네한테 이벤트를 emit해준다.
    # 일단 여기까지 해봐야겠어!
