# -*- coding: UTF-8 -*-
import os
import base64
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from easyun import db

class Users(db.Model):
    """
    Create a User table
    """
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    email = db.Column(db.String(60), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def __init__(self, username, password, token, token_expiration, email=None):
        self.username = username
        if password is not None:
            self.password_hash = generate_password_hash(password)
        self.token = token
        self.token_expiration = token_expiration
        self.email = email

    def set_password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.user_id)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = Users.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user        