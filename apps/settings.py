import os
from redis import Redis


def get_db_dir():
    path = os.path.dirname(os.path.dirname(__name__))
    return "sqlite:///{}/elm.db".format(path)


class DevConfig:
    DEBUG = True
    SECRET_KEY = 'a123b'
    # 相对于当前文件找绝对路径
    # SQLALCHEMY_DATABASE_URI = get_db_dir()
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/flask_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis(host="127.0.0.1",port=6379)
    SECRET_KEY_PREFIX = "hl"
