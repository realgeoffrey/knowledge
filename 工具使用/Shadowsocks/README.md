# Shadowsocks使用
>详细了解请访问：[ShadowSocks（影梭）不完全指南](http://www.auooo.com/2015/06/26/shadowsocks%EF%BC%88%E5%BD%B1%E6%A2%AD%EF%BC%89%E4%B8%8D%E5%AE%8C%E5%85%A8%E6%8C%87%E5%8D%97/)。

### 客户端使用
1. 系统代理：默认代理系统所有网络流量。

    1. 全局模式：所有访问请求都走Shadowsocks代理。
    2. PAC模式：按照PAC（代理自动配置）列表决定：①直接连接，②走Shadowsocks代理。
2. 关闭系统代理（手动模式）：配置了**SOCKS5**或**HTTP**代理（默认代理服务器为`127.0.0.1:1080`）的才走Shadowsocks代理，比如chrome的[SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega)插件或qq等可以使用SOCKS5或HTTP代理的软件。
3. PAC：代理自动配置，一般使用[gfwlist](https://github.com/gfwlist/gfwlist)列表。
4. 允许来自局域网的连接（windows）：同局域网下，其他设备填写好代理的主机ip和端口号，就可以走其他主机的Shadowsocks代理。

>SwitchyOmega配置备份文件：
>
>[https://raw.githubusercontent.com/realgeoffrey/knowledge/master/工具使用/Shadowsocks使用/OmegaOptions.bak](https://raw.githubusercontent.com/realgeoffrey/knowledge/master/工具使用/Shadowsocks使用/OmegaOptions.bak)