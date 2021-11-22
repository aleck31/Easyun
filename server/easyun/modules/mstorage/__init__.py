# -*- coding: utf-8 -*-
"""The Storage management module."""
from apiflask import APIBlueprint, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from common.auth import auth_token
import boto3
import os

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('存储管理', __name__, url_prefix = ver) 

CLIENT = boto3.client('cloudcontrol')
TYPE = 'AWS::S3::Bucket'

response = CLIENT.create_resource(
    TypeName=TYPE,
    DesiredState={
        "Namex": "xxxxx",
        "Typex": "xxxxx"
        },
    # TypeVersionId='string',
    # RoleArn='string',
    # ClientToken='string'
)