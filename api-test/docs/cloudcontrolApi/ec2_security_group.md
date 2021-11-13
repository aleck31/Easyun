## EC2 SecurityGroup

### create-resource 新建instance
```
aws cloudcontrol create-resource --type-name AWS::EC2::SecurityGroup --desired-state "{\"GroupDescription\": \"Allow http to client host\",\"RetentionInDays\":90}"
```
### list-resources 列出所有instance
```
aws cloudcontrol list-resources --type-name AWS::EC2::SecurityGroup
** cloud control不支持 **
```
### update-resource 更新指定instance
```
aws cloudcontrol update-resource --type-name AWS::Logs::LogGroup --identifier CloudControlExample --patch-document "[{\"op\":\"replace\",\"path\":\"/RetentionInDays\",\"value\":180}]"
```
### get-resource 查看指定instance
```
aws cloudcontrol get-resource --type-name AWS::Logs::LogGroup --identifier CloudControlExample
```
### delete-resource 删除指定instance
```
aws cloudcontrol delete-resource --type-name AWS::Logs::LogGroup --identifier CloudControlExample
```
### track the status of resource operation request
```
aws cloudcontrol get-resource-request-status --request-token 2026055d-f21c-4b50-bd40-111111111111
```





