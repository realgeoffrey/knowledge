### [Docker](https://github.com/docker/docker-ce)使用
>1. 虚拟机：虚拟出一套硬件，运行一个完整的操作系统，然后在这个系统上安装和运行软件。
>2. 容器：没有自己的内核、没有虚拟出硬件，容器内应用直接运行在宿主机（host machine）的内核（容器化技术并不是模拟的一个完整操作系统）。

1. 核心概念

    1. 镜像（Image）
    2. 容器（Container）
    3. 仓库（Repository）
2. [Docker命令](https://docs.docker.com/reference)

    >支持传参模式：`--key=value`或`--key value`。

    1. 安装、启动

        ```shell
        # 安装。或官网安装（https://www.docker.com/products/docker-desktop）
        curl -fsSL https://get.docker.com/ | sh

        # 启动
        service docker start

        # 安装信息
        docker info
        ```
    2. 查看、操作镜像

        >联合文件系统（UnionFS），支持分层（layer）。

        ```shell
        # 查看本地镜像
        docker images
        -a      # 显示所有的镜像，包括中间层镜像
        -q      # 仅显示镜像ID


        # 删除镜像（需要此镜像没有在容器中使用）
        docker rmi 「镜像ID或镜像名」
        -f      # 强制删除
        # 删除所有：`docker rmi $(docker images -a -q)`


        # 搜索镜像，或去网站搜索，如：https://hub.docker.com/
        docker search 「关键字」

        # 拉取镜像
        docker pull 「镜像名」


        # 查看镜像构建历史
        docker history 「镜像名或ID」


        # 使镜像增加镜像名、标签
        docker tag 「来源：用户名/镜像名[:「tag，如：1.0.0」]」 「目标：用户名/镜像名[:「tag，如：1.0.0」]」


        # 保存镜像到本地文件
        docker save --output=「地址/文件.tar」 「镜像名或ID」

        # 加载本地文件到镜像
        docker load --input=「地址/文件.tar」
        ```

    >配置镜像源：在`/etc/docker/daemon.json`输入`{ "registry-mirrors" : ["镜像源地址"] }`。

    3. 用镜像启动一个容器

        >用镜像启动一个容器时，会新增一个可写层到镜像层的顶部，称之为容器层，容器的所有操作都基于容器层。

        `docker run [「参数」] 「镜像名或ID」 [「命令」 [「命令参数」]]`

        >容器参数必须加在`run`和`镜像名或ID`之间。

        1. `-p=「（宿主机IP+）宿主机端口」:「容器端口」`

            容器暴露端口（把宿主机的端口与容器的端口关联起来）。

            ><details>
            ><summary>e.g.</summary>
            >
            >1. 宿主机监听80端口、配置转发xxx.com到1234端口，hosts配置：`127.0.0.1 xxx.com`，容器docker监听宿主机1234端口映射到容器内部4321端口（`-p=1234:4321`）。
            >2. 宿主机请求xxx.com：hosts到127.0.0.1:80->端口转发到127.0.0.1:1234->1234端口被docker镜像监听，转发到镜像内的4321端口，镜像内处理返回。
            ></details>

            1. `-P`

                随机指定端口。

            >相同的宿主机端口，不能被同时启动。
        2. `-d`

            后台方式运行。
        3. `-e 「环境变量名」=「值」`

            设置环境变量。
        4. `-it`

            使用交互方式运行，进入容器主shell进程（exit会使容器停止）。

            >e.g. `docker run -it 「镜像名或ID」 /bin/bash或/bin/sh`
        5. `--rm`

            若容器退出，则自动删除容器。
        6. `-v=[「宿主机目录或文件 或 数据卷名字」:]「容器内目录或文件」`

            宿主机与容器创建数据卷。
        7. `--volumes-from=「容器名」`

            容器间共用数据卷。从另一个容器中挂载已创建好的数据卷。
        8. `--name=「容器名」`

            给运行的容器增加一个容器别名，容器ID和容器名均指向此容器。
        9. `--cidfile=「新文件路径」`

            尝试创建一个新文件，并将容器ID写入它。若文件已存在，将返回一个错误。Docker运行退出时，Docker将关闭此文件。
        10. `--pid=host`或`--pid=container:「容器ID或容器名」`

            进程管理。
        11. `--uts=host`
        12. `--ipc=「none|private|shareable|container:「容器ID或容器名」|host|""（默认）」`
        13. 网络

            1. `--link=「容器ID或容器名」`

                在容器的hosts中，增加一个映射：`「容器桥接ip到容器ID或容器名」 「容器ID或容器名」`（如：`172.1.2.3 tomcat002`这样就可以在当前容器中`ping tomcat002`成功，可以单向连接到tomcat002）。
            2. `--dns=`
            3. `--network=「none|bridge（默认）」|host|container:「容器ID或容器名」|「用户自定义」`

                网络连通性。
            4. `--network-alias=`
            5. `--add-host=`
            6. `--mac-address=`
            7. `--ip=`
            8. `--ip6=`
            9. `--link-local-ip=`
        14. `--restart=「no（默认）|on-failure[:max-retries]|always|unless-stopped」`
        15. `--security-opt`

    - 数据卷（volume）：宿主机中的一个目录或文件。用于容器数据持久化 或 （外部服务与容器内部、容器间）数据同步。

        1. Docker容器中产生的数据 与 宿主机 互相同步。
        2. 一个数据卷可以同时被多个容器同时挂载（容器间数据同步）。
        3. 一个容器也可以被挂载多个数据卷。

        >容器不运行也可以正常同步。

        - `docker volume create/ls/inspect/rm/prune`

            处理手动挂载的数据卷。

            >在macOS，可能找不到宿主机路径。
    4. 容器操作

        >互相隔离，每个容器都有一个属于自己的文件系统、网络、进程树。

        1. 查看、启动/关闭/删除

            ```shell
            # 获取当前运行的容器信息（PORTS 宿主机端口 -> 容器内端口）
            docker ps
            -a      # 显示所有的容器，包括未运行的
            -q      # 仅显示容器ID


            # 删除容器（不能删除正在运行的容器）
            docker rm 「容器ID或容器名」
            -f      # 强制删除
            # 删除所有：`docker rm $(docker ps -a -q)`


            # 启动容器
            docker start 「容器ID或容器名」

            # 停止容器（`-t=「时间 默认10」`：若超时未能关闭则强制kill）
            docker stop 「容器ID或容器名」

            # 强制直接关闭容器
            docker kill 「容器ID或容器名」

            # 关闭容器，内部的文件也不会被清除。除非把容器删除，否则无论容器是否运行，文件都存在，并且文件都可以被宿主机拷贝

            # 重启容器（无论容器是否已启动）
            docker restart 「容器ID或容器名」
            ```
        2. 进入容器shell

            ```shell
            # shell进入容器内（创建新终端进程）
            docker exec -it 「容器ID或容器名」 /bin/bash或/bin/sh

            # shell进入容器内（进入容器主shell进程，exit会使此容器的主shell进程停止，从而使此容器停止）
            docker attach 「容器ID或容器名」
            ```
        3. 查看：

            1. 容器日志

                ```shell
                docker logs 「容器ID或容器名」
                -t      # 展示时间戳
                -f      # 流式输出（文件改动后重新输出）
                --tail=「数字」 # 最后n条日志
                ```
            2. 容器底层基础信息

                ```shell
                docker inspect 「容器ID或容器名」
                ```
            3. 容器资源使用情况

                ```shell
                docker stats [「容器ID或容器名」]
                ```
            4. 容器进程信息

                ```shell
                docker top 「容器ID或容器名」
                ```
        4. 拷贝内容

            >容器不运行也可以正常拷贝。

            ```shell
            docker cp 「容器ID或容器名」:「文件路径」 「宿主机保存路径」   # 容器 -> 宿主机
            docker cp 「宿主机文件路径」 「容器ID或容器名」:「保存路径」   # 宿主机 -> 容器
            ```
    5. 容器网络

        >docker使用linux桥接，宿主机是一个Docker容器的网桥：docker0。docker中所有的网络接口都是虚拟的（转发效率高）。私网地址、公网地址。

        `docker network create/connect/disconnect/inspect/ls/prune/rm`
    6. 新建、提交镜像

        >[Docker Hub](https://hub.docker.com/)。

        - 登录、登出

            ```shell
            # 登录
            docker login [--username=「用户名」 --password=「密码」 「docker源地址」]

            # 登出
            docker logout [「docker源地址」]


            # 查看登录信息
            cat ~/.docker/config.json
            ```

        1. 根据容器创建新镜像

            >最好用Dockerfile方式代替。

            ```shell
            # 根据一个已存在的容器创建一个新的镜像（不包括安装在容器内的数据卷中包含的任何数据）
            docker commit 「已存在的容器ID或容器名」 [「新的镜像名」[:「tag，如：1.0.0」]]
            -m="「描述信息」"        # Commit message
            -a="「作者」"           # 作者
            -c="「Dockerfile指令」" # Apply Dockerfile instruction to the created image
            ```
        2. 推送镜像到远程仓库

            ```shell
            # （除非是认证的组织）镜像名必须包含用户名的namespace，如：`你的账户名/镜像名`
            docker push 「镜像名」[:「tag，如：1.0.0」]
            ```
    7. Dockerfile

        包含一系列命令的文件，用于自动构建镜像。

        1. `docker build .`

            通过Dockerfile和context（`Path`递归的本地路径 + `URL`递归的git仓库地址），Docker daemon**逐一**执行指令，最终创建一个镜像。

            - 在`build`和`.`之间添加参数

                1. `-f 「文件路径」`

                    设置Dockerfile的文件路径。
                2. `-t 「用户名/镜像名[:「tag，如：1.0.0」]」`

                    创建镜像的名字。可以同时添加多个：`-t xx -t xx`。
        2. `.dockerignore`

            忽略文件（命令行操作 以及 Dockerfile的`ADD`和`COPY` 时忽略的文件/文件夹）。
        3. 指令书写

            ```shell
            # 注释会在执行命令前被删除

            # 解析器指令（Parser directives）
            # 「`syntax`或`escape`」=「值」

            # 指令不区分大小写。惯例是将它们大写以更轻松地将它们与参数区分开

            # 每条指令都是独立的，上一条指令不会影响下一条指令，因此`RUN`、`cd`等对下一条指令没有任何影响

            # 指令语法：INSTRUCTION arguments

            FROM        # 来源的基础镜像（最基本镜像：scrach）

            RUN         # 镜像构建的时候需要运行的命令

            CMD         # 指定这个容器启动时运行的命令。运行容器时追加的指令，会覆盖CMD

            ENTRYPOINT  # 指定这个容器启动时运行的命令。运行容器时追加的指令，不会覆盖ENTRYPOINT，而是添加在最后

            LABEL       # 向镜像添加元数据

            EXPOSE      # 设置对外暴露端口

            ENV         # 构建时，设置环境变量。定义后使用：`${变量名}`或`$变量名`。`\`转义的不会去使用变量：`\${xx}`或`\$xx`
                        # 一个ENV命令结束后的下一条才能使用之前设置的环境变量
                        # 能够使用变量的指令：ADD COPY ENV EXPOSE FROM LABEL STOPSIGNAL USER VOLUME WORKDIR ONBUILD

            ADD         # 添加文件（若是压缩文件则自动解压出）

            COPY        # 将文件拷贝到镜像中

            VOLUME      # 设置卷，挂载主机目录

            WORKDIR     # 设置当前工作目录。若提供了相对路径，则相对于前一条WORKDIR指令的路径

            ONBUILD     # 其他镜像使用当前镜像时（FROM），触发的指令

            ARG

            USER

            STOPSIGNAL

            HEALTHCHECK

            SHELL
            ```

            1. 每一个指令都会创建一个层（layer）

                ><details>
                ><summary>e.g.</summary>
                >
                >```shell
                >FROM ubuntu:18.04       # 1. `FROM` creates a layer from the ubuntu:18.04 Docker image.
                >COPY . /app             # 2. `COPY` adds files from your Docker client’s current directory.
                >RUN make /app           # 3. RUN builds your application with make.
                >CMD python /app/app.py  # 4. CMD specifies what command to run within the container.
                >```
                ></details>
