# import os


class Config(object):
    SERVICE_NAME = 'Fairy'

    JWT_TOKEN_LOCATION = 'headers'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE	= 'Bearer'
    MONGO_URI = ''


class DevConfig(Config):
    HOST = 'localhost'
    PORT = 5000
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017/test'
