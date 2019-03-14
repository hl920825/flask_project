from flask import Flask

def register_cms_bp(app:Flask):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


def register_db(app:Flask):
    from apps.models import db
    db.init_app(app)

def create_cms_app(config_str:str):
    app = Flask(__name__)
    app.config.from_object(config_str)
    register_db(app)
    register_cms_bp(app)
    return app