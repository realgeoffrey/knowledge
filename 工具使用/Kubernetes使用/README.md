### [Kubernetes](https://github.com/kubernetes/kubernetes)使用
1. [`kubectl`CLI](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)

    1. 查看指定命名空间中属于 `all` 类别的常用资源（如 Pod、Service、Deployment，另查 ConfigMap 等资源）：

        `kubectl get all -n 「namespace名字」`
    1. 查看所有命名空间：

        `kubectl get namespace`
    2. 查看pod信息：

        ```shell
        kubectl get pod     # 当前命名空间；加 -A 查看所有命名空间

        kubectl get pod -n 「namespace名字」 | grep 「筛选关键字」 # 查看所有某命名空间的pod

        kubectl describe pod 「pod名字」 -n 「namespace名字」 # 获取某一个pod详情
        ```
    3. 查看pod内日志：

        ```shell
        kubectl logs 「pod名字」 -n 「namespace名字」 -c 「container名字」  # 查看某一个pod内日志
        # 在上条命令末尾加 --previous 可查看该容器上一次已终止实例的日志（若仍保留）
        # 加 -f 持续输出新日志，加 --tail=100 查看最后 100 行
        ```
    3. 用可交互模式执行bash

        `kubectl exec -it 「pod名字」 -n 「namespace名字」 -c 「container名字」 -- bash`（单容器 Pod 可省略 `-c 「container名字」`；镜像只有 sh 时改用 `-- sh`。）
