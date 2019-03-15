from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    is_status = db.Column(db.Integer, default=1)

    def set_attrs(self, formdata: dict):
        for k, v in formdata.items():
            if hasattr(self, k):
                setattr(self, k, v)


from . import auth_model
