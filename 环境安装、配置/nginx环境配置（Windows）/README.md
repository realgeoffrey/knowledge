# nginx环境配置（Windows）

1. 安装

    [官网](https://nginx.org/)下载，解压缩后把文件夹放置系统路径并把文件夹改名为`nginx`。
2. 配置nginx

    1. 编辑`路径\nginx\conf\nginx.conf`：

        ```text
        worker_processes    1;

        error_log   logs/error.log;

        events {
            worker_connections  1024;
        }

        http {
            include         mime.types;
            default_type    application/octet-stream;

            sendfile        on;

            keepalive_timeout   65;

            server {
                listen      80;
                server_name localhost;

                location / {
                    root    '文件夹路径';
                    index   index.php index.html index.htm;
                    autoindex   on;
                }

                error_page  500 502 503 504  /50x.html;
                location = /50x.html {
                    root    html;
                }
            }

            include servers/*.conf;
        }
        ```
    2. 编辑`路径\nginx\conf\servers\域名.conf`：

        1. 虚拟主机

            ```text
            # 路径\nginx\conf\servers\域名1.conf

            server {
                listen      80;
                server_name 域名1;

                location / {
                    root    '文件夹路径';
                    index   index.php index.html;
                    autoindex   on;
                }
            }
            ```
        2. 代理转发

            ```text
            # 路径\nginx\conf\servers\域名2.conf

            server {
                listen      80;
                server_name 域名2;

                location / {
                    proxy_pass  http://域名3:端口号;
                }
            }
            ```
3. 启动nginx

    用Windows自带的cmd终端，`cd`进入nginx文件夹。

    1. 检查脚本

        `nginx -t`
    2. 启动

        `start nginx`或运行`nginx.exe`

        >1. 重启
        >
        >    `nginx -s reload`
        >2. 关闭
        >
        >    `nginx -s stop`或`nginx -s quit`
