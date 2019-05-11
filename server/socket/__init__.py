from server import socketio

resources = [
    'process_frame' # 영상 처리
]
for resource in resources:
    __import__('server.socket.resources.{}'.format(resource))
