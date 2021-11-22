### Task

1. 提供基于最佳实现的环境参数，反馈给前端作为默认环境参数
    VPC： Easyun-VPC , 10.10.0.0/16
    PubSubnet：
        Public Subnet 1: pub-subnet-1, 10.10.1.0/24, az-1a
        Public Subnet 2: pub-subnet-2, 10.10.2.0/24, az-1b
        route table: easyun-route-igw
    PriSubnet：
        Private Subnet 1: pri-subnet-1, 10.10.21.0/24, az-1a
        Private Subnet 2: pri-subnet-2, 10.10.22.0/24, az-1b
        route table: easyun-route-nat
    Gateway:
        Internet gateway: easyun-igw
        NAT gateway: easyun-nat
    Secrity Group:
        Default: easyun-sg-default
            In-bound:  Ping [option]
            In-bound:  ssh  [option]
            In-bound:  rdp  [option]
        Web: easyun-sg-webapp
            In-bound:  TCP:80 0.0.0.0/0
            In-bound:  TCP:443 0.0.0.0/0
        DB: easyun-sg-database
            In-bound:  TCP:3306 0.0.0.0/0
            In-bound:  TCP:5432 0.0.0.0/0
            In-bound:  TCP:1521 0.0.0.0/0
            In-bound:  TCP:1443 0.0.0.0/0
    Keypair：
        Default： key-easyun-user
    
2. 执行数据中心初始化，基于前端返回的实际参数进行资源创建，包括：
    a. create easyun vpc
    b. create 2 x pub-subnet
    c. create 2 x pri-subnet
    d. create 1 x easyun-igw (internet gateway)
    e. create 1 x easyun-nat (nat gateway)
    f. create 1 x easyun-route-igw
    g. create 1 x easyun-route-nat
    h. create 3 x easyun-sg-xxx
    i create 1 x key-easyun-user (默认keypair)
    
3. 响应前端api请求，反馈已创建的资源信息
    a. AWS环境：返回Easyun服务端部署所在region 及 Available Zones信息；
    b. 子网信息：返回当前环境下的子网信息，包含：id，名称，公网/私网，地址段，所处可用区 等信息；
    c. 安全组信息：返回当前环境下的安全组信息，包含：id，名称，
    d. AMI信息：返回当前region下的常用AMI信息，包括：ID，平台，OS名称，版本等信息；
    e. 实例类型：返回当前region下的实例类型(5大类，4小类)，包含：名称、家族分类、vCPU、内存、网络、单价(可选)等信息；
    f. Key信息：返回当前环境下的KeyPair名称，下载链接信息；