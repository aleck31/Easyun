### 任务拆分

**详见每个子目录readme文件** 


### 关于Boto3

Boto3 （AWS SDK for Python）开发工具包由两个关键的 Python 包组成：
* Botocore（提供在 Python 开发工具包和 AWS CLI 之间共享的 Low-level 功能的库）
* Boto3（实现 Python 开发工具包本身的包）

Boto3 支持两套API接口, 低级和高级。
* 其中低级 API 是和 AWS 的 HTTP 接口一一对应的，通过 boto3.client("ec2") 调用，执行aws cli调用的这一层api接口；
* 高级 API 是面向对象的，更加易于使用，通过 boto3.resource("ec2") 调用，美中不足是不一定覆盖了所有资源的API。

从易用性角度，Easyun建议优先用面向对象的的高级API接口 boto3.resource 进行功能实现。  

举个栗子：
```
import boto3 

# Create a low-level client with the service name
queue = boto3.client('sqs')

# High-level connections
sqs_resource = boto3.resource('sqs')
queue = sqs_resource.Queue(url='http://...')
```

同时，也可以从现有资源访问low-level的客户端，例如：
```
import boto3 

# Create the resource
sqs_resource = boto3.resource('sqs')

# Get the client from the resource
sqs = sqs_resource.meta.client
```

### 关于Cloudcontrol API

借助 Cloud Control API 标准化应用程序编程接口 (API) 集，我们可以很方便地对 AWS 账户中的任何受支持资源执行 CRUD-L 操作，包括：创建、读取、更新、删除和列出。  
使用 Cloud Control API 的好处在于无需为每个资源/服务生成特定的代码或脚本。 

//A low-level client representing AWS Cloud Control API (CloudControlApi)
```
import boto3
client = boto3.client('cloudcontrol')
```
cloudcontrol 支持的方法如下:
* create_resource()
* update_resource()
* delete_resource()
* get_paginator()
* get_resource()
* get_resource_request_status()
* get_waiter()
* list_resource_requests()
* list_resources()
* can_paginate()
* cancel_resource_request()

> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol.html
