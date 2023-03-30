### [Docker](https://www.docker.com/)使用
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

    - [Daemon配置文件](https://docs.docker.com/engine/reference/commandline/dockerd/)

        1. 地址（默认）：

            1. Linux：`/etc/docker/daemon.json`
            2. Windows：`%programdata%\docker\config\daemon.json`
            3. macOS：Docker Desktop -> Preferences -> Docker Engine
        2. 配置项

            1. 镜像源：`"registry-mirrors" : ["镜像源地址"]`

                >`镜像源地址（registry mirrors）` 不等于 `Docker源地址（Docker Registry）`。

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

        # 删除悬空镜像（没有仓库名或标签的镜像，`<none>`）
        docker images prune
        -f      # 不提示确认
        -a      # 删除所有未使用的镜像，而不仅仅是悬空的镜像
        --filter    # 过滤器


        # 搜索镜像，或去网站搜索，如：https://hub.docker.com/
        docker search 「关键字」

        # 拉取远程镜像到本地
        docker pull 「镜像名，如：Docker源地址/用户名/镜像名:tag名」


        # 查看镜像构建历史
        docker history 「镜像名或ID」


        # 使本地镜像增加镜像名、标签
        docker tag 「来源：Docker源地址/用户名/镜像名:tag名」 「目标：Docker源地址/用户名/镜像名:tag名」


        # 保存 镜像 到本地文件
        docker save --output=「地址/文件.tar」 「镜像名或ID」

        # 加载本地文件到镜像
        docker load --input=「地址/文件.tar」


        # 导出 容器的文件系统 到本地文件
        docker export --output=「地址/文件.tar」 「容器ID或容器名」

        # 导入本地文件到镜像
        docker import 「地址/文件.tar 或 URL 或 -」 [「Docker源地址/用户名/镜像名:tag名」]
        ```

        >镜像是 根文件系统更改 和 在容器运行时中使用的相应执行参数 的有序集合。镜像通常包含堆叠在彼此之上的分层文件系统的联合。镜像没有状态，它永远不会改变。
    3. 用镜像启动一个容器

        >用镜像启动一个容器时，会新增一个**可写**层到镜像层的顶部，称之为容器层，容器的所有操作都基于容器层。

        `docker run [「参数」] 「镜像名或ID」 [「命令」 [「命令参数」]]`

        >容器参数必须加在`run`和`镜像名或ID`之间。

        1. `-p=「（宿主机IP + ）宿主机端口」:「容器端口」`

            容器暴露端口（把宿主机的端口与容器的端口关联起来）。可以设置多个，e.g. `-p 1234:8080 -p 3333:3000`。

            ><details>
            ><summary>e.g.</summary>
            >
            >1. 宿主机监听80端口、配置转发xxx.com到1234端口，hosts配置：`127.0.0.1 xxx.com`，容器docker监听宿主机1234端口映射到容器内部4321端口（`-p=1234:4321`）。
            >2. 宿主机请求xxx.com：hosts到127.0.0.1:80->端口转发到127.0.0.1:1234->1234端口被docker镜像监听，转发到镜像内的4321端口，镜像内处理返回。
            ></details>

            1. `-P`

                随机宿主机端口:Dockerfile的EXPOSE。

            >相同的宿主机端口，不能被同时启动。
        2. `-d`

            后台方式运行。
        3. `-e 「本地环境变量名」`或`-e 「环境变量名」=「值」`

            设置容器内环境变量。若没有 ~~`=`~~，则使用宿主环境的环境变量值；若没有 ~~`=`~~ 且宿主环境没有这个环境变量值，则不设置。
        4. `-it`

            使用交互方式运行，进入容器主shell进程（exit会使容器停止）。

            >e.g. `docker run -it 「镜像名或ID」 /bin/bash或/bin/sh`
        5. `--rm`

            若容器退出，则自动删除容器。
        6. `-v=[「宿主机目录或文件 或 数据卷名字」:]「容器内目录或文件」`

            宿主机与容器创建数据卷。

            >若`数据卷名字`不存在，则会自动创建一个命名数据卷。
        7. `--volumes-from=「容器ID或容器名」`

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
        16. `-w=「容器内路径」`

            设置命令（`CMD`或替换命令）执行的路径（若容器内部不存在设置的路径，则新建）。
        17. `--entrypoint=「值」`

            覆盖镜像的ENTRYPOINT值。
        18. `--cap-add=「值」`、`--cap-drop=「值」`

            增加Linux能力、去除Linux能力。

    - 持久化存储：宿主机中的一个目录或文件。用于容器数据持久化 或 （外部服务与容器内部、容器间）数据同步。

        1. Docker容器中产生的数据 与 宿主机 互相同步。
        2. 一个数据卷可以同时被多个容器同时挂载（容器间数据同步）。
        3. 一个容器也可以被挂载多个数据卷。

        >容器不运行也可以正常同步。

        1. 命名数据卷（Named Volumes）

            `docker volume create/ls/inspect/rm/prune`
        2. 绑定挂载（Bind Mounts）

            - 挂载时文件或文件夹覆盖问题：

                1. 文件夹

                    1. 允许不存在的文件夹或存在的空文件夹挂载进container。
                    2. container中对应的文件夹将被清空覆盖或新建。
                2. 文件

                    1. 禁止将不存在的文件挂载进container。
                    2. container中对应的文件将被覆盖或新建。

        - 对比

            |  | Named Volumes | Bind Mounts |
            | :--- | :--- | :--- |
            | Host Location | Docker chooses | You control |
            | Mount Example (using `-v`) | `「my-volume」:/usr/local/data` | `「/path/to/data」:/usr/local/data` |
            | Populates new volume with container contents | yes | no |
            | Supports Volume Drivers | yes | no |

        3. tmps mounts（Linux）
        4. named pipes（Windows）

        >[Docker: storage](https://docs.docker.com/storage/)

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

            # 删除所有停止的容器
            docker container prune
            -f      # 不提示确认
            --filter    # 过滤器


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

        1. 若两个容器在同一个网络上，则它们可以相互通信。否则它们就不能通信。
        2. 将容器设置在网络上的两种方法：

            1. 在开始时分配它

                `docker run` + `--network=「网络名」`
            2. 连接现有的容器

                `docker network connect 「网络名」 「容器ID或容器名」`

        >[Docker: network](https://docs.docker.com/network/)。

    - Prune一切

        ```shell
        # all stopped containers
        # all networks not used by at least one container
        # all dangling images
        # all build cache
        docker system prune
        -f      # 不提示确认
        -a      # 删除所有未使用的镜像，而不仅仅是悬空的镜像
        --filter    # 过滤器
        --volumes   # 增加Prune volumes
        ```

    6. 新建、提交镜像

        >[Docker Hub](https://hub.docker.com/)是一个默认的官方的Docker源地址。

        - 登录、登出

            ```shell
            # 登录
            docker login [--username=「用户名」 --password=「密码」 「Docker源地址」]

            # 登出
            docker logout [「Docker源地址」]


            # 查看登录信息
            cat ~/.docker/config.json
            ```

        1. 根据容器创建新镜像

            >最好用Dockerfile方式替代。

            ```shell
            # 根据一个已存在的容器创建一个新的镜像（不包括安装在容器内的数据卷中包含的任何数据）
            docker commit 「容器ID或容器名」 [「新的镜像名」[:「tag，如：1.0.0」]]
            -m="「描述信息」"        # Commit message
            -a="「作者」"           # 作者
            -c="「Dockerfile指令」" # Apply Dockerfile instruction to the created image
            ```
        2. 推送镜像到远程仓库

            ```shell
            # （除非是认证的组织）镜像名必须包含用户名的namespace，如：`你的账户名/镜像名`
            docker push 「镜像名，如：Docker源地址/用户名/镜像名:tag名」
            ```

    - Dockerfile

        包含一系列命令的文件，用于自动构建镜像。

        1. `docker build [「参数」] 「路径（如：.） 或 URL 或 -」`

            通过Dockerfile和构建上下文（context），Docker守护进程（daemon）**逐一**执行指令，最终创建一个镜像。

            1. `-f 「文件路径」`

                设置Dockerfile的文件路径（默认当前目录下的`Dockerfile`）。
            2. `-t 「用户名/镜像名[:「tag，如：1.0.0」]」`

                创建镜像的名字。可以同时添加多个：`-t xx -t xx`。
            3. `--target 「多阶段构建的名字」`

                在构建具有多个构建阶段的Dockerfile时，可用于按名称将中间构建阶段指定为生成镜像的**最终阶段**。目标阶段之后的命令将被跳过（依旧会从Dockerfile的第一行开始按顺序执行指令至目标阶段结束）。
            4. `--build-arg 「名」=「值」`

                传入Dockerfile构建参数。构建时，docker无法获得系统环境变量，需要传入（`ARG`）或者构建文件自己声明（`ENV`）。

            - 构建上下文

                当发出`docker build` + `「路径」`命令时，「路径」称为构建上下文。（无论Dockerfile实际位于何处，）「路径」中的文件和目录的所有递归内容都将作为构建上下文发送到Docker守护进程。
        2. `.dockerignore`

            忽略文件（命令行操作 以及 Dockerfile的`ADD`和`COPY` 时忽略的文件/文件夹）。
        3. 指令书写

            ```shell
            # 解析器指令（Parser directives），需要在文本最前面书写
            # 「`syntax`或`escape`」=「值」

            # 注释会在执行命令前被删除

            # 指令不区分大小写。惯例是将它们大写以更轻松地将它们与参数区分开

            # 每条指令都是独立的，上一条指令不会影响下一条指令，因此`RUN`、`cd`等对下一条指令没有任何影响

            # 指令语法：INSTRUCTION arguments

            FROM        # 来源的基础镜像（最基本镜像：scrach） 或 （多阶段构建的）之前阶段
                        # 单个Dockerfile文件可以包含多个FROM指令从而进行多阶段构建
                        # + `as 「名字」`用于指定多阶段构建的某一阶段名字，作用：
                        #   1. `docker build`+`--target=「名字」`设置为最终阶段
                        #   2. `COPY --from=「名字」`指定复制来源为此构建内容
                        #   3. 之后阶段`FROM`之前阶段

            RUN         # 镜像构建的时候需要运行的命令
                        # 是在镜像中进行操作，不是在构建上下文

            LABEL       # 向镜像添加元数据

            EXPOSE      # 设置对外暴露端口（用于运行时`-P`的端口。运行时`-p`会覆盖掉`EXPOSE`）
                        # 可以设置多个：e.g. `EXPOSE 8080 3000`或多个EXPOSE指令

            ENV         # 构建时，设置环境变量。e.g. `ENV xx=「值」`
                        # 定义后使用：`${变量名}`或`$变量名`。`\`转义的不会去使用变量：`\${xx}`或`\$xx`
                        # 一个ENV命令结束后的下一条才能使用之前设置的环境变量
                        # 能够使用变量的指令：ADD COPY ENV EXPOSE FROM LABEL STOPSIGNAL USER VOLUME WORKDIR ONBUILD
                        # 构建时存在 且 镜像启动的容器也会保留（环境变量）

            ARG         # `docker build` + `--build-arg 「名」=「值」`传入的键-值
                        # e.g. 定义：ARG key1[=「默认值」]；使用：$key1
                        # 仅构建时存在，不会保留到容器中（不写入环境变量）

            ADD         # 添加文件（若是压缩文件则自动解压出）。从 构建上下文 向 镜像 操作

            COPY        # 将文件拷贝到镜像中。从 构建上下文 向 镜像 操作
                        # `--from=「多阶段构建的序号（从0开始）或名字，其他镜像」`：
                        #   用某个多阶段构建的内容 或 其他镜像内容 代替docker build的构建上下文

                        # 不太支持在Dockerfile内进行判断文件（夹）是否存在后进行复制操作，最好是在外部创建构建上下文的时候就确定文件（夹）已经存在：
                        #   https://stackoverflow.com/questions/31528384/conditional-copy-add-in-dockerfile
                        # 添加的同名文件夹会合并，同名文件以之后操作的覆盖之前的

            VOLUME      # 设置卷，挂载主机目录

            WORKDIR     # 设置当前工作目录。若提供了相对路径，则相对于前一条WORKDIR指令的路径
                        # 建议仅用绝对路径；建议替代难以维护的`cd`，如：`RUN cd ... && ...`

            ONBUILD     # 其他镜像使用当前镜像时（FROM），触发的指令

            USER

            STOPSIGNAL

            HEALTHCHECK

            SHELL

            CMD         # 指定这个容器启动时运行的命令。运行容器时追加的指令，会覆盖CMD
                        # 为了避免容器一启动运行完命令就停止，需要在最后添加占据前台的命令

            ENTRYPOINT  # 指定这个容器启动时运行的命令。运行容器时追加的指令，不会覆盖ENTRYPOINT，而是添加在最后
            ```

            1. 一个Docker镜像由**只读**层（layer）组成，每个层代表一个Dockerfile指令。这些层是堆叠的，每一层都是前一层变化的增量。

                应尽量减少层数，因此尽量合并指令（如：利用`&&`写命令，合并多个`RUN`为单个`RUN`）。

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
            2. 当运行一个镜像并生成一个容器时，会在层的顶部添加一个新的**可写**层（“容器层”）。对正在运行的容器所做的所有更改，例如写入新文件、修改现有文件和删除文件，都将写入此可写容器层。
        4. 多阶段构建

            多阶段构建允许大幅减少最终镜像的大小，而无需费力减少中间层和文件的数量。因为镜像是在构建过程的最后阶段构建的，所以可以通过利用构建缓存来最小化镜像层。
        5. 多服务执行

            >为了从Docker中获得最大收益，请避免一个容器负责整个应用程序的多个方面。可以使用用户定义的网络和共享数据卷连接多个容器。

            1. 把多服务放在一个脚本中，用`CMD`运行这个脚本。
            2. 或 使用其他守护进程管理多服务（如：supervisord等），用`CMD`运行这个守护进程。

    7. 扫描镜像

        >订阅收费内容。

        1. 推送Docker Hub之前自动触发
        2. 或 主动运行命令

            ```shell
            # 扫描需要登录，如：https://app.snyk.io/
            docker scan --login

            # 扫描镜像
            docker scan 「镜像名」
            ```
