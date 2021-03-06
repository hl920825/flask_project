from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from apps.models import db,BaseModel


class Auth(BaseModel,UserMixin):
    username = db.Column(db.String(16),unique=True,index=True)
    _password = db.Column('password',db.String(128),nullable=False)
    # password = db.Column(db.String(128),nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        self._password = generate_password_hash(value)

    def check_password(self,user_pwd):
        return check_password_hash(self._password,user_pwd)

