class DevConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/flask_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False