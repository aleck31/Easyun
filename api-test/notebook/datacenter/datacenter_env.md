# 数据中心初始化相关资源

网络部分
----
### 1. VPC
* Easyun-VPC:     10.10.0.0/16

### 2. Subnet
* pub-subnet-1:   10.10.1.0/24  
* pub-subnet-2:   10.10.2.0/24  
    Auto-assign IPv4Info:   Enable auto-assign public IPv4 address

* pri-subnet-1:   10.10.21.0/24  
* pri-subnet-2:   10.10.22.0/24

### 3. Gateway
* easyun-igw:
    - Attach to VPC:  Easyun-VPC
* easyun-nat:
    - Subnet:     pub-subnet-1
    - Connectivity type:  public
    - Elastic IP allocation ID:   new

### 4. Route table
* easyun-route-igw  
    - 0.0.0.0/0	igw-0f18ad5616188cc93  
    - subnet associations: pub-subnet-1,pub-subnet-2
* easyun-route-nat  
    - 0.0.0.0/0	nat-0f33325a2517a28d6  
    - subnet associations: pri-subnet-1,pri-subnet-2


EC2部分
----
### 5. Security Group: 
* easyun-webapp  
        IPv4	Custom ICMP - IPv4	Echo Request	N/A	0.0.0.0/0  
	    IPv4	SSH	TCP	22	0.0.0.0/0  
	    IPv4	HTTP	TCP	80	0.0.0.0/0  
	    IPv4	HTTPS	TCP	443
* easyun-database  
        IPv4	Custom ICMP - IPv4	Echo Request	N/A	0.0.0.0/0  
	    IPv4	MysQL	TCP	3306	0.0.0.0/0  
	    IPv4	PgSQL	TCP	5432  
        IPv4	MSSQL	TCP	1433  
        IPv4	Oracle	TCP	1521
* easyun-test  
        IPv4	Custom ICMP - IPv4	Echo Request	N/A	0.0.0.0/0  
	    IPv4	SSH	TCP	22	0.0.0.0/0  
	    IPv4	HTTP	TCP	80	0.0.0.0/0  
	    IPv4	HTTPS	TCP	443  

### 6. KeyPair
* easyun-user-key

其它
----
### 7. Tags
* 所有资源默认打上标签 
    - Flag:   Easyun