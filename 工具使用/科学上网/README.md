# 科学上网

## Shadowsocks

### 客户端使用
1. 系统代理：默认代理系统所有网络流量。

    1. PAC模式：按照PAC（代理自动配置）列表决定：①直接连接，②走Shadowsocks代理。
    2. 全局模式：所有访问请求都走Shadowsocks代理。
    3. 手动模式：监听特定端口号的请求。
2. 关闭系统代理（手动模式）：配置了**SOCKS5**或**HTTP**代理（默认代理服务器为`127.0.0.1:1080`）的才走Shadowsocks代理，比如chrome的[SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega)插件或qq等可以使用SOCKS5或HTTP代理的软件。
3. PAC：代理自动配置，一般使用[gfwlist](https://github.com/gfwlist/gfwlist)列表。
4. 允许来自局域网的连接（windows）：同局域网下，其他设备填写好代理的主机ip和端口号，就可以走其他主机的Shadowsocks代理。

>SwitchyOmega配置备份文件：
>
>[https://raw.githubusercontent.com/realgeoffrey/knowledge/master/工具使用/科学上网/OmegaOptions.bak](https://raw.githubusercontent.com/realgeoffrey/knowledge/master/工具使用/科学上网/OmegaOptions.bak)

### 服务端安装
>来自[teddysun:shadowsocks_install](https://github.com/teddysun/shadowsocks_install#shadowsocks-gosh)。

1. 在Linux服务器（CentOS，Debian，Ubuntu）安装[shadowsocks-go](https://github.com/shadowsocks/shadowsocks-go)。

    ```bash
    wget --no-check-certificate -O shadowsocks-go.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-go.sh

    chmod +x shadowsocks-go.sh
    ./shadowsocks-go.sh 2>&1 | tee shadowsocks-go.log
    ```

    >1. 密码：自己设定（默认：teddysun.com）
    >2. 服务器端口：自己设定（默认：8989）
2. 查看状态

    ```bash
    /etc/init.d/shadowsocks start   #启动
    /etc/init.d/shadowsocks stop    #停止
    /etc/init.d/shadowsocks restart #重启
    /etc/init.d/shadowsocks status  #状态
    ```
3. 卸载

    ```bash
    ./shadowsocks-go.sh uninstall
    ```

---
## IKEV2(IKEV1)的VPN
>来自[quericy:one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn)。

### 客户端使用
1. 选择VPN (IKEv2)或VPN (IKEv1)模式。
2. **服务器地址**和证书保持一致（取决于签发证书ca.cert.pem时使用的是ip还是域名）。
3. **远程ID**和服务器地址一致。
4. **本地ID**不填。
5. **鉴定设置**为用户名。**用户名**和**密码**根据服务器设置填写。

    1. 若服务器使用**SSL证书**，则客户端不需要导入证书。
    2. 若服务器使用**自签名证书**，则客户端必须导入证书

        把服务端证书ca.cert.pem改名为**ca.cert.per**，客户端导入并选择**始终信任此证书**。

### 服务端安装
>除了第一个vps类型选择、倒数第二个独立ip使用SNAT规则，其他都可以简单使用默认。

1. 下载、运行脚本

    ```bash
    wget --no-check-certificate https://raw.githubusercontent.com/quericy/one-key-ikev2-vpn/master/one-key-ikev2.sh

    chmod +x one-key-ikev2.sh
    bash one-key-ikev2.sh
    ```
2. 输入配置
    1. 选择**vps类型**：1：Xen、KVM，2：OpenVZ。
    2. 设置**ip**：服务器ip，绑定的域名（默认服务器ip）。
    3. 选择**证书类型**：yes：证书颁发机构签发的SSL证书，no：生成自签名证书（默认生成自签名证书）。

        1. 证书颁发机构签发的SSL证书

            未测试
        2. 生成自签名证书

            选择默认的Country（C）、Organization（O）、Common Name（CN）。
    4. 设置**pkcs12证书的密码**（默认为空）。
    5. 选择是否使用**SNAT规则**（默认不使用）

        独立ip的vps才可以使用SNAT，可提升防火墙对数据包的处理速度。如果服务器网络设置了NAT（如AWS的弹性ip机制），则填写网卡连接接口的ip地址。
    6. 选择**防火墙配置**：yes：firewall，no：iptables（默认no：iptables）。
3. 配置用户名、密码、密钥

    1. 默认用户名、密码、密钥将以绿字显示，可根据提示自行修改，多用户则在配置文件中按格式一行一个（多用户时用户名不能使用%any）

        ```bash
        vi /usr/local/etc/ipsec.secrets
        ```
    2. 保存并重启服务生效

        ```bash
        ipsec restart
        ```
4. 客户端验证

    1. 将提示信息中生成的证书文件**ca.cert.pem**拷贝到客户端，修改后缀名为**ca.cert.cer**后导入。

        远程拷贝：
        ```bash
        scp -P 端口号 服务器名@服务器地址:/root/my_key/ca.cert.pem 本地存放路径
        ```
    2. 设备使用Ikev1无需导入证书，而是需要在连接时输入密钥（PSK）。
5. ipsec启动问题

    服务器重启后默认ipsec不会自启动。

    1. 命令需要手动开启，

        ```bash
        ipsec start   #启动服务

        ipsec stop    #关闭服务
        ipsec restart #重启服务
        ipsec reload  #重新读取
        ipsec status  #查看状态
        ipsec --help  #查看帮助
        ```
    2. 添加**/usr/local/sbin/ipsec start**到自启动脚本文件中(如rc.local等)

        ```bash
        vi /etc/rc.d/rc.local

        #添加
        /usr/local/sbin/ipsec start
        ```
6. 卸载

    1. 卸载

        ```bash
        cd ~/strongswan-5.5.1

        make uninstall
        ```
    2. 删除脚本所在目录的相关文件（one-key-ikev2.sh、strongswan.tar.gz、strongswan文件夹、my_key文件夹）。
    3. 检查iptables配置。

---
## 通过docker安装shadowsocks服务器和VPN服务器（最快捷方式）
>[docker](https://www.docker.com/)建议Linux内核在3.0以上。[Bandwagon](https://bwh1.net/)内核只有2.6，无法使用docker。

1. 安装、启动docker

    ```bash
    curl -fsSL https://get.docker.com/ | sh #安装。或用官网安装方式

    service docker start    #启动
    ```
2. shadowsocks

    ```bash
    docker run -d -p 服务端口号:8888 imlonghao/shadowsocks-go -p 8888 -k 密码 -m aes-256-cfb -t 60
    ```

3. VPN

    1. IPsec(Cisco)

        ```bash
        docker run -d -p 500:500/udp -p 4500:4500/udp -p 1701:1701/udp -e VPN_USER=账户名称 -e VPN_PASSWORD=密码 -e VPN_PSK=密钥 --privileged philplckthun/strongswan
        ```
    2.  PPTP

        ```bash
        docker run -d --privileged -p 1723:1723 -v /etc/ppp/chap-secrets:/etc/ppp/chap-secrets mobtitude/vpn-pptp
        /etc/ppp/chap-secrets: 账户 * 密码 *
        ```