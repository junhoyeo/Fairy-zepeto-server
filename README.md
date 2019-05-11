# Fairy Server

## API

### 회원가입

### 로그인

### 사용자 정보

### zepeto rendering

#### `/render/{user_id}` 프로필

#### `/render/cover/{user_id}` 전신 이미지

### 소셜

#### 친구 추가

#### 친구 목록

## SocketIO

### 채팅

#### `client.emit('match', token)`
- 새로 connect 또는 셔플 시 사용

#### `client.on('paired')`
- 매칭됨
- 상대방 정보가 들어옴(_id 등등)

#### `client.emit('talk', {token, target, message})`
- target에게 메세지 전송

#### `client.on('received')`
- 메세지와 번역이 들어옴

#### `client.emit('question', {token})`
- 질문을 가져옴

#### `client.on('questioned')`
- 질문이 들어옴

#### `client.emit('answer', {token, answer})`
- 질문에 웅답

#### `client.on('opponent-answered')`
- 상대방의 응답이 들어옴

#### `client.on('clear')`
- 해당 질문이 끝남

#### `client.on('end-questions')`
- 질문하기가 끝남

### 프레임 처리

#### `client.emit('processed', 'data:image/png;base64,'`
- 프레임을 전송

#### `client.on('processed')`
- 처리된 프레임을 수신
