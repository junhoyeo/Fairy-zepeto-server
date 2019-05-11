import requests
from PIL import Image

API_HOST = '47.74.149.35/api'
PHOTOBOOTH_ID = '14H8320f7MYeqkg0UEwmGY'  # PHOTOBOOTH_ONE_87

URL = f'http://{API_HOST}/photo/{PHOTOBOOTH_ID}/?width=500&hashCodes='

def get_zepeto(user_id, filename, crop_pos=None):
    res = requests.get(URL + user_id)
    if res.status_code == 200:
        with open(filename, 'wb') as mask_file:
            for chunk in res:
                mask_file.write(chunk)

    face = Image.open(filename)

    if crop_pos:
        # crop_pos는 (left, top, right, bottom) 형식의 turple; 자를 위치 알려줌
        # PHOTOBOOTH_ONE_87에서 정면 얼굴만 잘린 마스크면 (125, 20, 375, 305)를 줘야함
        # 인수 안 들어오면 안 자름
        face = original.crop(face)
    face.save(filename)
    return filename.replace('server/', '')
