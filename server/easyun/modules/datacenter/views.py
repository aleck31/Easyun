#!/usr/bin/env python
# encoding: utf-8
"""
  @author:  shui
  @license: (C) Copyright 2021, Node Supply Chain Manager Corporation Limited. 
  @file:    views.py
  @desc:
"""


# 新建Datacenter
@bp.post('/datacenter')
@auth_required(auth_token)
@input(AddDatacenter)
@output({}, 201, description='add A new Datacenter')
def add_datacenter(data):
    # create easyun vpc
    # create 2 x pub-subnet
    # create 2 x pri-subnet
    # create 1 x easyun-igw (internet gateway)
    # create 1 x easyun-nat (nat gateway)
    # create 1 x easyun-route-igw
    # create 1 x easyun-route-nat
    # create 3 x easyun-sg-xxx
    # create 1 x key-easyun-user (默认keypair)
    print(data)
    region = data["region"]
    vpc_cidr = data["vpc_cidr"]
    public_subnet_1 = data["public_subnet_1"]
    public_subnet_2 = data["public_subnet_2"]
    private_subnet_1 = data["private_subnet_1"]
    private_subnet_2 = data["private_subnet_2"]

    vpc_resource = boto3.resource('ec2', region_name=region)
    ec2 = boto3.client('ec2', region_name=region)
    # step 1: create VPC
    vpc = vpc_resource.create_vpc(CidrBlock=vpc_cidr, TagSpecifications=[{
                                                'ResourceType':'vpc',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                }] )
    print('VPC ID= '+ vpc.id )

    # step 2: create Internet Gateway
    # Create and Attach the Internet Gateway
    igw = ec2.create_internet_gateway(TagSpecifications=[{
                                                'ResourceType':'internet-gateway',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }] )
    print(f'Internet gateway created with: {json.dumps(igw, indent=4)}')
    vpc.attach_internet_gateway(InternetGatewayId=igw['InternetGateway']['InternetGatewayId'])
    print('Internet Gateway ID= '+ igw['InternetGateway']['InternetGatewayId'])

    # Create a route table and a public route to Internet Gateway
    route_table = vpc.create_route_table(TagSpecifications=[{
                                                'ResourceType':'route-table',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                         }])
    route = route_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw['InternetGateway']['InternetGatewayId']

    )
    print('Route Table ID= '+ route_table.id)

    # step 3: create 2 pub-subnet

    # Create public Subnet1
    pub_subnet1 = ec2.create_subnet(CidrBlock=public_subnet_1, VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'subnet',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])
    print('Public subnet1= '+ pub_subnet1['Subnet']['SubnetId'])




    # associate the route table with the subnet
    route_table.associate_with_subnet(SubnetId=pub_subnet1['Subnet']['SubnetId'])

    # Create public Subnet2
    pub_subnet2 = ec2.create_subnet(CidrBlock=public_subnet_2, VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'subnet',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])
    print('Public subnet2= '+pub_subnet2['Subnet']['SubnetId'])

    # associate the route table with the subnet
    route_table.associate_with_subnet(SubnetId=pub_subnet2['Subnet']['SubnetId'])

    # step 3: create 2 private-subnet
    # Create private Subnet1
    private_subnet1 = ec2.create_subnet(CidrBlock=private_subnet_1, VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'subnet',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])
    print('Private subnet1= '+private_subnet1['Subnet']['SubnetId'])

    # associate the route table with the subnet
    route_table.associate_with_subnet(SubnetId=private_subnet1['Subnet']['SubnetId'])

    # Create private Subnet2
    private_subnet2 = ec2.create_subnet(CidrBlock=private_subnet_2, VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'subnet',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])
    print('Private subnet2= '+private_subnet2['Subnet']['SubnetId'])

    # associate the route table with the subnet
    route_table.associate_with_subnet(SubnetId=private_subnet2['Subnet']['SubnetId'])

    # step 2: create NAT Gateway and allocate EIP
    # allocate IPV4 address for NAT gateway
    eip = ec2.allocate_address(Domain='vpc')
    print(eip)
    # create NAT gateway
    response = ec2.create_nat_gateway(
        AllocationId=eip['AllocationId'],
        SubnetId=private_subnet1['Subnet']['SubnetId'],
        TagSpecifications=[{
            'ResourceType': 'natgateway',
            'Tags': [{
                'Key':
                    'Flag',
                'Value':
                    'Easyun'
            }]
        }],
        ConnectivityType='public')
    nat_gateway_id = response['NatGateway']['NatGatewayId']

    # wait until the NAT gateway is available
    waiter = ec2.get_waiter('nat_gateway_available')
    waiter.wait(NatGatewayIds=[nat_gateway_id])

    # eip = ec2.allocate_address(Domain='vpc')
    #
    # # Create and Attach the NAT Gateway
    # nat_gatway = ec2.create_nat_gateway(SubnetId=private_subnet1['Subnet']['SubnetId'],AllocationId=eip['AllocationId'],TagSpecifications=[{
    #                                             'ResourceType':'natgateway',
    #                                             'Tags': [{
    #                                                 'Key':'FLAG',
    #                                                 'Value':'easyun'
    #                                             }]
    #                                                 }])
    # nat_gateway_id = nat_gatway['NatGateway']['NatGatewayId']
    # print('NAT gateway id= '+nat_gateway_id)

            # wait until the NAT gateway is available
    # waiter = client1.get_waiter('nat_gateway_available')
    # waiter.wait(nat_gateway_id)

    #print(nat_gateway_id)

    # Step 5-1:  create security group easyun-sg-default
    # create security group allow SSH inbound rule through the VPC enable ssh/rdp/ping
    secure_group1 = ec2.create_security_group(GroupName='easyun-sg-default', Description='Secure Group For Default', VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'security-group',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])

    ec2.authorize_security_group_ingress(
        GroupId=secure_group1['GroupId'],
        IpPermissions=[{
            'IpProtocol': 'tcp',
            'FromPort': 3389,
            'ToPort': 3389,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }, {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }, {
            'IpProtocol': 'icmp',
            'FromPort': -1,
            'ToPort': -1,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }])
    # secure_group1.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)
    # secure_group1.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=3389, ToPort=3389)
    # secure_group1.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='icmp', FromPort=-1, ToPort=-1)
    print('secure_group1= '+secure_group1['GroupId'])

    # Step 5-2:  create security group easyun-sg-webapp

    secure_group2 = ec2.create_security_group(GroupName='easyun-sg-webapp', Description='Secure Group For Webapp', VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'security-group',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])
    # secure_group2.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=80)
    # secure_group2.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=443)
    ec2.authorize_security_group_ingress(
        GroupId=secure_group2['GroupId'],
        IpPermissions=[{
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 80,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }, {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 443,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }])
    print('secure_group2= '+secure_group2['GroupId'])

    # Step 5-3:  create security group easyun-sg-database

    secure_group3 = ec2.create_security_group(GroupName='easyun-sg-database', Description='Secure Group For Database', VpcId=vpc.id,TagSpecifications=[{
                                                'ResourceType':'security-group',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                                    }])
    # secure_group3.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=3306)
    # secure_group3.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=5432)
    # secure_group3.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=1521)
    # secure_group3.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=1443)
    ec2.authorize_security_group_ingress(
        GroupId=secure_group3['GroupId'],
        IpPermissions=[{
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 3306,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }, {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 5432,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        },{
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 1521,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }, {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 1443,
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }]
        }])
    print('secure_group3= '+secure_group3['GroupId'])

    # create key pairs
    response = ec2.create_key_pair(KeyName='key-easyun-user',TagSpecifications=[{
                                                'ResourceType':'key-pair',
                                                'Tags': [{
                                                    'Key':'FLAG',
                                                    'Value':'easyun'
                                                }]
                                    }])
    print(response)

    return '' #status: successful


# 获取当前Datacenter环境信息
@bp.get('/datacenters')
@auth_token.login_required
@input(VpcListIn)
@output(VpcListOut, description='Get Datacenter info')
def get_vpc(vpc_id):
    # get vpc info
    # get subnet info
    # get securitygroup info
    # get keypair info

    ec2 = boto3.resource('ec2', region_name=REGION)
    vpcs = ec2.describer_vpcs(VpcIds=[
        'VpcListIn',
    ],
        Filters=[
            {'Name': 'tag:Flag', 'Values': [FLAG]}
        ])
    vpclist = {}
    print(json.dumps(vpcs, sort_keys=True, indent=4))

    return jsonify(vpcs)

    return ''  # datacenter id


# 删除Datacenter
@bp.post('/cleanup')
@auth_token.login_required
@input({})
@output({}, 201, description='Remove the Datacenter')
def remove_datacenter(newdc):
    # delete easyun vpc
    # delete 2 x pub-subnet
    # delete 2 x pri-subnet
    # delete 1 x easyun-igw (internet gateway)
    # delete 1 x easyun-nat (nat gateway)
    # delete 1 x easyun-route-igw
    # delete 1 x easyun-route-nat
    # delete 3 x easyun-sg-xxx
    # delete 1 x key-easyun-user (默认keypair)
    try:
        ec2 = boto3.resource('ec2', region_name=REGION)
        vpc_id = ec2.describer_vpcs(VpcIds='vpc_id',
                                    Filters=[
                                        {'Name': 'tag:Flag', 'Values': [FLAG]}
                                    ])

    except  boto3.exceptions.Boto3Error as e:
        print(e)
        exit(1)
    else:
        del_igw(ec2, vpc_id)
        del_sub(ec2, vpc_id)
        del_rtb(ec2, vpc_id)
        del_acl(ec2, vpc_id)
        del_sgp(ec2, vpc_id)
        del_vpc(ec2, vpc_id)