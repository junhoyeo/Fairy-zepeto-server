import socketio
from test import user2

print('CLIENT:', user2['name'])
user2_token = user2['token']

sio = socketio.Client()
sio.connect('http://localhost:5000')
sio.emit('match', user2_token)

@sio.on('paired')
def paired(data):
    print(data)

@sio.on('received')
def received(data):
    print(data)

@sio.on('questioned')
def questioned(data):
    print('Q:', data)

@sio.on('opponent-answered')
def other_answered(data):
    print('client1:', data)
