# -*- coding: utf-8 -*-
'''
@Description: The Server Management module
@LastEditors: 
'''
import re
import boto3
from apiflask import APIBlueprint, Schema, input, output, auth_required
from apiflask.fields import Integer, String, List, Dict
from easyun.common.models import Account
from os import abort

from flask import jsonify

from easyun.common.auth import auth_token
from easyun.common.models import Account, Result

# define api version
ver = '/api/v1.0'

bp = APIBlueprint('服务器管理', __name__, url_prefix = ver+'/server') 

REGION = "us-east-1"
# AWS = Account.query.filter_by(cloud="aws").first()
# REGION = AWS.region
FLAG = "Easyun"

from . import server_add, server_act, server_get, server_mod
