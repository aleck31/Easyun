通过cloudcontrol api对资源生命周期管理示例
----

## create-resource
```
aws cloudcontrol create-resource --type-name AWS::Logs::LogGroup --desired-state "{\"LogGroupName\": \"CloudControlExample\",\"RetentionInDays\":90}"
```
**参数列举：**
* LogGroupName：String
* RetentionInDays：Integer
* Tags：[ JSONObject ] 

## list-resources 列出某类资源所有条目
```
aws cloudcontrol list-resources --type-name AWS::Logs::LogGroup
```

## update-resource 
```
aws cloudcontrol update-resource --type-name AWS::Logs::LogGroup --identifier CloudControlExample --patch-document "[{\"op\":\"replace\",\"path\":\"/RetentionInDays\",\"value\":180}]"
```

## get-resource 查看指定资源
```
aws cloudcontrol get-resource --type-name AWS::Logs::LogGroup --identifier CloudControlExample
```

## delete-resource
```
aws cloudcontrol delete-resource --type-name AWS::Logs::LogGroup --identifier CloudControlExample
```


## track the status of resource operation request
```
aws cloudcontrol get-resource-request-status --request-token 2026055d-f21c-4b50-bd40-111111111111
```

## Reference：  
[Cloud Control API **User Guide**](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/index.html)  

[Cloud Control API **API Reference**](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/index.html)  

[Cloud Control API in the AWS CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/index.html)