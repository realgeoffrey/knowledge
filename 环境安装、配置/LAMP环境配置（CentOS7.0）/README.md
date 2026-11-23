### LAMP环境配置（CentOS7.0）

>历史环境记录：CentOS Linux 7 已于 2024-06-30 EOL，新项目不建议继续使用；以下命令仅适合维护旧环境时参考。默认镜像下线后，yum 需要指向对应版本的 [CentOS Vault 归档](https://vault.centos.org/)。

1. 新增用户

    用 root 登录后创建用户、设置密码。如果该用户需要管理服务器，再把它加入 wheel 组：

    ```shell
    useradd 用户名
    passwd 用户名
    usermod -aG wheel 用户名
    ```

    >重新登录后可使用 sudo。若 wheel 组尚未获授权，由 root 运行 `visudo`，启用 `%wheel ALL=(ALL) ALL`。
2. 安装环境

    安装**apache，php**：

    ```shell
    sudo yum install httpd
    sudo yum install php
    ```

    安装**mysql**：

    1. CentOS 7 默认提供 MariaDB。以下以当时常用的 MySQL 5.6 为例，需要已配置可用、启用签名校验的 EL7 MySQL 5.6 软件源；旧版 RPM 可从 [MySQL 官方归档](https://downloads.mysql.com/archives/community/) 查找。已有数据库时先核对版本及备份。

        ```shell
        sudo yum install mysql-community-server
        ```
    2. 启动 MySQL 服务

        ```shell
        sudo systemctl start mysqld
        ```
    3. 首次初始化后按提示设置 MySQL 的 root 密码

        ```shell
        mysql_secure_installation
        ```

        再次登录时运行 `mysql -u root -p`，在提示符处输入密码。
    4. 安装依赖软件：

        ```shell
        sudo yum install php-mysql
        ```

3. 配置apache（ */etc/httpd/conf/httpd.conf* ）

    >以下事例，用3个域名a.com、b.com、c.com都指向本服务器，现在配置前两个域名的虚拟主机，使前两个指向各自的文件夹，第三个和其他没有配置的域名都指向默认的文件夹。

    1. 网站目录

        创建网站文件夹：

        ```shell
        sudo mkdir /var/www/a.com
        sudo mkdir /var/www/b.com
        ```

        修改文件夹所有者：

        ```shell
        sudo chown -R 用户名:apache /var/www/a.com
        sudo chown -R 用户名:apache /var/www/b.com
        ```

        设置新建网站目录的权限：

        ```shell
        sudo chmod 755 /var/www/a.com /var/www/b.com
        ```

        新建网站index.php页面，可以写入 `<?php echo "OK";` 验证 PHP 解析：

        ```shell
        vi /var/www/a.com/index.php
        vi /var/www/b.com/index.php
        ```
    2. 配置apache虚拟主机

        新建虚拟主机配置文件夹：

        ```shell
        sudo mkdir /etc/httpd/sites-available
        sudo mkdir /etc/httpd/sites-enabled
        ```

        修改apache配置，新增默认访问路径和包含配置文件夹：

        ```shell
        sudo vi /etc/httpd/conf/httpd.conf
        ```

        在模块加载之后、第一个虚拟主机配置之前增加默认主机：

        ```text
        <VirtualHost *:80>
            ServerName localhost
            DocumentRoot /var/www/html
            ErrorLog /var/log/httpd/html-error.log
            CustomLog /var/log/httpd/html-access.log combined
        </VirtualHost>
        ```

        最后一行增加：

        ```text
        IncludeOptional sites-enabled/*.conf
        ```

        添加虚拟主机配置：

        1. a.com

            ```shell
            sudo vi /etc/httpd/sites-available/a.com.conf
            ```

            添加：

            ```text
            <VirtualHost *:80>
                ServerName www.a.com
                ServerAlias a.com
                DocumentRoot /var/www/a.com
                ErrorLog /var/log/httpd/a.com-error.log
                CustomLog /var/log/httpd/a.com-access.log combined
            </VirtualHost>
            ```
        2. b.com

            ```shell
            sudo vi /etc/httpd/sites-available/b.com.conf
            ```

            添加：

            ```text
            <VirtualHost *:80>
                ServerName www.b.com
                ServerAlias b.com
                DocumentRoot /var/www/b.com
                ErrorLog /var/log/httpd/b.com-error.log
                CustomLog /var/log/httpd/b.com-access.log combined
            </VirtualHost>
            ```

        链接配置文件：

        ```shell
        sudo ln -s /etc/httpd/sites-available/a.com.conf /etc/httpd/sites-enabled/a.com.conf
        sudo ln -s /etc/httpd/sites-available/b.com.conf /etc/httpd/sites-enabled/b.com.conf
        ```

        验证配置后重启 Apache：

        ```shell
        sudo apachectl configtest && sudo systemctl restart httpd
        ```
4. 使用phpmyadmin

    仅在确需管理旧库时安装与现有 PHP、MySQL 版本兼容的 phpMyAdmin，并在 Apache 中限制为本机或受控的管理网络访问。按对应版本的[官方安装说明](https://docs.phpmyadmin.net/en/latest/setup.html)完成配置。
