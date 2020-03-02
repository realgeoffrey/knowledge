# 环境安装、配置

## 目录

><details>
><summary>若 同网关的其他机器 配置hosts：<code>「电脑A的ip」 「域名B」</code>，则这些机器访问 「域名B」 就可以走 电脑A 的映射。</summary>
>
>
>具体步骤：
>
>1. 电脑A的设置：
>
>    1. nginx（虚拟主机、或代理转发，或用其他工具）监听 「域名B」 到80端口
>    2. hosts设定 「域名B」 到 `127.0.0.1`
>2. 同网关的其他机器的设置：
>
>    1. hosts设定 「域名B」 到 「电脑A的ip」
>
>结果：电脑A、同网关的其他机器 访问 「域名B」 都可以映射到 电脑A 的80端口。
></details>

1. [nginx环境配置（Windows）](nginx环境配置（Windows）/README.md)
2. [nginx+PHP配置（macOS）](nginx+PHP配置（macOS）/README.md)

>1. [WAMP环境配置（Windows）](WAMP环境配置（Windows）/README.md)
>2. [LAMP环境配置（CentOS7.0）](LAMP环境配置（CentOS7.0）/README.md)
>3. [Laravel框架配置+LNMP环境配置（Ubuntu15.04）](Laravel框架配置+LNMP环境配置（Ubuntu15.04）/README.md)
>4. [SVN环境配置（CentOS）](SVN环境配置（CentOS）/README.md)
>5. [Vagrant环境配置](Vagrant环境配置/README.md)
