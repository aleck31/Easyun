# Easyun
A lightweight user portal for AWS Cloud. [Add-on]

## 关于
Easyun（易云），侧重于“易”，为AWS提供一个简单易用的云用户界面，对功能丰富的web console做减法，聚焦云用户最常用的IaaS资源使用管理功能，包括：
* 云数据中心快速部署
* 云上资源生命周期管理
* 云上资源全局视图
* 云上资源日志告警
* 账号基本信息
* ...

## 功能简介
1. 初始化云数据中心网络环境
    * 创建符合最佳实践的VPC
    * AZ可用区，IP段，子网、路由、公网访问等快速设置；
2. 云资源创建（IaaS层资源）
    * 新建云主机(EC2实例、卷)
    * 新建对象存储(S3 Bucket)
    * 新建文件共享(EFS、FSx)
    * 新建托管数据库(RDS)
    * 新建容器集群(非托管)
    * 基于快照的备份管理
    * 资源使用月度成本评估
3. 生命周期管理
    * 云主机信息查看、配置更新，实例删除
    * 对象存储信息查看、配置更新，存储桶删除
    * 文件共享存储信息查看、配置更新，文件系统删除
    * RDS数据库信息查看、配置更新，实例删除
    * 快照管理：查看、复制，删除
4. 全局视图
    * 当前区域资源分布；
    * 云上资源使用情况；
    * 资产清单列表
5. 日志列表
    * 异常事件日志查询展示
    * 事件告警通知(email)
6. 账户管理：
    * 用户联系方式维护
    * EC2 keypair管理
    * AK/SK 管理
    * Free-tier 到期提醒

## 部署方式
提供Cloudformation 或 Terraform 模板文件在自有AWS账户内进行快速独立部署。

## 各个feature的访问地址
- 在api-test目录下运行 `yarn dev`,如果运行失败请使用`yarn`或`npm install`安装依赖    
api-test: http://localhsot:8080

- 在`docs`目录下运行 `yarn dev`,如果运行失败请使用`yarn`或`npm install`安装依赖    
docs: http://localhost:8081

- 在`client`目录下运行 `yarn dev`,如果运行失败请使用`yarn`或`npm install`安装依赖    
client: http://localhost:8888