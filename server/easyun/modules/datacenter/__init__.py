# -*- coding: utf-8 -*-
"""The Datacenter creation module."""
from apiflask import APIBlueprint, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from common.auth import auth_token
import boto3
import os

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('数据中心管理', __name__, url_prefix = ver) 

# 新建Datacenter
@bp.post('/initial')
@auth_token.login_required
@input({})
@output({}, 201, description='add A new Datacenter')
def add_datacenter(newdc):
    # create easyun vpc
    # create 2 x pub-subnet
    # create 2 x pri-subnet
    # create 1 x easyun-igw (internet gateway)
    # create 1 x easyun-nat (nat gateway)
    # create 1 x easyun-route-igw
    # create 1 x easyun-route-nat
    # create 3 x easyun-sg-xxx
    # create 1 x key-easyun-user (默认keypair)

    # test added by peng 123
    # test added by peng 234
    #
    return '' #status: successful


# 获取当前Datacenter环境信息
@bp.get('/datacenter')
@auth_token.login_required
@input({})
@output({}, 201, description='Datacenter info')
def get_vpc():
    # get vpc info
    # get subnet info
    # get securitygroup info
    # get keypair info
    return '' #datacenter id
