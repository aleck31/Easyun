# -*- coding: utf-8 -*-
'''
@Description: The Server Management module
@LastEditors: 
'''
from apiflask import APIBlueprint
from easyun.common.models import Datacenter

from flask import jsonify

from easyun.common.auth import auth_token
from easyun.common.models import Account, Result

# define api version
ver = '/api/v1'

bp = APIBlueprint('服务器管理', __name__, url_prefix = ver+'/server') 

REGION = "us-east-1"
# dc = Datacenter.query.filter_by(name="Easyun").first()
# REGION = dc.get_region()
FLAG = "Easyun"

from . import server_add, server_act, server_get, server_mod
