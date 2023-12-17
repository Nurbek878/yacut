import os
import string

CHARACTERS = string.ascii_letters + string.digits
LOCAL_URL = 'http://localhost/'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')