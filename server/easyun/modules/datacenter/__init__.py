# -*- coding: utf-8 -*-
"""The Datacenter creation module."""
# -*- coding: utf-8 -*-
'''
@Description: The Server Management module
@LastEditors: 
'''
from apiflask import APIBlueprint
from easyun.common.models import Account

# define api version
ver = '/api/v1'

bp = APIBlueprint('数据中心管理', __name__, url_prefix = ver) 

REGION = "us-east-1"
# dc = Datacenter.query.filter_by(name="Easyun").first()
# REGION = dc.get_region()
FLAG = "Easyun"

from . import datacenter_add, datacenter_default, datacenter_get
