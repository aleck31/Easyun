
//筛选出 t2.micro 类型实例，并仅为每个匹配项输出 InstanceId 值
$ aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"
[
    "i-05e998023d9c69f9a"
]

//向实例添加标签Flag: Easyun
$ aws ec2 create-tags --resources i-5203422c --tags Key=Flag,Value=Easyun

//列出具有标签 Flag=Easyun 的任何实例
$ aws ec2 describe-instances --filters "Name=tag:Flag,Values=Easyun"

//终止实例(删除)
$ aws ec2 terminate-instances --instance-ids i-5203422c

//创建密钥对，保存至.pem 文件
$ aws ec2 create-key-pair --key-name easyun-user-key --query 'KeyMaterial' --output text > easyun-user-key.pem

//查看密钥对
$ aws ec2 describe-key-pairs --key-name MyKeyPair