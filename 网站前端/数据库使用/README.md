# 数据库使用

## 目录

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

---

- 数据库是用于持久化、组织和查询数据的软件。广义的数据库既包括使用表和 SQL 的关系型数据库，也包括键值、文档等 NoSQL 数据库，因此 Redis 也属于数据库。

    | 数据库 | 类型 | 数据组织方式 |
    | --- | --- | --- |
    | MySQL | 关系型数据库 | 表、行、列 |
    | PostgreSQL | 关系型数据库 | 表、行、列，并支持丰富的类型和扩展 |
    | MongoDB | NoSQL 文档数据库 | BSON 文档、集合 |
    | Redis | NoSQL 键值数据库 | 内存中的键和多种数据结构 |

    关系型数据库适合结构稳定、关联和事务要求明确的数据；NoSQL 是多种非关系型数据模型的统称，通常针对特定访问方式简化存储和查询。两者不是替代关系。全栈默认分工：MySQL 存事实并保证约束与事务；Redis 加速热点读、会话、计数、限流和锁。一起用时的读路径见 Redis 的 Cache Aside。

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

MySQL 是关系型数据库。一个服务里可有多个库（`DATABASE` 与 `SCHEMA` 基本同义）；库由表组成。约束挡脏数据，索引加速查找，事务保证多步同成同败，SQL 管读写。

列表超时、重复下单、金额对不上，根因经常在表、索引和事务，而不是页面渲染。访问链路：`页面 -> HTTP API -> 后端 -> JDBC/Mapper -> MySQL`。前端不直连库。下文以 **MySQL 8.4 LTS + InnoDB** 为准。

学习顺序：`表与约束 -> CRUD / JOIN / 聚合 -> 索引 -> 事务 -> Java`。进阶再看执行计划、连接池、一致性与备份。语法见「常用命令」；列类型见「列类型」。

1. **表与约束**

    表 = 一类对象，行 = 一条记录，列 = 属性。主键短、稳、不变；业务“不能重复”用 `UNIQUE`，不要拿业务号当主键。字符集 `utf8mb4`。先规范化，只为明确的性能或历史快照才冗余。`NULL` 是未知/不存在，不是 `''` 或 `0`。页面校验给人看，库约束挡绕过前端的脏写入。

    | 约束 | 作用 | 注意 |
    | --- | --- | --- |
    | `NOT NULL` / `DEFAULT` | 禁空 / 默认值 | 显式写入的 `NULL` 不会被默认值替换 |
    | `PRIMARY KEY` | 行的永久身份，非空且唯一 | 每表一个，可多列 |
    | `UNIQUE` | 非空值不重复 | MySQL 允许多个 `NULL` |
    | `CHECK` | 行内条件 | `TRUE` 或因 `NULL` 得到 `UNKNOWN` 都通过 |
    | `FOREIGN KEY` | 引用完整性 | 写明 `ON DELETE` / `ON UPDATE`，不要默认级联删 |

    一对一：外键 + `UNIQUE`。一对多：外键在“多”的一侧。多对多：中间表存两侧外键。有外键时先建父表、后建子表，删除相反。`UNIQUE` 冲突在 Java 常是 `DuplicateKeyException`，接口表现为“已存在”；外键失败常是“仍被引用”。不要为了联调关掉约束。

    `TRUNCATE` 清空数据、留表结构；`DROP TABLE` / `DROP DATABASE` 删对象。InnoDB 上 `TRUNCATE` 是 DDL（Data Definition Language，数据定义语言：改库/表/索引结构，不是改某一行）：隐式提交、不能 `ROLLBACK`、会重置 `AUTO_INCREMENT`；有指向本表的外键时会失败，应改用 `DELETE`。`COMMENT` 是表/列元数据（`SHOW CREATE TABLE` 可见），不是 SQL 注释。改列注释必须 `MODIFY`/`CHANGE` 并写出完整列定义，不能只改 `COMMENT`。

1. **查询与改数据**

    SQL 注释：`--` 后须有空格；`#` 是 MySQL 扩展；`/* */` 可跨行。`--` / `#` 只吃到行末，逗号不要跟列名一起注释掉。

    `INSERT` 写明列名并限制批次；`SELECT` 只取需要的列；`UPDATE` / `DELETE` 必须有 `WHERE`，改前用同一条件先查。空值用 `IS NULL` / `IS NOT NULL`。能一条 `UPDATE` 解决就不要先查再改。物理删除前确认审计和恢复要求。

    理解顺序（不是引擎真实执行顺序）：`FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT`。

    - `WHERE` 过滤行，`HAVING` 过滤聚合结果；`COUNT`/`SUM` 不能写进 `WHERE`。
    - `DISTINCT` 按选出的整行去重；要统计用 `GROUP BY`。
    - `LEFT JOIN` 对右表的过滤条件通常放在 `ON`，放 `WHERE` 容易把左表行滤掉。

    列表接口：过滤和排序字段要对得上索引。循环里按父 id 再查子表是 N+1，应 `JOIN` 或一次 `IN`。深分页少用大 `OFFSET`，用上一页的排序键 + 唯一 ID 继续查。`LIMIT` 要有上限，不要让前端传入无界 `pageSize`。

    视图 = 给一段 `SELECT` 起名，普通视图不另存数据，每次查会再跑定义。用来复用 JOIN，或对外只暴露部分列。`DROP VIEW` 不删底表。MySQL 没有物化视图；要落一份算好的结果，自己建表再 `INSERT`（底表变了不会自动更新）。对视图写入改的是底表；`JOIN` / `GROUP BY` / 聚合的视图通常不可写。带 `WHERE` 的视图写入后可能从视图里“消失”，`WITH CHECK OPTION` 会拒绝这种写入。

1. **索引与 `EXPLAIN`**

    索引是按列排好的查找目录，加速 `WHERE`、`JOIN`、`ORDER BY`。接口慢先看这条 SQL 走没走索引，不要先改前端。只为真实查询建；索引越多，写和存储越贵。

    两轴：几列、能不能重复。都是 B+Tree。

    | | 单列 | 复合 `(列1, 列2)` |
    | --- | --- | --- |
    | 写法 | 括号里一列 | 两列及以上，**顺序有意义** |
    | 能覆盖 | 该列上的过滤/排序/关联 | `列1=?` 以及 `列1=? AND 列2=?`；一般**不能**单独服务 `列2=?` |

    | | 普通索引 | 唯一索引 |
    | --- | --- | --- |
    | 加速查找 | 会 | 会 |
    | 同一非空值多次出现 | 可以 | 第二次写入报错 |
    | `NULL` | 可多个 | 也可多个（不参与唯一比较） |
    | 与主键 | 不是主键 | 也不是：主键每表一个且不能 `NULL`；`UNIQUE` 可多组 |

    `UNIQUE` 约束会自动建唯一索引，与 `CREATE UNIQUE INDEX` 相同。`SHOW INDEX` 里 `Non_unique = 0` 表示唯一。多列唯一约束的是**组合**，`UNIQUE(user_id, sku_id)` ≠ `UNIQUE(sku_id)`。

    InnoDB 数据按主键聚簇；二级索引带着主键，所以主键宜短。覆盖索引（查询列全在索引里）可避免回表。`LIKE '%xx'`、隐式类型转换、对索引列做函数/运算，常常用不上索引。只查复合索引的第 2 列，对不上最左前缀，容易全表扫。

    `EXPLAIN` 先看 `type`、`key`、`rows`、`filtered`、`Extra`。`EXPLAIN ANALYZE` 会真跑查询。优化：复现 → 看计划 → 小改 → 再测。

1. **事务、隔离与锁**

    事务 = 多步同成同败（ACID）。MySQL 默认自动提交；需要一起成败时 `START TRANSACTION`。未提交的改动只有当前会话能看见（`READ UNCOMMITTED` 才可能脏读）。默认 `REPEATABLE READ` 下，同一事务的一致性读还共用一份快照。`COMMIT` 持久并对他人可见，`ROLLBACK` 整笔丢掉。结束事务是 `COMMIT` 或 `ROLLBACK` 二选一，不是每条 SQL 后面的固定后缀。

    一个 HTTP 请求里开一段事务。不要把 HTTP / RPC / 发 MQ 包进事务。前端重复点击必须接口幂等；库的 `UNIQUE` 只能挡“完全相同的唯一键”，挡不住“两次不同请求各下一单”。

    DDL 常会隐式提交，不能当 DML（Data Manipulation Language，数据操纵语言：改行数据、不改表结构）那样回滚。某句 DML 失败只撤销这一句，前面已成功的仍在事务里——失败应整笔 `ROLLBACK`（或 `ROLLBACK TO` 保存点后再继续），不要对半成品 `COMMIT`。死锁时 InnoDB 常整笔回滚，须重新 `START TRANSACTION`。`UPDATE` 影响 0 行通常不算错，需要时查 `ROW_COUNT()`。

    `SAVEPOINT` 只在需要部分回滚时用。三选一、不要连着当脚本跑：全成功 → 只 `COMMIT`；整笔放弃 → 只 `ROLLBACK`；部分回滚 → `ROLLBACK TO` 后继续（该点之后的保存点会失效）。锁等待超时等瞬时失败才可用同一语句重试；唯一冲突应换键值或整笔 `ROLLBACK`，不要用同一 `VALUES` 再插。

    服务端只执行客户端发来的语句，失败不会自动 `COMMIT`/`ROLLBACK`。JDBC 抛错就停后续 SQL；`mysql>` 粘贴多条仍可能继续发。`mysql < 文件` 默认遇错停止。`IF ... THEN COMMIT ELSE ROLLBACK` 只能写在存储过程里。

    | 隔离级别 | 表现 |
    | --- | --- |
    | `READ UNCOMMITTED` | 可能脏读，业务几乎不用 |
    | `READ COMMITTED` | 每次一致性读看到当时已提交的数据 |
    | `REPEATABLE READ` | InnoDB 默认；同一事务的一致性读通常复用快照 |
    | `SERIALIZABLE` | 最强，并发最贵 |

    脏读 = 读到未提交；不可重复读 = 同一行两次结果不同；幻读 = 同一条件的行集合变了。MVCC 用 Read View 判断可见性；长事务拖住清理。`SELECT ... FOR UPDATE` 必须在事务里，锁范围跟扫描的索引走。事务要短、按固定顺序碰数据。乐观锁用 `version`；死锁重试必须整笔重跑，并设上限、退避和幂等。

1. **Java 访问**

    `连接池 -> Connection -> PreparedStatement/MyBatis -> 映射 -> Service 事务`。多步写入同一事务，失败 `rollback` 并停后续 SQL。`UNIQUE` / 外键失败不要吃掉异常后仍返回成功。

    | MySQL | Java | 注意 |
    | --- | --- | --- |
    | `DECIMAL` | `BigDecimal` | 金额定精度和舍入；比较用 `compareTo` |
    | `INT` / `BIGINT` | `Integer` / `Long` | 可空用包装类；`BIGINT UNSIGNED` 可能超过 `long` |
    | `DATE` / `DATETIME` / `TIMESTAMP` | `LocalDate` / `LocalDateTime` / `Instant` | `DATETIME` 无时区；绝对时间用 UTC |
    | `JSON` | `String` 或对象 | 统一序列化；高频查询字段拆成普通列 |

    SQL 值用参数绑定。MyBatis `${}` 是拼字符串，只许白名单后的标识符。[连接池](../Java学习笔记/README.md#jdbc-与数据库访问演进)：`每实例池上限 × 实例数 + 其他客户端` 必须低于库的 `max_connections`，留运维余量。`@Transactional` 通常不进新线程，同类自调用可能不生效；跨库 / HTTP / MQ 靠 outbox、重试和消费幂等。

1. **复制、迁移、备份、监控**

    redo log 做崩溃恢复，binlog 做复制和时间点恢复，**都不能替代备份**。复制默认异步，误删也会被副本跟上。刚写入再读自己的走主库；打到滞后副本，页面会看到旧数据。事务内不要切到副本。账号最小权限 + TLS，密码不进代码和日志。DDL 用迁移工具；大表变更先估锁、磁盘和复制延迟。备份要有范围、保留期、恢复目标，并定期在隔离环境恢复验证。监控连接等待、慢 SQL、扫描行数、锁等待、I/O、复制延迟；先定位 SQL 和执行计划，再谈扩容或分库分表。

    现场诊断：`EXPLAIN` 看走不走索引、估扫多少行；`SHOW FULL PROCESSLIST` 看谁在连、跑哪条 SQL、卡了多久；`SHOW VARIABLES` 看配置；`SHOW STATUS` 看运行计数；`SHOW WARNINGS` 看上一条的截断、类型转换等警告。对象定义用 `SHOW CREATE`；权限用 `SHOW GRANTS`；当前库用 `SELECT DATABASE()`。

- <details>

    <summary>列类型</summary>

    `NULL` 不是类型；列能不能空由 `NULL` / `NOT NULL` 决定。新表优先：

    | 用途 | 类型 |
    | --- | --- |
    | 主键 | `BIGINT UNSIGNED AUTO_INCREMENT` |
    | 金额 | `DECIMAL(p,s)`，不用 `FLOAT`/`DOUBLE` |
    | 短文本 | `VARCHAR(n)`，字符集 `utf8mb4` |
    | 长文本 / 原始字节 | `TEXT` / `BLOB` |
    | 日期时间 | `DATE`；墙上时间 `DATETIME`；带时区换算 `TIMESTAMP` |
    | 真假 | `BOOLEAN`（即 `TINYINT(1)`；非 0 为真，要严格 0/1 再加 `CHECK`） |
    | 半结构化 | `JSON`（稳定且常查的字段仍拆列） |

    其他类型用到再查：

    | 类 | 要点 |
    | --- | --- |
    | 整数 | `TINYINT`～`BIGINT`；`UNSIGNED` 只存非负。`INT(11)` 的 `11` 是已弃用的显示宽度，不是范围 |
    | 浮点 | `FLOAT`/`DOUBLE` 有二进制误差，科学计算才用 |
    | 位 / 别名 | `BIT(n)`；`SERIAL` = `BIGINT UNSIGNED AUTO_INCREMENT UNIQUE` |
    | 时间 | `TIME` 可表示时长；`fsp` 0～6 为小数秒；`YEAR` 只管年。`TIMESTAMP` 约 1970～2038 |
    | 定长串 | `CHAR(n)` 定长字符；`BINARY`/`VARBINARY` 按字节、无字符集 |
    | 大对象 | `TINY`/`MEDIUM`/`LONG` + `TEXT` 或 `BLOB`，上限按字节；多字节字符集下字符数更少 |
    | `ENUM`枚举/`SET`集合 | 固定小集合；值会变、要外键或额外属性时拆表 |
    | 空间 | `POINT` 等 GIS；可带 SRID 和空间索引 |
    | 向量 | [`VECTOR(n)`](https://dev.mysql.com/doc/refman/9.7/en/vector.html) 自 9.0，**8.4 LTS 没有** |
    | 旧别名 | `INT1`～`INT8`、`FLOAT4`/`FLOAT8`、`LONG VARCHAR` 等，读懂旧 SQL 即可，新表不用 |

    </details>

- <details>

    <summary>常用命令</summary>

    >除备份外均在 `mysql>` 执行。`「...」` 换成实际名。

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
    SHOW TABLES;
    DESCRIBE 「表」;
    SHOW CREATE TABLE 「表」;
    ALTER TABLE 「表」 ADD COLUMN 「列」 VARCHAR(255);
    ALTER TABLE 「表」 MODIFY COLUMN 「列」 TEXT;
    ALTER TABLE 「表」 RENAME COLUMN 「旧」 TO 「新」;
    ALTER TABLE 「表」 DROP COLUMN 「列」;
    RENAME TABLE 「旧」 TO 「新」;
    TRUNCATE TABLE 「表」;   -- DDL：清空并重置自增，不可 ROLLBACK
    DROP TABLE IF EXISTS 「表」;  -- 删对象

    -- CRUD（UPDATE/DELETE 先用同一 WHERE 查出再改）
    INSERT INTO 「表」 (「列1」, 「列2」) VALUES ('「值1」', '「值2」');
    SELECT 「列1」, 「列2」 FROM 「表」 WHERE 「条件」;
    UPDATE 「表」 SET 「列」 = '「新值」' WHERE 「条件」;
    DELETE FROM 「表」 WHERE 「条件」;

    SELECT DISTINCT 「列」 FROM 「表」 WHERE 「条件」 ORDER BY 「列」 DESC LIMIT 「n」 OFFSET 「m」;
    SELECT 「分组列」, COUNT(*) AS total FROM 「表」 GROUP BY 「分组列」 HAVING COUNT(*) >= 10;
    SELECT a.「列」, b.「列」 FROM 「表A」 a LEFT JOIN 「表B」 b ON b.「键」 = a.「键」;

    -- 索引（优化器决定是否使用）
    SHOW INDEX FROM 「表」;
    CREATE INDEX 「名」 ON 「表」 (「列1」, 「列2」);
    CREATE UNIQUE INDEX 「名」 ON 「表」 (「列」);
    DROP INDEX 「名」 ON 「表」;

    -- 事务
    START TRANSACTION;
    -- 然后三选一，不要连着跑：COMMIT;  |  ROLLBACK;  |  先 SAVEPOINT 「名」; 再 ROLLBACK TO SAVEPOINT 「名」;

    -- 视图 = 给 SELECT 起名，不另存数据；MySQL 没有物化视图。DROP VIEW 不删底表。
    -- JOIN/聚合/DISTINCT 的视图通常不可写；WITH CHECK OPTION 拒绝写出视图条件外的行。
    CREATE OR REPLACE VIEW 「视图」 AS SELECT 「列」 FROM 「表」 WHERE 「条件」; -- 可加 WITH CHECK OPTION
    SHOW CREATE VIEW 「视图」;
    DROP VIEW IF EXISTS 「视图」;

    -- 用户与权限
    CREATE USER IF NOT EXISTS '「用户」'@'「主机」' IDENTIFIED BY '「密码」';
    ALTER USER '「用户」'@'「主机」' IDENTIFIED BY '「新密码」';
    GRANT SELECT, INSERT, UPDATE, DELETE ON 「库」.* TO '「用户」'@'「主机」';
    SHOW GRANTS FOR '「用户」'@'「主机」';
    REVOKE SELECT, INSERT, UPDATE, DELETE ON 「库」.* FROM '「用户」'@'「主机」';
    DROP USER IF EXISTS '「用户」'@'「主机」';

    -- 诊断
    EXPLAIN SELECT 「列」 FROM 「表」 WHERE 「条件」;
    SHOW FULL PROCESSLIST;
    SHOW VARIABLES LIKE 'max_connections';
    SHOW STATUS LIKE 'Slow_queries';
    SHOW WARNINGS;
    ```

    ```shell
    mysqldump --single-transaction -h 「主机」 -u 「用户」 -p 「库」 > 「备份.sql」
    mysql -h 「主机」 -u 「用户」 -p 「库」 < 「备份.sql」
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

    把允许不受信任用户创建对象的 Schema 加入 `search_path` 会带来对象名称被遮蔽的风险。生产环境应明确 Schema 所有者和 `CREATE` 权限，迁移脚本宜使用带 Schema 的对象名。

- **特色类型与 SQL**

    | 能力 | 适合场景 | 边界 |
    | --- | --- | --- |
    | `UUID` | 跨系统生成标识 | 评估索引大小和写入局部性 |
    | [PostgreSQL `jsonb`](../前端内容/基础知识.md#postgresql-jsonb) | 查询半结构化数据 | 稳定且高频查询的字段仍优先使用普通列 |
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

    索引必须对应真实查询的操作符和数据分布，不要因为 PostgreSQL 支持的索引类型多就全部创建。`EXPLAIN` 只显示计划；`EXPLAIN (ANALYZE, BUFFERS)` 会实际执行语句并显示实际耗时、行数和缓冲区信息，对写语句使用前要放入可回滚事务并确认影响。

- **MVCC、VACUUM 与扩展**

    - PostgreSQL 使用 MVCC；`UPDATE` 和 `DELETE` 产生的旧版本由 `VACUUM` 清理并让空间复用，`ANALYZE` 更新优化器统计信息。
    - autovacuum 自动执行必要的清理、统计更新和事务 ID 回卷防护，应根据写入量调整，不要关闭。
    - `VACUUM FULL` 会重写表并取得强锁，不是日常清理命令；优先让普通 `VACUUM` 持续工作。
    - `CREATE EXTENSION` 把服务器已安装的扩展注册到当前数据库。引入扩展前要确认权限、版本升级、备份恢复和目标环境都支持它。

- **与 MySQL 的学习差异**

    MySQL 中 `SCHEMA` 与 `DATABASE` 基本同义，PostgreSQL 的 Schema 则是数据库内的命名空间；两者默认隔离级别分别为 InnoDB 的 `REPEATABLE READ` 和 PostgreSQL 的 `READ COMMITTED`。整数 ID 在 MySQL 常用 `AUTO_INCREMENT`，PostgreSQL 推荐标识列（Identity）。

</details>

---

## NoSQL 数据库

NoSQL 不是一种固定的数据模型，而是键值、文档、列族、图等非关系型数据库的统称。本节只介绍 MongoDB 和 Redis。

### MongoDB

<details>
<summary></summary>

MongoDB 是文档数据库：一条记录是一个 BSON 文档，多个文档组成集合（Collection）。文档类似 JSON 对象，可以包含数组和嵌套文档；同一集合中的文档不必拥有完全相同的字段。

- **[BSON](../前端内容/基础知识.md#bson) 与文档建模**

    BSON 是 MongoDB 存储和传输文档使用的带类型二进制格式；具体类型、Extended JSON、使用边界以及与 PostgreSQL `jsonb` 的区别见上方链接。此处重点是文档建模。

    | 关系 | 优先嵌入 | 优先引用 |
    | --- | --- | --- |
    | 读取方式 | 总是随父对象一起读取 | 经常独立查询 |
    | 生命周期 | 随父对象一起创建和删除 | 可独立修改或复用 |
    | 数据规模 | 数量有明确上限 | 数量可能持续增长 |
    | 典型关系 | 一对少量明细 | 多对多、共享对象、高基数关系 |

    文档结构应从主要读写路径反推：把需要原子更新、经常一起读取且规模可控的数据嵌入；不要为了减少一次查询，把会无限增长的数组塞进单个文档。

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

    能提前过滤的数据通常尽早使用 `$match`，并只传递后续需要的字段。复杂管道应使用 `explain()` 检查索引利用、扫描量和是否出现大量内存或磁盘处理。

- **索引与 Schema Validation**

    单字段、复合、唯一和 TTL 索引分别服务于不同查询与约束；复合索引的字段顺序影响可用前缀，TTL 删除也不保证在到期瞬间完成。索引会增加存储和写入成本，应按真实查询建立。Schema Validation 可限制必填字段、BSON 类型和值范围，结构演进仍需兼容和迁移步骤。

- **原子性、事务与高可用**

    - 单文档写操作具有原子性；多文档事务会增加协调成本，应保持简短。大量关联和复杂事务是主线时，关系型数据库通常更直接。
    - 副本集提供冗余和故障转移，但读写保证还取决于 read concern、write concern 和 read preference。
    - 分片用于扩展容量和吞吐，分片键决定数据分布、查询路由和热点；只有需求明确且团队能承担运维复杂度时再引入。

    灵活结构不等于没有 Schema，也不等于可以忽略约束、索引和恢复设计。

</details>

### Redis

Redis 主要在内存读写。事实数据仍在 MySQL；Redis 做缓存、会话、计数、排行、限流和分布式锁。丢了可以重建的才适合当缓存。接口突然打满数据库，根因经常是缓存失效或穿透，而不是页面多渲染了一次。访问链路：`页面 -> HTTP API -> 后端 -> Redis 客户端 -> Redis`。前端不直连。

学习顺序：`场景与 key -> 数据结构 -> 原子/Pipeline -> Cache Aside -> Java -> 锁 -> 过期与持久化 -> 复制`。命令入口见安装节的 `redis-cli`；机制对比见「原子操作」。

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

1. **数据结构**

    按操作选型，不要把所有对象都序列化成大字符串。计数用 `INCR`，集合运算用 Set，排名用 Sorted Set。

    | 数据结构 | 特点 | 常见用途 |
    | --- | --- | --- |
    | String | 字符串、数字或二进制 | 缓存值、计数器、状态 |
    | Hash | 一个 key 下多个字段 | 对象若干属性一起改 |
    | List | 有序序列 | 简单队列、时间线 |
    | Set | 无序且不重复 | 标签、去重、交并差 |
    | Sorted Set | 成员不重复，按分数排序 | 排行榜、按时间排序 |
    | Stream | 只追加，支持消费组 | 要确认和重试的消息流 |

1. **原子、Pipeline、事务**

    Redis 的“原子”是单条命令执行时不被插队，**不是** MySQL 那种失败整笔回滚。先 `GET` 再 `SET` 仍会被别的请求穿插。批量降低 RTT 用 Pipeline；要条件 + 多步不被打断，用短 Lua，不要自己拼一长串客户端往返。

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
