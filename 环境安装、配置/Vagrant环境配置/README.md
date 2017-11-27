# Vagrant环境配置

1. 官网下载、安装**virtualbox**和**vagrant**
2. 选择Vagrant Boxes：

	- [Vagrant cloud](https://atlas.hashicorp.com/boxes/search)
	- [个性化配置](https://www.puphpet.com)
3. 下载脚本配置文件**VagrantFile**：

	用终端cd到文件夹

	1. 在vagrant cloud中复制脚本名字，下载脚本

		```shell
        Vagrant init “内容”
        ```
	2. puphpet配置一个版本下载并拷进文件夹中
4. 设置端口映射：

	修改**Vagrantfile**文件。

	找到注释`#config.vm.network`，在后面增加：

	```text
    config.vm.network "forwarded_port", guest: 80, host: 8080
    ```

	主机浏览器输入`127.0.0.1:8080`即可访问虚拟机。

	同网段下的设备通过`192.168.*.*:8080`即可访问虚拟机。
5. 设置共享文件夹：

	找到注释`#config.vm.synced_folder`，

	1. apache：

        ```text
        config.vm.synced_folder "主机目录", "客户机目录" ,owner: "apache",group:"apache"
        ```
    2. nginx：

        ```text
        config.vm.synced_folder "主机目录", "客户机目录" ,owner: "www-data",group:"www-data"
        ```

	>1. 第一个参数为主机共享目录的绝对路径 *"E:/vagrant_ubuntu/shares/"* 或 *”/Users/Geoffrey/vagrant_centOS/shares”* ，
	>2. 第二个参数为客户机里的共享目录的绝对路径 *"/home/vagrant/shares/"* ，
	>3. 后面参数为设置所有者和所有组的名字，因为共享文件夹里面的所有者、所有组以及操作权限是无法修改的，并且权限为①文件夹755②文件775，要使www-data或apache对文件和文件夹都是775权限，所以要给共享文件夹的owner设置为服务器的组
	
	设置虚拟机的主机名字，在**Vagrantfile**中加入：

	```text
    config.vm.hostname = "myCentOS7"
    ```
6. 下载Vagrant Boxes：

	下载或更新镜像（可能需要打开vpn）（修改了配置文件vagrantfile才需要增加--provision）：

	```shell
    vagrant up
    ```

	停止当前正在运行的虚拟机并销毁所有内容，仅留下下载镜像文件：

    ```shell
    vagrant destroy
    ```
	
	若修改了VagrantFile，要使配置生效：

	- 退出客户机，关闭虚拟机：

	    ```shell
        vagrant halt
        ```
	- 在虚拟机文件夹中执行：

	    ```shell
        vagrant up --provision
        ```
	- 再登录虚拟机:

	    ```shell
        vagrant ssh
        ```
7. （仅在没有shell的windows系统下）安装ssh客户端（git-scm.com/downloads）：

	>配置环境变量：
	>Path增加`“;安装路径\Git\bin“`
	
	>用ssh登录虚拟机：
	>`vagrant ssh `
8. 如果不慎更新了虚拟机内核导致无法挂载共享文件夹，则要更新虚拟机中的客户端增强包，在虚拟机中执行：

    ```shell
    sudo yum -y update kernel
    sudo yum -y install kernel-devel kernel-headers dkms gcc gcc-c++
    sudo /etc/init.d/vboxadd setup
    ```

	>打开SVN，重启vagrant，输入`vagrant up`让其下载更新，即可重新挂载共享文件夹。
9. 要配置团队使用的一样的环境：

	1. 自己配置一套vagrant box（<https://www.puphpet.com>）
	2. 然后把安装好之后额外在系统里面运行的脚本记录下来
	3. 把这套vagrant box+额外的脚本发给团队
