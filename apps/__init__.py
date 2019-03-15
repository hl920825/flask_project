from flask import Flask


def register_cms_bp(app: Flask):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


def register_db(app: Flask):
    from apps.models import db
    db.init_app(app)


def init_session(app: Flask):
    from flask_session import Session
    Session(app)


def init_login_manager(app: Flask):
    from apps.tools.login_tools import login_manager
    login_manager.init_app(app)


def create_cms_app(config_str: str):
    app = Flask(__name__)
    app.config.from_object(config_str)
    init_session(app)
    register_db(app)
    init_login_manager(app)
    register_cms_bp(app)
    return app
