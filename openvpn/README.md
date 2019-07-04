## openvpn使用配置记录
>https://www.ilanni.com/?p=9847

### vars配置文件
```
[root@ easyrsa3]# cat vars

set_var EASYRSA_REQ_COUNTRY “CN” //定义所在国家

set_var EASYRSA_REQ_PROVINCE “ShangHai” //所在省份

set_var EASYRSA_REQ_CITY “ShangHai” //所在城市

set_var EASYRSA_REQ_ORG “Test” //所在组织

set_var EASYRSA_REQ_EMAIL “test@test.com” //定义邮箱地址

set_var EASYRSA_REQ_OU “TestOpenVpn” //所在单位
```
### server.conf服务器端配置文件
```
cal 192.168.255.128 #本地IP，既服务器的IP地址

port 1194 #vpn端口，定义openvpn监听的的端口，默认为1194端口。

proto udp #定义openvpn使用的协议，默认使用UDP。如果是生产环境的话，建议使用TCP协议。

dev tun #相对应的tab，tab是桥接模式，tun为虚拟网卡模式

#定义openvpn运行时使用哪一种模式，openvpn有两种运行模式一种是tap模式，一种是tun模式。

#tap模式也就是桥接模式，通过软件在系统中模拟出一个tap设备，该设备是一个二层设备，同时支持链路层协议。

#tun模式也就是路由模式，通过软件在系统中模拟出一个tun路由，tun是ip层的点对点协议。

#具体使用哪一种模式，需要根据自己的业务进行定义。

ca /etc/openvpn/keys/ca.crt #ca证书

#定义openvpn使用的CA证书文件，该文件通过build-ca命令生成，CA证书主要用于验证客户证书的合法性。

cert /etc/openvpn/keys/server.crt #服务器端证书

key /etc/openvpn/keys/server.key  #服务器端的key，需保密

dh /etc/openvpn/keys/dh.pem #定义Diffie hellman证书文件。

server 10.0.2.0 255.255.255.0 #普通vpn用户虚拟IP的网段 定义openvpn在使用tun路由模式时，分配给client端分配的IP地址段。

ifconfig-pool-persist /etc/openvpn/ipp.txt #虚拟IP记录文件，防止重复分发IP

push "route 192.168.0.0 255.255.255.0" #网客户端注入route规则，用来实现部分网段走vpn，其他网段仍然走客户端电脑的默认链路
                                        
push "route 192.168.1.0 255.255.255.0" #向客户端推送的路由信息，假如客户端的IP地址为10.8.0.2，要访问192.168.1.0网段的话，使用这条命令就可以

push "route 192.168.2.0 255.255.255.0"

push "route 192.168.3.0 255.255.255.0"

push "route 192.168.4.0 255.255.255.0"

push "route 192.168.5.0 255.255.255.0"

client-config-dir /etc/openvpn/ccd #用户个性化配置目录，特殊用户与管理员用户的网段就是通过这个文件夹下的配置实现的

route 10.0.0.0 255.255.255.0 #添加本地route，将特殊用户与管理员用户的网段加入vpn服务器的路由表中

route 10.0.1.0 255.255.255.0

push "dhcp-option DNS 114.114.114.114" #为客户端电脑得到的虚拟IP推送DNS

duplicate-cn #允许同一个证书或同一个用户同一时间多次登录

keepalive 10 120 #客户端与服务器的心跳包，互相知道对方是否断开

tls-auth /etc/openvpn/keys/ta.key 0 #ta证书，需保密

cipher AES-256-CBC #加密规则

comp-lzo #兼容旧的客户端

max-clients 100 #客户端数量

persist-key #通过keepalive检测超时后，重新启动VPN，不重新读取keys，保留第一次使用的keys。

persist-tun #通过keepalive检测超时后，重新启动VPN，一直保持tun或者tap设备是linkup的。否则网络连接，会先linkdown然后再linkup。

status /etc/openvpn/logs/openvpn-status.log #日志文件（状态信息）

log /etc/openvpn/logs/openvpn.log #日志文件（覆盖原有日志）

verb 3 #日志等级

plugin /usr/lib64/openvpn/plugin/lib/openvpn-auth-pam.so login #我是64位操作系统

client-cert-not-required #只需验证用户名密码，不要求客户端证书

username-as-common-name #用户名做common-name，既用户名相当于客户端名，个性化的时候使用用户名即可。
```
### client.conf配置文件
```
client #标记为客户端

dev tun #与服务器端配置一致

proto udp #与服务器端配置一致

remote 192.168.255.128 1194 #服务器端IP与端口,与服务器保持一致

resolv-retry infinite

nobind

persist-key

persist-tun

ca ca.crt #ca证书

;cert client.crt #客户端证书

;key client.key #客户端证书的key

remote-cert-tls server #服务器证书的名字

tls-auth ta.key 1 #ta证书，如果服务器端配置，则客户端必须配置

cipher AES-256-CBC #与服务器端配置一致

comp-lzo #与服务器端配置一致

verb 3 #设置日志记录冗长级别

auth-user-pass pwd.txt #读取pwd.txt用户密码文件
```

## mysql5.7.24离线安装配置
```
### 查看是否安装并删除旧版本
rpm -qa | grep mysql   // 这个命令就会查看该操作系统上是否已经安装了mysql数据库

// 普通删除模式   
rpm -e mysql-libs-5.1.73-3.el6_5.x86_64　　         
// 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令
rpm -e --nodeps mysql-libs-5.1.73-3.el6_5.x86_64　　

### 离线下载解压安装并启动
// 使用wget命令从mysql官网下载离线包(地址可能不一定是下面这个，请自行更改)
wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz

// 解压
tar -xvf mysql-5.7.24-1.el6.x86_64.rpm-bundle.tar

// 安装工具包以及兼容性相关包
rpm -ivh mysql-community-common-5.7.24-1.el6.x86_64.rpm
rpm -ivh mysql-community-libs-5.7.24-1.el6.x86_64.rpm
rpm -ivh mysql-community-libs-compat-5.7.24-1.el6.x86_64.rpm

// 安装mysql服务端
rpm -ivh mysql-community-server-5.7.24-1.el6.x86_64.rpm

// 安装mysql客户端
rpm -ivh mysql-community-client-5.7.24-1.el6.x86_64.rpm

// 启动mysql
service mysqld start

### 基本配置
// 创建配置文件
cp /usr/share/mysql/my-default.cnf /etc/my.cnf

// 修改配置文件/etc/my.cnf，最后一行加上
lower_case_table_names=1  #表名不区分大小写

// 由于mysql5.7有弱密码限制，可以在配置文件中加上下面内容，关闭限制
[mysqld]
validate_password=off

// 查看root用户初始密码并修改root密码
grep 'temporary password' /data/mysql/error.log 
set password = password('your_password');

// 创建用户并授权
grant all on *.* to name@'%' identified by "password" with grant option;
flush privileges;
```
