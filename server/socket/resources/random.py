from server.socket import socketio

chats = [] # 현재 서버에 존재하는 chat 오브젝트
users = [] # 현재 서버에 존재하는 user 중 chat에 소속 x

@socketio.on('match')
def match(data): # 랜덤 매칭?
    pass # 일단 패스

    # 먼저 data에는, 사용자의 인증 정보(토큰)이 있음 -> 토큰이 유효한지 확인하고, 해당 토큰에서 제페토 아이디 같은 정보를 extract 해야 함
    # 유효하지 않으면 에러 던짐

    # 그 다음에는 해당 사용자가 채팅 중인지(chats에 있는지) 확인함
    # 채팅 중이면 상대가 싫다던가 해서 다시 매칭하려는 거니까 chats에서 users로 옮김
    
    # chats에 없으면 users에 추가해준다 (이미 users에 있으면 상관없겠지)

    # users가 업데이트될 때마다 update_users 같은 걸 실행해주자
    # update_users는 users에서 최대한 많이 랜덤 짝을 만들어서 걔네한테 이벤트를 emit해준다.
    # 일단 여기까지 해봐야겠어!
