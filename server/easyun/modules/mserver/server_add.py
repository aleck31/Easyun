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
from werkzeug.wrappers import response
from easyun.common.auth import auth_token
from easyun.common.result import make_resp, error_resp, bad_request
from . import bp, REGION, FLAG



# 测试用云服务器参数定义
Svrargs = {
    "Number" : 1,
    "ImageId" : "ami-0447addf6c74624eb",
    "InstanceType" : "t4g.nano",
    "SubnetId" : "subnet-06bfe659f6ecc2eed",
    "SecurityGroupIds" : ["sg-05df5c8e8396d06e9",],
    "KeyName" : "key_easyun_dev",
    "BlockDeviceMappings" : [
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {            
                "DeleteOnTermination": True,
                "VolumeSize": 16,
                "VolumeType": "gp2"
                }
        },
        {
            "DeviceName": "/dev/sdf",
            "Ebs": {            
                "DeleteOnTermination": True,
                "VolumeSize": 13,
                "VolumeType": "gp2"
                } 
        }
    ],
    "TagSpecifications" : [
        {
        "ResourceType":"instance",
        "Tags": [
                {"Key": "Flag", "Value": "Easyun"},
                {"Key": "Name", "Value": "test-from-api"}
            ]
        }
        ]
}

class AddSvr(Schema):
    # name = String(                          #云服务器名称
    #     required=True, 
    #     validate=Length(0, 30),
    #     metadata={'title': 'Name', 'description': 'The Tag:Name of the server.'}
    # ) 
    Number = Integer(required=True, example=1)            #新建云服务器数量
    ImageId = String(required=True, example="ami-0447addf6c74624eb")          #ImageId
    InstanceType = String(required=True)            #INSTANCE_TYPE
    SubnetId = String(required=True) 
    SecurityGroupIds = String(required=True ) 
    KeyName = String(required=True)
    BlockDeviceMappings = List(
        Dict,
        required=True
    )
    TagSpecifications = List(
        Dict,
        required=True
    )


# 新增server
@bp.post('/add')
@auth_required(auth_token)
@input(AddSvr)
@output({}, 204)
def add_server(newsvr):
    '''新建云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    # server = RESOURCE.create_instances(newsvr)
    server = RESOURCE.create_instances(
        MaxCount = newsvr['Number'],
        MinCount = newsvr['Number'],
        ImageId = newsvr['ImageId'],
        InstanceType = newsvr['InstanceType'],
        SubnetId = newsvr['SubnetId'],
        SecurityGroupIds = newsvr['SecurityGroupIds'],
        KeyName = newsvr['KeyName'],
        BlockDeviceMappings = newsvr['BlockDeviceMappings'],
        TagSpecifications = newsvr['tag_spec']    
    )

    return make_resp("add a new server", 204, server[0].id)
    # return jsonify({'NewServer ID': server[0].id})