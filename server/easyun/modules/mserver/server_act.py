# -*- coding: utf-8 -*-
'''
@Description: Server Management - action: start, restart, stop, delete; and get status
@LastEditors: 
'''
import boto3
from apiflask import Schema, input, output, auth_required
from apiflask.fields import Integer, String, List, Dict
from apiflask.schemas import EmptySchema
from apiflask.validators import Length, OneOf
from werkzeug.wrappers import response
from easyun.common.auth import auth_token
from easyun.common.errors import bad_request
from . import bp, REGION, FLAG
from os import abort


class OperateIn(Schema):
    svr_ids = List(         #云服务器ID
        String(),
        required=True
    )     
    action = String(
        required=True, 
        validate=OneOf(['start', 'stop', 'restart'])  #Operation TYPE
        )   


class OperateOut(Schema):
    svr_ids = List(String) 

@bp.post('/action')
@auth_required(auth_token)
@input(OperateIn)
@output(OperateOut, description='Operation finished !')
def operate_svr(operate):
    '''启动/停止/重启 云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    servers = RESOURCE.instances.filter(
        InstanceIds=operate["svr_ids"]
        )
    if operate["action"] == 'start':
        response = servers.start()
    elif operate["action"] == 'stop':
        response = servers.stop()
    else:
        response = servers.restart()
    return response


@bp.delete('/delete')
@auth_required(auth_token)
@input(OperateIn)
@output(EmptySchema)
def del_svr(operate):
    '''删除指定云服务器'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)   
    servers = RESOURCE.instances.filter(
        InstanceIds=operate["svr_ids"],
        Filters=[
        {'Name': 'tag:Flag','Values': [FLAG]}
        ]
    )
    for server in servers:
        response = server.terminate()
        # server.wait_until_terminated()
    # return 'Server Deleted'
    return response