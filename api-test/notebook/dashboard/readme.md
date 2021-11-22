### Task

1. 首行Summary
    a. 获取当前region下subnet分布信息，返回az名称、国旗代码、国家地区信息、子网数 等信息；
    b. 健康状态：获取cloudwatch的alarms信息，返回 In alarm，Insufficient data，Ok 三类事件的数量信息；
    c. 看板链接：获取cloudwatch内的dashboard信息，基于favorite标签筛选出用户标星的看板名称及链接反馈前端；
2. 资源信息 Graphical视图
    a. 获取云服务器(ec2)信息，返回包括：总数，在运行数，关机数，vCPU总数，内存总容量 信息；
    b. 获取数据库(RDS)信息，返回包括：总数，MySQL实例数，MariaDB实例数，PostgreSQL实例数，Aurora等统计信息；
    c. 获取网络信息，返回包括：子网总数，公网数量、私网数量、IGW、NAT网关、安全组等信息；
    d. 获取对象存储(s3)信息，返回包括：桶总数，总数据容量，总对象数量，公开访问桶数，启用加密桶数 信息；
    e. 获取块存储(ebs)信息，返回包括：ebs可用量(待验证), ebs总容量，已分配/使用容量 信息；
    f. 获取文件存储(EFS&FSx)信息，返回包括：EFS文件系统数量,EFS总容量，FSx文件系统数量,FSx总容量 信息；
    g. 将以上信息拼装成1个json文件返回给前端（*注意跟前端沟通确认清楚json格式*）

3. 资源信息 List 视图
    a. 服务器列表：遍历云服务器(ec2)信息，给前端返回UI需要的各列属性信息（ID,Name,State,type, vCPU, RAM, Storage, OS, AZ, Public IPv4、launch time）
    b. 数据库列表：遍历数据库(RDS)信息，给前端返回UI需要的各列属性信息（Identifier,Role,Engine,Status,Size,vCPU, RAM, Storage, AZ, Endporint、launch time）
    c. 对象存储列表：遍历S3信息，给前端返回UI需要的各列属性信息（Identifier, region, Access, encryption, versiong, creation time）
    //如精力允许可以接着做以下功能：
    d. 块存储列表：
    e. 文件共享存储列表：
    f. 子网列表：
    g. 安全组列表：
    h. 备份(snapshot)列表：

**注意：以上所有资源获取的范围都基于当前region和Flag=Easyun 的标签。**