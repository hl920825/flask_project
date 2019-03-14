from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer,primary_key=True)
    is_status = db.Column(db.Integer,default=1)

from . import auth_model