# 命令行备忘

### 其他命令
1. ping地址测试

    ```bash
    ping IP地址
    ```
2. ssh登录

    ```bash
    ssh 用户名@地址 -p 端口号
    ```
3. 远程拷贝文件

    ```bash
    scp -P 端口号 远程用户名@远程地址:远程地址路径 本地存放路径
    ```

    >注意本机（目录权限）和远程主机的权限（文件权限）。
4. 改密码

    ```bash
    passwd
    ```
5. 指令在PATH变量的路径

    ```bash
    which 指令
    ```
6. 打开文件（夹）

    ```bash
    open 路径/文件  # macOS
    ```
7. hosts文件位置

    1. macOS、Linux：**/etc/hosts**
    2. Windows：**C:\Windows\System32\drivers\etc\hosts**
8. 验证文件的数字签名

    1. MD5

        ```bash
        md5 文件  #或md5sum
        ```
    2. SHA1

        ```bash
        shasum 文件  #或sha1sum
        ```
9. 查看设置环境变量

    ```bash
    echo $变量        # 查看变量

    export 变量=值    # 设置变量
    ```
10. 查看本机IP

    ```bash
    ipconfig    # Windows系统

    ifconfig    # macOS系统，查看en0后的inet数据
    ```