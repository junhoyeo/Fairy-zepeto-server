API_HOST = '47.74.149.35/api'

# profile
PROFILE_PHOTOBOOTH = '14H8320f7MYeqkg0UEwmGY'  # PHOTOBOOTH_ONE_87

# covers (random)
COVER_PHOTOBOOTHS = [
    'cGEJcQ325qOOkMsw2O4AS', # PHOTOBOOTH_ONE_1
    '2AAEVYUeIEewoSkqca2aaI', # PHOTOBOOTH_ONE_10
    '1mKwRiuLbK6GMumWymSCoa', # PHOTOBOOTH_ONE_29
    '5h2Tk9uJ0WoGg0A2aIwkQK', # PHOTOBOOTH_ONE_30
    '7MYgiC1IJ4UMxQQ0kH4xjI', # PHOTOBOOTH_ONE_136
    'G77gAt3eTYko1VvfON9Ra' # PHOTOBOOTH_ONE_210
]

def build_query_url(photobooth_id, zepeto_id):
    return f'http://{API_HOST}/photo/{photobooth_id}/?width=500&hashCodes={zepeto_id}'

from server.utils.profile import get_zepeto_profile
from server.utils.cover import get_zepeto_cover
