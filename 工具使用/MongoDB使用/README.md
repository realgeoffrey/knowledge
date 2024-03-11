### [MongoDB](https://github.com/mongodb/mongo)使用
1. CLI

    1. 启动服务器：`mongod`
    2. 启动客户端：[`mongo`](https://docs.mongodb.com/manual/reference/method/)

        1. `mongo 「数据库地址」`
        2. `show dbs`
        3. `use 「数据库」`
        4. `db`
        5. `show collections`
        6. `db.「collection名」.find()`
        7. `db.「collection名」.find({ 「字段名」: 「值」 })`

            1. +`.pretty()`
            2. +`.count()`
            3. +`.sort({ 「字段名」: 1或-1 })`
            4. `.limit(「数字」)`
2. 比较适用的场景：

    1. 数据模型比较简单。
    2. 数据库性能要求较高，但不需要高度的数据一致性。
    3. 给定的索引，容易查找；但不擅长筛选。
    4. 灵活性强（较多横向扩展）。
3. 工具

    1. 数据库的图形界面管理工具：[Compass](https://www.mongodb.com/download-center/compass)
    2. Node.js环境中对MongoDB数据库操作的封装：[mongoose](https://github.com/Automattic/mongoose)
4. 特性

    1. BSON
    2. （不用特意新建collection）当第一个document插入时，collection就会被创建。
