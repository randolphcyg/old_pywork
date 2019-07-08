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
local 192.168.255.128 #本地IP，既服务器的IP地址
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
### 1.查看是否安装并删除旧版本
rpm -qa | grep mysql   // 这个命令就会查看该操作系统上是否已经安装了mysql数据库

// 普通删除模式   
rpm -e mysql-libs-5.1.73-3.el6_5.x86_64　　         
// 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令
rpm -e --nodeps mysql-libs-5.1.73-3.el6_5.x86_64　　

### 2.离线下载解压安装并启动
// 使用wget命令从mysql官网下载离线包(地址可能不一定是下面这个，请自行更改)
wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz
*这里在主机下载好sftp get到虚机中* 
文件为mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz
// 解压
tar -xvf mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz
解压后文件夹为mysql-5.7.24-linux-glibc2.12-x86_64
将文件夹改名放到/usr/local/mysql
//安装
[root@ mysql]# pwd
/usr/local/mysql
[root@ mysql]# chown -R mysql:mysql *
[root@ mysql]#  ./bin/mysqld --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --initialize
2019-07-04T05:40:42.435333Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
2019-07-04T05:40:42.712449Z 0 [Warning] InnoDB: New log files created, LSN=45790
2019-07-04T05:40:42.771650Z 0 [Warning] InnoDB: Creating foreign key constraint system tables.
2019-07-04T05:40:42.844598Z 0 [Warning] No existing UUID has been found, so we assume that this is the first time that this server has been started. Generating a new UUID: 4365889b-9e1e-11e9-9cdd-000c291def52.
2019-07-04T05:40:42.846341Z 0 [Warning] Gtid table is not ready to be used. Table 'mysql.gtid_executed' cannot be opened.
2019-07-04T05:40:42.847849Z 1 [Note] A temporary password is generated for root@localhost: wHQz7N;w(n>_

这里出现了mysql登陆初始密码：wHQz7N;w(n>_

将mysql/目录下除了data/目录的所有文件，改回root用户所有
[root@localhost mysql]# chown -R root .
#mysql用户只需作为mysql/data/目录下所有文件的所有者
[root@localhost mysql]# chown -R mysql data

### 3.文件配置
复制启动文件 [root@localhost mysql]# cp support-files/mysql.server /etc/init.d/mysqld

[root@localhost mysql]# chmod 755 /etc/init.d/mysqld

[root@localhost bin]# cp /usr/local/mysql/bin/my_print_defaults  /usr/bin/

#修改启动脚本
[root@localhost mysql]# vi /etc/init.d/mysqld
#修改项：
basedir=/usr/local/mysql/
datadir=/usr/local/mysql/data
port=3306

### 4.启动服务并使用
[root@localhost mysql]# service mysqld start
#加入环境变量，编辑 /etc/profile，这样可以在任何地方用mysql命令了
[root@localhost mysql]# vi /etc/profile
#在末尾添加mysql路径
PATH=$PATH:/usr/local/mysql/bin
export PATH
#刷新立即生效
[root@localhost mysql]# source /etc/profile

 配置以上信息之后，基本就可以启动了mysql（如果不能启动，请看最后的配置文件），但是现在还缺少mysql的配置文件，即my.cnf文件（没有它Mysql也可以使用内置的默认参数启动），最后说
接下来就可以使用命令登录mysql了
[root@localhost bin]# mysql -uroot -p
Enter password: “ 这里数据上面的： m6Yifsio7n<*”
##登录成功

#然后设置root密码
mysql>SET PASSWORD = PASSWORD('3588');
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
--------------------- 

