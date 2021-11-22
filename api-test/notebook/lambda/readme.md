### Task

> Part1：Dashboard的数据获取和存储，定期更新资源信息，优化dashboard数据展示性能
1. 新建dynamoDB，定义好schema （参考dashboard部分需求）
2. 创建1个或多个lambda函数，将dashboard展示所需数据（参考dashboard部分需求）从Easyun环境下查出来写入dynamoDB
3. 创建cloudwatch event或 EventBridge 触发lambda执行(time-based)

> Part2: Easyun的serverless部署方案（先做一些验证工作）
1. 基于APIGateway提供后端api
2. 基于lambda函数实现管理功能 