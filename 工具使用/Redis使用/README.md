### [Redis](https://github.com/antirez/redis)使用

1. `redis-cli`命令

    1. `set 「key」 「value」 「EX或PX」 「秒或毫秒」 「NX或XX」`

        1. `NX`：Only set the key if it does not already exist.
        2. `XX`：Only set the key if it already exist.
    2. `get 「key」`
    3. `keys *`
2. 使用场景

    1. 获取「其他资源」（如：.json或其他接口）后返回信息的API

        1. ~~每次请求都抓取一次「其他资源」~~
        2. ~~使用Redis设置过期时间~~
        3. Redis相关存储：`{ 内容, 过期时间 }`、`互斥锁`

            1. Redis设置长时间存在；
            2. 任何请求都直接返回Redis保存的「内容」；
            3. 同时异步进行：若判定过期且「互斥锁」关闭，则开启「互斥锁」，异步抓取「其他资源」后更新「内容」、「过期时间」并打开「更新锁」。
