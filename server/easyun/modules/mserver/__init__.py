# -*- coding: utf-8 -*-
"""The Server management module."""
import boto3
from apiflask import APIBlueprint, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask import jsonify
from easyun.common.auth import auth_token
from datetime import date, datetime

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('服务器管理', __name__, url_prefix = ver) 

REGION = "us-east-1"
FLAG = "Easyun"

# 云服务器参数定义
NAME = 'boto3test'
NUM = 1
AMI = 'ami-0447addf6c74624eb'
TYPE = 't4g.nano'
SUBNET = 'subnet-06bfe659f6ecc2eed'
SGs = ['sg-05df5c8e8396d06e9',]
KEY = "key_easyun_dev"
DISK = [
    {
        'DeviceName': '/dev/xvda',
        'Ebs': {            
            'DeleteOnTermination': True,
            'VolumeSize': 16,
            'VolumeType': 'gp2'
            }
    },
    {
        'DeviceName': '/dev/sdf',
        'Ebs': {            
            'DeleteOnTermination': True,
            'VolumeSize': 13,
            'VolumeType': 'gp2'
            } 
    }
]
TAG_SPEC = [
    {
    "ResourceType":"instance",
    "Tags": [
            {"Key": "Flag", "Value": FLAG},
            {"Key": "Name", "Value": NAME}
        ]
    }
    ]

class ServerIn(Schema):
    name = String(required=True, validate=Length(0, 20))     #云服务器名称
    num = Integer(requir1=True)                              #新建云服务器数量
    ami_id = String(required=True, validate=Length(0, 20))         #ImageId
    type = String(required=True, validate=OneOf(['t3', 'g4', 'm5']))    #INSTANCE_TYPE
    subnet = String(required=True) 
    sgs = String(required=True ) 
    keypair = String(required=True)
    disk = dict(
        required=True,
        metadata={'title': 'Volumes', 'description': 'The volume of the server.'}
    )


class ServerOut(Schema):
    ami_id = Integer()
    instance_type = String()
    subnet_id = String()
    ssubnet_id = String()
    key_name = String()
    category = String()


# 新增server
@bp.post('/server')
@auth_token.login_required
@input(ServerIn)
@output(ServerOut, 201, description='add A new server')
def add_server(newsvr):
    '''新建云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    newsvr = RESOURCE.create_instance(
        ImageId = AMI,
        InstanceType = TYPE,
        MaxCount = NUM,
        MinCount = NUM,
        BlockDeviceMappings = DISK,
        SubnetId = SUBNET,
        SecurityGroupIds = SGs,
        KeyName = KEY,
        TagSpecifications = TAG_SPEC
    )
    return newsvr[0].id


@bp.get('/servers')
@output(ServerOut, description='Get Servers list')
def list_svrs():
    '''获取Easyun环境下云服务器列表(测试未加授权)'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    servers = RESOURCE.instances.filter(
    Filters=[
        {'Name': 'tag:Flag','Values': [FLAG]}
    ])
    svrlist = {}
    for server in servers:
        svrlist[str(server)]= server.id
    return jsonify(svrlist) 


@bp.get('/server/<svr_id>')
@auth_token.login_required
@output(ServerOut, description='Server info')
def get_svr(svr_id):
    '''查看指定云服务器详情'''
    CLIENT = boto3.client('ec2', region_name=REGION)

    # Helper method to serialize datetime fields
    def json_datetime_serializer(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))

    response = CLIENT.describe_instances(InstanceIds=[svr_id])

    return jsonify(response['Reservations'])


class OperateIn(Schema):
    svr_ids = list()     #云服务器ID
    action = String(required=True, validate=OneOf(['start', 'stop', 'restart','delete']))    #Operation TYPE

class OperateOut(Schema):
    svr_ids = list() 

@bp.post('/server/<action>/<svr_ids>')
@auth_token.login_required
@input(OperateIn)
@output(OperateOut, description='Operation finished !')
def operate_svr(action, svr_ids):
    '''启动/停止/重启 云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    servers = RESOURCE.instances.filter(InstanceIds=svr_ids)
    if action == 'start':
        servers.start()
        return 'starting'
    elif action == 'stop':
        servers.stop()
        return 'stopping'
    elif action == 'restart':
        servers.restart()  
        return 'restarting'
    else:
        return 


@bp.delete('/server/<svr_ids>')
@auth_token.login_required
@input(OperateIn)
@output({}, 204)
def del_svr(svr_ids):
    '''删除指定云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)   
    servers = RESOURCE.instances.filter(InstanceIds=svr_ids)
    for server in servers:
        server.terminate()
        server.wait_until_terminated()
    return 'Server Deleted'