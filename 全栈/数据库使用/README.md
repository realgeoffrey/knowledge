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

- 数据库是有组织的数据集合，数据库管理系统（DBMS）是管理、存取这些数据的软件。下文按惯例把 MySQL、Redis 等产品简称为数据库。

    | 数据库 | 类型 | 数据组织方式 |
    | --- | --- | --- |
    | MySQL | 关系型数据库 | 表、行、列 |
    | PostgreSQL | 关系型数据库 | 表、行、列，并支持丰富的类型和扩展 |
    | MongoDB | NoSQL 文档数据库 | BSON 文档、集合 |
    | Redis | NoSQL 键值数据库 | 内存中的键和多种数据结构 |

    >本文的订单示例用 MySQL 保存订单、执行事务和约束，用 Redis 缓存可重建的查询结果。两者如何配合读写，见 [Redis](#redis) 一节的 Cache Aside。

---

## 数据库

1. 数据库类型

    1. 关系型数据库管理系统（relational database management system，RDBMS）

        Oracle、MySQL、PostgreSQL、SQL Server。

        >- MySQL 的官方读法是 `My S-Q-L`，也有人读作 `my sequel`。
        >- 数据按表组织，每行是一条记录，每列有指定类型。SQL 描述要取哪些数据，外键维护表之间的引用关系，事务把多步修改作为一个单元提交。
    2. 非关系型数据库（Not only SQL，NoSQL）

        >NoSQL 涵盖多种数据模型。选型时先看读写方式，再核实产品支持的查询、事务和分片能力。

        1. 面向文档（document-oriented）

            MongoDB、CouchDB。

            >database → collection → document / field。文档多为 BSON/JSON，嵌套结构贴近对象；适合内容、配置、日志等结构易变数据。
        2. 键值存储（key-value）

            Redis、DynamoDB（也支持文档模型）。浏览器里的 IndexedDB 也能按键存取对象，适合客户端本地存储。

            >给定键就能定位对应的值。例如 Redis 可以按会话 ID 读取会话，也可以用原子命令更新计数器。
        3. 列族 / 宽列（column-family / wide-column）

            Cassandra、HBase、Bigtable。

            >查询通常围绕行键或分区键设计，例如按设备和时间段读取测量值。列如何定义因产品而异。分析型列式数据库（如 ClickHouse）按列压缩、扫描数据，Parquet 则是列式文件格式。
        4. 图数据库（graph）

            Neo4j、Amazon Neptune。

            >节点 + 边建模关系；适合社交关系、推荐、权限、知识图谱等「多跳关系」查询。
        5. 搜索引擎（常被归进广义 NoSQL）

            Elasticsearch、OpenSearch。

            >全文搜索常用倒排索引来查找包含词项的文档。用作搜索副本时，主数据存于业务库，需要安排索引更新和重建。

    >- 选型直觉：结构稳定 + 关联 + 事务 → RDBMS；热点读 / 会话 / 限流 → Redis；文档形态易变 → MongoDB；多跳关系 → 图库；全文检索 → ES。可组合，不是二选一。
    >- 分布式系统还会谈到 CAP 与 BASE。CAP 指网络发生分区时，无法同时保证线性一致性和可用性（每个发给正常节点的请求都能得到有效响应）。BASE 指基本可用、软状态、最终一致。
2. 关系型数据库的范式

    范式根据属性之间的依赖判断表结构可能出现哪些冗余和更新异常。拆表后应能通过连接还原原来的关系。[《数据库系统概念》：关系数据库设计](https://www.db-book.com/slides-dir/PDF-dir/ch7.pdf)

    1. 第一范式（1NF）

        每行的每个属性取其定义域中的一个原子值。是否当作整体，取决于业务怎样使用这个值。

        >例如，一个用户有多个电话号码，业务要按号码查找或单独验证。将它们存为 `user_phone(user_id, phone)` 中的多行，就能直接查询和约束每个号码。拼成逗号分隔的字符串会让这两件事都变难。
    2. 第二范式（2NF）

        在满足 1NF 的基础上，每个非主属性（不属于任何候选键的属性）都**完全依赖**于每个候选键。去掉该键的任何一列，剩余部分都不足以决定这个属性。

        >若所有候选键都是单列，满足 1NF 的表就满足 2NF；单列主键之外若还有复合候选键，也要检查后者。违反例：订单明细用 `(order_id, product_id)` 作主键，却把 `product_name` 放在明细里——`product_name` 只依赖 `product_id`，应放到商品表。

        >键的常见说法：
        >
        >1. 候选键能唯一标识一行，去掉其中任何一列都会失去这个保证。一张表可以有多组候选键。
        >2. 主键：从候选键中选定的那一组，非空、唯一，一表一个。
        >3. 复合主键（也常称联合主键）：同一表内主键由多列组成，如 `PRIMARY KEY (字段1, 字段2)`；单列不必唯一，合在一起必须唯一。跨表关联用外键（或中间表）表达，不要把「多表主键拼起来查」叫作联合主键。
        >4. 外键：引用本表或另一表的键（通常是主键 / 唯一键），由 DBMS 维护参照完整性。
    3. 第三范式（3NF）

        函数依赖 `X → A` 表示任意两行的 X 相同，A 也一定相同。3NF 要求每个非平凡依赖（A 不在 X 中）至少满足一项：X 是超键，即能唯一定位一行；或 A 属于某个候选键。

        >非主属性只应直接依赖候选键。违反例：员工表存 `dept_id` 又存 `dept_name`，而 `dept_name` 由 `dept_id` 决定——部门名应在部门表。
    4. 巴斯-科德范式（BCNF）

        对每个**非平凡**函数依赖 `X → A`，`X` 都必须是**超键**。满足 BCNF 的关系也满足 3NF。

        >即使 A 属于候选键，BCNF 对 X 也有同样的要求。一张满足 BCNF 的表可以有多个候选键。

    >实际工作中，逻辑模型做到 3NF（必要时 BCNF）通常够用；物理落地可按读路径适度反范式。4NF / 5NF 解决多值依赖、连接依赖，业务库很少主动追到那一层。

    >1. 拆表前先明确每个属性描述哪个业务事实。拆表后，再检查原有约束能否继续由数据库直接维护。
    >2. 对热点查询，可根据执行计划和测量结果引入冗余字段、汇总表或物化视图，并约定刷新方式。
    >
    >    >例如，订单冗余用户的**当前姓名**，用户改名后要更新副本。若字段记录的是**下单时的姓名**，它描述订单当时的事实，用户后来改名仍应保留原值。
    >3. 范式主要缓解的问题
    >
    >    1. 操作异常
    >
    >        1. 插入异常：某实体必须挂靠另一实体才能落库，导致无法单独表示。
    >        2. 更新异常：改一个业务事实要改多行，易漏改不一致。
    >        3. 删除异常：删一行时把本应保留的另一实体信息一并删掉。
    >    2. 数据冗余：同一事实多处存放，或某列可由其他列计算得出却仍重复存储。
3. 数据库设计

    >已上线的表可能有旧版应用和历史数据。改列类型、删列或收紧约束前，要考虑新旧应用能否同时读写，以及历史数据怎样迁移。

    1. 需求分析

        1. 有哪些实体、事件、状态（数据是什么）。

            >- 实体：要持久化、可单独辨认的业务对象，设计上常对应一张表。e.g. 用户、商品、店铺。
            >- 事件是某时刻发生的事实，如支付成功、退款完成。需要审计或追溯时，单独记录事件及时间。仅凭订单当前状态，无法还原每次状态变更。
            >- 状态：实体或流程当前所处档位，多落成枚举 / 状态字段，有时配状态变更日志。e.g. 订单：待付 / 已付 / 已取消。
            >- 同一业务常三者并存：实体是「订单」，事件是「支付成功」，状态从「待付」变为「已付」。临时 UI 态、纯缓存一般不算要进库的实体。
        2. 属性、基数、唯一性、是否可空。

            >- 属性：实体要存哪些字段及其含义。e.g. 用户：邮箱、昵称、注册时间。
            >- 基数：与其他实体「几个对几个」，决定要不要中间表。e.g. 用户 1 : N 订单；订单 N : N 商品。
            >- 唯一性：哪些值在表内不能重复，对应主键 / `UNIQUE`。e.g. 邮箱全局唯一；`(order_id, product_id)` 联合唯一。
            >- 是否可空决定列能否存 `NULL`，默认值决定插入时省略该列会填什么。例如昵称可空，订单的 `user_id` 必须有值。
        3. 生命周期、增长速度、读写比、一致性要求、是否值得进库（有的只适合日志 / 对象存储 / 缓存）。

            >- 生命周期：活多久、何时归档 / 删除。e.g. 会话三十分钟过期；订单保留数年再归档。
            >- 增长速度：预估增量，决定分区、分表或独立存储。e.g. 访问日志日增千万行，不宜与核心业务表同库同表策略。
            >- 读写比影响索引和缓存的收益。商品详情读多写少，可以缓存。埋点表写入频繁，每个额外索引都会增加写入成本。
            >- 一致性：能否接受短暂不一致。e.g. 扣库存可用带余量条件的原子更新，或在事务中加锁检查；个人主页粉丝数可通过消息异步更新。
            >- 是否进库：不是所有数据都进业务库。大文件进对象存储只存 URL；验证码 / 限流进 Redis；可重建的搜索索引 / 报表可丢了再算。
    2. 逻辑设计

        ER 建模：一对一、一对多、多对多；用范式约束；明确主键、外键、唯一约束。

        >- 多对多通常用中间表保存两侧外键。如果同一对只允许出现一次，可将两列设为复合主键或加组合唯一约束。若允许同一商品在订单中分成多行，可用订单行号区分。
        >- 一个用户可有多笔订单，外键放在订单表。若一个用户最多只有一份资料，可用 `user_profile.user_id` 同时作主键和外键。只加外键仍允许多条资料指向同一个用户。
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

            1. 参与算术的数量用数值类型；邮编等编码若要保留前导零，用字符串。
            2. `CHAR` 定长；`VARCHAR` 变长；超长文本用 `TEXT` / 对象存储，避免无意义的超大 `VARCHAR`。
            3. 金额用 `DECIMAL`（或整数分），不用 `FLOAT` / `DOUBLE`。
            4. 时间按语义选型。支付发生的时间点可用 PostgreSQL `timestamptz` 或 MySQL `TIMESTAMP`，两者均按会话时区显示。MySQL 8.4 的 `TIMESTAMP` 上限在 2038 年，超出时可约定用 `DATETIME` 保存 UTC。[MySQL 日期时间类型](https://dev.mysql.com/doc/refman/8.4/en/datetime.html) · [PostgreSQL 日期时间类型](https://www.postgresql.org/docs/17/datatype-datetime.html)

                >门店预约可用 MySQL `DATETIME` 或 PostgreSQL `timestamp` 保存当地日期时间，并另存门店时区。在采用夏令时的地区，拨快时有些本地时间会跳过，拨慢时有些会出现两次。确认预约时应处理这两种情况，并记录最终选定的时间点。[PostgreSQL 对夏令时时间歧义的说明](https://www.postgresql.org/docs/17/datetime-invalid-input.html)
            5. 主键宜短且稳定。选自增 ID 或 UUID 时，考虑是否要在多节点发号，以及写入对索引的影响。使用 `deleted_at` 做软删除，还要明确查询是否包含已删除行。
        4. 索引与反范式。

            >索引服务真实 `WHERE` / `JOIN` / `ORDER BY`，不是越多越好；写放大与空间是成本。反范式是空间换时间，要适度并保证冗余可维护。

            1. 减少热点读路径上的联表次数。
            2. 汇总表 / 冗余列服务列表与报表。
            3. 冗余字段 / 冗余表要事先约定：**谁改、何时改**（同步写、异步校正，或当作历史快照故意不改）。

                >例如，订单表缓存用户当前姓名时，可由改名事务同步更新，也可在提交后异步刷新。选异步方案时，要约定页面可接受的延迟以及刷新失败后的补偿方式。
    4. 维护优化

        1. 维护数据字典与变更记录。
        2. 新需求优先加表 / 加列，破坏性变更走迁移与兼容窗口。
        3. 用执行计划和实际负载评估索引。删索引前核实低频任务是否使用它，以及唯一约束、外键是否依赖它。
        4. 大表按时间 / 业务键拆分（分区、冷热分离、归档）。

            >例如，按 `created_at` 给订单表做月分区，数据库可对带日期范围的查询裁剪分区，也更容易整月归档。若瓶颈是单机容量或写吞吐，可按 `user_id` 把数据分片到多台机器，代价是跨用户查询可能访问多个分片。冷热分离则按访问频率选择存储位置。[PostgreSQL 表分区](https://www.postgresql.org/docs/current/ddl-partitioning.html)

        >维护阶段最容易「只加不收」。每次大改仍应回到：需求 → 逻辑 → 物理，避免表结构无序膨胀。
4. 事务（transaction）

    事务把一组数据库修改作为一个逻辑单元提交或回滚。例如转账的扣款和入账应一起生效。回滚只撤销本事务内可回滚的修改，已发送的邮件或 HTTP 请求仍然有效。

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
        3. 幻读：同一事务内按相同条件两次查，行集合因别人已提交的插入、删除或改变匹配条件的更新而变化。

        标准四级从弱到强：`READ UNCOMMITTED`、`READ COMMITTED`、`REPEATABLE READ`、`SERIALIZABLE`。哪一级挡住哪种异常、引擎默认与 `SET` 写法见 [MySQL](#mysql) 的事务、隔离与锁；JDBC / Spring 见其后的 Java 访问。

        - 写冲突解决方案（多人改同一行 / 争同一业务键）：

            1. 唯一约束适合防止重复创建。例如，给报名表的 `user_id` 和 `activity_id` 都加 `NOT NULL`，再声明 `UNIQUE (user_id, activity_id)`。即使两个请求同时查到「尚未报名」，也只有一条能提交。竞争同一键的插入可能先等待对方提交或回滚。MySQL 和 PostgreSQL 默认允许唯一键含 `NULL` 的多行共存。[PostgreSQL 约束](https://www.postgresql.org/docs/17/ddl-constraints.html)
            2. 乐观锁：默认觉得很少撞车，先读后改，写时再验。行上有 `version`，必须**验旧值并抬版本**：`UPDATE … SET …, version = version + 1 WHERE id=? AND version=?`；影响 0 行表示记录不存在或版本已变，重读后按业务决定是否重试。缺「抬版本」则冲突检测形同虚设。适合个人资料等冲突少的场景。
            3. 悲观锁适合必须先读取再判断的修改。在同一事务、同一连接里用 `SELECT … FOR UPDATE` 读取记录，检查后再写。冲突的写入通常要等锁释放，也可能因超时或死锁失败。如果条件只取决于待改的那一行，可以一次完成检查和更新，见下文的扣库存示例。

            >可组合：用唯一约束防「多造一行」；改已有行再用乐观或悲观。持有 `FOR UPDATE` 时不要调外部 HTTP / RPC。

    - 跨服务时，可将业务变更和待发送事件写入同一个本地事务（事务发件箱，outbox）。提交后由独立任务投递，失败可重试；消费者按事件 ID 幂等处理重复投递。

---

## 服务安装、启动与连接

以下命令用于已安装 Homebrew 的 macOS 本地开发环境，以当前用户运行。`brew services start 包名` 立即启动服务并注册为登录时启动。只想运行本次可把 `start` 换成 `run`。需要时用 `brew services info 包名` 查看状态、`brew services restart 包名` 重启、`brew services stop 包名` 停止并取消登录时启动。`brew services list` 可查看所有受管服务。[Homebrew 命令手册](https://docs.brew.sh/Manpage)

### [`MySQL`](https://dev.mysql.com/doc/refman/en/)服务安装、启动与连接

以下在全新的本地环境安装 MySQL 8.4 LTS。Homebrew 的 `mysql` 和 `mysql@8.4` 服务默认都使用 `$(brew --prefix)/var/mysql`。如果这个目录已有其他版本的数据，请为练习使用独立实例。下面的 `export` 只为当前终端选择 8.4 客户端。[Homebrew 的 MySQL 8.4 安装说明](https://formulae.brew.sh/formula/mysql@8.4)

```shell
brew install mysql@8.4
export PATH="$(brew --prefix mysql@8.4)/bin:$PATH"
brew services start mysql@8.4
```

Homebrew 全新初始化的本地实例默认 `root` 密码为空，此时可用 `mysql -u root` 连接。首次启动后可运行 `mysql_secure_installation` 设置密码，随后用 `mysql -u root -p` 登录。连接已有业务库时，替换下面的账号和库名。`-P` 指定 TCP 端口，`-p` 提示输入密码。

```shell
mysql -h 127.0.0.1 -P 3306 -u app_user -p -D app_db --default-character-set=utf8mb4
```

> 在 `mysql>` 输入 `SELECT VERSION();` 可确认服务端版本。SQL 以 `;` 或 `\g` 执行，`\?` 列出客户端命令，`HELP SELECT;` 查询 SQL 帮助，`\q` 退出。

### [PostgreSQL](https://www.postgresql.org/docs/)服务安装、启动与连接

以下使用 PostgreSQL 17。Homebrew 会在首次安装时初始化数据目录，初始超级用户默认与运行 `initdb` 的 macOS 用户同名。这里假设当前用户完成了安装。[Homebrew 的 PostgreSQL 17 安装说明](https://formulae.brew.sh/formula/postgresql@17) · [PostgreSQL 的 initdb 文档](https://www.postgresql.org/docs/17/app-initdb.html)

```shell
brew install postgresql@17
export PATH="$(brew --prefix postgresql@17)/bin:$PATH"
brew services start postgresql@17
psql -h 127.0.0.1 -p 5432 -U "$(id -un)" -d postgres
```

要在前台观察启动日志，可用 `postgres -D "$(brew --prefix)/var/postgresql@17"` 替代上面的 `brew services start`，然后在另一终端连接。同一数据目录一次只能由一个实例使用。新终端如找不到 `psql`，重新执行上面的 `export`。

> 在 `psql` 中，SQL 以 `;` 结束。反斜杠开头的元命令单独占一行，例如 `\?` 查看命令，`\h SELECT` 查询 SQL 帮助，`\q` 退出。

```text
SELECT version(), current_database(), current_user;
\conninfo
\l
\dn
\dt
\du
```

`\conninfo` 显示当前连接，`\l` 列库，`\dn` 列模式，`\dt` 列出当前搜索路径可见的表，`\du` 列角色。要切换到已有库，可执行 `\c 库名`。

### [MongoDB](https://www.mongodb.com/docs/)服务安装、启动与连接

以下使用 MongoDB Community 8.0 和随包安装的 `mongosh`。安装前先核对官方指南列出的 macOS 与处理器要求。下面按 Homebrew 6.0 及以上版本演示首次安装；使用较早版本时跳过 `brew trust mongodb/brew` 一行。[MongoDB 8.0 的 macOS 安装指南](https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-os-x/)

```shell
brew tap mongodb/brew
brew trust mongodb/brew
brew install mongodb-community@8.0
brew services start mongodb-community@8.0
mongosh 'mongodb://127.0.0.1:27017'
```

实例启用认证后，例如要用创建于 `admin` 的 `app_user` 访问 `app_db`，可运行 `mongosh 'mongodb://127.0.0.1:27017/app_db' --username app_user --authenticationDatabase admin`，按提示输入密码。认证库应填写创建该用户的库。[mongosh 连接选项](https://www.mongodb.com/docs/mongodb-shell/connect/)

> 在 `mongosh` 中，`help` 查看帮助，`exit` 退出。`use` 切换当前数据库，首次插入文档时会创建尚不存在的数据库和集合。以下示例在本地练习库中操作本次插入的文档。

```text
db.runCommand({ ping: 1 })
show dbs
use db_notes_demo
db
const result = db.items.insertOne({ name: "coffee", stock: 3 })
db.items.find({ name: "coffee" }).sort({ stock: -1 }).limit(5)
db.items.countDocuments({ name: "coffee" })
db.items.updateOne({ _id: result.insertedId }, { $set: { stock: 2 } })
db.items.deleteOne({ _id: result.insertedId })
show collections
```

### [Redis](https://redis.io/docs/latest/)服务安装、启动与连接

使用支持 `brew services` 的 Homebrew `redis` formula。默认连接本机 `127.0.0.1:6379` 的逻辑库 0。[Homebrew Redis 安装包](https://formulae.brew.sh/formula/redis) · [Redis 的 macOS 安装指南](https://redis.io/docs/latest/install/install-redis/install-redis-on-mac-os/)

```shell
brew install redis
brew services start redis
redis-cli PING
redis-cli INFO server
redis-cli
```

若要前台观察日志，可用 `redis-server "$(brew --prefix)/etc/redis.conf" --daemonize no` 替代 `brew services start redis`，另开终端连接。连接其他实例时用 `redis-cli -h 主机 -p 端口 -n 库号 PING`。需要认证时加 `--askpass` 交互输入密码，使用 ACL 命名用户时再加 `--user 用户名`。TLS 连接可用 `redis-cli -u 'rediss://主机:端口/库号' --askpass PING`。[redis-cli 连接参数](https://redis.io/docs/latest/develop/tools/cli/)

>`PING` 应返回 `PONG`，`INFO server` 可查看服务端版本和运行时间。单独运行 `redis-cli` 会进入交互终端，可用 `HELP SET` 查看帮助，输入 `quit` 退出。

在交互终端逐行执行下面的命令。`SET` 返回 `OK` 时，`GET` 应读到 `hello`，`TTL` 显示剩余秒数；60 秒到期后键自动清理。如果 `SET` 返回 `(nil)`，说明该键已存在，换一个练习键名重试。

```text
SET demo:greeting hello EX 60 NX
GET demo:greeting
TTL demo:greeting
```

> `NX` 表示仅在键不存在时写入，`EX` 和 `PX` 分别以秒和毫秒设置过期时间。普通 `SET` 覆盖已有键时会清除原过期时间，需保留时可用 `KEEPTTL`。

---

## 关系型数据库

### MySQL

>基准：**MySQL 8.4 LTS + InnoDB**。

MySQL 服务中可建多个数据库（`DATABASE` 与 `SCHEMA` 同义），每个数据库可建多张表。典型 Java 应用由后端通过 JDBC 访问数据库，也可用 MyBatis 等框架封装 SQL。下文从表与约束开始，再看查询、索引、事务与运维。

>**InnoDB** 是 MySQL 默认的存储引擎，支持事务、崩溃恢复和行级锁。它用 B+ 树组织普通索引，按聚簇索引保存行，默认隔离级别为 `REPEATABLE READ`。旧表若使用 MyISAM，则采用表级锁且不支持事务。

1. **表与约束**

    | 概念 | 要点 |
    | --- | --- |
    | 表 / 行 / 列 | 一类对象 / 一条记录 / 属性 |
    | 主键 | 优先选短且稳定的键。业务号可能变化时，可单设主键，再对业务号加 `UNIQUE` |
    | 字符集 | `utf8mb4` |
    | `NULL` | 未知/不存在 ≠ `''` / `0` |
    | 校验 | 前端校验及时提示用户，数据库约束对所有写入方生效 |

    | 约束 | 作用 | 注意 |
    | --- | --- | --- |
    | `NOT NULL` / `DEFAULT` | 禁空 / 默认值 | 例如 `qty INT DEFAULT 1`：插入时省略 `qty` 会得到 1，显式传 `NULL` 会保存空值。必填需另加 `NOT NULL` |
    | `PRIMARY KEY` | 非空且唯一 | 每表一个，可多列 |
    | `UNIQUE` | 非空值不重复 | MySQL 允许多个 `NULL`。若要求每行都有唯一业务号，配合 `NOT NULL` |
    | `CHECK` | 行内条件 | 检查表达式为 FALSE 才拒绝写入。`CHECK (price > 0)` 允许空价，必填时再加 `NOT NULL` |
    | `FOREIGN KEY` | 引用完整性 | 写明 `ON DELETE`/`ON UPDATE`；别默认级联删 |

    | 关系 | 做法 |
    | --- | --- |
    | 一对一 | 外键 + `UNIQUE` |
    | 一对多 | 外键在「多」侧 |
    | 多对多 | 中间表存两侧外键；查询时经中间表两次关联 |
    | 建删顺序 | 先父后子建；先子后父删。（因为外键） |

    | 操作 | 含义 |
    | --- | --- |
    | `TRUNCATE` | 清空留结构；InnoDB 上是 **DDL**：隐式提交、不可 `ROLLBACK`、重置 `AUTO_INCREMENT`；有其他表的外键指向本表则失败，改用 `DELETE` 仍须遵守外键约束 |
    | `DROP TABLE`/`DATABASE` | 删对象 |
    | `COMMENT` | 表/列元数据（`SHOW CREATE TABLE`）；改列注释须 `MODIFY`/`CHANGE` 写全列定义 |

1. **查询与改数据**

    SQL 是声明式：写「要什么」，优化器决定「怎么拿」。

    | 主题 | 规则 |
    | --- | --- |
    | 注释 | `--` 后须空格；`#` MySQL 扩展；`/* */` 可跨行；逗号别跟列名一起注释掉 |
    | `INSERT` | 写明列名；批量有上限，避免超大单包 |
    | `SELECT` | 只取需要的列 |
    | `UPDATE`/`DELETE` | 省略 `WHERE` 会作用于全表。人工改数据时可先查询核对范围；影响业务正确性的条件应保留在写语句中，以应对并发变化 |
    | 空值 | `IS NULL` / `IS NOT NULL`，不要 `= NULL` |
    | 理解顺序 | `FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`（写作辅助序，非引擎真实执行序） |

    | 易混 | 记法 |
    | --- | --- |
    | `WHERE` vs `HAVING` | 滤行 vs 滤聚合结果；`COUNT`/`SUM` 不能进 `WHERE` |
    | `DISTINCT` | 按选出的整行去重；统计用 `GROUP BY` |
    | `INNER JOIN` | 两侧都匹配才保留 |
    | `LEFT JOIN` | 保留左表全部；右表条件放 `ON`，放进 `WHERE` 易变成内连接 |
    | N+1 | 查出一页订单后逐单取明细，会多发 N 次查询。可用 `JOIN`，或一次按 `WHERE order_id IN (...)` 批量取该页订单的明细 |
    | 深分页 | 例如按 `ORDER BY created_at DESC, id DESC` 展示订单，下一页取时间早于上页末行、或时间相同且 ID 更小的行，沿用同一排序和 `LIMIT`。这里假设时间非空、ID 唯一，可配索引 `(created_at, id)` |
    | `LIMIT` | 列表要有上限；勿让前端传无界 `pageSize` |

    | 视图 | 要点 |
    | --- | --- |
    | 是什么 | 给 `SELECT` 起名；普通视图不另存数据 |
    | 物化 | MySQL **没有**；要落结果自己建表再 `INSERT`（底表变了不自动更新） |
    | 写入 | 改的是底表；含 `GROUP BY` 或聚合的视图不可更新，部分内连接视图可一次更新其中一张底表 |
    | `WITH CHECK OPTION` | 拒绝写出视图条件外的行 |
    | `DROP VIEW` | 不删底表 |

1. **索引与 `EXPLAIN`**

    索引占用空间，修改索引列时也有维护成本。按实际查询的过滤、关联和排序条件选择索引；用于定位待更新行的索引也能减少扫描和加锁范围。

    | | 单列 | 复合 `(列1, 列2)` |
    | --- | --- | --- |
    | 列的顺序 | 一列 | 先看常用的等值条件，再看范围条件与排序顺序 |
    | 定位记录 | 可用该列等值或范围查找 | `列1=?` 和 `列1=? AND 列2=?` 都能利用最左前缀。只有列 2 条件时，通常无法直接定位一个连续区间；优化器仍可能选择索引扫描，满足条件时可用跳跃扫描（Skip Scan）。[MySQL 范围优化](https://dev.mysql.com/doc/refman/8.4/en/range-optimization.html) |

    | | 普通索引 | 唯一索引 |
    | --- | --- | --- |
    | 用于查找 | 优化器可选用 | 优化器可选用 |
    | 非空重复 | 可以 | 第二次报错 |
    | `NULL` | 可多个 | 也可多个 |
    | vs 主键 | 不是主键 | 也不是（主键每表一个且非空；`UNIQUE` 可多组） |

    | 要点 | 说明 |
    | --- | --- |
    | `UNIQUE` 约束 | 自动建唯一索引 = `CREATE UNIQUE INDEX`；`SHOW INDEX` 里 `Non_unique=0` |
    | 组合唯一 | `UNIQUE(user_id, sku_id)` ≠ `UNIQUE(sku_id)` |
    | 聚簇 | 声明主键时，InnoDB 将整行存入主键索引的叶子。二级索引记录含主键值，取缺少的列时再按主键查找。结果展示顺序由 `ORDER BY` 指定。[InnoDB 聚簇索引与二级索引](https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html) |
    | 覆盖索引 | 查询需要的列都在同一索引里，通常可省去回表。例如主键为 `id` 时，二级索引 `(user_id)` 可覆盖 `SELECT id FROM orders WHERE user_id = ?` |
    | 难以缩小扫描范围 | `LIKE '%xx'` 缺少固定前缀。对索引列做函数运算或隐式类型转换，也可能妨碍利用普通索引定位。含 `OR` 的查询仍可能合并多个索引，以执行计划为准 |
    | `IN` / `NOT IN` | 按包含或排除的语义选；若排除集合含 `NULL`，未匹配行的 `NOT IN` 结果为 UNKNOWN，会被 `WHERE` 滤掉。可按业务空值规则改用 `NOT EXISTS` |
    | 驱动表 | 小结果集驱动大表只是嵌套循环直觉；优化器可能改写，以执行计划为准 |
    | 批量写 | 短事务、限制批次，少锁时间、少日志抖动 |
    | `EXPLAIN` | 表格格式中，`key` 是选用的索引，`type` 是访问方式，`rows`、`filtered` 是估算值。`Extra` 可显示额外排序或临时表。用 `EXPLAIN ANALYZE SELECT ...` 查看实际行数、耗时和循环次数；带 `ANALYZE` 会实际执行语句。[MySQL 执行计划](https://dev.mysql.com/doc/refman/8.4/en/explain.html) |

1. **事务、隔离与锁**

    多步修改必须一起生效时，在**同一连接**上执行 `START TRANSACTION`。全部成功后 `COMMIT`，放弃修改时 `ROLLBACK`。默认开启自动提交，单独执行的 DML 会自行提交。

    | 主题 | 规则 |
    | --- | --- |
    | 边界 | 按必须同成同败的业务操作划分；勿把 HTTP/RPC/发 MQ 包进数据库事务 |
    | 幂等 | 重复点击靠接口幂等；`UNIQUE` 只挡相同唯一键，挡不住两次不同下单 |
    | DDL vs DML | DDL 常隐式提交；多数 DML 错误只撤该句。若业务无法继续，应整笔 `ROLLBACK` |
    | 死锁 | InnoDB 回滚被选为牺牲者的整个事务；重试须从事务开头开始 |
    | `UPDATE` 0 行 | 默认按实际改动行数计，同值更新也可能返回 0。启用 `CLIENT_FOUND_ROWS` 的连接按匹配行数计；在同一连接紧接着用 `SELECT ROW_COUNT();` 可查看上条语句的计数。[MySQL 受影响行数](https://dev.mysql.com/doc/refman/8.4/en/information-functions.html#function_row-count) |
    | `SAVEPOINT` | 部分回滚：`ROLLBACK TO` 后继续（其后保存点失效） |
    | 重试 | 锁等待超时默认只撤当前语句；启用 `innodb_rollback_on_timeout` 时须整笔重试。唯一键冲突按业务判断重复或报错，幂等键应保留 |
    | 客户端 | 事务仍活跃时须显式提交或回滚；JDBC 抛出异常后由调用方处理；`mysql>` 粘贴仍可能继续；`mysql < 文件` 默认遇错停 |

    三种异常的含义见上文事务。下表按 InnoDB；PostgreSQL 默认是 `READ COMMITTED`。

    | 隔离级别 | 脏读 | 不可重复读 | 幻读 | 说明 |
    | --- | --- | --- | --- | --- |
    | `READ UNCOMMITTED` | 可能 | 可能 | 可能 | 几乎不用 |
    | `READ COMMITTED` | 否 | 可能 | 可能 | 每次一致性读见当时已提交 |
    | `REPEATABLE READ` | 否 | 否 | 重复快照读看不到并发提交的新行 | InnoDB 默认。首次一致性读建立快照；锁定读及写操作访问当前版本，可能与之前的快照读所见不同 |
    | `SERIALIZABLE` | 否 | 否 | 否 | 结果须等价于某个串行执行顺序；冲突时可能等待或中止事务 |

    当前事务的隔离级别须在开始前设置；事务中执行 `SET SESSION TRANSACTION` 只影响后续事务。默认自动提交时，把多次一致性读放进同一个显式事务，才能比较两次读取之间的快照变化。

    | 范围 | 写法 |
    | --- | --- |
    | 本连接之后 | `SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;` |
    | 仅下一事务 | `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;` 然后 `START TRANSACTION`；该事务结束回到会话级别 |
    | 查看会话默认值 | `SELECT @@SESSION.transaction_isolation;`；这项查询无法验证仅对下一事务设置的覆盖值 |

    >`SET GLOBAL transaction_isolation` 只影响之后新建的会话。JDBC / Spring 见下一节。

    | 机制 | 含义 |
    | --- | --- |
    | MVCC | Read View 判可见性；长事务拖清理 |
    | `FOR UPDATE` | 将读取和依赖该结果的写入放在同一显式事务内；提交或回滚时释放锁 |
    | 行锁范围 | 锁加在扫描到的索引记录上。没有合适索引时可能锁住大量记录，阻塞其他写入 |
    | 间隙锁 | `REPEATABLE READ` 下，按主键等值查到已有行时，只需锁住该记录。范围锁定读还可锁住索引记录之间的间隙，阻止其他事务往相应间隙插入。[InnoDB 隔离级别与锁范围](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) |

    在已选中练习数据库的新连接中，可用临时库存表试扣 1 件。把余量条件和扣减写进同一条语句，应用就能按受影响行数决定是否建单。

    ```sql
    CREATE TEMPORARY TABLE demo_inventory (
        sku_id BIGINT PRIMARY KEY,
        stock INT NOT NULL
    ) ENGINE=InnoDB;
    INSERT INTO demo_inventory (sku_id, stock) VALUES (42, 1);

    START TRANSACTION;
    UPDATE demo_inventory SET stock = stock - 1 WHERE sku_id = 42 AND stock >= 1;
    SELECT ROW_COUNT();  -- 1 表示已扣减，0 表示商品不存在或库存不足
    ROLLBACK;            -- 演示结束。实际下单仅在扣减和建单都成功后提交
    SELECT stock FROM demo_inventory WHERE sku_id = 42;  -- 回滚后仍为 1
    ```

1. **Java 访问**

    原生 JDBC 从连接池获取 `Connection`，调用 `setAutoCommit(false)` 后在同一连接上完成多步写入，失败时回滚。使用 Spring 时通常在 Service 方法上声明事务，由事务管理器负责提交或回滚。

    | MySQL | Java | 注意 |
    | --- | --- | --- |
    | `DECIMAL` | `BigDecimal` | 定精度/舍入；比较用 `compareTo` |
    | `INT`/`BIGINT` | `Integer`/`Long` | 可空用包装类；`BIGINT UNSIGNED` 可能超 `long` |
    | `DATE`/`DATETIME`/`TIMESTAMP` | `LocalDate`/`LocalDateTime`/`java.sql.Timestamp`（可转 `Instant`） | `DATETIME` 无时区；读写绝对时间时统一连接时区 |
    | `JSON` | `String` 或对象 | 统一序列化；高频查询字段拆普通列 |

    | 主题 | 规则 |
    | --- | --- |
    | 参数 | 值用绑定 / `#{}` 防注入；`${}` 只许白名单标识符（表名、列名） |
    | [连接池](../Java学习笔记/README.md#jdbc-与数据库访问演进) | `每实例池上限 × 实例数 + 其他客户端` < `max_connections`，留余量给管理与批跑 |
    | ORM | MyBatis、JPA、Sequelize 等省样板，仍要看生成 SQL；事务边界、批量、索引要自己管 |
    | `@Transactional` | 在 Spring 默认的代理模式下，同类自调用不经过代理。JDBC 事务绑定当前线程。默认情况下，未捕获的 `RuntimeException` / `Error` 触发回滚，受检异常可用 `rollbackFor` 配置。[Spring 回滚规则](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/rolling-back.html) |
    | 隔离级别 JDBC | 第一条 SQL 前 `connection.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED)`；常量还有 `TRANSACTION_READ_UNCOMMITTED`、`TRANSACTION_REPEATABLE_READ`、`TRANSACTION_SERIALIZABLE` |
    | 隔离级别 Spring | `@Transactional(isolation = Isolation.READ_COMMITTED)` 在开启新的物理事务时生效，`Isolation.DEFAULT` 沿用底层设置。`REQUIRED` 加入已有事务时沿用外层隔离级别，JDBC 的 `NESTED` 在已有事务中使用保存点，`REQUIRES_NEW` 则新开事务。编程式可用 `TransactionTemplate.setIsolationLevel(...)` |
    | 跨边界 | 跨库/HTTP/MQ 靠 outbox、重试、消费幂等 |

1. **复制、迁移、备份、监控**

    | 主题 | 要点 |
    | --- | --- |
    | redo / binlog | 崩溃恢复 / 复制与时间点恢复；**都不能替代备份**（PostgreSQL 的 WAL 同理） |
    | 复制 | 读扩展与容灾；默认异步，误删也会跟上副本。复制本身不是备份 |
    | 读自己 | 刚写再读走主库；事务内勿切副本 |
    | 高可用 | 自动切换仍可能丢数据；约定可接受的数据丢失时间窗口（RPO）和恢复服务的目标时长（RTO） |
    | 安全 | 最小权限，生产不用超级用户跑业务；TLS；密码与连接串不进仓库、代码、日志 |
    | DDL | 结构变更走版本化迁移（可回滚或向前兼容）；大表先估锁、磁盘、复制延迟 |
    | 备份 | 定期全量 + 按需增量；定范围、保留期、恢复目标，并在隔离环境演练恢复 |
    | 监控 | 连接等待、慢 SQL、扫描行、锁等待、I/O、复制延迟。扩展顺序：索引 / SQL / 缓存 / 归档 → 读写分离 → 分库分表（见 [知识点备忘](#知识点备忘)） |

    | 诊断命令 | 用途 |
    | --- | --- |
    | `EXPLAIN` | 是否走索引、估扫行数 |
    | `SHOW FULL PROCESSLIST` | 谁在连、跑哪条、卡多久 |
    | `SHOW VARIABLES` / `SHOW STATUS` | 配置 / 运行指标；查看实例累计指标用 `SHOW GLOBAL STATUS` |
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
    | 真假 | `BOOLEAN` 是 `TINYINT(1)` 的别名。仅允许 0、1 时可用 `flag BOOLEAN NOT NULL CHECK (flag IN (0, 1))` |
    | 半结构化 | `JSON`（常查字段仍拆列） |

    | 类 | 要点 |
    | --- | --- |
    | 整数 | `TINYINT`～`BIGINT`；`UNSIGNED` 非负；`INT(11)` 的 `11` 是弃用显示宽度 |
    | 浮点 | `FLOAT`/`DOUBLE` 保存近似值，适合容许舍入误差的测量、统计等数据 |
    | 位 / 别名 | `BIT(n)`；`SERIAL` = `BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE` |
    | 时间 | `TIME` 可表时长；`fsp` 0～6；`YEAR` 只管年；`TIMESTAMP` ≈1970～2038 |
    | 定长串 | `CHAR`；`BINARY`/`VARBINARY` 按字节 |
    | 大对象 | `TINY`/`MEDIUM`/`LONG` + `TEXT`/`BLOB` |
    | `ENUM`/`SET` | 固定小集合；会变或要外键则拆表 |
    | 空间 | `POINT` 等 GIS |
    | 向量 | [`VECTOR(n)`](https://dev.mysql.com/doc/refman/9.7/en/vector.html) 自 9.0，**8.4 没有** |
    | 整数别名 | `INT1`、`INT2`、`INT3`、`INT4`、`INT8` 依次代表 `TINYINT`、`SMALLINT`、`MEDIUMINT`、`INT`、`BIGINT` |

    </details>

- <details>

    <summary>标识符与引号</summary>

    | 东西 | 写法 | 例子 |
    | --- | --- | --- |
    | 标识符 | 反引号 `` ` `` | `` SELECT `order-id` FROM `t` `` |
    | 字符串值 | 单引号 `'` | `WHERE name = 'Alice'` |
    | 数字 / 布尔 / `NULL` | 不加引号 | `WHERE id = 1` |

    >含 `-` 或空格、全为数字或使用保留字的标识符用反引号；以数字开头本身不要求加引号。优先 `snake_case`。串内 `'` 写成 `''`。双引号 `"` 勿当默认：无 `ANSI_QUOTES` 当字符串，有则当标识符 → 字符串只用 `'`。

    ```sql
    SELECT 'order-id' FROM t;   -- 常量
    SELECT `order-id` FROM t;   -- 列
    ```

    </details>

- <details>

    <summary>常用命令</summary>

    >以下是独立命令示例。SQL 在 `mysql>` 执行，`「...」` 替换为实际名称、值或条件。

    ```sql
    -- 库
    SHOW DATABASES;
    CREATE DATABASE IF NOT EXISTS 「库」;
    USE 「库」;
    SELECT DATABASE();
    SHOW CREATE DATABASE 「库」;
    -- 删除整个库：DROP DATABASE IF EXISTS 「库」;

    -- 表
    CREATE TABLE IF NOT EXISTS 「表」 (
        id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL COMMENT '「列注释」',
        PRIMARY KEY (id)
    ) COMMENT='「表注释」';
    SHOW TABLES; DESCRIBE 「表」; SHOW CREATE TABLE 「表」;
    ALTER TABLE 「表」 ADD COLUMN remark VARCHAR(100);
    ALTER TABLE 「表」 MODIFY COLUMN remark VARCHAR(200);
    -- 删除列：ALTER TABLE 「表」 DROP COLUMN remark;
    ALTER TABLE 「表」 RENAME COLUMN 「旧」 TO 「新」;
    RENAME TABLE 「旧」 TO 「新」;
    -- 清空表：TRUNCATE TABLE 「表」;  属于 DDL，不可 ROLLBACK
    -- 删除表：DROP TABLE IF EXISTS 「表」;

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
    CREATE INDEX 「名」 ON 「表」 (「列」);  -- 需保证唯一时写 CREATE UNIQUE INDEX
    DROP INDEX 「名」 ON 「表」;
    START TRANSACTION;  -- 等价 BEGIN / BEGIN WORK
    -- 事务中可先 SAVEPOINT 「名」; 再用 ROLLBACK TO SAVEPOINT 「名」; 部分回滚
    ROLLBACK;  -- 结束本次示例事务；需要保留改动时改用 COMMIT
    CREATE OR REPLACE VIEW 「视图」 AS SELECT id, name FROM 「表」;  -- 可加 WITH CHECK OPTION
    SHOW CREATE VIEW 「视图」;
    DROP VIEW IF EXISTS 「视图」;

    -- 用户 / 诊断
    CREATE USER IF NOT EXISTS '「用户」'@'「主机」' IDENTIFIED BY '「密码」';
    GRANT SELECT, INSERT, UPDATE, DELETE ON 「库」.* TO '「用户」'@'「主机」';
    SHOW GRANTS FOR '「用户」'@'「主机」';
    REVOKE SELECT, INSERT, UPDATE, DELETE ON 「库」.* FROM '「用户」'@'「主机」';
    DROP USER IF EXISTS '「用户」'@'「主机」';
    EXPLAIN SELECT id FROM 「表」 WHERE id = 1;
    SHOW FULL PROCESSLIST;
    SHOW VARIABLES LIKE 'max_connections';
    SHOW GLOBAL STATUS LIKE 'Slow_queries';
    SHOW WARNINGS;
    ```

    在 shell 中导出单个数据库，将输出写入新的备份文件。下面的命令未使用 `--databases`，默认不生成建库语句。

    ```shell
    mysqldump --single-transaction -h 「源主机」 -u 「用户」 -p 「源库」 > 「备份.sql」
    ```

    确认导出成功后，在隔离的恢复实例上新建**空目标库**，再执行导入。`mysqldump` 默认会在建表前写入 `DROP TABLE IF EXISTS`。若目标库已有同名表，导入会先删除它；中途报错时，之前已提交的修改会保留。[mysqldump 默认选项](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html#option_mysqldump_opt)

    ```shell
    mysql --default-character-set=utf8mb4 -h 「目标主机」 -u 「用户」 -p 「目标库」 < 「备份.sql」
    ```

    已在 `mysql>` 中选好这个空目标库时，也可用 `SOURCE 「路径」` 载入同一份备份。

    >`--single-transaction` 为 InnoDB 表取得一致快照。导出期间应避开对相关表的 DDL；MyISAM 等非事务表无法获得同样的一致性。若还要备份存储过程、函数或事件，加 `--routines --events`。[mysqldump 备份选项](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html)

    </details>

### PostgreSQL

<details>
<summary>对象层级、SQL、索引与事务（以 PostgreSQL 17 为例）</summary>

PostgreSQL 是开源的对象关系型数据库管理系统，支持事务、关联查询，以及自定义类型、函数和扩展。

- **对象层级与角色**

    `集群（Cluster） -> 数据库（Database） -> 模式（Schema） -> 表、视图、函数等对象`

    - 一个集群可包含多个数据库；角色（Role）属于集群，带 `LOGIN` 属性的角色可作为登录用户。
    - 每个客户端连接对应一个数据库。在 `psql` 中用 `\c 「数据库名」` 切换时，客户端会重新连接。
    - Schema 是数据库内的命名空间，可以组织同名对象；未写 Schema 的对象名按 `search_path` 查找，可用 `SHOW search_path;` 查看。

    >把允许不受信任用户创建对象的 Schema 加入 `search_path` 会带来对象名称被遮蔽的风险。生产环境应明确 Schema 所有者和 `CREATE` 权限，迁移脚本宜使用带 Schema 的对象名。

- **特色类型与 SQL**

    | 能力 | 适合场景 | 边界 |
    | --- | --- | --- |
    | `UUID` | 跨系统生成标识 | 评估索引大小和写入局部性 |
    | [PostgreSQL `jsonb`](../../网站前端/前端内容/基础知识.md#postgresql-jsonb) | 查询半结构化数据 | 稳定且高频查询的字段仍优先使用普通列 |
    | 数组、范围类型 | 短小同类值、区间与重叠判断 | 高频关联或独立更新的数据更适合子表 |
    | `RETURNING` | 插入、更新时可返回写入后的值，删除时可返回被删行的值 | 减少额外查询，仍在同一事务内 |
    | `INSERT ... ON CONFLICT` | `DO UPDATE` 做原子 upsert，`DO NOTHING` 跳过冲突行 | `DO UPDATE` 必须写冲突目标；`DO NOTHING` 省略目标时处理所有可用的唯一或排他冲突。外键、非空等约束错误仍会报错 |
    | CTE、窗口函数 | 拆分复杂查询，计算排名或累计值 | 仍需结合执行计划判断成本 |

    >在同一连接创建下面的临时报名表，再执行两次 `INSERT`。第一次返回 `(42, 7)`，第二次因重复报名返回零行。如果改用另一个用户但沿用同一票号，则触发 `ticket_code` 唯一约束错误。[PostgreSQL 冲突处理与返回值](https://www.postgresql.org/docs/17/sql-insert.html)

    ```sql
    CREATE TEMP TABLE signup (
        user_id bigint NOT NULL,
        event_id bigint NOT NULL,
        ticket_code text NOT NULL UNIQUE,
        PRIMARY KEY (user_id, event_id)
    );

    INSERT INTO signup (user_id, event_id, ticket_code)
    VALUES (42, 7, 'T-001')
    ON CONFLICT (user_id, event_id) DO NOTHING
    RETURNING user_id, event_id;
    ```

- **索引与执行计划**

    | 索引 | 常见用途 |
    | --- | --- |
    | B-tree | 默认索引，适合等值、范围和排序 |
    | GIN | 适合数组、`JSONB`、全文检索等“一个值包含多个元素”的查询 |
    | GiST | 可扩展的搜索框架，常用于范围、几何、最近邻等操作 |

    >按查询使用的操作符、数据分布选索引。`EXPLAIN` 显示估算计划，`EXPLAIN (ANALYZE, BUFFERS)` 实际运行语句，可比较估算行数与实际行数，并查看缓冲区访问情况。分析写入时宜在测试库执行；即使用 `BEGIN` 和 `ROLLBACK` 撤销表数据改动，序列已分配的值仍会消耗。[PostgreSQL 执行计划](https://www.postgresql.org/docs/17/sql-explain.html) · [序列行为](https://www.postgresql.org/docs/17/functions-sequence.html)

- **MVCC、VACUUM 与扩展**

    - PostgreSQL 使用 MVCC。仍可能被其他事务快照读到的旧行版本必须保留。普通 `VACUUM` 回收可清理的版本，空间通常留给表内后续写入复用；`ANALYZE` 更新优化器统计信息。[PostgreSQL 日常清理](https://www.postgresql.org/docs/17/routine-vacuuming.html)
    - autovacuum 自动执行必要的清理、统计更新和事务 ID 回卷防护，应根据写入量调整，不要关闭。
    - `VACUUM FULL` 会重写表并取得强锁，不是日常清理命令；优先让普通 `VACUUM` 持续工作。
    - `CREATE EXTENSION` 把服务器已安装的扩展注册到当前数据库。引入扩展前要确认权限、版本升级、备份恢复和目标环境都支持它。

- **与 MySQL 的学习差异**

    - **隔离级别**。PostgreSQL 默认 `READ COMMITTED`，同一事务中两次普通查询可看到不同的已提交结果。`REPEATABLE READ` 的事务快照也能防止幻读，但仍可能出现无法按串行顺序解释的并发结果。使用 `REPEATABLE READ` 或 `SERIALIZABLE` 时，遇到序列化失败（SQLSTATE `40001`），应从头重试整个事务。[PostgreSQL 事务隔离](https://www.postgresql.org/docs/17/transaction-iso.html)
    - **错误恢复**。在 PostgreSQL 的显式事务里，普通 SQL 报错后事务进入失败状态。执行 `ROLLBACK`，或回滚到出错前设置的保存点，才能继续。InnoDB 的许多语句错误则只撤销当前语句。[PostgreSQL 事务与保存点](https://www.postgresql.org/docs/17/tutorial-transactions.html) · [InnoDB 错误处理](https://dev.mysql.com/doc/refman/8.4/en/innodb-error-handling.html)
    - **主键与存储**。MySQL 常用 `AUTO_INCREMENT`，PostgreSQL 可写 `id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY`。`IDENTITY` 负责生成值，`PRIMARY KEY` 负责保证唯一。PostgreSQL 普通表的数据保存在堆中，主键索引指向堆中的行版本。[PostgreSQL 标识列](https://www.postgresql.org/docs/17/ddl-identity-columns.html)

</details>

---

## NoSQL 数据库

NoSQL 不是一种固定的数据模型，而是键值、文档、列族、图等非关系型数据库的统称。本节只介绍 MongoDB 和 Redis。

### MongoDB

<details>
<summary>文档建模、查询与事务</summary>

MongoDB 是文档数据库：一条记录是一个 BSON 文档，多个文档组成集合（Collection）。文档类似 JSON 对象，可以包含数组和嵌套文档；同一集合中的文档不必拥有完全相同的字段。

- **[BSON](../../网站前端/前端内容/基础知识.md#bson) 与文档建模**

    BSON 是 MongoDB 存储和传输文档使用的带类型二进制格式；具体类型、Extended JSON、使用边界以及与 PostgreSQL `jsonb` 的区别见上方链接。此处重点是文档建模。

    | 关系 | 优先嵌入 | 优先引用 |
    | --- | --- | --- |
    | 读取方式 | 总是随父对象一起读取 | 经常独立查询 |
    | 生命周期 | 随父对象一起创建和删除 | 可独立修改或复用 |
    | 数据规模 | 数量有明确上限 | 数量可能持续增长 |
    | 典型关系 | 一对少量明细 | 多对多、共享对象、高基数关系 |

    >文档结构应从主要读写路径反推：把需要原子更新、经常一起读取且规模可控的数据嵌入；单个 BSON 文档上限为 16 MiB，应避免无限增长的数组。

- **查询与聚合管道**

    聚合管道把文档依次交给多个阶段处理。下面的查询先筛出已付款订单，再按用户汇总金额，返回消费额最高的 20 位用户。金额相同的用户按用户 ID 排序，使第 20 名的取舍可复现。

    ```javascript
    db.orders.aggregate([
      { $match: { status: "PAID" } },
      { $group: { _id: "$userId", paidTotal: { $sum: "$totalAmount" } } },
      { $sort: { paidTotal: -1, _id: 1 } },
      { $limit: 20 }
    ])
    ```

    >开头的 `$match` 有机会使用索引。MongoDB 会自动裁剪未使用的字段，`$project` 通常放在末尾指定返回字段。用 `db.orders.explain("executionStats").aggregate(管道数组)` 查看实际扫描的文档数、索引使用情况和执行阶段。[MongoDB 聚合优化](https://www.mongodb.com/docs/manual/core/aggregation-pipeline-optimization/)

- **索引与 Schema Validation**

    复合索引的字段顺序影响哪些查询能利用索引前缀，唯一索引可以约束单个字段或字段组合。索引会增加存储和写入成本，应按真实查询建立。普通集合中的 TTL 索引建在单个日期字段（或包含日期的数组字段）上，后台任务异步删除过期文档。会话鉴权等有硬截止时间的逻辑应在读取时检查有效期。[MongoDB TTL 索引](https://www.mongodb.com/docs/manual/core/index-ttl/)

    Schema Validation 可限制必填字段、BSON 类型和值范围。给已有集合新增规则时，要考虑后续写入如何校验，以及历史文档如何迁移。[MongoDB Schema Validation](https://www.mongodb.com/docs/manual/core/schema-validation/)

- **原子性、事务与高可用**

    - 一次写入可原子地修改同一文档的多个字段。`updateMany()` 命中多条时，每个文档的修改分别具有原子性。要求整批同时提交或回滚时，需要在副本集或分片集群上使用多文档事务。[MongoDB 原子性与事务](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/)
    - 副本集提供冗余和故障转移。read preference 决定从哪些成员读取，read concern 控制读取时的数据可见性，write concern 控制写入返回成功所需的确认条件。读副本时要考虑复制延迟。
    - 分片用于扩展容量和吞吐，分片键决定数据分布、查询路由和热点；只有需求明确且团队能承担运维复杂度时再引入。

</details>

### Redis

Redis 主要在内存中读写数据。以下用 MySQL 保存订单、库存等业务记录，用 Redis 缓存可从数据库重建的数据。会话、计数、排行和限流也可以放在 Redis，各自需要考虑丢失后的业务影响。浏览器通过 HTTP API 访问后端，由后端持有 Redis 连接和凭据。

学习顺序：`场景与 key -> 数据结构 -> 原子/Pipeline -> Cache Aside -> Java -> 锁 -> 过期与持久化 -> 复制`。

1. **什么时候用**

    | 场景 | 用 Redis | 仍以 MySQL 为准 |
    | --- | --- | --- |
    | 热点详情、配置 | 缓存查询结果，带 TTL | 写入和强一致读 |
    | 登录会话 | 可存 Session / token 元数据 | 账号、权限等事实 |
    | 计数、限流 | 固定窗口可用短 Lua 原子执行 `INCR` 并在首次计数时设 TTL，避免两步之间中断留下永久 key | 对账、累计以库为准 |
    | 排行榜 | Sorted Set | 结算、发奖落库 |
    | 简易队列 | List 可入队、出队，Stream 消费组可跟踪待确认消息 | 需随业务提交的事件可在同一数据库事务中写入事件表，再异步投递 |
    | 余额、库存 | 可缓存展示，不作唯一真相 | 扣减走库事务或明确方案 |

    key 可按环境、业务和对象命名，如 `prod:order:88`。查询结果的 TTL 应根据可接受的旧值时长和回源成本设定。对持续增长的列表，还应限制单个 key 的元素数或字节数。

    - <details>

        <summary>无界列表与大 key</summary>

        >用户的全部订单、帖子的全部评论，都可能随时间持续增长。把它们打包进一个 String，或放在同一集合中再一次读全，成本会随业务数据累积。

        `maxmemory` 限制实例用于数据的内存，淘汰以整个 key 为单位。随着单个 key 的数据量增长，要关注以下成本。

        | 风险 | 表现 |
        | --- | --- |
        | 内存失控 | 活跃用户 / 热门对象各自拖一个越来越大的 value，实例被少数大 key 占满 |
        | 读取变重 | `GET` 整份 JSON 或 `LRANGE 0 -1` 读取完整列表时，传输和客户端处理成本随结果增大 |
        | 更新和回填变贵 | 序列化为一个 String 的对象改一项就需重写整份，失效后也需整份回填；Hash 和 List 支持按字段或元素操作 |
        | 服务延迟上升 | 同步释放含大量元素的集合会占用命令执行线程，大值写入也会增加复制流量 |

        可以从以下几个方面控制单个 key 的大小。

        1. 详情或配置只缓存接口需要的字段，限制大文本和嵌套列表的长度。
        2. 时间线用 List 加 `LTRIM` 保留最近 N 条。若排行只展示前 N 名，可缓存计算好的 Top N，把完整分数留在数据源。
        3. 按固定页大小拆 key，如 `prod:order:user:123:p:1`。按天分桶时，仍要按单日流量峰值估算大小。
        4. 对需要求交集或去重的 Set，按业务范围和保留期控制成员数量。

        </details>

1. **数据结构**

    按操作选型，不要把所有对象都序列化成大字符串。计数用 `INCR`，集合运算用 Set，排名用 Sorted Set。

    - <details>

        <summary>怎么读 Redis 命令（语法入门）</summary>

        >以下命令采用 `redis-cli` 交互模式的写法，空格分隔参数，带空格的值用引号包裹。程序里的客户端把命令名和各个参数按 Redis 协议分别发送。代码块中的 `#` 行是说明。

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

        **常见命令前缀**（帮助记忆，具体类型以命令定义为准）

        | 前缀 | 类型 | 记忆 |
        | --- | --- | --- |
        | （无，如 `SET`/`GET`/`INCR`） | String | 最基础 |
        | `H` | Hash | Hash field |
        | `LPUSH` / `RPUSH` / `BRPOP` | List | 这些列表命令中的 L / R 表示左右两端，B 表示阻塞等待 |
        | `SADD` / `SINTER` | Set | 添加成员 / 取交集 |
        | `Z` | Sorted Set | 有序，带 score |
        | `X` | Stream | 流式消息 |

        **常见选项词**（后面示例会反复出现）

        | 词 | 含义 |
        | --- | --- |
        | `EX 秒` | 多少秒后过期（和 `SET` 连用） |
        | `PX 毫秒` | 多少毫秒后过期 |
        | `SET … NX` | 仅当 key **不存在** 时才写入（常用于锁） |
        | `SET … XX` | 仅当 key **已存在** 时才写入 |
        | `WITHSCORES` | 查出成员时带上分数 |
        | `LIMIT 偏移 条数` | 只取一段结果 |

        **和 SQL 的直觉对照**

        | 你熟悉的 | Redis 里大致对应 |
        | --- | --- |
        | 表名 + 主键 | 一个 **key**（整份数据的名字） |
        | 一行里的列 | Hash 的 **field**，或 String 里整段 JSON |
        | `UPDATE t SET c=1 WHERE id=?` | 更新 Hash 中一个字段可用 `HSET key c 1`；覆盖整份 String 用 `SET key value` |
        | `SELECT c FROM t WHERE id=?` | `HGET key c` 读 Hash 的一个字段；若整行存成 String，则用 `GET key` 读整值 |

        >Java 里一般不手敲这些字符串，而是 `stringRedisTemplate.opsForValue().set(...)`；但客户端发出去的仍是同一套命令。先会读 `redis-cli` 示例，再去对模板方法名。

        </details>

    | 数据结构 | 特点 | 常见用途 |
    | --- | --- | --- |
    | String | 字符串、数字或二进制 | 缓存值、计数器、状态 |
    | Hash | 一个 key 下多个字段 | 对象若干属性一起改 |
    | List | 有序序列 | 简单队列、时间线 |
    | Set | 无序且不重复 | 标签、去重、交并差 |
    | Sorted Set | 成员不重复，按分数排序 | 排行榜、按时间排序 |
    | Stream | 按 ID 追加，支持裁剪和消费组 | 要确认和重试的消息流 |

    - <details>

        <summary>各数据结构怎么选（含示例）</summary>

        >选型看「要做的操作」，不是看「业务对象叫什么」。能用原子命令完成的，就不要整对象序列化成大 String 再在应用里改。下面每行右侧 / `#` 后是人话翻译。

        1. **String**：一个 key 对应一块二进制 / 文本 / 数字。适合整份缓存、计数、简单状态。

            ```text
            # 命令  key            值                         选项
            SET    prod:user:42   '{"id":42,"name":"Ada"}'   EX 600
            # → 把用户 42 的详情缓存 600 秒

            INCR   prod:article:9:views
            # → 文章 9 的阅读数 +1；key 不存在时从 0 开始，已有值须可解析为 64 位有符号整数

            SET    prod:feature:dark_mode   1   EX 3600
            # → 功能开关打开，1 小时后过期
            ```

            >整份 JSON 缓存详情没问题；若经常只改其中一个字段，用 Hash 更合适。计数用 `INCR` / `INCRBY`，不要 `GET` 再 `SET`。

        2. **Hash**：一个 key 下多个 field-value，像「小对象」。写法：`HSET key 字段 值 [字段 值 ...]`。

            ```text
            HSET  prod:article:9:metrics  views  120  likes  8
            # → 文章 9 的两个指标一次写好

            HINCRBY  prod:article:9:metrics  likes  1
            # → likes 字段加 1，返回 9

            HGET  prod:article:9:metrics  views
            # → 只读 views 字段，值仍为 120
            ```

            >Hash 适合按字段读写会话元数据、商品属性或统计指标。字段数量和单个字段的值都会影响内存占用。

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

            >`BRPOP` 会在返回元素时把它移出队列，消费者此时崩溃就可能丢任务。需要跟踪未完成任务时，可使用下文的 Stream 消费组。

        4. **Set**：无序、成员唯一。`SADD key 成员...`；判断用 `SISMEMBER`；交集 `SINTER`。

            ```text
            SADD  prod:post:9:tags  redis  cache  java
            # → 文章 9 打上三个标签（重复添加无效）

            SISMEMBER  prod:post:9:tags  redis
            # → redis 是不是该文章的标签？返回 1/0

            SINTER  prod:user:1:liked  prod:user:2:liked
            # → 用户 1 和 2「都喜欢」的成员（交集）
            ```

            >上面的 `SINTER` 可在单实例运行。在 Redis Cluster 中，参与交集的 key 必须位于同一哈希槽。规划集合大小时也要留意交集计算和结果传输的成本。

        5. **Sorted Set（ZSet）**：成员唯一，各带一个 **score（分数）** 用来排序。`ZADD key 分数 成员 [分数 成员 ...]`。

            ```text
            ZADD  prod:rank:game  980  u:42  1200  u:7
            # →                分数 成员   分数  成员：u:7 分更高

            ZRANGE  prod:rank:game  0  9  REV  WITHSCORES
            # → 从高到低取前 10 名，含分数；下标从 0 开始，两端都包含

            ZADD  prod:delay:jobs  1730003600  job:55
            # → score = 执行时间戳，到点再捞

            ZRANGE  prod:delay:jobs  -inf  1730003600  BYSCORE  LIMIT 0 20
            # → 查询截至给定时间已到期的任务，最多 20 条；任务仍保留在集合中
            ```

            >示例使用 Redis 6.2 起的 `ZRANGE` 语法。用执行时间作分数可以筛出到期任务。多个消费者同时查询可能读到同一项，需要单独设计原子领取与失败重试。[Redis ZRANGE](https://redis.io/docs/latest/commands/zrange/)

        6. **Stream** 按 ID 追加消息。`XADD key * 字段 值 [字段 值 ...]` 中的 `*` 让 Redis 自动生成消息 ID。

            ```text
            XADD  prod:events:order  *  orderId  88  status  paid
            # → 追加一条订单事件；* 表示自动分配 ID

            XGROUP CREATE  prod:events:order  cg1  0  MKSTREAM
            # → 建消费组 cg1；从 ID 0 开始；没有流就建流

            XREADGROUP GROUP  cg1  worker1  COUNT 10  STREAMS  prod:events:order  >
            # → 组 cg1、消费者 worker1，最多读 10 条；> = 尚未派给组内的新消息

            XACK  prod:events:order  cg1  「XREADGROUP 返回的消息 ID」
            # → 业务处理成功后确认，移出本组的待确认列表；消息仍保留在流中
            ```

            >消费者崩溃后，其他消费者可用 `XAUTOCLAIM`（Redis 6.2 起）认领空闲超时的待确认消息。业务已完成但确认丢失时会重复处理，可用事件 ID 做幂等。裁剪流时要为慢消费者和重试留出保留期。[Redis XAUTOCLAIM](https://redis.io/docs/latest/commands/xautoclaim/)

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

    两个客户端先 `GET` 再 `SET` 一个计数器，都可能读到 10，最终都写回 11。改用 `INCR`，两次增量会依次生效，结果为 12。多条独立命令可以用 Pipeline 减少等待网络往返的次数。后一步要根据前一步结果做判断时，可用短 Lua 脚本在服务端完成。

    - <details>

        <summary>原子操作、Pipeline、事务与脚本</summary>

        | 机制 | 解决的问题 | 边界 |
        | --- | --- | --- |
        | 单条命令 | 一次数据结构操作不被打断 | 多条命令之间仍可被穿插 |
        | Pipeline | 连续发送多条命令，再批量读取响应 | 其他客户端的命令可能穿插，批次大小也会影响响应缓冲占用 |
        | [`MULTI` / `EXEC`](https://redis.io/docs/latest/develop/using-commands/transactions/) | 排队后连续执行 | 入队时报错会使 `EXEC` 放弃整批；执行时某条报错，其余仍继续，已成功的不回滚；可配合 `WATCH` |
        | [Lua / Redis Functions](https://redis.io/docs/latest/develop/programmability/) | 在服务端连续判断和修改数据 | 执行时占用当前节点，脚本报错前已完成的写入会保留 |

        | 对比项 | Redis | MySQL InnoDB 事务 |
        | --- | --- | --- |
        | 基本保证 | 单条原子；`MULTI`/`EXEC` 连续执行、不被插入 | 多条 SQL 提交或回滚 |
        | 执行错误 | `EXEC` 执行队列时，某条失败，其余仍执行 | 许多错误只回滚当前语句，可显式回滚整个未提交事务；死锁受害者会被整笔回滚 |
        | 并发 | `WATCH` 发现 key 被改则放弃 `EXEC`，客户端重试 | 隔离级别、锁、MVCC |
        | 持久 | 崩溃后的可恢复范围取决于 RDB / AOF 和刷盘策略 | 已提交数据的崩溃恢复依赖 redo log 和提交时的刷盘配置 |

        >以上 MySQL 比较针对事务性 DML，许多 DDL 会隐式提交。

        </details>

1. **Cache Aside 与拖垮接口的几种情况**

    Cache Aside（旁路缓存）由应用管理缓存。以商品详情为例，MySQL 保存商品记录，Redis 缓存读取结果。[微软架构中心：旁路缓存](https://learn.microsoft.com/zh-cn/azure/architecture/patterns/cache-aside)

    - 读：先 Redis；命中直接返回；未命中再查 MySQL，把结果回填进 Redis（带 TTL）。
    - 写：先提交 MySQL，再**删掉**对应缓存。下次缓存未命中时，按读流程重新查询 MySQL。如果读请求走异步复制的只读副本，复制延迟也可能让旧值重新进入缓存。

    提交与删缓存之间仍可能读到旧值。即使删除成功，也可能有读请求早已从库中读到旧值，在删除之后才回填。TTL 限制这次回填的旧值能保留多久。删除失败且需可靠补偿时，可在更新商品的同一数据库事务中记录失效任务，由后台重试。余额扣款、库存扣减等读改写决策应由数据库事务或条件更新保证。

    | 问题 | 页面/接口上像什么 | 常用处理 |
    | --- | --- | --- |
    | 穿透 | 乱 id / 不存在的资源把数据库打满 | 参数校验、短时缓存空结果 |
    | 击穿 | 单个热门 key 失效，大量请求同时回源 | 合并同一 key 的回填请求、提前刷新 |
    | 雪崩 | 大批 key 同时失效或缓存服务不可用，数据库流量激增 | 分散 TTL、预热；缓存整体不可用时对回源限流或降级 |
    | 污染 | 内存被一次性查询占满 | 合理 TTL、`maxmemory`、淘汰策略 |
    | 热 key | 同一 key 的请求集中在一个节点 | 合并请求；对允许短时旧值的读热点可加本地缓存 |
    | 大 key | 读取、传输或删除单个大值时延迟上升 | 用 `MEMORY USAGE key` 估算占用，按访问方式拆分，删除大集合时可用 `UNLINK` |

    结合命中率、回源请求量、内存、淘汰数和延迟判断原因。线上遍历键空间时，用 `SCAN` 按游标分批迭代到 0，并控制速率。迭代期间可能返回重复项，结果也不是同一时刻的快照。[Redis SCAN](https://redis.io/docs/latest/commands/scan/)

1. **Java 访问**

    `spring-boot-starter-data-redis` 默认使用 Lettuce。读写同一组 key 的客户端应约定序列化格式。Redis 和数据库分别配置超时与重试，特别注意 `INCR` 等操作在响应丢失后重试可能重复生效。

    使用 Spring Cache 时，`@Cacheable` 默认按方法参数生成 key。Spring Data Redis 默认不给缓存条目设过期时间，可用 `RedisCacheConfiguration.entryTtl(…)` 配置。要让常规缓存 `put`、`evict`、`clear` 在 Spring 管理的数据库事务提交后执行，可在 `RedisCacheManager` 构建器启用 `transactionAware()`。数据库提交后，缓存操作仍可能失败，补偿方式见上节。[Spring Data Redis 缓存配置](https://docs.spring.io/spring-data/redis/reference/redis/redis-cache.html)

1. **分布式锁**

    在一个 Redis 主节点上，用 `SET key token NX PX 毫秒数` 获取有期限的锁，每次申请生成新的随机令牌。Redis 8.4 起可用 `DELEX key IFEQ token` 原子地比较令牌并解锁，旧版本用短 Lua 脚本完成同一步骤。[Redis 分布式锁](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)

    进程暂停超过租期后可能继续写入，此时别的客户端已取得锁。异步复制也可能在主节点故障时丢掉刚写入的锁。若过期持有者写入会破坏业务数据，应由被写入的系统校验单调递增的 fencing token 并拒绝旧令牌，或在数据库中通过约束、条件更新保证正确性。

1. **过期、内存与持久化**

    TTL 决定 key 的有效期，到期后访问会按不存在处理，回收内存可能稍晚。内存超过 `maxmemory` 时按 `maxmemory-policy` 处理，允许淘汰的 key 可能提前消失。`noeviction` 策略下需要增加内存的写命令可能报错，读取仍可进行。[Redis 内存淘汰](https://redis.io/docs/latest/develop/reference/eviction/)

    RDB 保存某个时刻的快照，单用 RDB 时崩溃可能丢失最近一次成功快照后的写入。AOF 记录写操作，恢复时重放，丢失窗口取决于刷盘策略。例如 `appendfsync everysec` 通常有约一秒的窗口。两种持久化方式可单用、组合或关闭。需要从误删或整机丢失中恢复时，还要独立保留备份并验证恢复流程。[Redis 持久化](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)

1. **复制与高可用**

    | 方案 | 作用 | 需要注意 |
    | --- | --- | --- |
    | 主从复制 | 保留数据副本，分担允许旧值的读取 | 默认异步，副本可能滞后，单靠复制不会自动选主 |
    | Sentinel | 监控、发现、自动故障转移 | 客户端要支持 Sentinel；故障时已确认写入仍可能丢 |
    | Redis Cluster | 将 16,384 个哈希槽分配到多个主节点，可为各主节点配置副本做故障转移 | 需支持 Cluster 的客户端；多 key 命令（如 `SINTER`）要求同槽，可用相同的哈希标签（如 `{user:42}`）让相关 key 同槽 |

    复制、自动故障转移与备份分别解决副本、服务恢复、历史数据恢复的问题。部署前明确能接受的数据丢失窗口，并演练故障转移和客户端重连。[Redis 复制](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/) · [Redis Cluster 规范](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)

---

## 知识点备忘

1. **分库分表**

    这里讨论按行水平拆分。同机分表可以缩小单表规模。将分片部署到不同机器，才有机会分摊单机的存储和请求负载。应用或中间件（如 ShardingSphere）负责把请求路由到物理库表。

    | 做法 | 做什么 | 例子 |
    | --- | --- | --- |
    | 分表 | 同一库内把一张逻辑表拆成多张物理表 | `orders` → `orders_0` … `orders_15` |
    | 分库 | 将行分布到多个库，各库可沿用同一表名 | `db_0.orders` … `db_3.orders` |

    **路由示例**：假设用户 ID 为非负整数，4 个库各有 16 张表。库号取 `user_id % 4`，表号取 `⌊user_id / 4⌋ % 16`。用户 42 的订单会落在 `db_2.orders_10`。按用户查订单时能定位一张表；若只有订单号，可维护「订单号 → 分片」映射，否则查询可能需要访问全部分片。[Vitess 分片路由](https://vitess.io/docs/reference/vindexes/)

    各分片独立自增默认只能保证本地唯一。业务若要求全局唯一订单号，可使用雪花 ID 或统一分配号段。

    >- 雪花 ID：按「时间 + 机器号 + 序列」拼出的 64 位整数，本地发号自己算、不查库。
    >- 号段：向发号中心一次领一段连续号，本地慢慢用，仍像自增整数。

    >**举例**：订单写入已打满单机，而主要查询是「我的订单」。按上述规则，每张表对应 `user_id % 64` 的一个余数。只有订单行数在这 64 个余数间分布均匀，每张表才约有原来 1/64 的行。还要单独看各分片的写入量：同一用户的订单始终落到一张表，少数活跃用户就可能造成热点。

    | 解决的问题 | 不解决 / 变难的 |
    | --- | --- |
    | 单表过大、单机吞吐不够 | 全站汇总、复杂 JOIN、全局排序分页 |
    | 单分片故障影响面与单次备份体积缩小（运维对象变多） | 按订单号查但不知 `user_id`（需映射或广播） |
    | 带分片键的读写可以分摊到多机 | 跨库事务需要协调；采用最终一致方案时要处理重试、幂等和对账 |
    | 可单独迁移部分数据以增加容量 | 改路由规则时要搬迁已写入的数据，校验新旧分片后再切换流量 |

    >先测量瓶颈。查询扫描过多可先改索引，历史数据挤占空间可先归档。需要分担单机写入时，再评估分片键能否覆盖主要请求。
1. **dry-run**

    dry-run 的具体行为取决于工具。先确认它会生成 SQL、读取目标库元数据，还是实际执行语句。三者能回答的问题不同。

    | 场景 | 审阅时看什么 |
    | --- | --- |
    | Schema 迁移 | 将对哪些对象执行哪些变更，顺序是否符合预期 |
    | DDL（加列、改索引等） | 根据目标引擎、版本和表定义判断是否可能重建表或等待锁 |
    | 导入 / 批量改数 | 用相同筛选条件核对范围，在代表性数据上检查类型和约束 |

    | 做法 | 能回答什么 |
    | --- | --- |
    | 生成 SQL 供审阅 | 可以核对对象、顺序和过滤条件。仅生成脚本无法验证数据库会接受语法、权限或现有数据 |
    | 连接目标库读取元数据 | 可识别已应用的迁移或结构差异。检查范围取决于工具，生产锁等待、耗时和磁盘需求仍需单独评估 |

    在隔离库执行再回滚，是一次真实试跑。执行期间会获取锁、消耗 I/O；PostgreSQL 的 `nextval()` 即使回滚也可能留下序列空号。MySQL 的 `ALTER TABLE`、`TRUNCATE TABLE` 等会隐式提交，事后执行 `ROLLBACK` 无法撤销这些变更。[PostgreSQL 序列函数](https://www.postgresql.org/docs/17/functions-sequence.html) · [MySQL 隐式提交语句](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html)

    >- **查询计划**：普通 `EXPLAIN` 用于查看计划。`EXPLAIN ANALYZE` 会实际执行受支持的语句，例如在 PostgreSQL 上分析 `UPDATE` 会真的更新行。[PostgreSQL EXPLAIN](https://www.postgresql.org/docs/17/sql-explain.html)
    >- **恢复演练**：在隔离环境中从备份恢复，再检查数据并记录耗时，才能验证恢复目标。

    >**工具示例**：Flyway Teams 的 dry run 可输出待执行的 SQL 迁移。Liquibase 的 `update-sql` 用于审阅将要执行的 SQL。Prisma 的 `migrate diff --script` 输出两份结构间的差异，覆盖范围限于 Prisma 支持的特性。[Flyway 迁移预演](https://documentation.red-gate.com/fd/migration-command-dry-runs-275218517.html) · [Liquibase update-sql](https://docs.liquibase.com/secure/reference-guide-6-0-2/update-sql) · [Prisma migrate diff](https://docs.prisma.io/docs/cli/v7/migrate/diff)
