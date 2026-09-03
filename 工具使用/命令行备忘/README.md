# 命令行备忘

## 目录
1. [命令花费时间](#命令花费时间)
1. [查找命令](#查找命令)
1. [网络连接测试](#网络连接测试)
1. [IPv6相关命令](#ipv6相关命令)
1. [`ssh`](#ssh)
1. [远程复制文件（夹）](#远程复制文件夹)
1. [同步文件（夹）](#同步文件夹)
1. [图形界面文件上传/下载（lrzsz）](#图形界面文件上传下载lrzsz)
1. [改密码](#改密码)
1. [hosts文件位置](#hosts文件位置)
1. [校验文件哈希](#校验文件哈希)
1. [查看本机 IP](#查看本机-ip)
1. [执行或加载脚本](#执行或加载脚本)
1. [Shell 类型与登录 Shell](#shell-类型与登录-shell)
1. [Shell 启动配置文件](#shell-启动配置文件)
1. [查看端口、网络连接和进程](#查看端口网络连接和进程)
1. [查看磁盘空间占用](#查看磁盘空间占用)
1. [创建文件](#创建文件)
1. [查看文件](#查看文件)
1. [清空文件内容](#清空文件内容)
1. [查看 group、user](#查看-groupuser)
1. [指令的别名](#指令的别名)
1. [`adb`](#adb)
1. [`sleep`](#sleep)
1. [`xargs`](#xargs)
1. [批量删除文件](#批量删除文件)

1. [`read`](#read)
1. [`sed`](#sed)
1. [`ln`](#ln)
1. [`vi`](#vi)
1. [Shell环境的运行参数](#shell环境的运行参数)
1. [压缩、解压缩](#压缩解压缩)
1. [macOS命令](#macos命令)

    1. [（macOS）brew更新](#macosbrew更新)
    1. [（macOS）打开文件（夹）](#macos打开文件夹)
    1. [（macOS）钥匙串](#macos钥匙串)
    1. [（macOS）管理配置描述文件](#macos管理配置描述文件)

---
>- 学会在终端中进行命令查询
>
>    1. `「命令」 --help`
>    2. `man 「命令」`
>    3. [`tldr`](https://github.com/tldr-pages/tldr) `「命令」`（安装：`brew install tldr`）
>    4. `info 「命令」`
>    5. `whatis 「命令」`
>
>    >`「命令」`可以是 「命令」+「子命令」，如：`docker info`。

>可阅读：[You-Dont-Need-GUI](https://github.com/you-dont-need/You-Dont-Need-GUI)、[bash-guide](https://github.com/Idnan/bash-guide)。

#### 命令花费时间
```shell
time 「命令」
# e.g. time ls
```
- [hyperfine](https://github.com/sharkdp/hyperfine)：多次运行对比耗时（`brew install hyperfine`）

#### 查找命令
```shell
command -v 「命令」  # 输出将被执行的路径或定义（POSIX 推荐）
type -a 「命令」     # 列出同名别名、函数、内建与可执行文件
which 「命令」       # 仅查 PATH 中的可执行文件，看不到别名/函数
```

#### 网络连接测试

><details>
><summary>e.g. <code>22</code>端口号测试都通过，但一执行git操作就报<code>22</code>端口号问题</summary>
>
>`Connection closed` 或 `Connection reset` 表示 TCP 可能已通，但 SSH 协议交互被中断：
>
>1. `nc`/`telnet` 只能确认 TCP 端口可达，不能证明 SSH 握手成功。
>2. 防火墙、代理、网关、服务端配置或临时故障都可能中断连接。
>3. 可用 `ssh -T git@github.com`（或对应 Git 主机）验证 SSH 交互。
></details>

1. `ping`

    发 ICMP 回显请求，看可达性、延迟、丢包；不代表带宽。ICMP 无端口概念，不能测端口；目标禁 ICMP 时也会“不通”。

    ```shell
    ping -c 4 「域名或IP」   # Linux / 多数环境：发 4 次后退出
    ping -c 4 「域名或IP」   # macOS 同样支持 -c；不写 -c 会一直 ping 直到 Ctrl+C
    ```
2. `curl`

    发起 HTTP(S) 等请求，查看响应。

    ```shell
    curl "「URL」"                                      # 响应体
    curl -i "「URL」"                                   # 响应头 + 响应体
    curl -I "「URL」"                                   # 仅响应头（HEAD）
    curl -L "「URL」"                                   # 跟随重定向
    curl -o "「文件」" "「URL」"                        # 下载到文件
    curl -H '「请求头: 值」' "「URL」"                  # 设置请求头
    curl -X 「方法，如 POST」 -d '「body」' "「URL」"   # 方法与请求体
    curl -g "「URL」"                                   # 不解析 URL 中的 `{}`、`[]`
    curl -x http://127.0.0.1:8899 "「URL」"              # 经 HTTP 代理
    ```
3. `nc` / `telnet`

    测 TCP 端口是否可连。`telnet` 明文，勿用于真实登录；端口检测优先 `nc`。

    ```shell
    nc -vz 「IP/域名」 「端口」
    # macOS：brew install telnet
    telnet 「IP/域名」 「端口」
    ```
4. `nslookup`

    查 DNS 记录，排查解析问题。

    ```shell
    nslookup 「域名」
    nslookup -type=MX 「域名」
    ```
5. `dig`

    从 DNS 服务器查主机记录，输出比 `nslookup` 更完整，排障时常用。

    ```shell
    dig 「域名」
    dig 「域名」 +short          # 仅答案
    dig @8.8.8.8 「域名」 A     # 指定服务器与类型
    ```
#### IPv6相关命令
```shell
nslookup -type=AAAA 「域名」

dig 「域名」 AAAA

ping6 「域名」    # macOS（也可用 ping -6）
ping -6 「域名」  # Linux
curl -6 "「URL」"
```

#### `ssh`
```shell
ssh -p 「端口号，默认 22」 「用户名@地址」
ssh -i 「私钥路径」 「用户名@地址」
ssh -v 「用户名@地址」   # 调试连接；-vv / -vvv 更详细
```

- 确认远程主机密钥确已更换后，删除 `known_hosts` 中该主机旧记录；勿整文件删除。

    ```shell
    ssh-keygen -R 「地址」
    ssh-keygen -R '[「地址」]:「端口号」'  # 非默认端口
    ```

#### 远程复制文件（夹）
```shell
# 注意：scp 用大写 -P 指定端口；ssh 用小写 -p
scp -P 「端口号，默认 22」 「来源文件」 「目标路径」
scp -r -P 「端口号」 「来源目录」 「目标路径」
```

1. 远程 -> 本地

    ```shell
    scp 「远程用户名@远程地址」:「远程文件」 「本地存放路径」
    ```
2. 本地 -> 远程

    ```shell
    scp 「本地文件」 「远程用户名@远程地址」:「远程存放路径」
    ```

>注意本机与远程的目录/文件权限。大目录、断点续传、排除规则优先用 `rsync`。

#### 同步文件（夹）
```shell
rsync -av --progress 「来源路径」 「目标路径」
rsync -avn 「来源路径」 「目标路径」   # dry-run：只预览，不真正写
```

后续同步只传差异。源路径末尾有 `/` 表示“同步目录**内容**”，无 `/` 表示“同步目录**本身**”（目标下多一层同名目录）。

#### 图形界面文件上传/下载（[lrzsz](https://www.ohse.de/uwe/software/lrzsz.html)）
```shell
rz

sz 「文件路径」
```

>iTerm2 用 ZMODEM 需配 Trigger，见 [iTerm2 Triggers](https://iterm2.com/documentation-triggers.html) 与 [iTerm2-zmodem 示例](https://github.com/RobberPhex/iTerm2-zmodem)。脚本里 `rz`/`sz` 路径以 `command -v rz`、`command -v sz` 为准；脚本只需 `chmod +x 「脚本」`，勿 `chmod 777`。

#### 改密码

```shell
passwd                 # 改当前用户密码
# passwd 「用户名」    # 改指定用户（通常需 root）
```

#### hosts文件位置
1. macOS、Linux

    `/etc/hosts`
2. Windows

    `C:\Windows\System32\drivers\etc\hosts`

#### 校验文件哈希
>哈希可做下载完整性校验；MD5、SHA-1 不适合抗碰撞/安全签名，安全用途用 SHA-256/SHA-512 等。

1. MD5

    ```shell
    # macOS
    md5 「文件」
    md5 -s 「字符串」    # 或 echo -n 「字符串」 | md5

    # Linux
    md5sum 「文件」
    echo -n 「字符串」 | md5sum

    # Windows PowerShell / cmd.exe
    certutil -hashfile 「文件」 MD5
    ```

    - Node.js

        ```js
        const crypto = require('node:crypto');
        crypto.createHash('md5').update('字符串').digest('hex');
        ```
2. SHA

    ```shell
    # macOS、Linux（默认算法多为 SHA-1，校验请显式指定）
    shasum -a 256 「文件」
    echo -n 「字符串」 | shasum -a 256
    # -a：1（默认）、224、256、384、512、512224、512256
    # Linux 也可：sha256sum / sha512sum 等

    # Windows PowerShell / cmd.exe
    certutil -hashfile 「文件」 SHA256
    ```
- base64（编码，不是哈希）

    ```shell
    # 字符串
    printf '%s' '字符串' | base64
    printf '%s' '5a2X56ym5LiyCg==' | base64 -d  # Linux
    printf '%s' '5a2X56ym5LiyCg==' | base64 -D  # macOS

    # 文件
    base64 「文件」                 # Linux 编码
    base64 -d 「文件」              # Linux 解码
    base64 -i 「文件」              # macOS 编码
    base64 -D -i 「文件」           # macOS 解码
    ```

    - Node.js

        ```js
        Buffer.from('任意字符串', 'utf-8').toString('base64')               // 编码
        Buffer.from('5Lu75oSP5a2X56ym5Liy', 'base64').toString('utf-8');  // 解码

        // 浏览器：btoa/atob 只适合 Latin-1；Unicode 需先 TextEncoder/解码再转
        btoa('ASCII')
        atob('编码值')
        ```

#### 查看本机 IP
```shell
# macOS（en0 常为 Wi-Fi，以 ifconfig/networksetup 实际接口名为准）
ipconfig getifaddr en0
ifconfig

# Linux
ip -brief address

# Windows
ipconfig
```

>以上是本机网卡地址，不一定是公网出口 IP。查公网可试：`curl -4 ifconfig.me`（第三方服务，结果仅供参考）。

#### 执行或加载脚本
>路径含空格或特殊字符时，用引号包住整个路径。

```shell
chmod +x "「路径/脚本.sh」"
"「路径/脚本.sh」"       # 子 Shell 执行，需正确 Shebang 与执行权限
bash "「路径/脚本.sh」"  # 显式用 Bash，无需执行权限

. "「路径/脚本.sh」"     # 加载进当前 Shell，会改当前环境
# Bash/Zsh 等价：source "「路径/脚本.sh」"
```

#### Shell 类型与登录 Shell
1. 查看系统允许使用的登录 Shell

    ```shell
    cat /etc/shells
    ```
2. 查看当前正在执行的 Shell

    ```shell
    ps -p $$ -o comm=
    ```
3. 查看当前用户的登录 Shell

    ```shell
    printf '%s\n' "$SHELL"
    ```

    >`$SHELL` 是登录 Shell，不一定等于当前正在跑的 Shell。
4. 修改当前用户的登录 Shell

    ```shell
    chsh -s 「Shell 路径，如 /bin/zsh 或 /bin/bash」
    ```

#### Shell 启动配置文件
```shell
# Zsh
vi ~/.zshrc       # 交互式
vi ~/.zprofile    # 登录

# Bash
vi ~/.bashrc        # 交互式非登录
vi ~/.bash_profile  # 登录（若无此文件，部分系统会读 ~/.profile）

# 改完立即生效，或重开终端
source "「刚修改的配置文件」"
```

>这些是 Shell 启动时加载的配置，不是开机服务；开机任务用 macOS `launchd` 或 Linux `systemd`。

#### 查看端口、网络连接和进程
1. 查看端口和网络连接

    ```shell
    # macOS、Linux：谁在监听该 TCP 端口
    lsof -nP -iTCP:「端口号」 -sTCP:LISTEN

    # Linux：所有监听中的 TCP 端口与进程
    ss -lntp

    # Windows cmd.exe
    netstat -aon | findstr 「端口号」
    tasklist | findstr 「PID」
    ```
2. 查看进程

    ```shell
    ps -ef
    pgrep -fl '「命令关键字」'  # macOS、Linux；-f 匹配完整命令行
    ```
3. 结束进程

    ```shell
    # macOS、Linux：先正常退出
    kill 「PID」
    kill -9 「PID」              # 仅在无法正常退出时强制
    pkill -f '「命令关键字」'    # 可能匹配多个，先用 pgrep -fl 确认
    killall 「进程名」

    # Windows cmd.exe
    taskkill /T /PID 「PID」
    taskkill /F /T /PID 「PID」  # 必要时强制
    ```

    >macOS 手势突然失效时可试 `killall Dock`。
#### 查看磁盘空间占用
1. 以磁盘分区为单位查看文件系统的磁盘空间情况

    ```shell
    df -h
    ```
2. 指定的目录或文件所占用的磁盘空间

    ```shell
    # macOS
    du -h -d1 「路径」

    # Linux
    du -h --max-depth=1 「路径」
    ```
3. 查找超过10M的文件

    ```shell
    find 「路径」 -type f -size +10M
    ```

#### 创建文件
1. `touch 「文件名」`

    >已存在则只更新时间戳。
2. `vi 「文件名」`

    >不存在则创建后编辑。
3. `printf '%s\n' '「内容」' > "「文件名」"`

    >已存在则覆盖内容；追加用 `>>`。

#### 查看文件
1. `cat`、`nl`（`nl` 带行号）
2. `tac` 颠倒行序输出（macOS 默认无，可用 `tail -r`）
3. `more`、`less` 分页（交互浏览优先 `less`）
4. `tail` 看尾部

    ```shell
    tail -n 「行数」 「文件名」
    tail -f 「文件名」        # 跟随追加内容（常用于看日志）
    ```
5. `head` 看头部
6. `od` 按字节/八进制等转储

- 查看文件属性

    `ls -lh 「文件名」`

#### 清空文件内容
>会覆盖原内容且通常不可恢复。先确认路径，必要时 `cp "「文件名」" "「文件名」.bak"`。

```shell
: > "「文件名」"             # 清空为 0 字节
printf '\n' > "「文件名」"  # 只留一个换行
```

#### 查看 group、user
1. 查看 Linux 组信息

    ```shell
    cat /etc/group  # 组名:密码占位符:GID:附加成员列表
    ```
2. 查看 Linux 用户信息

    ```shell
    cat /etc/passwd # 用户名:密码占位符:UID:GID:备注:主目录:登录 Shell
    ```
3. `groups`

    ```shell
    groups            # 当前用户所在组
    groups 「用户名」 # 指定用户所在组
    ```

#### 指令的别名
```shell
# alias 只替换命令的第一个词；长路径可包进 cd 别名

alias   # 列出已设别名

alias 「自定义命令名」='「执行命令1」; 「执行命令2」'
alias cproj='cd "「很长的路径」"'

alias 「自定义命令名」      # 打印该别名定义

# 别名后的参数追加到替换后的命令；别名体内不能用 $1 等位置参数

unalias 「自定义命令名」
```

>需要位置参数时用函数：
>
>```shell
>sync-public() {
>  curl --request PUT "https://registry-direct.npmmirror.com/-/package/$1/syncs"
>}
>sync-public fabric-demo
>```

#### `adb`
1. 查看已连接的设备（尝试连接手机）

    ```shell
    adb devices -l
    # List of devices attached
    # 「序列号」       device usb:「…」 product:「…」 model:「…」 device:「…」 transport_id:「数字」
    ```
2. 系统消息输出

    ```shell
    adb logcat
    adb logcat -s 「TAG」:V   # 按 tag 过滤示例

    # 或进设备 shell 再过滤
    adb shell
    logcat | grep 「筛选内容」
    ```
3. 端口转发

    1. 手机访问「手机端口」的流量转发到 PC「PC端口」：

        ```shell
        adb reverse --list
        adb reverse tcp:「手机端口」 tcp:「PC端口」
        adb reverse --remove tcp:「手机端口」
        adb reverse --remove-all
        ```
    2. PC 访问「PC端口」的流量转发到手机「手机端口」：

        ```shell
        adb forward --list
        adb forward tcp:「PC端口」 tcp:「手机端口」
        adb forward --remove tcp:「PC端口」
        adb forward --remove-all
        ```

    >可串联，如：手机端口 A → PC 端口 B → 手机端口 C。
4. 查看手机中所有安装的包

    ```shell
    adb shell pm list packages
    # package:「包名」
    # e.g. package:com.android.settings
    ```
5. 查看界面性能数据

    >来自：[测试界面性能](https://developer.android.com/training/testing/performance)。

    ```shell
    # 需将「GPU 呈现模式分析」设为「在 adb shell dumpsys gfxinfo 中」
    adb shell dumpsys gfxinfo 「PACKAGE_NAME」
    adb shell dumpsys gfxinfo 「PACKAGE_NAME」 framestats
    ```
6. 安装本地包

    ```shell
    adb install 「包地址」
    adb install -r 「包地址」   # 覆盖安装
    ```

#### `sleep`
```shell
sleep 「秒数」           # 延迟后再继续；多数实现支持小数，如 sleep 0.5
```

#### `xargs`
将标准输入转为命令行参数。

```shell
printf '%s\0' '1.txt' '2.txt' '3.txt' | xargs -0 touch  # -0 正确处理空格/特殊字符
# 每批一个参数示例：
# find . -name '*.log' -print0 | xargs -0 -n1 rm
```

#### 批量删除文件
```shell
# 先预览
find . -type f -name "「文件名或通配模式」" -print
# 确认后再删（只匹配文件，不删目录）
find . -type f -name "「文件名或通配模式」" -delete
```

#### `read`
>以下为 Bash 语法；Zsh 等部分选项含义不同。通常加 `-r`，避免把 `\` 当转义。

```shell
# 按 IFS 拆分赋给变量；无变量名时用 REPLY
read -r 「变量名，默认 REPLY」
read -r -t 「秒数」 「变量名」          # 超时
read -r -p '「提示信息」' 「变量名」  # 提示
read -r -a 「数组名」                   # 从下标 0 起
read -r -n 「字符数」 「变量名」       # 读满指定字符数
read -r -e 「变量名」                  # 启用 Readline
read -r -d '「结束符」' 「变量名」      # 读到指定结束符
read -r -s 「变量名」                  # 不回显（密码）
read -r -u 「文件描述符」 「变量名」   # 从指定 fd 读
```

- 逐行读取文件

    ```shell
    #!/bin/bash

    filename='「文件绝对路径」'

    while IFS= read -r myline; do
      printf '%s\n' "$myline"
    done < "$filename"
    ```

#### `sed`
`sed` 默认逐行处理并打印到标准输出，不改原文件；加 `-i` 才就地改。macOS 为 BSD `sed`，`-i` 后必须跟备份后缀参数（可为空字符串）；Linux GNU `sed` 的 `-i` 语法不同。

```shell
# 先预览，不改原文件
sed 's/「匹配内容」/「修改内容」/g' "「原文件」"

# macOS：就地改，并保留 .bak 备份
sed -i '.bak' 's/「匹配内容」/「修改内容」/g' "「原文件」"
sed -i '' 's/「匹配内容」/「修改内容」/g' "「原文件」"  # 不备份

# Linux：就地改，并保留 .bak 备份
sed -i.bak 's/「匹配内容」/「修改内容」/g' "「原文件」"
sed -i 's/「匹配内容」/「修改内容」/g' "「原文件」"  # 不备份

# 匹配内容含 / 时换分隔符
sed "s#abc/def#${变量名}#g" "文件1" > "文件2"
```

#### `ln`
```shell
ln "「源文件」" "「目标文件」"             # 硬链接：同 inode，不复制内容
ln -s "「源文件/目录」" "「目标链接」"  # 符号链接：存路径，源移动/删除后可能失效
```

>硬链接不能跨文件系统，通常也不能指向目录；符号链接可以。

#### `vi`
1. `:set nu` 显示行号；`:set nonu` 关闭
2. `:行号,$s/内容1/内容2` 从「行号」到末行，每行**首次**匹配替换

    `:行号,$s/内容1/内容2/g` 同上，每行**全部**匹配替换

    `:%s/内容1/内容2/g` 全文全部替换

#### Shell环境的运行参数
- `set` 改当前 Shell 选项；子 Shell 会继承，新开的独立 Shell 不一定继承。

    1. [`set`](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) + 配置项

        >e.g. `set -u`
    2. `bash`（或其他 Shell）+ 配置项 + 脚本

        显式指定解释器时，脚本 Shebang 及其参数不参与执行。

        >e.g. `bash -u ./脚本`
    3. 脚本 Shebang 行 + 配置项

        >e.g. `#!/bin/sh -u`

```shell
# 常用配置项：

-u          # 展开未设置变量时报错；非交互式常退出。或 -o nounset
+u          # 默认；取消 -u。或 +o nounset

-x          # 执行前打印命令行（前缀由 PS4 决定，常见为 +）。或 -o xtrace
+x          # 默认；取消 -x。或 +o xtrace

-e          # 未在条件等上下文中处理的命令非 0 则退出（例外较多）。或 -o errexit
+e          # 默认；取消 -e。或 +o errexit

# 默认管道取最后一个命令的退出状态
-o pipefail # 任一命令失败则管道非 0；是否退出另由 -e 等决定
+o pipefail # 默认；取消 pipefail

-E          # ERR trap 可被函数、命令替换、子 Shell 继承。或 -o errtrace
+E          # 默认；取消 -E

-n          # 只查语法不执行。或 -o noexec

-f          # 关闭通配符文件名扩展。或 -o noglob
+f          # 默认；取消 -f。或 +o noglob

-v          # 打印读入的每一行输入。或 -o verbose
+v          # 默认；取消 -v。或 +o verbose
```

#### 压缩、解压缩
1. 压缩文件（夹）

    ```shell
    zip 「归档.zip」 「文件」
    zip -r 「归档.zip」 「源目录」
    zip -er 「归档.zip」 「源目录」  # 交互设密码
    ```
2. 解压缩

    ```shell
    unzip 「归档.zip」
    unzip -l 「归档.zip」   # 只列内容
    unzip -d 「目录」 「归档.zip」
    ```
- 其他压缩/解压缩

    - `lzip`（`brew install lzip`）

        压单个文件；目录需先 `tar` 再压。对已压缩的 `.zip`/`.gz` 再压通常收益很小。

        ```shell
        lzip 「文件」           # 压缩 → 「文件」.lz
        lzip -d 「文件.lz」     # 解压
        ```
    - `gzip` / `gunzip`，`bzip2` / `bunzip2`（通常只处理单个文件）

        ```shell
        gzip 「文件」           # → 「文件」.gz，默认删原文件
        gzip -k 「文件」        # 保留原文件（GNU gzip）
        gunzip 「文件.gz」
        ```

- 归档 `tar`

    | 特性 | Gzip | Tar |
    |------|------|-----|
    | 主要功能 | 压缩（减小体积） | 归档（多文件合成一个） |
    | 处理对象 | 单个文件 | 多个文件和目录结构 |
    | 保留元数据 | 原文件名、时间等有限信息 | 权限、所有者、时间戳等 |
    | 文件扩展名 | .gz | .tar；常与压缩组合为 .tar.gz / .tgz |
    | 典型用途 | 压单个大文件 | 打包目录；再配合 gzip/bzip2 等 |
    | 压缩能力 | 有（DEFLATE） | 无（仅打包）；`tar -z`/`-j` 等才带压缩 |
    | 处理目录 | 不能直接处理目录 | 可以 |

    ```shell
    tar -cvf 「归档.tar」 「源目录」           # 打包
    tar -zcvf 「归档.tar.gz」 「源目录」       # 打包并 gzip
    tar -xvf 「归档.tar」                     # 解包
    tar -zxvf 「归档.tar.gz」                 # 解包 gzip
    tar -tf 「归档.tar.gz」                   # 只列内容（.gz 可用 -ztf）
    ```

---
### macOS命令

#### （macOS）brew更新
```shell
brew update && brew upgrade
# update：更新 Homebrew 与 formulae 元数据；upgrade：升级已装 formula/cask
```

>`brew install --cask 「软件名」` 装 Cask 应用；先 `brew search 「软件名」`。清理可用 `brew cleanup`。

#### （macOS）打开文件（夹）
```shell
open 「路径/文件」
open -t 「文件」        # 默认文本编辑器
open -a 「应用名」 「路径」  # 指定应用，如 open -a Preview 「图.png」
```

>安装 [duti](https://github.com/moretension/duti)（`brew install duti`）后可设类型默认应用：
>
>```shell
>duti -s com.sublimetext.4 public.plain-text all  # Sublime Text
>duti -s com.apple.TextEdit public.plain-text all # TextEdit
>```

#### （macOS）钥匙串
「钥匙串访问」应用可查看、管理 macOS 及部分应用保存的密码、密钥和证书。命令行可用 `security find-generic-password -a 「账号」 -s 「服务名」 -w`（需钥匙串权限，慎用）。

#### （macOS）管理配置描述文件
1. 打开「系统设置 → 通用 → 设备管理」（旧版系统多为「描述文件」）。
2. 选择配置描述文件，点击移除。

>若移除不可用，设备可能由公司/学校管理，应联系管理员。勿手动删 `/var/db/ConfigurationProfiles` 等系统目录。见 [Apple 官方说明](https://support.apple.com/guide/mac-help/change-device-management-settings-mh35474/mac)。
