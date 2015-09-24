from zoo.core import db

from ..wrappers import BaseModel


class UserDb(BaseModel):
    __tablename__ = 'users'
    __json_hidden = ['password']

    name = db.Column(db.String(70))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(70))
