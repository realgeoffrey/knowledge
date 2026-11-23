### Vagrant环境配置

1. 从官网安装 [Vagrant](https://developer.hashicorp.com/vagrant/install) 和与该版本兼容的 [VirtualBox](https://developer.hashicorp.com/vagrant/docs/providers/virtualbox)。以下示例使用 Linux 客户机。
2. 选择 Vagrant Box：

    - 在 [HCP Vagrant Registry](https://portal.cloud.hashicorp.com/vagrant/discover) 选择支持 VirtualBox 且与主机 CPU 架构匹配的 box，记下发布者、名称和版本。
    - 维护旧的 PuPHPet 项目时，使用项目已有的 Vagrantfile 和配套脚本。
3. 创建配置文件 **Vagrantfile**

    在主机终端进入空的项目目录。将下面的 `发布者/名称` 替换为选定的 box 名称。这条命令在当前目录生成 Vagrantfile，首次启动时才会按需下载 box。

    ```shell
    vagrant init 发布者/名称
    ```

4. 设置端口映射：

    在 **Vagrantfile** 的 `Vagrant.configure("2") do |config|` 和对应的 `end` 之间添加以下配置。后面的共享目录和主机名配置也放在这个块内。

    ```ruby
    config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    ```

    主机 8080 端口须空闲。启动虚拟机后，客户机的 Web 服务须在其网络接口的 80 端口监听，主机浏览器即可访问 `http://127.0.0.1:8080`。

    若需供局域网设备访问，将 `host_ip` 改为主机的局域网 IP，并在主机防火墙允许相应来源访问 TCP 8080；其他设备使用 `http://主机局域网IP:8080` 访问。[转发端口文档](https://developer.hashicorp.com/vagrant/docs/networking/forwarded_ports)
5. 设置共享文件夹：

    先在主机项目目录创建 `shares` 文件夹。若基础 box 已包含 Web 服务账户，按实际账户和组选择以下一种写法。首次启动才安装 Web 服务的，可先省略 `owner` 和 `group`，待账户创建后补上，再执行 `vagrant reload`。

    1. Apache（例如 CentOS 的 `apache` 用户和组）：

        ```ruby
        config.vm.synced_folder "shares", "/srv/shares", owner: "apache", group: "apache"
        ```
    2. Nginx（例如 Ubuntu 的 `www-data` 用户和组）：

        ```ruby
        config.vm.synced_folder "shares", "/srv/shares", owner: "www-data", group: "www-data"
        ```

    >1. 第一个参数是主机共享目录，支持绝对路径（如 `E:/vagrant_ubuntu/shares/`）或相对于项目根目录的路径。
    >2. 第二个参数为客户机里的共享目录的绝对路径。
    >3. `owner` 和 `group` 指定属主和属组，文件与目录的权限取决于共享方式和挂载选项。[共享目录文档](https://developer.hashicorp.com/vagrant/docs/synced-folders/basic_usage)

    如需设置客户机主机名，在 **Vagrantfile** 中加入：

    ```ruby
    config.vm.hostname = "myCentOS7"
    ```
6. 启动与管理虚拟机

    在主机项目目录执行以下命令。首次启动时，Vagrant 会在需要时下载 box，创建虚拟机并运行已配置的 provisioner（环境初始化脚本）。

    ```shell
    vagrant up --provider=virtualbox
    ```

    - 修改端口、共享目录等设置后，在主机执行 `vagrant reload` 重启并应用。若还需重新运行初始化脚本，使用 `vagrant reload --provision`。[reload 文档](https://developer.hashicorp.com/vagrant/docs/cli/reload)
    - 暂停使用且需要保留虚拟机磁盘时，用 `vagrant halt` 关机，下次用 `vagrant up` 启动。
    - 仅在需要删除虚拟机时使用 `vagrant destroy`。先备份仅保存在虚拟机磁盘上的数据。基础 box 和主机项目文件会保留。[destroy 文档](https://developer.hashicorp.com/vagrant/docs/cli/destroy)
7. 登录客户机

    在主机项目目录执行 `vagrant ssh`。Windows 的 Vagrant 官方安装包附带 SSH 客户端；若所用终端与它不兼容，请安装适用于该终端的 OpenSSH 客户端。[SSH 文档](https://developer.hashicorp.com/vagrant/docs/cli/ssh)
8. 排查内核更新后 VirtualBox 共享目录挂载失败

    若报错涉及 `vboxsf`，先在客户机确认当前运行的内核及其匹配的内核开发包与编译工具。对于使用 Oracle 安装程序安装 Guest Additions、并提供 `rcvboxadd` 的 Linux 客户机，可在客户机执行：

    ```shell
    sudo rcvboxadd setup
    ```

    若增强包来自发行版，按该发行版的方法修复模块。确认模块构建成功后，回到主机项目目录执行 `vagrant reload`，检查共享目录能否挂载。[Oracle Guest Additions 文档](https://docs.oracle.com/en/virtualization/virtualbox/7.1/user/guestadditions.html)
9. 要配置团队使用的一样的环境：

    1. 在 Vagrantfile 中用 `config.vm.box_version` 固定所选 box 的版本。
    2. 将额外的软件安装步骤写入 provisioner 脚本。
    3. 将 Vagrantfile 和脚本一同交给团队，成员即可在兼容的主机上运行 `vagrant up --provider=virtualbox`。
