from apps import create_cms_app

cms_app = create_cms_app("apps.settings.DevConfig")


if __name__ == '__main__':
    with cms_app.app_context():
        from apps.models import db
        db.create_all()
    cms_app.run()