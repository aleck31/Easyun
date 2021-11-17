# -*- coding: utf-8 -*-
"""server models."""

import math
from easyun import db
from apiflask.validators import Length, OneOf


class server_ami(db.Model):
    """
    Create a Diamond table
    """

    __tablename__ = 'server_ami'

    ami_id = db.Column(db.Integer, primary_key=True)    # "ImageId": "ami-00001ae98aac59c70",
    name = db.Column(db.String)     # "Name": "Windows_Server-2016-2021.08.11",
    platform = db.Column(db.String)     # "Platform": "windows",
    platformdes = db.Column(db.String)     # "PlatformDetails": "Windows with SQL Server Enterprise",
    osdetails = db.Column(db.String)    # "Description": "Microsoft Windows Server 2016 AMI provided by Amazon",
    osversion = db.Column(db.String)    # "2016",
    rootdevname = db.Column(db.String)  # "RootDeviceName": "/dev/sda1",
    rootdevtype = db.Column(db.String)  # "RootDeviceType": "ebs",
    

    def __init__(self, ami_id=None, name=None, platform=None, odesname=None, osversion=None, ):
        self.ami_id = ami_id
        self.platform = platform
        self.osname = osname
        self.osversion = osversion
        self.platform = platform
        self.description = description

    def foo(self):
        # do something
        
        return ''
