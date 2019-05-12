import base64
from datetime import datetime
from io import BytesIO
from PIL import Image
from server.socket import socketio

# process received frame
@socketio.on('frame')
def received_frame(url):
    url = url.replace('data:image/png;base64,', '')
    print(datetime.now(), 'Frame Received!')

    frame = Image.open(BytesIO(base64.b64decode(url)))

    # 여기서 프레임 처리
    
    frame = frame.convert('RGB') # get rid of alpha channel for JPEG format
    buffered = BytesIO()
    frame.save(buffered, format='JPEG')
    processed_url = base64.b64encode(buffered.getvalue())

    socketio.mit('processed', 'data:image/png;base64,' + str(processed_url.decode()))
