# -*- coding: UTF-8 -*-
'''
@Description: The user auth module.
@LastEditors: 
'''
import functools
from flask import jsonify, g, redirect, request, session, url_for
from apiflask import APIBlueprint, HTTPTokenAuth, HTTPBasicAuth, Schema, input, output
from apiflask.validators import Length, OneOf
from apiflask.fields import String, Integer
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db
from .models import User
from .errors import error_response, bad_request

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('用户认证', __name__, url_prefix = ver) 

auth_basic = HTTPBasicAuth()
auth_token = HTTPTokenAuth(scheme='Bearer')


@auth_basic.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        return user

@auth_basic.error_handler
def basic_auth_error(status):
    return error_response(status)


@auth_token.verify_token
def verify_token(token):
    return User.check_token(token) if token else None
    if token in tokens:
        return tokens[token]

@auth_token.error_handler
def token_auth_error(status):
    return error_response(status)


class NewInSchema(Schema):
    username = String(required=True, validate=Length(0, 10))
    password = String(required=True, validate=Length(0, 20))
    email = String(required=True, validate=Length(0, 20))

class UserInSchema(Schema):
    username = String(required=True, validate=Length(0, 10))
    password = String(required=True, validate=Length(0, 20))

class UserOutSchema(Schema):
    id = Integer()
    username = String()
    email = String()


@bp.post('/adduser')
@input(NewInSchema)
@output(UserOutSchema, 201, description='add A new user')
def add_user(newuser):
    if 'username' not in newuser or 'password' not in newuser:
        return bad_request('must include username and password fields')
    if User.query.filter_by(username=newuser['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=newuser['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(newuser, new_user=True)
    db.session.add(user)
    db.session.commit()
    return user.username


@bp.get('/token')
@auth_basic.login_required
@input(UserInSchema)
def get_auth_token():
    token = auth_basic.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})


@bp.delete('/logout/<username>')
@auth_token.login_required
def revoke_auth_token():
    # Headers
    # Token Bearer Authorization
    #     token    
    auth_token.current_user().revoke_token()
    db.session.commit()
    return '', 204