

### Amazon Price List Service API provides the following two endpoints:
* https://api.pricing.us-east-1.amazonaws.com
* https://api.pricing.ap-south-1.amazonaws.com


```
//AmazonEC2 Object Inside the Primary AWS Price List
//提示： ec2 currentVersionUrl index.json 单个文件2.4G
    "AmazonEC2" : {
      "offerCode" : "AmazonEC2",
      "versionIndexUrl" : "/offers/v1.0/aws/AmazonEC2/index.json",
      "currentVersionUrl" : "/offers/v1.0/aws/AmazonEC2/current/index.json",
      "currentRegionIndexUrl" : "/offers/v1.0/aws/AmazonEC2/current/region_index.json",
      "savingsPlanVersionIndexUrl" : "/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/index.json",
      "currentSavingsPlanIndexUrl" : "/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json"
    },


    "AmazonS3" : {
      "offerCode" : "AmazonS3",
      "versionIndexUrl" : "/offers/v1.0/aws/AmazonS3/index.json",
      "currentVersionUrl" : "/offers/v1.0/aws/AmazonS3/current/index.json",
      "currentRegionIndexUrl" : "/offers/v1.0/aws/AmazonS3/current/region_index.json"
    },

```    

### 访问api需要的IAM权限
https://docs.amazonaws.cn/en_us/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-policy-pe-api