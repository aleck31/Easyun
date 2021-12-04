# -*- coding: UTF-8 -*-
import os
import base64
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from easyun import db


class User(db.Model):
    """
    Create a User table
    """
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(60), unique=True)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def __init__(self, username=None, password=None, email=None, token=None, token_expiration=None):
        self.username = username
        if password is not None:
            self.password_hash = generate_password_hash(password)
        self.email = email
        self.token = token
        self.token_expiration = token_expiration

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
        return (self.id)

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data and data[field]:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=7200):  #设置 2 小时过期
        utcnow = datetime.utcnow()
        if self.token and self.token_expiration > utcnow + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = utcnow + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user



class Account(db.Model):
    """
    Create a Account table
    """
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True) 
    cloud = db.Column(db.String(10), primary_key=True)     # AWS
    account_id = db.Column(db.String(20), nullable=False, unique=True)  # e.g. 567820214060
    role = db.Column(db.String(100), nullable=False)       # e.g easyun-service-control-role    
    type = db.Column(db.String(10))        # Global / GCR
    atvdate = db.Column(db.Date)           # Account Activation date
    remind = db.Column(db.Boolean) 

    def get_role(self):
        return (self.role)

    def get_days(self):
        now = datetime.now()
        nowday = datetime.date(now)
        days =  nowday - self.atvdate
        return days


class Datacenter(db.Model):
    """
    Create a Account table
    """
    __tablename__ = 'datacenter'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)    # Datacenter Name: Easyun
    cloud = db.Column(db.String(20), nullable=False)                # Cloud Provider: AWS
    account_id = db.Column(db.String(30), nullable=False)           # Account ID
    region = db.Column(db.String(120))          # Deployed Region
    vpc_id = db.Column(db.String(30))           # VPC ID 
    credate = db.Column(db.Date)                # Datacenter Create date

    def get_region(self):
        return (self.region)