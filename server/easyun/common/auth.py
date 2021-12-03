# -*- coding: UTF-8 -*-
'''
@Description: The user auth module.
@LastEditors: 
'''
from flask import jsonify, make_response
from apiflask import APIBlueprint, HTTPTokenAuth, HTTPBasicAuth, auth_required, Schema, input, output, doc
from apiflask.validators import Length, OneOf
from apiflask.fields import String, Integer
from .. import db
from .models import User
from .result import make_resp, error_resp, bad_request

# define api version
ver = '/api/v1'

bp = APIBlueprint('用户认证', __name__, url_prefix = ver+'/user') 

auth_basic = HTTPBasicAuth()
auth_token = HTTPTokenAuth(scheme='Bearer')


@auth_basic.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        return user

@auth_basic.error_handler
def basic_auth_error(status):
    return error_resp(status)

@auth_token.verify_token
def verify_token(token):
    return User.check_token(token) if token else None
    if token in tokens:
        return tokens[token]

@auth_token.error_handler
def token_auth_error(status):
    return error_resp(status)


class UserInSchema(Schema):
    username = String(required=True, validate=Length(0, 20))
    password = String(required=True, validate=Length(0, 30))

class UserOutSchema(Schema):
    id = Integer()
    username = String()
    email = String()

class NewUser(Schema):
    username = String(required=True, validate=Length(0, 20))
    password = String(required=True, validate=Length(0, 30))
    email = String(required=True, validate=Length(0, 80))


@bp.post('/adduser')
@input(NewUser)
@output(UserOutSchema, 201)
@doc(tag='【仅限测试用】', operation_id='Add New User')
def add_user(newuser):
    '''向数据库添加新用户'''
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
    return make_resp("Add a new user.", 201, user)


class NewPassword(Schema):
    password = String(required=True, validate=Length(0, 20))

@bp.put('/change_password')
@auth_required(auth_token)
@input(NewPassword)
@output({}, 204, description='Password changed.')
def change_passowrd(newpwd):
    '''修改当前用户密码'''
    auth_token.current_user.set_password(newpwd['password'])
    db.session.commit()
    return ''


class TokenOutSchema(Schema):
    api_code = Integer()
    api_msg = String()
    token = String()


@bp.post('/auth')
@input(UserInSchema)
def post_auth_token(user):
    '''用户登录 (auth_token，Post方法获取token)'''
    if 'username' not in user or 'password' not in user:
        return bad_request('must include username and password fields')
    inname = user["username"]
    inpwd = user['password']
    login_user = User.query.filter_by(username=inname).first()
    if login_user and login_user.verify_password(inpwd):
        # token = auth_token.current_user.get_token()
        token = login_user.get_token()
        db.session.commit()
        return make_resp('Success', 200, {'token': token}) ,201
        # jsonify({'token': token})
    else:
        return error_resp(401)


@bp.get('/token')
@auth_required(auth_basic)
@doc(tag='【仅限测试用】', operation_id='Get token')
def get_auth_token():
    '''基于auth_basic, Get方法获取token'''
    token = auth_basic.current_user.get_token()
    db.session.commit()
    # return jsonify({'token': token})
    return make_resp('Success', 200, {'token': token})


@bp.delete('/logout')
@auth_required(auth_token)
@output({}, 204, description='Current user logout')
def revoke_auth_token():
    '''注销当前用户 (撤销token)'''
    # Headers
    # Token Bearer Authorization
    #     token    
    auth_token.current_user.revoke_token()
    db.session.commit()
    return ''