# 数据库使用

## 目录

1. [数据库](#数据库)
1. [服务安装、启动与连接](#服务安装启动与连接)

    1. [MySQL](#mysql服务安装启动与连接)
    1. [PostgreSQL](#postgresql服务安装启动与连接)
    1. [MongoDB](#mongodb服务安装启动与连接)
    1. [Redis](#redis服务安装启动与连接)
1. [关系型数据库](#关系型数据库)

    1. [MySQL](#mysql)
    1. [PostgreSQL](#postgresql)
1. [NoSQL 数据库](#nosql-数据库)

    1. [MongoDB](#mongodb)
    1. [Redis](#redis)
1. [知识点备忘](#知识点备忘)

---

- 数据库是用于持久化、组织和查询数据的软件。广义的数据库既包括使用表和 SQL 的关系型数据库，也包括键值、文档等 NoSQL 数据库，因此 Redis 也属于数据库。

    | 数据库 | 类型 | 数据组织方式 |
    | --- | --- | --- |
    | MySQL | 关系型数据库 | 表、行、列 |
    | PostgreSQL | 关系型数据库 | 表、行、列，并支持丰富的类型和扩展 |
    | MongoDB | NoSQL 文档数据库 | BSON 文档、集合 |
    | Redis | NoSQL 键值数据库 | 内存中的键和多种数据结构 |

    >关系型数据库适合结构稳定、关联和事务要求明确的数据；NoSQL 是多种非关系型数据模型的统称，通常针对特定访问方式简化存储和查询。两者不是替代关系。全栈默认分工：MySQL 存事实并保证约束与事务；Redis 加速热点读、会话、计数、限流和锁。一起用时的读路径见 Redis 的 Cache Aside。

---

## 数据库

1. 数据库类型

    1. 关系型数据库（relational database management system，RDBMS）

        Oracle、MySQL、PostgreSQL、SQL Server。

        >- MySQL 读作 `/maɪ ˈsiːkwəl/` 或 `My S-Q-L`，不是 ~~`maɪ ˈsəkoʊ`~~。
        >- database → table → row / column。用 SQL 声明式查询；强 schema、外键、事务与复杂关联是强项。
    2. 非关系型数据库（Not only SQL，NoSQL）

        >schema 往往更灵活，按访问模式建模，通常更容易按节点横向扩展。不是「不用 SQL」，而是「不止一种数据模型」。

        1. 面向文档（document-oriented）

            MongoDB、CouchDB。

            >database → collection → document / field。文档多为 BSON/JSON，嵌套结构贴近对象；适合内容、配置、日志等结构易变数据。
        2. 键值存储（key-value）

            Redis、DynamoDB、浏览器 IndexedDB。

            >按 key 读写，结构简单、延迟低；适合缓存、会话、计数、限流、分布式锁。Redis 常与 RDBMS 并用，不替代事实库。
        3. 列族 / 宽列（column-family / wide-column）

            Cassandra、HBase、Bigtable。

            >行按主键定位，列可动态扩展；适合海量写入、时序与宽表分析。注意：分析型「列存」（如 ClickHouse、Parquet）侧重按列压缩扫描，与宽列 NoSQL 不是同一类产品。
        4. 图数据库（graph）

            Neo4j、Amazon Neptune。

            >节点 + 边建模关系；适合社交关系、推荐、权限、知识图谱等「多跳关系」查询。
        5. 搜索引擎（常被归进广义 NoSQL）

            Elasticsearch、OpenSearch。

            >倒排索引做全文与聚合检索；一般作查询副本，主数据仍落在 RDBMS / 文档库。

    >- 选型直觉：结构稳定 + 关联 + 事务 → RDBMS；热点读 / 会话 / 限流 → Redis；文档形态易变 → MongoDB；多跳关系 → 图库；全文检索 → ES。可组合，不是二选一。
    >- 分布式系统还会谈到 CAP（一致性 / 可用性 / 分区容错，分区时最多保其二）与 BASE（基本可用、软状态、最终一致）。实践上多为取舍与补偿，不是口号。
2. 关系型数据库的范式

    表结构设计所符合的级别：减少冗余与更新异常，让数据组织更干净。越高冗余越小，但联表越多、读路径往往更贵。

    1. 第一范式（1NF）

        属性原子、不可再分。

        >属性不可以是集合、数组、记录等组合型数据。例如「电话」列不要存 `138xxx,139xxx`，应拆行或独立联系方式表（1对多）。
    2. 第二范式（2NF）

        （符合 1NF，）非主属性**完全依赖**于每一个候选键，而不是只依赖候选键的一部分。

        >只有单列主键（如：	`PRIMARY KEY (user_id)`。因而通常也只有这一组候选键）的表，若已满足 1NF，一定满足 2NF。违反例：订单明细用 `(order_id, product_id)` 作主键，却把 `product_name` 放在明细里——`product_name` 只依赖 `product_id`，应放到商品表。

        >键的常见说法：
        >
        >1. 候选键：能唯一标识一行的最小属性集；可有多组。
        >2. 主键：从候选键中选定的那一组，非空、唯一，一表一个。
        >3. 复合主键（也常称联合主键）：同一表内主键由多列组成，如 `PRIMARY KEY (字段1, 字段2)`；单列不必唯一，合在一起必须唯一。跨表关联用外键（或中间表）表达，不要把「多表主键拼起来查」叫作联合主键。
        >4. 外键：引用另一表（通常是其主键 / 唯一键），表达关联并可由 DBMS 做参照完整性约束。
    3. 第三范式（3NF）

        （符合 2NF，）消除非主属性对非主属性的**传递依赖**。

        >非主属性只应直接依赖候选键。违反例：员工表存 `dept_id` 又存 `dept_name`，而 `dept_name` 由 `dept_id` 决定——部门名应在部门表。
    4. 巴斯-科德范式（BCNF）

        （符合 3NF，）对每个**非平凡**函数依赖 `X → A`，`X` 必须是**超键**（含候选键及其超集）。

        >比 3NF 更严：3NF 主要约束非主属性；BCNF 连主属性之间的不当依赖也要拆掉。常见说法「一表只有一个候选键」并不准确——可以有多个候选键，但每个非平凡 FD 的左边都必须是超键。

    >实际工作中，逻辑模型做到 3NF（必要时 BCNF）通常够用；物理落地可按读路径适度反范式。4NF / 5NF 解决多值依赖、连接依赖，业务库很少主动追到那一层。

    >1. 范式越高，冗余越小，插入 / 更新 / 删除异常越少；联表与查询复杂度可能上升。
    >2. 零冗余未必最优。概念 / 逻辑设计先守 3NF；物理设计再按热点读路径降范式（加冗余字段、汇总表、物化视图）。
    >
    >    >e.g. 订单表除 `user_id` 外冗余 `user_name`：违反 3NF，但列表页少一次联表；代价是改名要同步更新，需约定写入路径或异步校正。
    >3. 范式主要缓解的问题
    >
    >    1. 操作异常
    >
    >        1. 插入异常：某实体必须挂靠另一实体才能落库，导致无法单独表示。
    >        2. 更新异常：改一个业务事实要改多行，易漏改不一致。
    >        3. 删除异常：删一行时把本应保留的另一实体信息一并删掉。
    >    2. 数据冗余：同一事实多处存放，或某列可由其他列计算得出却仍重复存储。
3. 数据库设计

    >库一旦上线，改列类型、删列、改约束的成本远高于加列加表。前期模型差，后期只能打补丁。

    1. 需求分析

        1. 有哪些实体、事件、状态（数据是什么）。

            >- 实体：要持久化、可单独辨认的业务对象，设计上常对应一张表。e.g. 用户、商品、店铺。
            >- 事件：某时刻发生的事，常带时间戳，可落成流水表或由实体状态机推导。e.g. 下单、支付、退款、登录。
            >- 状态：实体或流程当前所处档位，多落成枚举 / 状态字段，有时配状态变更日志。e.g. 订单：待付 / 已付 / 已取消。
            >- 同一业务常三者并存：实体是「订单」，事件是「支付成功」，状态从「待付」变为「已付」。临时 UI 态、纯缓存一般不算要进库的实体。
        2. 属性、基数、唯一性、是否可空。

            >- 属性：实体要存哪些字段及其含义。e.g. 用户：邮箱、昵称、注册时间。
            >- 基数：与其他实体「几个对几个」，决定要不要中间表。e.g. 用户 1 : N 订单；订单 N : N 商品。
            >- 唯一性：哪些值在表内不能重复，对应主键 / `UNIQUE`。e.g. 邮箱全局唯一；`(order_id, product_id)` 联合唯一。
            >- 是否可空：缺省能否落库，对应 `NULL` / `NOT NULL` 与业务校验。e.g. 昵称可空；下单必须有 `user_id`。
        3. 生命周期、增长速度、读写比、一致性要求、是否值得进库（有的只适合日志 / 对象存储 / 缓存）。

            >- 生命周期：活多久、何时归档 / 删除。e.g. 会话三十分钟过期；订单保留数年再归档。
            >- 增长速度：预估增量，决定分区、分表或独立存储。e.g. 访问日志日增千万行，不宜与核心业务表同库同表策略。
            >- 读写比：读多可索引 / 缓存 / 冗余；写多少建索引、慎用重联表。e.g. 商品详情读多写少；埋点几乎只写。
            >- 一致性：能否接受短暂不一致。强一致用事务；最终一致可用缓存、消息、异步校正。e.g. 扣库存要强一致；个人主页粉丝数可最终一致。
            >- 是否进库：不是所有数据都进业务库。大文件进对象存储只存 URL；验证码 / 限流进 Redis；可重建的搜索索引 / 报表可丢了再算。
    2. 逻辑设计

        ER 建模：一对一、一对多、多对多；用范式约束；明确主键、外键、唯一约束。

        >- 多对多必须拆中间表（关系表），中间表至少含两侧外键，常再加自身主键或业务字段（数量、创建时间等）。
        >- 一对一常见于按列拆表（两侧最多一行对应，外键侧常兼唯一 / 主键），不是默认业务关系。一对多才是默认形态（用户 → 订单）。
        >1. 垂直拆敏感 / 大字段：`user(id, name)` + `user_private(user_id, id_card, password_hash)`。列表只扫轻量表；高敏列少暴露、权限更好控。
        >2. 扩展表按需加载：`user` 放核心常读列；`user_profile(user_id, bio, …)` 进详情才 JOIN。主表更瘦，热点查询更快。
        >
        >列危险或很大且列表不需要 → 前者；列无害但少用 → 后者。列表详情都总要的列不必拆。
    3. 物理设计

        1. 选 DBMS（事务强度、生态、运维、团队经验）。
        2. 命名规范。

            1. 可读性：库表字段风格统一（如 `snake_case`）。
            2. 表意性：名字能说明对象，避免 `data1`、`tmp`。
            3. 长名原则：宁可全称，少用晦涩缩写；团队内缩写表要文档化。
        3. 按 DBMS 选类型与约束。

            1. 能用数值 / 枚举就不要用字符串存「看起来像数」的编码（视查询与比较需求而定）。
            2. `CHAR` 定长；`VARCHAR` 变长；超长文本用 `TEXT` / 对象存储，避免无意义的超大 `VARCHAR`。
            3. 金额用 `DECIMAL`（或整数分），不用 `FLOAT` / `DOUBLE`。
            4. 时间：按引擎区分——MySQL 常用 `DATETIME` 存业务墙钟，`TIMESTAMP` 按 session `time_zone` 转 UTC 存放（注意范围与坑）；PostgreSQL 用 `timestamp` / `timestamptz`（后者带时区语义）。也有人存 Unix 秒（`INT` / `BIGINT`）。亦可统一存 UTC、展示交给应用；读写约定必须一致。
            5. 主键倾向短、稳、不业务含义（自增或 UUID，按分布式与索引局部性权衡）；状态、软删（`deleted_at`）提前想好查询条件。
        4. 索引与反范式。

            >索引服务真实 `WHERE` / `JOIN` / `ORDER BY`，不是越多越好；写放大与空间是成本。反范式是空间换时间，要适度并保证冗余可维护。

            1. 减少热点读路径上的联表次数。
            2. 汇总表 / 冗余列服务列表与报表。
            3. 冗余字段 / 冗余表要事先约定：**谁改、何时改**（同步写、异步校正，或当作历史快照故意不改）。

                >反范式只解决读；写完源数据后，冗余副本不会自动变。必须明确责任方与触发时机，例如：改用户名的服务在同一事务里更新订单上的 `user_name`；或发消息由消费者异步刷；或业务认定订单名为下单快照、改名后不再动。约定要落到数据字典、写入路径或消费者逻辑里，不能口头「以后再说」，否则源表已改、冗余仍旧，会静默不一致。
    4. 维护优化

        1. 维护数据字典与变更记录。
        2. 新需求优先加表 / 加列，破坏性变更走迁移与兼容窗口。
        3. 用执行计划做索引优化；删掉长期无用的索引。
        4. 大表按时间 / 业务键拆分（分区、冷热分离、归档）。

            >拆分 = 按某列决定行进哪一块。时间键如 `created_at`（便于归档、查近期）；业务键如 `user_id` / `tenant_id` / `shop_id`（便于「只查某用户/租户」落到单分片）。选哪列看最热查询常带谁；按自增 `id` 也能切，但业务查询很少带它，易变成扫全部分片。分区 / 冷热 / 归档都是把大表变小块的手段，可按时间或业务键划界。

        >维护阶段最容易「只加不收」。每次大改仍应回到：需求 → 逻辑 → 物理，避免表结构无序膨胀。
4. 事务（transaction）

    DBMS 中一组作为逻辑单元的操作序列：要么一起成功，要么一起回到开始前的状态。

    1. 失败时可恢复，异常时仍能回到一致状态。
    2. 多会话并发时提供隔离，减少彼此干扰。

    - ACID：

        1. 原子性（atomicity）：事务内操作全部成功或全部不生效（提交 / 回滚）。
        2. 一致性（consistency）：事务结束后，库仍满足事先定义的约束与业务不变量（常由应用 + 约束共同保证）。
        3. 隔离性（isolation）：并发事务彼此干扰的程度由隔离级别控制。
        4. 持久性（durability）：已提交的修改在宕机后仍可恢复（依赖日志与落盘）。

    - 并发异常与隔离级别：

        1. 脏读：读到别的事务未提交的数据。
        2. 不可重复读：同一事务内两次读同一行，结果因别人已提交的更新/删除而不同。
        3. 幻读：同一事务内按相同条件两次查，行集合因别人已提交的插入/删除而变化。

        标准四级从弱到强：`READ UNCOMMITTED`、`READ COMMITTED`、`REPEATABLE READ`、`SERIALIZABLE`。哪一级挡住哪种异常、引擎默认与 `SET` 写法见 [MySQL](#mysql) 的事务、隔离与锁；JDBC / Spring 见其后的 Java 访问。

        - 写冲突解决方案（多人改同一行 / 争同一业务键）：

            1. 唯一约束：表上规定某列（或几列组合）不能重复，第二个相同写入直接失败。e.g. `UNIQUE(order_no)` 防同号订单；`UNIQUE(user_id, activity_id)` 防同一人重复报名。能靠它挡的优先用——不必先查再插（两人都查到「没有」仍可能双双插入）。注意：多行 `NULL` 在 MySQL/PG 的 `UNIQUE` 下通常不互斥，可空列别单靠 UNIQUE 防重。
            2. 乐观锁：默认觉得很少撞车，先读后改，写时再验。行上有 `version`，必须**验旧值并抬版本**：`UPDATE … SET …, version = version + 1 WHERE id=? AND version=?`；影响 0 行 = 期间被人改过，整笔重读重试。缺「抬版本」则冲突检测形同虚设。适合个人资料等冲突少的场景。
            3. 悲观锁：默认会撞车，先占住再改。事务内 `SELECT … FOR UPDATE` 锁住该行，别人要改同一行必须等你提交。适合库存扣减等热点；锁期间只做本库读写，事务要短。

            >可组合：用唯一约束防「多造一行」；改已有行再用乐观或悲观。持有 `FOR UPDATE` 时不要调外部 HTTP / RPC。

    - 与分布式的关系：单库事务靠 ACID；跨库 / 跨服务常用本地事务 + 消息出箱、幂等、最终一致，而不是处处上分布式强事务。

---

## 服务安装、启动与连接

### [`MySQL`](https://dev.mysql.com/doc/refman/en/)服务安装、启动与连接

```shell
# 1. 安装
brew install mysql  # 安装 Homebrew 当前稳定版

# 2. 启动服务
brew services start mysql
brew services stop mysql
brew services restart mysql
brew services info mysql  # 查看服务状态和PID
# brew services list        # 列出全部已安装服务的名称和状态，如 mysql、postgresql@17、redis
# brew services info --all  # 列出全部已安装服务的状态和PID
mysql_secure_installation # 首次安装后按需设置 root 密码和安全选项

# 3. 连接服务
# Homebrew 首次安装且尚未设置 root 密码时：
mysql -u root   # 需要密码时：mysql -u root -p
# 通用连接：`-h 主机`；`-P 端口`；`-u 用户名`；`-p` 交互输入密码；`-D` 选择数据库（可省略）
mysql -h 127.0.0.1 -P 3306 -u 「用户名」 -p -D 「数据库名」 --default-character-set=utf8mb4
```

>进入 `mysql>` 后，`「SQL 语句」;` 或 `「SQL 语句」\g` 表示执行；`\?` 查看客户端命令，`HELP 「SQL 语句」;` 查看 SQL 帮助，`\q` 退出。

### [PostgreSQL](https://www.postgresql.org/docs/)服务安装、启动与连接

```shell
# 1. 安装
brew install postgresql@17  # 安装，版本按需

# 2. 启动服务
brew services start postgresql@17
brew services stop postgresql@17
brew services restart postgresql@17
brew services info postgresql@17  # 查看服务状态和PID
# brew services list        # 列出全部已安装服务的名称和状态
# brew services info --all  # 列出全部已安装服务的状态和PID
# 前台运行；数据目录以 Homebrew 实际路径为准
"$(brew --prefix postgresql@17)/bin/postgres" -D "$(brew --prefix)/var/postgresql@17"

# 3. 连接服务
# 连接 postgres 数据库：`-h 主机`；`-p 端口`；`-U 用户名`；`-d 数据库名`
psql -h localhost -p 5432 -U "$(whoami)" -d postgres
```

>进入 psql 交互环境（`数据库名=>` 或 `数据库名=#`）后，`\?` 查看 psql 命令，`\h 「SQL 语句」` 查看 SQL 帮助。SQL 语句以 `;` 结束，psql 元命令（如 `\l`、`\du`）不需要。

```text
SELECT version();
SELECT current_database();
\l
\c 「数据库名」
\dn
\dt
\du
```

### [MongoDB](https://www.mongodb.com/docs/)服务安装、启动与连接

```shell
# 1. 安装（macOS）
brew tap mongodb/brew
brew install mongodb-community@8.0

# 2. 管理服务
brew services start mongodb-community@8.0
brew services stop mongodb-community@8.0
brew services restart mongodb-community@8.0
brew services info mongodb-community@8.0

# 3. 连接；本地默认地址为 mongodb://127.0.0.1:27017
mongosh
mongosh 'mongodb://「用户名」:「密码」@「主机」:「端口」/「数据库名」'
```

>进入 `mongosh` 后，`help` 查看帮助，`exit` 退出。`use` 只切换当前数据库；首次写入数据后，不存在的数据库和集合才会被创建。

```javascript
show dbs
use 「数据库名」
db
db.runCommand({ ping: 1 })
show collections

db.「集合名」.insertOne({ 「字段名」: 「值」 })
db.「集合名」.find({ 「字段名」: 「值」 }).sort({ 「排序字段」: -1 }).limit(「数量」)
db.「集合名」.countDocuments({ 「字段名」: 「值」 })
db.「集合名」.updateOne({ 「查询条件」 }, { $set: { 「字段名」: 「新值」 } })
db.「集合名」.deleteOne({ 「查询条件」 })
```

### [Redis](https://redis.io/docs/latest/)服务安装、启动与连接

```shell
# 1. 安装
brew install redis      # 安装 Redis

# 2. 启动服务
brew services start redis
brew services stop redis
brew services restart redis
brew services info redis  # 查看服务状态和PID
# brew services list        # 列出全部已安装服务的名称和状态
# brew services info --all  # 列出全部已安装服务的状态和PID
brew services run redis   # 只启动本次，不注册为登录时自动启动

# 前台运行：若后台服务已占用 6379，先执行 brew services stop redis，或用 --port 更换端口
# 不指定配置文件时使用内置默认配置；dir 默认为当前目录，RDB 文件默认为 dump.rdb
redis-server
redis-server "$(brew --prefix)/etc/redis.conf"  # 显式使用与 brew services 一致的配置文件
redis-server "$(brew --prefix)/etc/redis.conf" --port 6380 --dir /tmp  # 命令行参数覆盖配置文件

# 3. 连接服务
# 默认连 127.0.0.1:6379、逻辑库 0；ping 通返回 PONG
redis-cli                      # 进入交互式 REPL；可尝试执行 SCAN 0
redis-cli ping                 # 单次命令，不进 REPL
redis-cli -h 「地址」 -p 「端口」 -n 「逻辑库序号」 ping
# URL 形式：redis://[:密码@]主机:端口[/逻辑库序号]
redis-cli -u 'redis://:「密码」@「地址」:「端口」/「逻辑库序号」' ping
redis-cli INFO server          # 看版本、uptime 等；确认连的是哪台实例
```

>进入 `redis-cli` 后，可直接执行 Redis 命令；`HELP 「命令」` 查看帮助，`QUIT` 退出。

```text
SET 「key」 「value」
SET 「key」 「value」 EX 「秒数」 NX
GET 「key」
TTL 「key」
DEL 「key」
```

>`NX` 表示仅在 key 不存在时写入；`EX` 和 `PX` 分别以秒和毫秒设置过期时间。

---

## 关系型数据库

### MySQL

>基准：**MySQL 8.4 LTS + InnoDB**。

关系型库。服务 → 库（`DATABASE` ≈ `SCHEMA`）→ 表。链路：`页面 → API → 后端 → JDBC/Mapper → MySQL`（前端不直连）。列表超时 / 重复下单 / 金额错，优先查表、索引、事务。学习顺序：`表与约束 → CRUD/JOIN/聚合 → 索引 → 事务 → Java`；进阶：执行计划、连接池、备份。

>**InnoDB**：MySQL 默认**存储引擎**（表怎么落盘、怎么索引/加锁、怎么做事务）。MySQL 是产品；真正存表的默认是 InnoDB。记：事务与崩溃恢复；索引默认 B+树（主键聚簇）；行级锁；隔离默认 `REPEATABLE READ`。新表默认即它（旧引擎 MyISAM：基本无事务、偏表锁）。

1. **表与约束**

    | 概念 | 要点 |
    | --- | --- |
    | 表 / 行 / 列 | 一类对象 / 一条记录 / 属性 |
    | 主键 | 短、稳、不变；业务唯一用 `UNIQUE`，别拿业务号当主键 |
    | 字符集 | `utf8mb4` |
    | `NULL` | 未知/不存在 ≠ `''` / `0` |
    | 校验 | 页面给人看；库约束挡绕过前端的脏写 |

    | 约束 | 作用 | 注意 |
    | --- | --- | --- |
    | `NOT NULL` / `DEFAULT` | 禁空 / 默认值 | 显式 `NULL` 不会被默认值替换 |
    | `PRIMARY KEY` | 非空且唯一 | 每表一个，可多列 |
    | `UNIQUE` | 非空值不重复 | 允许多个 `NULL`；Java 冲突常 `DuplicateKeyException` |
    | `CHECK` | 行内条件 | `TRUE` 或 `NULL→UNKNOWN` 都通过 |
    | `FOREIGN KEY` | 引用完整性 | 写明 `ON DELETE`/`ON UPDATE`；别默认级联删 |

    | 关系 | 做法 |
    | --- | --- |
    | 一对一 | 外键 + `UNIQUE` |
    | 一对多 | 外键在「多」侧 |
    | 多对多 | 中间表存两侧外键；查询时经中间表两次关联 |
    | 建删顺序 | 先父后子建；先子后父删。（因为外键） |

    | 操作 | 含义 |
    | --- | --- |
    | `TRUNCATE` | 清空留结构；InnoDB 上是 **DDL**：隐式提交、不可 `ROLLBACK`、重置 `AUTO_INCREMENT`；有外键指向本表则失败 → 用 `DELETE` |
    | `DROP TABLE`/`DATABASE` | 删对象 |
    | `COMMENT` | 表/列元数据（`SHOW CREATE TABLE`）；改列注释须 `MODIFY`/`CHANGE` 写全列定义 |

1. **查询与改数据**

    SQL 是声明式：写「要什么」，优化器决定「怎么拿」。

    | 主题 | 规则 |
    | --- | --- |
    | 注释 | `--` 后须空格；`#` MySQL 扩展；`/* */` 可跨行；逗号别跟列名一起注释掉 |
    | `INSERT` | 写明列名；批量有上限，避免超大单包 |
    | `SELECT` | 只取需要的列 |
    | `UPDATE`/`DELETE` | 必须有 `WHERE`；改前同一条件先查 |
    | 空值 | `IS NULL` / `IS NOT NULL`，不要 `= NULL` |
    | 理解顺序 | `FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`（写作辅助序，非引擎真实执行序） |

    | 易混 | 记法 |
    | --- | --- |
    | `WHERE` vs `HAVING` | 滤行 vs 滤聚合结果；`COUNT`/`SUM` 不能进 `WHERE` |
    | `DISTINCT` | 按选出的整行去重；统计用 `GROUP BY` |
    | `INNER JOIN` | 两侧都匹配才保留 |
    | `LEFT JOIN` | 保留左表全部；右表条件放 `ON`，放进 `WHERE` 易变成内连接 |
    | N+1 | 循环按主键查子表 → 一次 `JOIN` 或 `WHERE id IN (...)` |
    | 深分页 | 少用大 `OFFSET`；用上一页排序键 + 唯一 ID 续查 |
    | `LIMIT` | 列表要有上限；勿让前端传无界 `pageSize` |

    | 视图 | 要点 |
    | --- | --- |
    | 是什么 | 给 `SELECT` 起名；普通视图不另存数据 |
    | 物化 | MySQL **没有**；要落结果自己建表再 `INSERT`（底表变了不自动更新） |
    | 写入 | 改的是底表；`JOIN`/`GROUP BY`/聚合通常不可写 |
    | `WITH CHECK OPTION` | 拒绝写出视图条件外的行 |
    | `DROP VIEW` | 不删底表 |

1. **索引与 `EXPLAIN`**

    用空间和写放大换读加速。读多写少、条件稳定的路径才建；写极多、条件飘忽的少建。只服务真实的 `WHERE` / `JOIN` / `ORDER BY`。InnoDB 默认 B+ 树。

    | | 单列 | 复合 `(列1, 列2)` |
    | --- | --- | --- |
    | 写法 | 一列 | 多列，**顺序有意义**（最左前缀；按区分度与查询排） |
    | 能覆盖 | 该列过滤/排序/关联 | `列1=?`、`列1=? AND 列2=?`；一般**不能**单独服务 `列2=?` |

    | | 普通索引 | 唯一索引 |
    | --- | --- | --- |
    | 加速 | 会 | 会 |
    | 非空重复 | 可以 | 第二次报错 |
    | `NULL` | 可多个 | 也可多个 |
    | vs 主键 | 不是主键 | 也不是（主键每表一个且非空；`UNIQUE` 可多组） |

    | 要点 | 说明 |
    | --- | --- |
    | `UNIQUE` 约束 | 自动建唯一索引 = `CREATE UNIQUE INDEX`；`SHOW INDEX` 里 `Non_unique=0` |
    | 组合唯一 | `UNIQUE(user_id, sku_id)` ≠ `UNIQUE(sku_id)` |
    | 聚簇 | 数据按主键排；二级索引叶子带到主键再回表取整行。主键宜递增，减少页分裂 |
    | 覆盖索引 | 查询列全在索引里 → 免回表 |
    | 用不上索引 | `LIKE '%xx'`、对索引列做函数/运算/隐式类型转换、跳过最左前缀、`OR` 两侧难同时用上、无界 `SELECT *` 放大回表与网络 |
    | `IN` / `NOT` | 优先 `IN`；`NOT IN`、`≠`、`NOT` 不宜当主过滤（`NOT IN` 还要当心 `NULL`）。以 `EXPLAIN` 为准 |
    | 驱动表 | 小结果集驱动大表只是嵌套循环直觉；优化器可能改写，以执行计划为准 |
    | 批量写 | 短事务、限制批次，少锁时间、少日志抖动 |
    | `EXPLAIN` | 接口慢先看 `type`/`key`/`rows`/`filtered`/`Extra`（临时表、filesort）；`EXPLAIN ANALYZE` 真跑，对照慢查询日志。改完用同一条 SQL 复测 |

1. **事务、隔离与锁**

    事务 = 多步同成同败（ACID）。默认自动提交；需一起成败 → `START TRANSACTION`。结束：**只** `COMMIT` 或 `ROLLBACK` 二选一（不是每条 SQL 后缀）。

    | 主题 | 规则 |
    | --- | --- |
    | 边界 | 一个 HTTP 请求开一段；勿把 HTTP/RPC/发 MQ 包进事务 |
    | 幂等 | 重复点击靠接口幂等；`UNIQUE` 只挡相同唯一键，挡不住两次不同下单 |
    | DDL vs DML | DDL 常隐式提交、不可当 DML 回滚；某句 DML 失败只撤该句，失败应整笔 `ROLLBACK` |
    | 死锁 | InnoDB 常整笔回滚 → 须重新 `START TRANSACTION` |
    | `UPDATE` 0 行 | 通常不算错；需要时查 `ROW_COUNT()` |
    | `SAVEPOINT` | 部分回滚：`ROLLBACK TO` 后继续（其后保存点失效） |
    | 重试 | 锁超时等瞬时失败可同语句重试；唯一冲突换键或整笔 `ROLLBACK` |
    | 客户端 | 显式事务里语句失败不会自动整笔回滚，须客户端 `COMMIT` / `ROLLBACK`；JDBC 抛错停后续；`mysql>` 粘贴仍可能继续；`mysql < 文件` 默认遇错停 |

    三种异常的含义见上文事务。下表按 InnoDB；PostgreSQL 默认是 `READ COMMITTED`。

    | 隔离级别 | 脏读 | 不可重复读 | 幻读 | 说明 |
    | --- | --- | --- | --- | --- |
    | `READ UNCOMMITTED` | 可能 | 可能 | 可能 | 几乎不用 |
    | `READ COMMITTED` | 否 | 可能 | 可能 | 每次一致性读见当时已提交 |
    | `REPEATABLE READ` | 否 | 否 | 快照读通常不见；锁定读靠间隙锁 | InnoDB 默认；同事务一致性读复用快照 |
    | `SERIALIZABLE` | 否 | 否 | 否 | 最强，并发最贵 |

    事务开始前设置（进行中不能改）。`autocommit=1` 时每条语句自成事务，单语句上看不出 `READ COMMITTED` 与 `REPEATABLE READ` 的差别，要把多条语句放进同一个事务。

    | 范围 | 写法 |
    | --- | --- |
    | 本连接之后 | `SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;` |
    | 仅下一事务 | `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;` 然后 `START TRANSACTION`；该事务结束回到会话级别 |
    | 查看 | `SELECT @@transaction_isolation;` |

    >`SET GLOBAL transaction_isolation` 只影响之后新建的会话。JDBC / Spring 见下一节。

    | 机制 | 含义 |
    | --- | --- |
    | MVCC | Read View 判可见性；长事务拖清理 |
    | `FOR UPDATE` | 必须在事务里；锁范围跟扫描索引走 |
    | 行锁 / 表锁 | 锁跟索引走；条件无合适索引易扫太多行甚至表级影响 |
    | 间隙锁 | `REPEATABLE READ` 下锁定读可能锁间隙，用来防幻；事务短、固定顺序碰数据 |

1. **Java 访问**

    链路：`连接池 → Connection → PreparedStatement/MyBatis → 映射 → Service 事务`。多步同事务；失败 `rollback` 并停后续。`UNIQUE`/外键失败勿吞异常后仍返回成功。

    | MySQL | Java | 注意 |
    | --- | --- | --- |
    | `DECIMAL` | `BigDecimal` | 定精度/舍入；比较用 `compareTo` |
    | `INT`/`BIGINT` | `Integer`/`Long` | 可空用包装类；`BIGINT UNSIGNED` 可能超 `long` |
    | `DATE`/`DATETIME`/`TIMESTAMP` | `LocalDate`/`LocalDateTime`/`Instant` | `DATETIME` 无时区；绝对时间用 UTC |
    | `JSON` | `String` 或对象 | 统一序列化；高频查询字段拆普通列 |

    | 主题 | 规则 |
    | --- | --- |
    | 参数 | 值用绑定 / `#{}` 防注入；`${}` 只许白名单标识符（表名、列名） |
    | [连接池](https://github.com/realgeoffrey/knowledge/blob/master/全栈/Java学习笔记/README.md#jdbc-与数据库访问演进) | `每实例池上限 × 实例数 + 其他客户端` < `max_connections`，留余量给管理与批跑 |
    | ORM | MyBatis、JPA、Sequelize 等省样板，仍要看生成 SQL；事务边界、批量、索引要自己管 |
    | `@Transactional` | 通常不进新线程；同类自调用可能不生效 |
    | 隔离级别 JDBC | 第一条 SQL 前 `connection.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED)`；常量还有 `TRANSACTION_READ_UNCOMMITTED`、`TRANSACTION_REPEATABLE_READ`、`TRANSACTION_SERIALIZABLE` |
    | 隔离级别 Spring | `@Transactional(isolation = Isolation.READ_COMMITTED)`；`Isolation.DEFAULT` 跟库。只写到新开的事务上：当时没有事务的 `REQUIRED` / `NESTED`，以及总会新开的 `REQUIRES_NEW`。加入外层的 `REQUIRED`，和已有事务上的 `NESTED`（保存点），沿用外层。编程式：`TransactionTemplate.setIsolationLevel(TransactionDefinition.ISOLATION_READ_COMMITTED)` |
    | 跨边界 | 跨库/HTTP/MQ 靠 outbox、重试、消费幂等 |

1. **复制、迁移、备份、监控**

    | 主题 | 要点 |
    | --- | --- |
    | redo / binlog | 崩溃恢复 / 复制与时间点恢复；**都不能替代备份**（PostgreSQL 的 WAL 同理） |
    | 复制 | 读扩展与容灾；默认异步，误删也会跟上副本。复制本身不是备份 |
    | 读自己 | 刚写再读走主库；事务内勿切副本 |
    | 高可用 | 自动切换不等于零丢失；事先接受 RPO / RTO |
    | 安全 | 最小权限，生产不用超级用户跑业务；TLS；密码与连接串不进仓库、代码、日志 |
    | DDL | 结构变更走版本化迁移（可回滚或向前兼容）；大表先估锁、磁盘、复制延迟 |
    | 备份 | 定期全量 + 按需增量；定范围、保留期、恢复目标，并在隔离环境演练恢复 |
    | 监控 | 连接等待、慢 SQL、扫描行、锁等待、I/O、复制延迟。扩展顺序：索引 / SQL / 缓存 / 归档 → 读写分离 → 分库分表（见 [知识点备忘](#知识点备忘)） |

    | 诊断命令 | 用途 |
    | --- | --- |
    | `EXPLAIN` | 是否走索引、估扫行数 |
    | `SHOW FULL PROCESSLIST` | 谁在连、跑哪条、卡多久 |
    | `SHOW VARIABLES` / `STATUS` | 配置 / 运行计数 |
    | `SHOW WARNINGS` | 上一条截断、类型转换等 |
    | `SHOW CREATE TABLE` / `VIEW` / `DATABASE` | 对象定义 |
    | `SHOW GRANTS` | 权限 |
    | `SELECT DATABASE()` | 当前库 |

- <details>

    <summary>列类型</summary>

    >`NULL` 不是类型；能否空由 `NULL`/`NOT NULL` 决定。

    | 用途 | 类型 |
    | --- | --- |
    | 主键 | `BIGINT UNSIGNED AUTO_INCREMENT` |
    | 金额 | `DECIMAL(p,s)`，不用 `FLOAT`/`DOUBLE` |
    | 短文本 | `VARCHAR(n)` + `utf8mb4` |
    | 长文本 / 字节 | `TEXT` / `BLOB` |
    | 日期时间 | `DATE`；墙上时间 `DATETIME`；带时区换算 `TIMESTAMP` |
    | 真假 | `BOOLEAN`（=`TINYINT(1)`；严格 0/1 加 `CHECK`） |
    | 半结构化 | `JSON`（常查字段仍拆列） |

    | 类 | 要点 |
    | --- | --- |
    | 整数 | `TINYINT`～`BIGINT`；`UNSIGNED` 非负；`INT(11)` 的 `11` 是弃用显示宽度 |
    | 浮点 | `FLOAT`/`DOUBLE` 有误差，科学计算才用 |
    | 位 / 别名 | `BIT(n)`；`SERIAL` = `BIGINT UNSIGNED AUTO_INCREMENT UNIQUE` |
    | 时间 | `TIME` 可表时长；`fsp` 0～6；`YEAR` 只管年；`TIMESTAMP` ≈1970～2038 |
    | 定长串 | `CHAR`；`BINARY`/`VARBINARY` 按字节 |
    | 大对象 | `TINY`/`MEDIUM`/`LONG` + `TEXT`/`BLOB` |
    | `ENUM`/`SET` | 固定小集合；会变或要外键则拆表 |
    | 空间 | `POINT` 等 GIS |
    | 向量 | [`VECTOR(n)`](https://dev.mysql.com/doc/refman/9.7/en/vector.html) 自 9.0，**8.4 没有** |
    | 旧别名 | `INT1`～`INT8` 等，读懂即可，新表不用 |

    </details>

- <details>

    <summary>标识符与引号</summary>

    | 东西 | 写法 | 例子 |
    | --- | --- | --- |
    | 标识符 | 反引号 `` ` `` | `` SELECT `order-id` FROM `t` `` |
    | 字符串值 | 单引号 `'` | `WHERE name = 'Alice'` |
    | 数字 / 布尔 / `NULL` | 不加引号 | `WHERE id = 1` |

    >含 `-`/空格/数字开头/保留字 → 标识符**必须**反引号；单引号会变成字符串常量。优先 `snake_case`。串内 `'` 写成 `''`。双引号 `"` 勿当默认：无 `ANSI_QUOTES` 当字符串，有则当标识符 → 字符串只用 `'`。

    ```sql
    SELECT 'order-id' FROM t;   -- 常量
    SELECT `order-id` FROM t;   -- 列
    ```

    </details>

- <details>

    <summary>常用命令</summary>

    > 除 shell 备份/导入外均在 `mysql>`。`「...」` 换实际名。

    ```sql
    -- 库
    SHOW DATABASES;
    CREATE DATABASE IF NOT EXISTS 「库」;
    USE 「库」;
    SELECT DATABASE();
    SHOW CREATE DATABASE 「库」;
    DROP DATABASE IF EXISTS 「库」;

    -- 表
    CREATE TABLE IF NOT EXISTS 「表」 (
        id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL COMMENT '「列注释」',
        PRIMARY KEY (id)
    ) COMMENT='「表注释」';
    SHOW TABLES; DESCRIBE 「表」; SHOW CREATE TABLE 「表」;
    ALTER TABLE 「表」 ADD/MODIFY/DROP COLUMN ...;
    ALTER TABLE 「表」 RENAME COLUMN 「旧」 TO 「新」;
    RENAME TABLE 「旧」 TO 「新」;
    TRUNCATE TABLE 「表」;   -- DDL，不可 ROLLBACK
    DROP TABLE IF EXISTS 「表」;

    -- CRUD（UPDATE/DELETE 先同一 WHERE 查出再改）
    INSERT INTO 「表」 (「列1」, 「列2」) VALUES ('「值1」', '「值2」');
    SELECT 「列」 FROM 「表」 WHERE 「条件」;
    UPDATE 「表」 SET 「列」 = '「新值」' WHERE 「条件」;
    DELETE FROM 「表」 WHERE 「条件」;
    SELECT DISTINCT 「列」 FROM 「表」 WHERE 「条件」 ORDER BY 「列」 DESC LIMIT 「n」 OFFSET 「m」;
    SELECT 「列」, COUNT(*) AS total FROM 「表」 GROUP BY 「列」 HAVING COUNT(*) >= 10;
    SELECT a.「列」, b.「列」 FROM 「表A」 a LEFT JOIN 「表B」 b ON b.「键」 = a.「键」;

    -- 索引 / 事务 / 视图
    SHOW INDEX FROM 「表」;
    CREATE [UNIQUE] INDEX 「名」 ON 「表」 (「列」);
    DROP INDEX 「名」 ON 「表」;
    START TRANSACTION;  -- 等价 BEGIN / BEGIN WORK
    -- 三选一，不要连着跑：COMMIT;  |  ROLLBACK;  |  先 SAVEPOINT 「名」; 再 ROLLBACK TO SAVEPOINT 「名」;
    CREATE OR REPLACE VIEW 「视图」 AS SELECT ...;  -- 可加 WITH CHECK OPTION
    SHOW CREATE VIEW 「视图」;
    DROP VIEW IF EXISTS 「视图」;

    -- 用户 / 诊断
    CREATE USER IF NOT EXISTS '「用户」'@'「主机」' IDENTIFIED BY '「密码」';
    GRANT SELECT, INSERT, UPDATE, DELETE ON 「库」.* TO '「用户」'@'「主机」';
    SHOW GRANTS FOR '「用户」'@'「主机」';
    REVOKE SELECT, INSERT, UPDATE, DELETE ON 「库」.* FROM '「用户」'@'「主机」';
    DROP USER IF EXISTS '「用户」'@'「主机」';
    EXPLAIN SELECT ...;
    SHOW FULL PROCESSLIST;
    SHOW VARIABLES LIKE 'max_connections';
    SHOW STATUS LIKE 'Slow_queries';
    SHOW WARNINGS;
    ```

    ```shell
    # 导出 / 导入（勿把多行 SQL 粘贴进 mysql>；遇错前已成功语句不自动撤销）
    mysqldump --single-transaction -h 「主机」 -u 「用户」 -p 「库」 > 「备份.sql」
    mysql --default-character-set=utf8mb4 -h 「主机」 -u 「用户」 -p 「库」 < 「脚本.sql」
    # 已在 mysql>：SOURCE 「路径」;  或  \. 「路径」
    ```

    </details>

### PostgreSQL

<details>
<summary></summary>

PostgreSQL 是开源的对象关系型数据库管理系统，与 MySQL 一样使用表和 SQL，适合事务、关联查询和结构化数据。它强调标准 SQL、复杂查询以及类型、函数和扩展机制；是否选择它，应由项目需求和团队经验决定，而不是简单比较“谁更强”。

- **对象层级与角色**

    `集群（Cluster） -> 数据库（Database） -> 模式（Schema） -> 表、视图、函数等对象`

    - 一个集群可包含多个数据库；角色（Role）属于集群，带 `LOGIN` 属性的角色可作为登录用户。
    - 一次客户端连接只能访问一个数据库。访问其他数据库时，需要重新连接或使用 `\c 「数据库名」` 切换。
    - Schema 是数据库内的命名空间，可以组织同名对象；未写 Schema 的对象名按 `search_path` 查找，可用 `SHOW search_path;` 查看。

    >把允许不受信任用户创建对象的 Schema 加入 `search_path` 会带来对象名称被遮蔽的风险。生产环境应明确 Schema 所有者和 `CREATE` 权限，迁移脚本宜使用带 Schema 的对象名。

- **特色类型与 SQL**

    | 能力 | 适合场景 | 边界 |
    | --- | --- | --- |
    | `UUID` | 跨系统生成标识 | 评估索引大小和写入局部性 |
    | [PostgreSQL `jsonb`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#postgresql-jsonb) | 查询半结构化数据 | 稳定且高频查询的字段仍优先使用普通列 |
    | 数组、范围类型 | 短小同类值、区间与重叠判断 | 高频关联或独立更新的数据更适合子表 |
    | `RETURNING` | 直接返回增删改后的值 | 减少额外查询，不改变事务边界 |
    | `INSERT ... ON CONFLICT` | 依靠唯一约束实现原子 upsert | 冲突目标必须与约束匹配 |
    | CTE、窗口函数 | 拆分复杂查询，计算排名或累计值 | 仍需结合执行计划判断成本 |

- **索引与执行计划**

    | 索引 | 常见用途 |
    | --- | --- |
    | B-tree | 默认索引，适合等值、范围和排序 |
    | GIN | 适合数组、`JSONB`、全文检索等“一个值包含多个元素”的查询 |
    | GiST | 可扩展的搜索框架，常用于范围、几何、最近邻等操作 |

    >索引必须对应真实查询的操作符和数据分布，不要因为 PostgreSQL 支持的索引类型多就全部创建。`EXPLAIN` 只显示计划；`EXPLAIN (ANALYZE, BUFFERS)` 会实际执行语句并显示实际耗时、行数和缓冲区信息，对写语句使用前要放入可回滚事务并确认影响。

- **MVCC、VACUUM 与扩展**

    - PostgreSQL 使用 MVCC；`UPDATE` 和 `DELETE` 产生的旧版本由 `VACUUM` 清理并让空间复用，`ANALYZE` 更新优化器统计信息。
    - autovacuum 自动执行必要的清理、统计更新和事务 ID 回卷防护，应根据写入量调整，不要关闭。
    - `VACUUM FULL` 会重写表并取得强锁，不是日常清理命令；优先让普通 `VACUUM` 持续工作。
    - `CREATE EXTENSION` 把服务器已安装的扩展注册到当前数据库。引入扩展前要确认权限、版本升级、备份恢复和目标环境都支持它。

- **与 MySQL 的学习差异**

    >MySQL 中 `SCHEMA` 与 `DATABASE` 基本同义，PostgreSQL 的 Schema 则是数据库内的命名空间；两者默认隔离级别分别为 InnoDB 的 `REPEATABLE READ` 和 PostgreSQL 的 `READ COMMITTED`。整数 ID 在 MySQL 常用 `AUTO_INCREMENT`，PostgreSQL 推荐标识列（Identity）。PostgreSQL 索引通常指向堆元组，行不聚在主键索引里。

</details>

---

## NoSQL 数据库

NoSQL 不是一种固定的数据模型，而是键值、文档、列族、图等非关系型数据库的统称。本节只介绍 MongoDB 和 Redis。

### MongoDB

<details>
<summary></summary>

MongoDB 是文档数据库：一条记录是一个 BSON 文档，多个文档组成集合（Collection）。文档类似 JSON 对象，可以包含数组和嵌套文档；同一集合中的文档不必拥有完全相同的字段。

- **[BSON](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#bson) 与文档建模**

    BSON 是 MongoDB 存储和传输文档使用的带类型二进制格式；具体类型、Extended JSON、使用边界以及与 PostgreSQL `jsonb` 的区别见上方链接。此处重点是文档建模。

    | 关系 | 优先嵌入 | 优先引用 |
    | --- | --- | --- |
    | 读取方式 | 总是随父对象一起读取 | 经常独立查询 |
    | 生命周期 | 随父对象一起创建和删除 | 可独立修改或复用 |
    | 数据规模 | 数量有明确上限 | 数量可能持续增长 |
    | 典型关系 | 一对少量明细 | 多对多、共享对象、高基数关系 |

    >文档结构应从主要读写路径反推：把需要原子更新、经常一起读取且规模可控的数据嵌入；不要为了减少一次查询，把会无限增长的数组塞进单个文档。

- **查询与聚合管道**

    聚合管道把文档依次交给多个阶段处理。常用阶段可按 `筛选（$match） -> 变形（$project） -> 分组（$group） -> 排序（$sort） -> 限制数量（$limit）` 理解，但实际顺序应由结果语义和执行计划决定。

    ```javascript
    db.orders.aggregate([
      { $match: { status: "PAID" } },
      { $group: { _id: "$userId", paidTotal: { $sum: "$totalAmount" } } },
      { $sort: { paidTotal: -1 } },
      { $limit: 20 }
    ])
    ```

    >能提前过滤的数据通常尽早使用 `$match`，并只传递后续需要的字段。复杂管道应使用 `explain()` 检查索引利用、扫描量和是否出现大量内存或磁盘处理。

- **索引与 Schema Validation**

    单字段、复合、唯一和 TTL 索引分别服务于不同查询与约束；复合索引的字段顺序影响可用前缀，TTL 删除也不保证在到期瞬间完成。索引会增加存储和写入成本，应按真实查询建立。Schema Validation 可限制必填字段、BSON 类型和值范围，结构演进仍需兼容和迁移步骤。

- **原子性、事务与高可用**

    - 单文档写操作具有原子性；多文档事务会增加协调成本，应保持简短。大量关联和复杂事务是主线时，关系型数据库通常更直接。
    - 副本集提供冗余和故障转移，但读写保证还取决于 read concern、write concern 和 read preference。
    - 分片用于扩展容量和吞吐，分片键决定数据分布、查询路由和热点；只有需求明确且团队能承担运维复杂度时再引入。

    >灵活结构不等于没有 Schema，也不等于可以忽略约束、索引和恢复设计。

</details>

### Redis

Redis 主要在内存读写。事实数据仍在 MySQL；Redis 做缓存、会话、计数、排行、限流和分布式锁。丢了可以重建的才适合当缓存。接口突然打满数据库，根因经常是缓存失效或穿透，而不是页面多渲染了一次。访问链路：`页面 -> HTTP API -> 后端 -> Redis 客户端 -> Redis`。前端不直连。

学习顺序：`场景与 key -> 数据结构 -> 原子/Pipeline -> Cache Aside -> Java -> 锁 -> 过期与持久化 -> 复制`。

1. **什么时候用**

    | 场景 | 用 Redis | 仍以 MySQL 为准 |
    | --- | --- | --- |
    | 热点详情、配置 | 缓存查询结果，带 TTL | 写入和强一致读 |
    | 登录会话 | 可存 Session / token 元数据 | 账号、权限等事实 |
    | 计数、限流 | `INCR` + TTL | 对账、累计以库为准 |
    | 排行榜 | Sorted Set | 结算、发奖落库 |
    | 简易队列 | List；要确认/重试再用 Stream 或 MQ | 不能丢的业务事件优先 MQ |
    | 余额、库存 | 可缓存展示，不作唯一真相 | 扣减走库事务或明确方案 |

    key 用稳定前缀：`「环境」:「业务」:「对象」:「id」`。每个缓存 key 都要有 TTL。不要把无界列表塞进一个 key。

    - <details>

        <summary>无界列表与大 key</summary>

        >「无界」指元素会随业务持续增长、没有自然上限的集合。常见误用：把某用户全部订单、某帖全部评论、全站消息 / 浏览历史，整包序列化进一个 String，或塞进同一个 List / Set / Sorted Set，指望「一次 GET 全拿走」。

        Redis 按 key 计内存与淘汰。单 key 体积与元素数没有业务上限时，问题会叠在一起：

        | 风险 | 表现 |
        | --- | --- |
        | 内存失控 | 活跃用户 / 热门对象各自拖一个越来越大的 value，实例被少数大 key 占满 |
        | 读写变重 | `GET`、整段 `LRANGE`、反序列化都按「整份数据」付费，延迟随体积上涨 |
        | 局部改不动 | 只增删一条也常要读改写整包；TTL 一过要整份回填，雪崩时重建更贵 |
        | 运维卡顿 | 大 key 删除、过期、主从复制、`RDB`/`AOF` 时更容易抖动；应用侧偶发超时 |

        >和后面「大 key / 热 key」同源：规模不可预期的列表，本质就是在制造大 key。

        做法上，让每个 key 里的数据**规模可预期、可过期**：

        1. 只缓存有界结果：详情对象、配置、排行榜 Top N、限流计数——本身就有上限。
        2. 列表只留窗口：最近 N 条时间线用 List + `LTRIM`；排行用 Sorted Set 只保留 Top N，完整历史走 MySQL / ES 分页。
        3. 按页或时间窗拆 key：如 `prod:order:user:123:p:1`、`prod:feed:2026-10-19`，单 key 体积可控，失效粒度也更细。
        4. 需要集合运算时，成员集合本身也要有边界或淘汰策略，不要把「全站用户 ID」当成一个永久 Set。

        >判别：这个 key 一年后会不会大一个数量级？会，就不要整包进一个 key。

        </details>

1. **数据结构**

    按操作选型，不要把所有对象都序列化成大字符串。计数用 `INCR`，集合运算用 Set，排名用 Sorted Set。

    - <details>

        <summary>怎么读 Redis 命令（语法入门）</summary>

        >Redis 命令行（`redis-cli`）和多数客户端，本质都是：**命令名 + 空格分隔的参数**。没有 SQL 那种 `SELECT ... FROM`；一条命令做一件事。

        **通用形状**

        ```text
        命令  key  [参数...]  [选项...]
        ```

        | 位置 | 是什么 | 例子里的词 |
        | --- | --- | --- |
        | 命令 | 动词，全大写习惯写法 | `SET`、`HGET`、`ZADD` |
        | key | 数据名字，你自己定 | `prod:user:42` |
        | 参数 | 值、字段名、分数、下标等 | `'{"id":42}'`、`userId`、`980` |
        | 选项 | 改命令行为的关键字 | `EX 600`（600 秒后过期） |

        **拆一条读**

        ```text
        SET   prod:user:42   '{"id":42,"name":"Ada"}'   EX 600
        │     │              │                          │
        │     │              │                          └─ 选项：600 秒后过期
        │     │              └─ 参数：要存的值（一段 JSON 字符串）
        │     └─ key：环境 prod、对象 user、id 42
        └─ 命令：写入一个 String
        ```

        **命令名前缀 ≈ 数据结构**（看到前缀就知道在操作哪种类型）

        | 前缀 | 类型 | 记忆 |
        | --- | --- | --- |
        | （无，如 `SET`/`GET`/`INCR`） | String | 最基础 |
        | `H` | Hash | Hash field |
        | `L` / `R` / `B` | List | Left / Right / Blocking（阻塞） |
        | `S`（非 `SET` 那条） | Set | Set，如 `SADD` |
        | `Z` | Sorted Set | 有序，带 score |
        | `X` | Stream | 流式消息 |

        **常见选项词**（后面示例会反复出现）

        | 词 | 含义 |
        | --- | --- |
        | `EX 秒` | 多少秒后过期（和 `SET` 连用） |
        | `PX 毫秒` | 多少毫秒后过期 |
        | `NX` | 仅当 key **不存在** 时才写入（常用于锁） |
        | `XX` | 仅当 key **已存在** 时才写入 |
        | `WITHSCORES` | 查出成员时带上分数 |
        | `LIMIT 偏移 条数` | 只取一段结果 |

        **和 SQL 的直觉对照**

        | 你熟悉的 | Redis 里大致对应 |
        | --- | --- |
        | 表名 + 主键 | 一个 **key**（整份数据的名字） |
        | 一行里的列 | Hash 的 **field**，或 String 里整段 JSON |
        | `UPDATE t SET c=1` | `SET key value` 或 `HSET key field value` |
        | `SELECT c FROM t WHERE id=?` | `GET key` / `HGET key field` |
        | 没有「查所有表」的常规写法 | 禁止用 `KEYS *` 扫全库；按已知 key 读写 |

        >Java 里一般不手敲这些字符串，而是 `stringRedisTemplate.opsForValue().set(...)`；但客户端发出去的仍是同一套命令。先会读 `redis-cli` 示例，再去对模板方法名。

        </details>

    | 数据结构 | 特点 | 常见用途 |
    | --- | --- | --- |
    | String | 字符串、数字或二进制 | 缓存值、计数器、状态 |
    | Hash | 一个 key 下多个字段 | 对象若干属性一起改 |
    | List | 有序序列 | 简单队列、时间线 |
    | Set | 无序且不重复 | 标签、去重、交并差 |
    | Sorted Set | 成员不重复，按分数排序 | 排行榜、按时间排序 |
    | Stream | 只追加，支持消费组 | 要确认和重试的消息流 |

    - <details>

        <summary>各数据结构怎么选（含示例）</summary>

        >选型看「要做的操作」，不是看「业务对象叫什么」。能用原子命令完成的，就不要整对象序列化成大 String 再在应用里改。下面每行右侧 / `#` 后是人话翻译。

        1. **String**：一个 key 对应一块二进制 / 文本 / 数字。适合整份缓存、计数、简单状态。

            ```text
            # 命令  key            值                         选项
            SET    prod:user:42   '{"id":42,"name":"Ada"}'   EX 600
            # → 把用户 42 的详情缓存 600 秒

            INCR   prod:article:9:views
            # → 文章 9 的阅读数 +1（值必须是整数）

            SET    prod:feature:dark_mode   1   EX 3600
            # → 功能开关打开，1 小时后过期
            ```

            >整份 JSON 缓存详情没问题；若经常只改其中一个字段，用 Hash 更合适。计数用 `INCR` / `INCRBY`，不要 `GET` 再 `SET`。

        2. **Hash**：一个 key 下多个 field-value，像「小对象」。写法：`HSET key 字段 值 [字段 值 ...]`。

            ```text
            # 命令  key                 字段      值   字段  值     字段      值
            HSET   prod:session:abc    userId    42   role  admin  lastSeen  1730000000
            # → 会话 abc：三个字段一次写好

            HINCRBY  prod:sku:1001  stock  -1
            # →          key         字段   增量：库存减 1

            HGET  prod:session:abc  role
            # → 只取一个字段，返回 admin
            ```

            >会话元数据、商品可展示字段、配置块常用。字段很多或 value 很大时，仍要注意单 key 体积；不是无限字段的垃圾桶。

        3. **List**：有序、可重复；`L`=左边（头），`R`=右边（尾），`B`=阻塞等待。

            ```text
            LPUSH  prod:queue:email  '{"to":"a@x.com","tpl":"welcome"}'
            # → 从左边推进一条待发邮件

            BRPOP  prod:queue:email  5
            # → 从右边取一条；没有就最多等 5 秒（左进右出 ≈ 队列）

            LPUSH  prod:feed:42  post:9
            LTRIM  prod:feed:42  0  99
            # → 用户 42 时间线塞入 post:9，再只保留下标 0..99（最近 100 条）
            ```

            >`LTRIM` 把时间线截成最近 100 条，避免无界膨胀。要确认、重试、多消费者协作时，升级到 Stream 或外部 MQ，不要硬扛 List。

        4. **Set**：无序、成员唯一。`SADD key 成员...`；判断用 `SISMEMBER`；交集 `SINTER`。

            ```text
            SADD  prod:post:9:tags  redis  cache  java
            # → 文章 9 打上三个标签（重复添加无效）

            SISMEMBER  prod:post:9:tags  redis
            # → redis 是不是该文章的标签？返回 1/0

            SINTER  prod:user:1:liked  prod:user:2:liked
            # → 用户 1 和 2「都喜欢」的成员（交集）
            ```

            >「共同喜欢」「双方好友」这类集合运算是 Set 的强项。成员集合本身也要有边界或 TTL，不要把全站 ID 灌进一个永久 Set。

        5. **Sorted Set（ZSet）**：成员唯一，各带一个 **score（分数）** 用来排序。`ZADD key 分数 成员 [分数 成员 ...]`。

            ```text
            ZADD  prod:rank:game  980  u:42  1200  u:7
            # →                分数 成员   分数  成员：u:7 分更高

            ZREVRANGE  prod:rank:game  0  9  WITHSCORES
            # → 按分数从高到低取第 0..9 名，并带上分数（Top 10）

            ZADD  prod:delay:jobs  1730003600  job:55
            # → score = 执行时间戳，到点再捞

            ZRANGEBYSCORE  prod:delay:jobs  0  1730003600  LIMIT 0 20
            # → 取出 score 在 [0, 该时刻] 的任务，最多 20 条
            ```

            >排行榜只保留 Top N 或定期裁剪；延迟任务用「执行时间戳当 score」。需要按多个维度排序时，往往要多个 ZSet 或回表，不要指望一个 ZSet 解决所有排序。

        6. **Stream**：只追加的消息流。字段成对出现：`XADD key * 字段 值 [字段 值 ...]`（`*` = 让 Redis 自动生成消息 ID）。

            ```text
            XADD  prod:events:order  *  orderId  88  status  paid
            # → 追加一条订单事件；* 表示自动分配 ID

            XGROUP CREATE  prod:events:order  cg1  0  MKSTREAM
            # → 建消费组 cg1；从 ID 0 开始；没有流就建流

            XREADGROUP GROUP  cg1  worker1  COUNT 10  STREAMS  prod:events:order  >
            # → 组 cg1、消费者 worker1，最多读 10 条；> = 尚未派给组内的新消息

            XACK  prod:events:order  cg1  1730000000000-0
            # → 确认这条消息已处理完（ID 形如 时间戳-序号）
            ```

            >比 List 多了消费进度与确认；仍不是 Kafka 的完整替代——跨机房、长期堆积、复杂路由优先专业 MQ。Redis 丢了可重建的事件可以进 Stream；不能丢的核心业务事件优先 MQ + 落库。

        | 你想做的事 | 优先选 |
        | --- | --- |
        | 缓存整份详情 / 计数 / 开关 | String |
        | 改对象的某几个字段 | Hash |
        | 简单排队、最近 N 条 | List（定长） |
        | 标签、去重、交并差 | Set |
        | 排行、按分取 Top、延迟队列 | Sorted Set |
        | 要 ACK / 消费组的消息 | Stream（或 MQ） |

        </details>

1. **原子、Pipeline、事务**

    Redis 的“原子”是单条命令执行时不被插队，**不是** MySQL 那种失败整笔回滚。先 `GET` 再 `SET` 仍会被别的请求穿插。批量降低 RTT（Round-Trip Time，一次请求打到 Redis 再收到响应的网络往返耗时）用 Pipeline；要条件 + 多步不被打断，用短 Lua，不要自己拼一长串客户端往返。

    - <details>

        <summary>原子操作、Pipeline、事务与脚本</summary>

        >对 Redis 单条命令：服务端执行时不可分割，过程中不会被其他客户端插队。不等于多步失败后自动回滚，也不等于已经持久化。

        | 机制 | 解决的问题 | 边界 |
        | --- | --- | --- |
        | 单条命令 | 一次数据结构操作不被打断 | 多条命令之间仍可被穿插 |
        | Pipeline | 一次发送多条，减少网络往返 | 不是事务，整批不原子 |
        | [`MULTI` / `EXEC`](https://redis.io/docs/latest/develop/using-commands/transactions/) | 排队后连续执行 | 某条报错，其余仍继续，已成功的不回滚；可配合 `WATCH` |
        | [Lua / Redis Functions](https://redis.io/docs/latest/develop/programmability/) | 服务端原子做判断和多步 | 执行期间阻塞其他活动，必须短 |

        | 对比项 | Redis | MySQL 事务 |
        | --- | --- | --- |
        | 基本保证 | 单条原子；`MULTI`/`EXEC` 连续执行、不被插入 | 多条 SQL 提交或回滚 |
        | 执行错误 | `EXEC` 后某条失败，其他仍执行 | 可 `ROLLBACK`，可用保存点 |
        | 并发 | `WATCH` 发现 key 被改则放弃 `EXEC`，客户端重试 | 隔离级别、锁、MVCC |
        | 持久 | 取决于 RDB / AOF，不是原子自带的 | ACID 里单独一项 |

        >一句话：Redis 强调“这组命令执行时不被插队”；MySQL 还提供失败回滚和可配置隔离。MySQL 部分 DDL 会隐式提交。

        </details>

1. **Cache Aside 与拖垮接口的几种情况**

    Cache Aside（旁路缓存）：应用自己管缓存，数据库不管 Redis。MySQL 仍是事实，Redis 只加速读。缓存站在库旁边，由后端决定何时读、何时填、何时删，不是库触发器自动同步。

    - 读：先 Redis；命中直接返回；未命中再查 MySQL，把结果回填进 Redis（带 TTL）。
    - 写：先提交 MySQL，再**删掉**对应缓存（不要先改 Redis）。下次读未命中时从库加载新值。

    只缩短「库已新、缓存还旧」的窗口，不是强一致。删缓存失败、两个请求并发回填，都可能短暂读到旧数据，失败要重试或补偿。余额、库存的强一致读直接查库。

    | 问题 | 页面/接口上像什么 | 常用处理 |
    | --- | --- | --- |
    | 穿透 | 乱 id / 不存在的资源把数据库打满 | 参数校验、短时缓存空结果 |
    | 击穿 | 某个热点突然变慢、库 CPU 飙 | 互斥回填、逻辑过期、提前刷新 |
    | 雪崩 | 大批接口同时变慢 | TTL 加随机值、预热、限流降级 |
    | 污染 | 内存被一次性查询占满 | 合理 TTL、`maxmemory`、淘汰策略 |
    | 热 key | 单接口或单用户把实例打满 | 本地缓存、合并请求、拆 key |
    | 大 key | 偶发超时、主从同步卡住 | `MEMORY USAGE` / `--bigkeys`，拆分，删除用 `UNLINK` |

    监控命中率、内存、淘汰、延迟和复制；`KEYS *` 和全量扫描避开高峰。

1. **Java 访问**

    Spring Boot 默认常用 Lettuce 连接；序列化要全项目统一（JSON 与 JDK 序列化不能混读）。`@Cacheable` 必须明确 key 和 TTL，不要用默认“永不超时”。在 `@Transactional` 提交成功后再删/写缓存，避免库回滚了缓存还在。锁不要手写一长串 `SETNX`，用短 Lua 或成熟客户端（如 Redisson）。Redis 连接和 MySQL 连接池不是一回事，超时、重试要单独配。

1. **分布式锁**

    简单互斥：`SET 「lockKey」 「唯一令牌」 NX PX 「超时毫秒」`。解锁必须原子地“比较令牌后再删除”，避免误删别人后来拿到的锁。锁超时、业务跑太久、网络分区仍可能破坏互斥；要续期或 fencing token 用经过验证的方案，不能只靠一个 `SETNX`。有锁不等于有事务：锁只互斥，改库存仍要落到 MySQL。

1. **过期、内存与持久化**

    TTL 是过期；内存碰到 `maxmemory` 后按 `maxmemory-policy` 淘汰。过期 key 不保证到期瞬间立刻释放。`noeviction` 达到上限后写命令可能报错。RDB 是快照，AOF 是写命令重放；可单用、组合或关闭。任何持久化都不能代替备份。缓存实例丢数据应能从 MySQL 重建；把唯一真相只放 Redis 时，丢失窗口要事先接受。

1. **复制与高可用**

    | 方案 | 作用 | 需要注意 |
    | --- | --- | --- |
    | 主从复制 | 副本和读扩展 | 默认异步，不负责自动故障转移 |
    | Sentinel | 监控、发现、自动故障转移 | 客户端要支持 Sentinel；故障时已确认写入仍可能丢 |
    | Redis Cluster | 多分片扩容量，带副本切换 | 客户端要支持 Cluster；跨槽多 key 受限 |

    高可用不等于不丢数据，也不等于备份。部署前明确允许的丢失窗口，并演练故障转移和客户端重连。

---

## 知识点备忘

1. **分库分表**

    把原本「一个库、一张表」里的数据，按规则拆到多个库、多张物理表，摊薄单机容量与 QPS。中间件（如 ShardingSphere、TDDL）或应用路由把逻辑表映射到物理表；业务仍写逻辑表名。可只分库、只分表，或两者并用。

    | 做法 | 做什么 | 例子 |
    | --- | --- | --- |
    | 分表 | 同一库内一张逻辑表 → 多张物理表 | `order` → `order_0` … `order_15` |
    | 分库 | 拆到多个库（常多机） | `db_0.order_*` … `db_3.order_*` |

    路由靠**分片键**（如 `user_id`）：`库 = user_id % 4`，`表 = ⌊user_id / 4⌋ % 16`（整除）。带分片键的读写只打一台库一张表；没有分片键就要广播或另建映射。主键需全局唯一（雪花 ID / 号段等），不能依赖各分片本地自增当全局 ID。

    >- 雪花 ID：按「时间 + 机器号 + 序列」拼出的 64 位整数，本地发号自己算、不查库。
    >- 号段：向发号中心一次领一段连续号，本地慢慢用，仍像自增整数。

    >- **举例：电商订单**：单表 `db.order` 做到数亿行、高峰写数万/秒时：索引巨大、按用户查变慢、备份/DDL 太重、单机磁盘与连接顶满。按 `user_id` 拆成 4 库 × 16 表后，分布均匀时每张表行数约为原来的 1/64，写流量摊到多机，「查我的订单」仍走单分片，接近单表体验。分布不均（大卖家/热用户）仍会倾斜，热点需单独治理。

    | 解决的问题 | 不解决 / 变难的 |
    | --- | --- |
    | 单表过大、单机吞吐不够 | 全站汇总、复杂 JOIN、全局排序分页 |
    | 单分片故障影响面与单次备份体积缩小（运维对象变多） | 按订单号查但不知 `user_id`（需映射或广播） |
    | 带分片键的读写可水平扩展<br>（扩分片/改键常需迁数据、改路由：双写 → 对账校验 → 切流） | 跨库强事务贵 → 多改**最终一致**（本地事务 + 消息/任务补齐；重试、幂等、对账） |
    |  | 扩容或改分片键成本高；选键能覆盖主路径查询 |

    >能不分先垂直优化、读写分离、归档；真不够再上。分库分表换的是容量与吞吐，不是万能查询加速。
1. **dry-run**

    预演将要执行的库变更（看计划、做校验），**不提交实际写库结果**；有的实现只打印 SQL / 计划，根本不连库。

    | 场景 | dry-run 通常看什么 |
    | --- | --- |
    | Schema 迁移 | 将跑哪些变更、顺序、与当前库是否冲突 |
    | DDL（加列、改索引等） | 语句是否合法、对象是否存在、是否明显会锁表/重建 |
    | 导入 / 批量改数 | 影响范围（行数估计）、约束与类型是否过得去 |

    | 常能验到 | 验不到 / 别当成安全保证 |
    | --- | --- |
    | 语法、对象名、部分权限与依赖冲突 | 生产真实耗时、锁等待、磁盘打满、并发下的竞态 |
    | 「打算执行什么」（计划是否符合预期） | 工具若仍写 changelog、或短暂加锁——名义 dry-run 也可能有副作用 |

    深度大致三档（越往后越「像真跑」，也越可能碰到库）：只出计划 → 连库校验但不落变更 → 在事务里执行再 `ROLLBACK`（手工 dry-run）。后两档仍可能读生产元数据或短暂占锁。

    >- **`EXPLAIN`**：看查询怎么走，不预演「改库」。
    >- **事务里试跑再回滚**：一种手工 dry-run；自动提交、或 DDL 在部分引擎上隐式提交时，回滚救不了。
    >- **隔离环境恢复演练**：真恢复一遍，验证备份可用；不是 dry-run。

    >上线前用 dry-run 减「跑错语句 / 漏步骤」；生产仍要备份、变更窗口和回滚方案。Flyway、Liquibase、Prisma 等迁移工具多带 dry-run / 打印计划能力，以各工具文档为准。
