from server.socket import socketio

chats = [] # 현재 서버에 존재하는 chat 오브젝트
users = [] # 현재 서버에 존재하는 user 중 chat에 소속 x

@socketio.on('match')
def match(data): # 랜덤 매칭?
    pass
