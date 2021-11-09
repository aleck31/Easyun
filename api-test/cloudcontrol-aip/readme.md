确定资源类型是否支持 Cloud Control API
----
### 1. 查询Cloud Control API支持的资源类型清单
```
aws cloudformation list-types --type RESOURCE --visibility PUBLIC --provisioning-type FULLY_MUTABLE --max-results 100 

或参考文档： https://docs.aws.amazon.com/zh_cn/cloudcontrolapi/latest/userguide/supported-resources.html
```
### 2. 确认资源类型是否支持Cloud Control API
```
aws cloudformation describe-type --type RESOURCE --type-name "AWS::S3::Bucket" 

//如果资源的 ProvisioningType 为 FULLY_MUTABLE 或 IMMUTABLE 的资源类型支持 Cloud Control API 资源操作。 
```

### 3. 查看资源类型支持的操作 
如果资源类型支持某个操作，则它会在  handlers 部分中列出，并且它包含一个 permissions 元素，该元素列出了处理程序所需的权限。   
常见的操作如： create, read, update, delete, list 

---

IaaS相关资源类型列表及 ProvisioningType
----
* Amazon EC2
    - AWS::EC2::Instance        - NON_PROVISIONABLE
    - AWS::EC2::SecurityGroup   - NON_PROVISIONABLE
    - AWS::EC2::Volume          - NON_PROVISIONABLE    
    - AWS::EC2::VPC         - FULLY_MUTABLE
    - AWS::EC2::Subnet      - FULLY_MUTABLE
    - AWS::EC2::KeyPair     - cannot be found.

* Amazon S3
    - AWS::S3::Bucket       - FULLY_MUTABLE
    - AWS::S3::AccessPoint  - FULLY_MUTABLE

* Amazon EFS
    - AWS::EFS::FileSystem  - FULLY_MUTABLE
    - AWS::EFS::AccessPoint - FULLY_MUTABLE
    - AWS::EFS::MountTarget - FULLY_MUTABLE

* Amazon RDS [TBD]
    - 
    - 
    - 

* Amazon ECS [TBD]
    - AWS::ECS::Cluster     - FULLY_MUTABLE
    - AWS::ECS::Service
    - AWS::ECS::TaskSet
    - AWS::ECS::TaskDefinition
    - AWS::ECS::PrimaryTaskSet
    - AWS::ECS::CapacityProvider

---

如不在 Cloud Control API 支持范围，基于现有sdk 实现
----
例如，对EC2管理相关可参考AWS SDK for python文档：  
<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html#launching-new-instances>

Boto3 Code examples：  
<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/examples.html>

Boto3 Available services：  
<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html>  


  