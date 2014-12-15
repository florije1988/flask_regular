# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import db
from wtforms.validators import Email
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class UserModel(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class TodoModel(BaseModel):
    __tablename__ = 'tasks'

    title = db.Column(db.String(length=20), default='')
    # user_id = db.Column(db.Integer, nullable=True)
    content = db.Column(db.String(length=50), default='')

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Task title is %r, content is %r>' % (self.title, self.content)