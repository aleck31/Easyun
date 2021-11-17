# -*- coding: utf-8 -*-
'''
@Description: The public module, including the login and user auth.
@LastEditors: 
'''
from apiflask import APIBlueprint

bp = APIBlueprint('公共组件', __name__)

from . import auth, errors, models