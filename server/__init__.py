from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
import os

from config import DevConfig


def create_app():
    _app = Flask(__name__)

    CORS().init_app(_app)
    JWTManager().init_app(_app)
    # _app.secret_key = os.urandom(24)
    _app.secret_key = 'JunctionX-seoul' # 서버 디버깅 중 restart 되어도 토큰 expire 되지 않게
    _app.config.from_object(DevConfig)
    return _app


app = create_app()
mongo = PyMongo(app)

from server.namespaces import api
api.init_app(app)

socketio = SocketIO(app)
__import__('server.socket')
