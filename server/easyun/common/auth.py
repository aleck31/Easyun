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
from .models import Users
from .errors import error_response

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('用户认证', __name__, url_prefix = ver) 

auth_basic = HTTPBasicAuth()
auth_token = HTTPTokenAuth(scheme='Bearer')


class UserInSchema(Schema):
    username = String(required=True, validate=Length(0, 10))
    password = String(required=True, validate=Length(0, 20))

class UserOutSchema(Schema):
    id = Integer()
    username = String()
    password = String()
    
def set_password(self, password):
    # Set password to a hashed password
    self.password_hash = generate_password_hash(password)

def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

@auth_basic.verify_password
def verify_password(user_name, password):
    user = Users.query.filter_by(user_name=user_name).first()
    if user and user.verify_password(password):
        return user

@auth_basic.error_handler
def basic_auth_error(status):
    return error_response(status)


@auth_token.verify_token
def verify_token(token):
    return Users.check_token(token) if token else None
    if token in tokens:
        return tokens[token]


@bp.post('/auth/')
@auth_basic.login_required
@input(UserInSchema)
def get_token():
    token = auth_basic.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})


@bp.delete('/logout/<int:user_id>')
@input(UserInSchema)
@auth_token.login_required
def revoke_token():
    # Headers
    # Token Bearer Authorization
    #     token    
    auth_token.current_user().revoke_token()
    db.session.commit()
    return '', 204