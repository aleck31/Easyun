import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']
TAG_SPEC = [
        {
        "ResourceType":"instance",
        "Tags": [
                {
                    "Key": "Flag",
                    "Value": "Easyun"
                }
            ]
    }
    ]

ec2 = boto3.resource('ec2')
 
instance = ec2.create_instance(
    ImageID=AMI,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    SubnetID=SUBNET_ID,
    TagSpecifications = TAG_SPEC,
    MaxCount=1,
    MinCount=1
    )
    
print("New instance created:", instance[0].id)