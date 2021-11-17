# -*- coding: utf-8 -*-
"""The Server management module."""
from apiflask import APIBlueprint, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask import jsonify
from easyun.common.auth import auth_token
import boto3
import os

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('服务器管理', __name__, url_prefix = ver) 

# 定义创建 instance 的参数
# 可以通过cli获取参数及值域参考： aws ec2 describe-instances
# AMI = os.environ['AMI']
# INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
# KEY_NAME = os.environ['KEY_NAME']
# SUBNET_ID = os.environ['SUBNET_ID']
TAG_SPEC = [
        {
        "ResourceType":"instance",
        "Tags": [
                {
                    "Key": "Flag",
                    "Value": "Easyun"
                }
            ]
    }
    ]


class InstanceIn(Schema):
    svrname = String(required=True, validate=Length(0, 20))     #云服务器名称
    svrnum = Integer(requir1=True)                              #新建云服务器数量
    image_id = String(required=True, validate=Length(0, 20))         #ImageId
    ins_type = String(required=True, validate=OneOf(['t3', 'g4', 'm5']))    #INSTANCE_TYPE
    subnet_id = String(required=True) 
    sg_id = String(required=True ) 
    keypair = String(required=True)
    tags = list()


class InstanceOut(Schema):
    ami_id = Integer()
    instance_type = String()
    subnet_id = String()
    ssubnet_id = String()
    key_name = String()
    category = String()


# 新增server
@bp.post('/server')
@auth_token.login_required
@input(InstanceIn)
@output(InstanceOut, 201, description='add A new server')
def add_server(newsvr):
    ec2 = boto3.resource('ec2')
    server = ec2.create_instance(
    ImageID="ami-0447addf6c74624eb",
    InstanceType="t4g.micro",
    SubnetID="subnet-06bfe659f6ecc2eed",
    KeyName="key_easyun_dev",
    SecurityGroupIds=[
        'sg-1f39854x',
    ],
    MaxCount=1,
    MinCount=1,    
    TagSpecifications = TAG_SPEC
    )
    return server[0].id 


# 删除指定server
@bp.delete('/server/<svr_ids>')
@auth_token.login_required
@output({}, 204)
def del_svr(svr_ids):
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=svr_ids).terminate()
    return ''


# 修改server状态 - stop
@bp.patch('/server/<svr_ids>')
@auth_token.login_required
@input(InstanceIn(partial=True))
@output(InstanceOut)
def stop_svr(svr_ids, data):
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=svr_ids).stop()
    return ''


# 修改server状态 - start
@bp.patch('/server/<svr_ids>')
@auth_token.login_required
@input(InstanceIn(partial=True))
@output(InstanceOut)
def start_svr(svr_ids, data):
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=svr_ids).start()
    return ''


# 查看server清单
@bp.get('/server')
@auth_token.login_required
@output(InstanceOut, description='Servers list')
def list_svrs():
    # ec2.instances.filter

    return jsonify()


# 查看指定server信息
@bp.get('/server/<svr_id>')
@auth_token.login_required
@output(InstanceOut, description='Server info')
def get_svr(svr_id):
    # ec2.instances.filter

    return jsonify()
