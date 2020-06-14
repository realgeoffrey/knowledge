### nginx+PHP配置（macOS）

>用户名 = Geoffrey；所在组 = staff。

1. `brew`安装nginx，php-fpm自带。

    ```text
    /usr/local/etc/nginx/nginx.conf   # 配置文件路径
    /usr/local/Cellar/nginx/「版本号」   # 安装路径
    ```
2. PHP

    1. 配置PHP

        `cp /etc/php-fpm.conf.default /etc/php-fpm.conf`：设置`user = 用户名`、`group = 组名`
    2. 启动php-fpm

        `sudo /usr/sbin/php-fpm -y /etc/php-fpm.conf`

        >1. 查看进程：`ps -ef | grep php-fpm`
        >2. 关闭php-fpm：`sudo pkill php-fpm`
3. nginx

    1. 配置nginx

        1. `vi /usr/local/etc/nginx/nginx.conf`：

            ```text
            user 用户名 组名;
            worker_processes  1;

            error_log  /tmp/nginx_error.log;

            events {
                worker_connections  1024;
            }

            http {
                include       mime.types;
                default_type  application/octet-stream;

                sendfile        on;

                keepalive_timeout  65;

                server {
                    listen       80;
                    server_name  localhost;

                    location / {
                        root 文件夹路径;     # 如：/Users/Geoffrey/www
                        index index.php index.html index.htm;
                        try_files $uri $uri/ /index.html;
                        #try_files $uri $uri/ /index.php?$query_string;
                        autoindex on;
                    }

                    error_page   500 502 503 504  /50x.html;
                    location = /50x.html {
                        root   html;
                    }
                }

                include servers/*;
            }
            ```
        2. `vi /usr/local/etc/nginx/servers/域名.conf`：

            1. 虚拟主机

                ```text
                # /usr/local/etc/nginx/servers/域名1.conf

                server {
                    listen       80;
                    server_name  域名1;

                    location / {
                        root 文件夹路径;     # 如：/Users/Geoffrey/www/dev.me
                    }
                }
                ```
            2. 代理转发

                ```text
                # /usr/local/etc/nginx/servers/域名2.conf

                server {
                    listen       80;
                    server_name  域名2;

                    location / {
                        proxy_pass http://域名3:端口号;
                    }

                }
                ```
    2. 启动nginx

        1. 检查脚本（语法正确性、配置脚本位置）

            `sudo nginx -t`
        2. 启动

            `sudo nginx -c /usr/local/etc/nginx/nginx.conf`

            >1. 重启
            >
            >    `sudo nginx -s reload`
            >2. 关闭
            >
            >    `sudo nginx -s stop`或`sudo nginx -s quit`
4. 绑定hosts

    `vi /etc/hosts`：`127.0.0.1 域名`

- 文件权限根据具体出现的问题调整。
