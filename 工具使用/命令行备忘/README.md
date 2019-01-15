# 命令行备忘

>- 学会在终端中进行命令查询
>
>    1. `命令 --help`
>    2. `man 命令`
>    3. `info 命令`
>    4. `whatis 命令`
>    - [tldr](https://github.com/tldr-pages/tldr)

### 其他命令
1. ping地址测试

    ```bash
    ping “IP地址”
    ```
2. ssh登录

    ```bash
    ssh “用户名@地址” -p “端口号”
    ```
3. 远程复制文件

    ```bash
    scp -P “端口号” “远程用户名@远程地址”:“远程地址路径” “本地存放路径”
    ```

    >注意：本机（目录权限）和远程主机的权限（文件权限）。
4. 改密码

    ```bash
    passwd
    ```
5. 指令在PATH变量的路径

    ```bash
    which “指令”
    ```
6. （macOS）打开文件（夹）

    ```bash
    open “路径/文件”
    ```
7. hosts文件位置

    1. macOS、Linux

        `/etc/hosts`
    2. Windows

        `C:\Windows\System32\drivers\etc\hosts`
8. 验证文件的数字签名

    1. MD5

        ```bash
        # macOS
        md5 “文件”
        md5 -s “字符串”    # 或`echo -n “字符串” | md5`

        # Windows
        md5sum.exe “文件”
        echo -n “字符串” | md5sum.exe
        ```
    2. SHA

        ```bash
        # macOS
        shasum “文件”
        echo -n “字符串” | shasum
        # 使用特定算法：`-a, --algorithm   1 (default), 224, 256, 384, 512, 512224, 512256`

        # Windows
        sha1sum.exe “文件”
        echo -n “字符串” | sha1sum.exe
        # 使用特定算法：`sha224sum.exe sha256sum.exe sha384sum.exe sha512sum.exe`
        ```
9. 查看设置环境变量

    ```bash
    echo $“变量”          # 查看变量

    export “变量”=“值”     # 设置变量
    ```
10. 查看本机IP

    ```bash
    # macOS
    ifconfig    # 查看`en0 的 inet`

    # Windows
    ipconfig    # 查看`以太网适配器 本地连接 的 IPv4 地址`
    ```
11. 执行文件

    >要对路径名/文件名中的`标点`和`空格`进行`\`转义。

    ```bash
    ./文件名.sh

    . 路径名/文件名.sh
    ```
12. （Unix-like）开机自动运行的脚本

    ```bash
    # macOS
    vi ~/.bash_profile  # bash
    vi ~/.zshrc         # zsh

    # 如：可以把定义环境变量放在里面`export NODE_ENV=development`

    # source 脚本   # 当前运行一遍
    ```
13. 查看端口占用，杀掉进程

    1. macOS

        ```bash
        lsof -i :“端口号”

        kill “PID”
        ```
    2.  Windows（需要在cmd.exe进行）

        ```bash
        netstat -aon | findstr “端口号”  # 获得某端口号的任务PID

        tasklist | findstr “PID”          # 获得某PID的任务名
        # 获得任务名之后可以再用`tasklist | findstr “任务名”`确认是否有多个子任务

        taskkill /F /T /PID “PID”           # 需要杀死主进程，否则仅杀死的子进程会被主进程再次创建
        # 或`taskkill /F /T /IM “任务名”`
        # 或去任务管理器结束进程（打开进程->查看->选择列的PID）
        ```
14. （macOS）brew更新

    ```bash
    brew update && brew upgrade && brew cask upgrade
    ```
