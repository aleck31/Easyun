# -*- coding: utf-8 -*-
"""server models."""

import math
from easyun import db
from apiflask.validators import Length, OneOf


class server_ami:
    """
    Create a Server AMI list table
    """

    __tablename__ = 'server_ami'

    ami_id = db.Column(db.Integer, primary_key=True)    # "ImageId": "ami-00001ae98aac59c70",
    name = db.Column(db.String)     # "Name": "Windows_Server-2016-2021.08.11",
    platform = db.Column(db.String)     # "Platform": "windows",
    detail = db.Column(db.String)       # "PlatformDetails": "Windows with SQL Server Enterprise",
    osname = db.Column(db.String)    # "Description": "Microsoft Windows Server 2016 AMI provided by Amazon",
    osversion = db.Column(db.String)    # "2016",
    rootdev = db.Column(db.String)  # "RootDeviceName": "/dev/sda1",
    rootype = db.Column(db.String)  # "RootDeviceType": "ebs",
    

    def __init__(self, ami_id=None, name=None, platform=None, detail=None, osname=None, osversion=None):
        self.ami_id = ami_id
        self.name = name
        self.platform = platform
        self.detail = platform
        self.osname = osname
        self.osversion = osversion


    def foo(self):
        # do something
        
        return ''
