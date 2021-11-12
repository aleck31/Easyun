
Instance相关
----
### 筛选出 t2.micro 类型实例，并仅为每个匹配项输出 InstanceId 值
```
$ aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"
[
    "i-05e998023d9c69f9a"
]
```
### 创建ec2实例 (含EBS)
```
aws ec2 run-instances --image-id ami-7axxxx3f --count 1 --instance-type t1.micro \
--key-name MyTestCalifornia --security-group-ids sg-dxxxxbb4 \
--placement AvailabilityZone=us-west-1c --subnet-id subnet-5exxxx3b \
--block-device-mappings "[{\"DeviceName\": \"/dev/sdf\",\"Ebs\":{\"VolumeSize\":100}}]"\
--user-data  "/sbin/mkfs.ext4 /dev/xvdf && /bin/mount /dev/xvdf /home"
```

### 向实例添加标签Flag: Easyun
```
$ aws ec2 create-tags --resources i-5203422c --tags Key=Flag,Value=Easyun
```

### 列出具有标签 Flag=Easyun 的任何实例
```
$ aws ec2 describe-instances --filters "Name=tag:Flag,Values=Easyun"
```

### 终止实例(删除)
```
$ aws ec2 terminate-instances --instance-ids i-5203422c
```

### 查询实例metadata
```
$ curl -w "\n" http://169.254.169.254/latest/meta-data

// 获取 Account ID
$ curl -w "\n" http://169.254.169.254/latest/meta-data/identity-credentials/ec2/info

{
  "Code" : "Success",
  "LastUpdated" : "2021-10-07T14:40:07Z",
  "AccountId" : "5655356406051"
}

```

AMI相关
----
### 获取指定region内AMI信息
```
//过滤 windows 平台的AMI信息
$ aws ec2 describe-images  --region us-east-1 --owners amazon --filters "Name=platform,Values=windows"

{
    "Images": [
        {
            "Architecture": "x86_64",
            "CreationDate": "2021-08-11T07:24:29.000Z",
            "ImageId": "ami-00001ae98aac59c70",
            "ImageLocation": "amazon/Windows_Server-2016-English-64Bit-SQL_2012_SP4_Enterprise-2021.08.11",
            "ImageType": "machine",
            "Public": true,
            "OwnerId": "801119661308",
            "Platform": "windows",
            "PlatformDetails": "Windows with SQL Server Enterprise",
            "UsageOperation": "RunInstances:0102",
            "State": "available",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "DeleteOnTermination": true,
                        "SnapshotId": "snap-0ac0d914930ec3de7",
                        "VolumeSize": 65,
                        "VolumeType": "gp2",
                        "Encrypted": false
                    }
                },
                {
                    "DeviceName": "xvdca",
                    "VirtualName": "ephemeral0"
                },
                ...
                {
                    "DeviceName": "xvdcz",
                    "VirtualName": "ephemeral25"
                }
            ],
            "Description": "Microsoft Windows Server 2016 Locale English with SQL Enterprise 2012 AMI provided by Amazon",
            "EnaSupport": true,
            "Hypervisor": "xen",
            "ImageOwnerAlias": "amazon",
            "Name": "Windows_Server-2016-English-64Bit-SQL_2012_SP4_Enterprise-2021.08.11",
            "RootDeviceName": "/dev/sda1",
            "RootDeviceType": "ebs",
            "SriovNetSupport": "simple",
            "VirtualizationType": "hvm"
        },


//增加查询过滤条件
$ aws ec2 describe-images  --region us-east-1 --owners amazon --query 'Images[*].[ImageLocation]' --filters "Name=platform,Values=windows"  --output text

amazon/Windows_Server-2016-English-64Bit-SQL_2012_SP4_Enterprise-2021.08.11
amazon/aws-elasticbeanstalk-amzn-2019.02.13.x86_64-WindowsServer2012R2-V2-hvm-201903122020
amazon/aws-elasticbeanstalk-amzn-2020.07.15.x86_64-WindowsServer2012R2Core-hvm-202007230520
amazon/aws-elasticbeanstalk-amzn-2020.04.15.x86_64-WindowsServer2012R2Core-hvm-202004240508
amazon/aws-elasticbeanstalk-amzn-2020.08.12.x86_64-WindowsServer2012R2-hvm-202008291900
amazon/Windows_Server-2012-R2-English-STIG-Core-2021.10.13
...
```


Key pair相关
----
### 创建密钥对，保存至.pem 文件
```
$ aws ec2 create-key-pair --key-name easyun-user-key --query 'KeyMaterial' --output text > easyun-user-key.pem
```

### 查看密钥对
```
$ aws ec2 describe-key-pairs --key-name MyKeyPair
```

VPC相关
----
### 创建密钥对，保存至.pem 文件
```
$ aws ec2 create-key-pair --key-name easyun-user-key --query 'KeyMaterial' --output text > easyun-user-key.pem
```

安全组
----
```
//创建SG
$ aws ec2 create-security-group --group-name easyun-sg-webapp --description "sg for webapp" --vpc-id vpc-id

//向SG添加规则示例：
$ aws ec2 authorize-security-group-ingress --group-id sg-xxxxyyyy --protocol tcp --port 22 --cidr 0.0.0.0/0

$ aws ec2 authorize-security-group-ingress --group-id sg-xxxxyyyy --protocol tcp --port 9999 --source-group sg-xxxxxxxx

$ aws ec2 authorize-security-group-ingress --group-id sg-d1xxxxb4 \
--protocol tcp --port 22 --cidr 202.x.x.120/29  --protocol tcp --port 8080-8082 --cidr 10.10.0.0/16 \
--protocol tcp --port 80 --cidr 0.0.0.0/0

//查询SG名称和id
$ aws ec2 describe-security-groups  --query SecurityGroups[*].[GroupName,GroupId,VpcId]

```

