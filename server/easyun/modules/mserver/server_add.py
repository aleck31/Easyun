# -*- coding: utf-8 -*-
'''
@Description: Server Management - Add new server
@LastEditors: 
'''
import boto3
from apiflask import Schema, input, output, auth_required
from apiflask.fields import Integer, String, List, Dict
from apiflask.validators import Length, OneOf
from flask import jsonify
from easyun.common.auth import auth_token
from . import bp, REGION, FLAG



# 云服务器参数定义
Svrargs = {
    'name' : 'boto3test',
    'numb' : 1,
    'image' : 'ami-0447addf6c74624eb',
    'type' : 't4g.nano',
    'subnet' : 'subnet-06bfe659f6ecc2eed',
    'sgs' : ['sg-05df5c8e8396d06e9',],
    'key' : "key_easyun_dev",
    'disk' : [
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
    ],
    'tag_spec' : [
        {
        "ResourceType":"instance",
        "Tags": [
                {"Key": "Flag", "Value": FLAG},
                {"Key": "Name", "Value": 'test-from-api'}   # 测试用实例名称
            ]
        }
        ]
}

class AddSvr(Schema):
    name = String(                          #云服务器名称
        required=True, 
        validate=Length(0, 30),
        metadata={'title': 'Name', 'description': 'The Tag:Name of the server.'}
    )    
    num = Integer(required=True)            #新建云服务器数量
    ami_id = String(required=True)          #ImageId
    type = String(required=True)            #INSTANCE_TYPE
    subnet = String(required=True) 
    sgs = String(required=True ) 
    keypair = String(required=True)
    disk = List(
        Dict(),
        required=True
    )
    tag_spec = List(
        Dict(),
        required=True
    )


# 新增server
@bp.post('/add')
@auth_required(auth_token)
@input(AddSvr)
@output({}, 204, description='add A new server')
def add_server(newsvr):
    '''新建云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    newsvr = RESOURCE.create_instances(
    ImageId = Svrargs['image'],
    InstanceType = Svrargs['type'],
    MaxCount = Svrargs['numb'],
    MinCount = Svrargs['numb'],
    BlockDeviceMappings = Svrargs['disk'],
    SubnetId = Svrargs['subnet'],
    SecurityGroupIds = Svrargs['sgs'],
    KeyName = Svrargs['key'],
    TagSpecifications = Svrargs['tag_spec']    
    )
    return jsonify({'NewServer ID': newsvr[0].id})