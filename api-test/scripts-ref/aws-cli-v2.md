
Region 相关
----
//获取所有region信息  
```
$ aws ec2 describe-regions --all-regions
```

//基于endpoint 名称筛选region
```
$ aws ec2 describe-regions --filters "Name=endpoint,Values=*us*"
{
    "Regions": [
        {
            "Endpoint": "ec2.us-east-1.amazonaws.com",
            "RegionName": "us-east-1",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.us-east-2.amazonaws.com",
            "RegionName": "us-east-2",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.us-west-1.amazonaws.com",
            "RegionName": "us-west-1",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.us-west-2.amazonaws.com",
            "RegionName": "us-west-2",
            "OptInStatus": "opt-in-not-required"
        }
    ]
}
```

Account相关
----
```
$ aws organizations describe-account --account-id 555555555555

$ aws account get-alternate-contact --alternate-contact-type OPERATIONS
```

