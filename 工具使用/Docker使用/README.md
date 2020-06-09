### [Docker](https://github.com/docker/docker-ce)使用
1. 核心概念

    1. 镜像（Image）
    2. 容器（Container）
    3. 仓库（Repository）
2. 使用

    1. 安装、启动

        ```shell
        curl -fsSL https://get.docker.com/ | sh # 安装。或官网安装（https://www.docker.com/products/docker-desktop）

        service docker start    # 启动
        ```
    2. 查看、操作镜像

        ```shell
        docker images          # 查看本地镜像

        docker pull 「镜像名」    # 拉取镜像

        docker run -p 宿主机端口:容器端口 「镜像名」  # 运行镜像
        # e.g.
        #   宿主机nginx监听80端口、配置转发xxx.com到1234端口，hosts配置：`127.0.0.1 xxx.com`，容器docker监听宿主机1234端口映射到容器内部x端口。
        #   宿主机请求xxx.com：hosts到127.0.0.1:80->nginx端口转发到127.0.0.1:1234->1234端口被docker镜像监听，转发到镜像内的x端口，镜像内处理返回。

        docker rmi 「镜像ID」     # 删除镜像，需要此镜像没有在容器中使用（`docker rm 「容器ID」`）
        -f  # 强制删除
        ```
    3. 查看、操作容器

        ```shell
        docker ps              # 获取容器信息（`-a`：显示所有的容器，包括未运行的）
        # PORTS 本地端口 -> 容器内端口


        docker start 「容器ID」   # 启动容器

        docker stop 「容器ID」    # 停止容器（`-t=「时间 默认10」`：若超时未能关闭则强制kill）
        # 或
        docker kill 「容器ID」    # 直接关闭容器

        docker restart 「容器ID」 # 重启容器（无论容器是否已启动）

        docker rm 「容器ID」      # 删除容器

        docker logs -f 「容器ID」 # 查看容器的日志。流式输出（文件改动后重新输出）

        docker exec -it 「容器ID」 /bin/bash  # 进入容器内
        ```
