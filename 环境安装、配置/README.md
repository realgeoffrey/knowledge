# 环境安装、配置

## 目录

><details>
><summary>其他机器如何通过 hosts 访问电脑 A 上的本地站点？</summary>
>
>
>具体步骤：
>
>1. 电脑A的设置：
>
>    1. nginx 监听电脑 A 的局域网 IP 和端口（如 80），用 `server_name 域名B;` 匹配站点。确认防火墙允许测试机器访问该端口。
>    2. 若 A 自己也要用该域名访问，可在 A 的 hosts 中将域名指向监听地址；只有 nginx 也监听回环接口时才填 `127.0.0.1`。
>2. 能连接电脑 A 的其他机器：
>
>    1. hosts设定 「域名B」 到 「电脑A的ip」
>
>在客户端访问 `http://域名B/` 即可使用 80 端口。若 nginx 监听 8080，地址写作 `http://域名B:8080/`；hosts 只负责域名到 IP 的映射。
></details>

1. [nginx环境配置（Windows）](nginx环境配置（Windows）/README.md)
2. [nginx+PHP配置（macOS）](nginx+PHP配置（macOS）/README.md)

- <details>

    <summary>其他（多为历史环境记录，使用前需确认系统版本仍受支持）</summary>

    1. [WAMP环境配置（Windows）](WAMP环境配置（Windows）/README.md)
    2. [LAMP环境配置（CentOS7.0）](LAMP环境配置（CentOS7.0）/README.md)
    3. [Laravel框架配置+LNMP环境配置（Ubuntu15.04）](Laravel框架配置+LNMP环境配置（Ubuntu15.04）/README.md)
    4. [SVN环境配置（CentOS）](SVN环境配置（CentOS）/README.md)
    5. [Vagrant环境配置](Vagrant环境配置/README.md)
    </details>
