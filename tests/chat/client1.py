import socketio
from test import user1

print('CLIENT:', user1['name'])
user1_token = user1['token']

sio = socketio.Client()
sio.connect('http://localhost:5000')
sio.emit('match', user1_token)

@sio.on('paired')
def paired(data):
    target = data['_id']
    message = '안녕'
    chat = {
        'token': user1_token,
        'target': target,
        'message': message
    }
    print('SEND:', chat)
    sio.emit('talk', chat)

    sio.emit('question', { 'token': user1_token })
    sio.emit('answer', { 'token': user1_token, 'answer': 'asdf' })

@sio.on('questioned')
def questioned(data):
    print('Q:', data)
