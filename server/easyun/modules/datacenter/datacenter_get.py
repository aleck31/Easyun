# -*- coding: utf-8 -*-
'''
@Description: DataCenter Management - Get info: Data Center
@LastEditors: 
'''
import boto3
from apiflask import input, output, auth_required
from apiflask.validators import Length, OneOf
from easyun.common.auth import auth_token
from datetime import date, datetime
from . import bp, REGION, FLAG
from flask import jsonify

from .schemas import DataCenterListOut
from ...common.result import Result

NewDataCenter = {
    'region': 'us-east-2',
    'vpc_cidr' : '10.10.0.0/16',
    'avaibility_zone' : '10.10.0.0/16',
    'pub_subnet1' : '192.168.1.0/24',
    'pub_subnet2' : '192.168.2.0/24',
    'pri_subnet1' : '192.168.3.0/24',
    'pri_subnet2' : '192.168.4.0/24',
    'key' : "key_easyun_dev",
    'secure_group1' : 'easyun-sg-default',
    'secure_group2' : 'easyun-sg-webapp',
    'secure_group3' : 'easyun-sg-database',
    'tag_spec' : [
        {
        "ResourceType":"instance",
        "Tags": [
                {"Key": "Flag", "Value": FLAG},
                {"Key": "Name", "Value": 'test-from-api'}
            ]
        }
        ]
}

@bp.get('/datacenter/region')
@auth_required(auth_token)
@output(DataCenterListOut, description='Get DataCenter Region Info')
def get_datacenter_region():
    '''获取Easyun环境下云数据中心信息'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)

    vpcs = RESOURCE.describe_vpcs(Filters=[
            {'Name': 'tag:FLAG','Values': [FLAG],},
        ])

    regions = RESOURCE.describe_regions(Filters=[
            {'Name': 'region-name','Values': [REGION],},
        ])

    azs = RESOURCE.describe_availability_zones(Filters=[
            {'Name': 'group-name','Values': [REGION],},
        ])

    response = Result(detail=NewDataCenter['region'], status_code=2001,
                      message="ok", http_status_code=200)
    return response.make_resp()

@bp.get('/datacenter/AZ')
@auth_required(auth_token)
@output(DataCenterListOut, description='Get DataCenter AZ Info')
def get_datacenter_AZ():
    '''获取Easyun环境下云数据中心信息'''
    RESOURCE = boto3.resource('ec2', region_name=REGION)
    azs = RESOURCE.describe_availability_zones(Filters=[
            {'Name': 'group-name','Values': ['us-east-1'],},
        ])

