S3 Bucket
----

## create-resource 新建 bucket
```
aws cloudcontrol create-resource --type-name AWS::S3::Bucket --desired-state "{\"BucketName\": \"bktexample17\",\"VersioningConfiguration\": \"Suspended\",\"Tags": \"[Flag,Easyun]\"}"
```
**参数列举：**
* BucketName：String
* VersioningConfiguration : JSONObject,
* PublicAccessBlockConfiguration : JSONObject,
* Tags : [ Tag, ... ]

ref: <https://docs.aws.amazon.com/zh_cn/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html>

## list-resources 列出所有 bucket
```
aws cloudcontrol list-resources --type-name AWS::S3::Bucket

{
    "TypeName": "AWS::S3::Bucket",
    "ResourceDescriptions": [
        {
            "Identifier": "amplify-amplify2799b35d0ae94-staging-80616-deployment",
            "Properties": "{\"BucketName\":\"amplify-amplify2799b35d0ae94-staging-80616-deployment\"}"
        },
        {
            "Identifier": "imgstore779180616-staging",
            "Properties": "{\"BucketName\":\"imgstore779180616-staging\"}"
        },
        {
            "Identifier": "cdktoolkit-stagingbucket-1254ykp5179br",
            "Properties": "{\"BucketName\":\"cdktoolkit-stagingbucket-1254ykp5179br\"}" 
        }
    ]
} 
```
## update-resource 更新指定 bucket
```

```
## get-resource 查看指定 bucket
```
aws cloudcontrol get-resource --type-name AWS::S3::Bucket --identifier bktexample17

{
    "TypeName": "AWS::S3::Bucket",
    "ResourceDescription": {
        "Identifier": "bkt782897",
        "Properties": "{\"BucketName\":\"bkt782897\",\"RegionalDomainName\":\"bkt782897.s3.us-east-1.amazonaws.com\",\"DomainName\":\"bkt782897.s3.amazonaws.com\",\"WebsiteURL\":\"http://bkt782897.s3-website-us-east-1.amazonaws.com\",\"DualStackDomainName\":\"bkt782897.s3.dualstack.us-east-1.amazonaws.com\",\"Arn\":\"arn:aws:s3:::bkt782897\"}"
    }
}
```
## delete-resource 删除指定 bucket
```
aws cloudcontrol delete-resource --type-name AWS::S3::Bucket --identifier bktexample17

{
    "ProgressEvent": {
        "TypeName": "AWS::S3::Bucket",
        "Identifier": "bktexample17",
        "RequestToken": "70306290-12d6-413b-bde8-5269ac486abc",
        "Operation": "DELETE",
        "OperationStatus": "IN_PROGRESS",
        "EventTime": "2021-11-06T13:25:32.398000+08:00"
    }
}
```
## track the status of resource operation request
```
aws cloudcontrol get-resource-request-status --request-token 70306290-12d6-413b-bde8-5269ac486abc

{
    "ProgressEvent": {
        "TypeName": "AWS::S3::Bucket",
        "Identifier": "bktexample17",
        "RequestToken": "70306290-12d6-413b-bde8-5269ac486abc",
        "Operation": "DELETE",
        "OperationStatus": "SUCCESS",
        "EventTime": "2021-11-06T13:25:32.955000+08:00"
    }
}
```


## Reference：  
<https://docs.aws.amazon.com/zh_cn/cloudcontrolapi/latest/userguide/supported-resources.html>  
<https://docs.aws.amazon.com/zh_cn/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html>




