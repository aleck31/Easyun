### Task

1. 获取key pair信息：遍历用户account在当前region下的keypair，将名称和下载链接返回给前端；
2. 创建key pair：，在当前region下创建新的keypair，并返回必要状态信息给前端；
3. FreeTier提醒功能：
    a. 日期设置：前端传入账号激活日期，将日期存入easyun后端数据库；
    b. 生命值反馈：提供查询api接口便于前端获取提醒颜色信息在UI上展示，提醒颜色规则：基于当前时间计算出剩余天数，红<30天，绿≥30天
