#!/usr/bin/env python
# encoding: utf-8
"""
  @author:  shui
  @license: (C) Copyright 2021, Node Supply Chain Manager Corporation Limited. 
  @file:    schemas.py
  @desc:
"""


class AddDatacenter(Schema):
    region = String(required=True, validate=Length(0, 20))     #VPC name
    vpc_cidr = String(required=True, validate=Length(0, 20))     #VPC name
    public_subnet_1 = String(required=True)
    public_subnet_2 = String(required=True)
    private_subnet_1 = String(required=True)
    private_subnet_2 = String(required=True)
    sgs1 = String(required=True )
    sgs2 = String(required=True )
    sgs3 = String(required=True )
    keypair = String(required=True)


class VpcListIn(Schema):
    vpc_id = String()


class VpcListOut(Schema):
    vpc_id = String()
    pub_subnet1 = String()
    pub_subnet2 = String()
    private_subnet1 = String()
    private_subnet2 = String()
    sgs = String()
    keypair = String()