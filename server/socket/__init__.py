from server import socketio

resources = [
    'process_frame', # 영상 처리
    'random' # 랜덤 채팅
]
for resource in resources:
    __import__('server.socket.resources.{}'.format(resource))
