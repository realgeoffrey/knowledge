### [Redis](https://github.com/antirez/redis)使用
1. 启动客户端：[`redis-cli`](https://redis.io/commands)

    1. `set 「key」 「value」 「EX或PX」 「秒或毫秒」 「NX或XX」`

        1. `NX`：Only set the key if it does not already exist.
        2. `XX`：Only set the key if it already exist.
    2. `get 「key」`
    3. `del 「key1」 「key2」`
    4. `keys *`
2. 特性

    1. 存储在内存磁盘上。

        速度快，但内存不是持久存储、容易丢失。
    2. 键-值方式存储和使用。
3. 案例

    1. 获取「其他资源」（如：.json或其他接口）并处理后返回信息的API

        1. ~~每次请求都抓取一次「其他资源」~~
        2. ~~使用Redis设置过期时间~~
        3. Redis相关存储：`{ 内容, 过期时间 }`、`锁`（并发控制）

            1. Redis设置长时间存在；
            2. 任何请求都直接返回Redis保存的「内容」（若首次请求没有存入Redis，则获取「其他资源」后存入Redis）；
            3. 同时异步进行：若判定过期且「锁」关闭，则开启「锁」，异步抓取「其他资源」后更新「内容」、「过期时间」并关闭「锁」。
