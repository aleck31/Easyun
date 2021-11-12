
S3 相关
----
### 获取S3存储桶容量占用
```
//s3 ls汇总
$ aws s3 ls --summarize --human-readable --recursive s3://cdktoolkit-stagingbucket-1254ykp5179br
2021-11-04 04:07:22  324 Bytes assets/5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e.zip
2021-11-04 04:53:46  822 Bytes assets/e6e8bcdd6a7ec6d780a2dfe866afae9cb0af2089ceef14e5ccdbc888463ec07d.zip

Total Objects: 2
   Total Size: 1.1 KiB

//s3api 使用sum(Contents[].Size)对所有对象大小值求和，length(Contents[])
$  aws s3api list-objects --bucket cdktoolkit-stagingbucket-1254ykp5179br --output json --query "[sum(Contents[].Size), length(Contents[])]"
[
    1146,   //size
    2       //number
]

//增加格式化示例：
$ aws s3api  list-objects --bucket cdktoolkit-stagingbucket-1254ykp5179br --output json --query "[sum(Contents[].Size), length(Contents[])]" | awk 'NR!=2 {print $0;next} NR==2 {print $0/1024/1024/1024" GB"}'
```
//利用cloudwatch获取s3桶的存储容量(统计最近24h的容量平均值), 不需要遍历对象，适合大桶下使用：  
```
$ aws cloudwatch get-metric-statistics --namespace AWS/S3 --start-time 2021-11-10T01:00:00 --end-time 2021-11-11T01:00:00 --period 86400 --statistics Average --region us-east-1 --metric-name BucketSizeBytes --dimensions Name=BucketName,Value=cdktoolkit-stagingbucket-1254ykp5179br Name=StorageType,Value=StandardStorage
{
    "Label": "BucketSizeBytes",
    "Datapoints": [
        {
            "Timestamp": "2021-11-10T10:00:00+00:00",
            "Average": 1372.0,
            "Unit": "Bytes"
        }
    ]
}

//必须在Dimensions参数中同时指定 StorageType 和 BucketName。你只需要改变的是--start-date，--end-time 和 Value=toukakoukan.com
```
//bash 脚本参考：
```
#!/bin/bash
region=$1
bucket=$2
now=$(date +%s)
aws cloudwatch get-metric-statistics --namespace AWS/S3 --start-time "$(echo "$now - 86400" | bc)" --end-time "$now" --period 86400 --statistics Average --region $region --metric-name BucketSizeBytes --dimensions Name=BucketName,Value="$bucket" Name=StorageType,Value=StandardStorage
```

//基于python开发的 s4cmd 小工具获取容量：
```
$ pip install s4cmd
$ s4cmd du s3://bucket-name
```

### 获取存储桶属性