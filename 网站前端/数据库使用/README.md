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
1. [选型总结](#选型总结)

---

- 数据库是用于持久化、组织和查询数据的软件。广义的数据库既包括使用表和 SQL 的关系型数据库，也包括键值、文档等 NoSQL 数据库，因此 Redis 也属于数据库。

    | 数据库 | 类型 | 数据组织方式 |
    | --- | --- | --- |
    | MySQL | 关系型数据库 | 表、行、列 |
    | PostgreSQL | 关系型数据库 | 表、行、列，并支持丰富的类型和扩展 |
    | MongoDB | NoSQL 文档数据库 | BSON 文档、集合 |
    | Redis | NoSQL 键值数据库 | 内存中的键和多种数据结构 |

    关系型数据库适合结构稳定、关联和事务要求明确的数据；NoSQL 是多种非关系型数据模型的统称，通常针对特定访问方式简化存储和查询。两者不是替代关系，一个系统可以同时使用多种数据库。

## 服务安装、启动与连接

### [`MySQL`](https://dev.mysql.com/doc/refman/en/)服务安装、启动与连接

```shell
# 1. 安装
brew install mysql  # 安装 Homebrew 当前稳定版

# 2. 启动服务
brew services start mysql
brew services stop mysql
brew services restart mysql
brew services info mysql  # 查看服务状态和 PID
brew services list        # 查看 Homebrew 管理的后台服务，如 mysql、postgresql@17、redis
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
brew services info postgresql@17  # 查看服务状态和 PID
brew services list                # 查看 Homebrew 管理的后台服务
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
brew services info redis  # 查看服务状态和 PID
brew services list        # 查看 Homebrew 管理的后台服务
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

MySQL 是关系型数据库管理系统。一个 MySQL 服务可包含多个数据库（`DATABASE` 与 `SCHEMA` 在 MySQL 中基本同义）；数据库由表组成，约束保证数据规则，索引加快查询，SQL 用来读写和管理数据。

后端访问链路：`页面 -> HTTP API -> Controller -> Service -> Mapper/JDBC -> MySQL`。前端不应直接连接数据库。

- 学习主线：

    - 基础：`表与约束 -> CRUD -> JOIN/聚合 -> 索引 -> 事务 -> Java 集成`
    - 进阶：`执行计划 -> 并发与幂等 -> 连接池 -> 读写一致性 -> 生产诊断与容灾`

- <details>

    <summary>常用命令速查</summary>

    除“备份与恢复”外，以下命令均在 `mysql>` 中执行；`「...」` 需替换为实际内容。

    1. 数据库

        ```sql
        SHOW DATABASES;
        CREATE DATABASE IF NOT EXISTS 「数据库名」;
        USE 「数据库名」;
        SELECT DATABASE();
        SHOW CREATE DATABASE 「数据库名」;
        DROP DATABASE IF EXISTS 「数据库名」;
        ```

    1. 表与列

        ```sql
        SHOW TABLES;
        CREATE TABLE IF NOT EXISTS 「表名」 (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            PRIMARY KEY (id)
        ) 「表类型」 「字符集设置」 「注释」;
        DESCRIBE 「表名」;
        SHOW CREATE TABLE 「表名」;
        ALTER TABLE 「表名」 ADD COLUMN 「列名」 VARCHAR(255);
        ALTER TABLE 「表名」 MODIFY COLUMN 「列名」 TEXT;
        ALTER TABLE 「表名」 RENAME COLUMN 「旧列名」 TO 「新列名」;
        ALTER TABLE 「表名」 DROP COLUMN 「列名」;
        RENAME TABLE 「旧表名」 TO 「新表名」;
        TRUNCATE TABLE 「表名」;
        DROP TABLE IF EXISTS 「表名」;
        ```

    1. 数据增删改查（CRUD）

        ```sql
        INSERT INTO 「表名」 (「列1」, 「列2」) VALUES ('「值1」', '「值2」');
        SELECT 「列1」, 「列2」 FROM 「表名」 WHERE 「条件」;
        UPDATE 「表名」 SET 「列名」 = '「新值」' WHERE 「条件」;
        DELETE FROM 「表名」 WHERE 「条件」;
        ```

        >执行 `UPDATE` / `DELETE` 前，先用相同的 `WHERE` 条件查询确认；`TRUNCATE` 会清空整表，`DROP` 会删除对象。

    1. 筛选、聚合与关联

        ```sql
        SELECT DISTINCT 「列名」
        FROM 「表名」
        WHERE 「条件」
        ORDER BY 「列名」 DESC
        LIMIT 「数量」 OFFSET 「偏移量」;

        SELECT 「分组列」, COUNT(*) AS total, SUM(「数值列」) AS amount
        FROM 「表名」
        WHERE 「条件」
        GROUP BY 「分组列」
        HAVING COUNT(*) > 0;

        SELECT a.「列名」, b.「列名」
        FROM 「表A」 AS a
        LEFT JOIN 「表B」 AS b ON b.「关联列」 = a.「关联列」;
        ```

    1. 索引

        ```sql
        SHOW INDEX FROM 「表名」;
        CREATE INDEX 「索引名」 ON 「表名」 (「列1」, 「列2」);
        CREATE UNIQUE INDEX 「唯一索引名」 ON 「表名」 (「列名」);
        DROP INDEX 「索引名」 ON 「表名」;
        ```

    1. 事务

        ```sql
        START TRANSACTION;
        SAVEPOINT 「保存点名」;
        ROLLBACK TO SAVEPOINT 「保存点名」;
        COMMIT;
        ROLLBACK;
        ```

        >`COMMIT` 与 `ROLLBACK` 是事务最终处理的两种选择，不是按顺序都执行。

    1. 视图

        ```sql
        CREATE OR REPLACE VIEW 「视图名」 AS SELECT 「列名」 FROM 「表名」 WHERE 「条件」;
        SHOW CREATE VIEW 「视图名」;
        DROP VIEW IF EXISTS 「视图名」;
        ```

    1. 用户与权限

        ```sql
        CREATE USER IF NOT EXISTS '「用户名」'@'「主机」' IDENTIFIED BY '「密码」';
        ALTER USER '「用户名」'@'「主机」' IDENTIFIED BY '「新密码」';
        GRANT SELECT, INSERT, UPDATE, DELETE ON 「数据库名」.* TO '「用户名」'@'「主机」';
        SHOW GRANTS FOR '「用户名」'@'「主机」';
        REVOKE SELECT, INSERT, UPDATE, DELETE ON 「数据库名」.* FROM '「用户名」'@'「主机」';
        DROP USER IF EXISTS '「用户名」'@'「主机」';
        ```

    1. 执行计划与诊断

        ```sql
        EXPLAIN SELECT 「列名」 FROM 「表名」 WHERE 「条件」;
        SHOW FULL PROCESSLIST;
        SHOW VARIABLES LIKE '「变量名或模式」';
        SHOW STATUS LIKE '「状态名或模式」';
        SHOW WARNINGS;
        ```

    1. 备份与恢复（在终端执行）

        ```shell
        mysqldump --single-transaction -h 「主机」 -u 「用户名」 -p 「数据库名」 > 「备份文件.sql」
        mysql -h 「主机」 -u 「用户名」 -p 「数据库名」 < 「备份文件.sql」
        ```

    </details>

- <details>

    <summary>列数据类型</summary>

    MySQL 的列类型分为数值、日期时间、字符串/二进制、`JSON`、空间和向量类型。`NULL` 表示“未知或不存在”，不是一种数据类型；列是否允许 `NULL` 由 `NULL` / `NOT NULL` 约束决定。

    1. **数值类型**

        - 整数类型：

            | 类型 | 存储 | 有符号范围 | `UNSIGNED` 范围 |
            | --- | ---: | ---: | ---: |
            | `TINYINT` | 1 字节 | -128～127 | 0～255 |
            | `SMALLINT` | 2 字节 | -32,768～32,767 | 0～65,535 |
            | `MEDIUMINT` | 3 字节 | -8,388,608～8,388,607 | 0～16,777,215 |
            | `INT` / `INTEGER` | 4 字节 | -2,147,483,648～2,147,483,647 | 0～4,294,967,295 |
            | `BIGINT` | 8 字节 | -9,223,372,036,854,775,808～9,223,372,036,854,775,807 | 0～18,446,744,073,709,551,615 |

            `UNSIGNED` 表示无符号，只能存非负数。`INT(11)` 中的 `11` 曾是显示宽度，不是取值范围；显示宽度和 `ZEROFILL` 已弃用，新表直接使用 `INT` 等类型即可。

        - 定点数与浮点数：

            | 类型 | 特点 | 常见用途 |
            | --- | --- | --- |
            | `DECIMAL(p,s)` / `NUMERIC(p,s)` | 精确小数；`p` 是总位数，`s` 是小数位数 | 金额、精确比例 |
            | `FLOAT` | 单精度近似值 | 允许误差的科学计算 |
            | `DOUBLE` / `DOUBLE PRECISION` | 双精度近似值 | 需要更大范围或更高精度的科学计算 |

            金额使用 `DECIMAL`，不使用会产生二进制舍入误差的 `FLOAT` / `DOUBLE`。`DEC` 和 `FIXED` 是 `DECIMAL` 的别名；`REAL` 默认是 `DOUBLE` 的别名，开启 `REAL_AS_FLOAT` SQL 模式后表示 `FLOAT`。

        - 其他数值类型：

            | 类型 | 含义 |
            | --- | --- |
            | `BIT(n)` | 位值，`n` 为 1～64，默认为 1 |
            | `BOOL` / `BOOLEAN` | `TINYINT(1)` 的别名；0 为假，非 0 为真 |
            | `SERIAL` | `BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE` 的别名 |

            `BOOLEAN` 并不会自动将值限制为 0 或 1；严格布尔列可再添加 `CHECK (column_name IN (0, 1))`。

    1. **日期和时间类型**

        | 类型 | 格式/范围 | 关键区别 |
        | --- | --- | --- |
        | `DATE` | `YYYY-MM-DD`；1000-01-01～9999-12-31 | 只保存日期 |
        | `TIME(fsp)` | `HH:MM:SS[.微秒]`；-838:59:59～838:59:59 | 可表示时间点或时长 |
        | `DATETIME(fsp)` | `YYYY-MM-DD HH:MM:SS[.微秒]`；1000～9999 年 | 保存原样日期时间，不做时区转换 |
        | `TIMESTAMP(fsp)` | 约 1970～2038 年 | 写入时按会话时区转为 UTC，读取时再转回 |
        | `YEAR` | 1901～2155，以及 0000 | 只保存年份 |

        `fsp` 表示小数秒精度，可为 0～6，例如 `DATETIME(3)` 保留毫秒。`YEAR(4)` 已弃用，使用 `YEAR` 即可。

    1. **字符串和二进制类型**

        - 定长和变长值：

            | 类型 | 内容 | 长度特点 |
            | --- | --- | --- |
            | `CHAR(n)` | 字符串 | 定长，`n` 为 0～255 个字符 |
            | `VARCHAR(n)` / `CHARACTER VARYING(n)` | 字符串 | 变长；实际上限受字符集和单行最大 65,535 字节限制 |
            | `BINARY(n)` | 二进制字节 | 定长，不按字符集比较 |
            | `VARBINARY(n)` | 二进制字节 | 变长，不按字符集比较 |

            普通文本优先使用 `utf8mb4` 字符集。`NCHAR` / `NVARCHAR` 是“国家字符集”写法，MySQL 8.4 中仍对应已弃用的 `utf8mb3`，新表不建议使用。

        - 大文本和大二进制值：

            | 文本类型 | 二进制类型 | 最大长度 |
            | --- | --- | ---: |
            | `TINYTEXT` | `TINYBLOB` | 255 字节 |
            | `TEXT` | `BLOB` | 65,535 字节 |
            | `MEDIUMTEXT` | `MEDIUMBLOB` | 16,777,215 字节 |
            | `LONGTEXT` | `LONGBLOB` | 4,294,967,295 字节 |

            `TEXT` 系列存字符，有字符集和排序规则；`BLOB` 系列存原始字节。多字节字符集下，`TEXT` 能存的字符数少于表中的字节数。

        - 枚举和集合：

            | 类型 | 含义 | 上限 |
            | --- | --- | ---: |
            | `ENUM('a', 'b', ...)` | 只能选一个预定义值 | 65,535 个成员 |
            | `SET('a', 'b', ...)` | 可同时选多个预定义值 | 64 个成员 |

            值集频繁变化、需要外键关联或携带额外属性时，优先拆成普通表，而不是使用 `ENUM` / `SET`。

    1. **`JSON` 类型**

        `JSON` 保存 JSON 文档。MySQL 会验证语法，并以内部二进制格式存储，可使用 JSON 函数和路径查询。结构稳定、经常查询或需要约束的字段，仍应拆成普通列。

    1. **空间数据类型**

        | 分类 | 类型 |
        | --- | --- |
        | 通用几何 | `GEOMETRY` |
        | 单个几何 | `POINT`、`LINESTRING`、`POLYGON` |
        | 几何集合 | `MULTIPOINT`、`MULTILINESTRING`、`MULTIPOLYGON`、`GEOMETRYCOLLECTION` / `GEOMCOLLECTION` |

        空间类型用于坐标、路线、区域等 GIS 数据，可指定 SRID 并建立空间索引。

    1. **向量类型**

        [`VECTOR(n)`](https://dev.mysql.com/doc/refman/9.7/en/vector.html) 用于保存 `n` 个 32 位浮点数组成的向量，常见于 AI 嵌入。它从 MySQL 9.0 开始提供，MySQL 8.4 LTS 不支持；省略 `n` 时默认维度为 2,048，最大为 16,383。

    1. **兼容别名（读懂旧 SQL 即可）**

        | 别名 | 实际类型 |
        | --- | --- |
        | `INT1` / `INT2` / `INT3` / `INT4` / `INT8` | `TINYINT` / `SMALLINT` / `MEDIUMINT` / `INT` / `BIGINT` |
        | `MIDDLEINT` | `MEDIUMINT` |
        | `FLOAT4` / `FLOAT8` | `FLOAT` / `DOUBLE` |
        | `CHAR BYTE` | `BINARY` |
        | `LONG VARBINARY` | `MEDIUMBLOB` |
        | `LONG VARCHAR` / `LONG` | `MEDIUMTEXT` |

        初学时优先掌握 `INT` / `BIGINT`、`DECIMAL`、`VARCHAR` / `TEXT`、`DATE` / `DATETIME` / `TIMESTAMP`、`BOOLEAN` 和 `JSON`；其他类型在遇到对应业务时再深入。

    </details>

以下知识点以 **MySQL 8.4 LTS + InnoDB** 为主；MySQL 8.0.16 开始真正执行 `CHECK` 约束。

1. **表设计与约束**

    - 表表示一类对象，行表示一条记录，列表示属性。每张表应有稳定、简短且不变的主键，业务唯一性另用 `UNIQUE` 表达。

        | 约束 | 作用 | 边界 |
        | --- | --- | --- |
        | `NOT NULL` / `DEFAULT` | 限制空值 / 提供默认值 | 默认值不会替换显式写入的 `NULL` |
        | `PRIMARY KEY` | 唯一标识每行，隐含唯一且非空 | 每张表只有一个主键，可由多列组成 |
        | `UNIQUE` | 防止非空值重复 | MySQL 允许唯一索引中存在多个 `NULL` |
        | `CHECK` | 校验行内条件 | 表达式为 `TRUE` 或含 `NULL` 导致的 `UNKNOWN` 时通过 |
        | `FOREIGN KEY` | 维护表间引用完整性 | 需明确 `ON DELETE` / `ON UPDATE` 策略，不要默认级联删除 |

    - 一对一用外键加 `UNIQUE`，一对多在“多”的一方保存外键，多对多使用包含两侧外键的中间表。
    - 使用 `utf8mb4`；先规范化，只为明确的性能或历史快照需求冗余。有外键时先建父表、后建子表，删除顺序相反。
    - 应用校验提供友好错误，数据库约束作为最终防线。`NULL` 表示未知或不存在，不是空字符串或 `0`。

1. **数据操作与查询**

    - `INSERT` 显式写列名并限制单批大小；`SELECT` 只取所需列；`UPDATE` / `DELETE` 必须明确 `WHERE` 并检查受影响行数。
    - 查询语义可按 `FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT` 理解，但这不是数据库的实际执行顺序。
    - `LEFT JOIN` 右表的筛选条件通常放在 `ON`；`WHERE` 过滤分组前的行，`HAVING` 过滤聚合后的结果。
    - 空值用 `IS NULL` / `IS NOT NULL` 判断。能用单条条件 `UPDATE` 时不要先查再改；物理删除前确认审计与恢复要求。

1. **索引与 `EXPLAIN`**

    - InnoDB 普通索引通常使用 B+Tree。数据按主键组织在聚簇索引中，二级索引记录会携带主键值，因此主键宜短、稳定；索引越多，写入和存储成本越高。
    - 复合索引遵循最左前缀，列顺序由过滤、排序和数据分布决定。查询列全在索引中可避免回表。
    - 前导通配符、隐式类型转换和对索引列运算可能导致索引利用率下降。
    - `EXPLAIN` 重点看 `type`、`key`、`rows`、`filtered` 和 `Extra`；`EXPLAIN ANALYZE` 会实际执行查询，使用前评估开销。
    - 优化遵循“复现 -> 查看计划 -> 小幅调整 -> 复测”；深分页优先基于上一页的排序字段和唯一 ID 继续查询。

1. **事务、隔离级别与锁**

    - 事务保证 ACID（原子性、一致性、隔离性、持久性）。MySQL 默认自动提交；多步需要共同成败时显式开启事务。DDL（Data Definition Language，数据定义语言：操作的是库/表/索引等结构，不是普通业务行数据） 通常会隐式提交，不能当成普通 DML（Data Manipulation Language，数据操纵语言：操作的是表里的数据，不改表结构本身） 回滚。

        | 隔离级别 | 核心表现 |
        | --- | --- |
        | `READ UNCOMMITTED` | 可能读到未提交数据，业务中很少使用 |
        | `READ COMMITTED` | 每次一致性读看到当时已提交的数据 |
        | `REPEATABLE READ` | InnoDB 默认级别；同一事务的一致性读通常复用快照 |
        | `SERIALIZABLE` | 隔离最强，并发成本最高 |

    - 脏读、不可重复读和幻读分别是读到未提交值、同一行两次读取不同、同一条件的记录集变化。
    - MVCC 用 Read View 判断快照可见性，undo log 支持回滚和旧版本读取；长事务会阻碍旧版本清理。
    - `SELECT ... FOR UPDATE` 必须在明确事务中。锁范围由扫描的索引决定；事务应短小、按固定顺序访问数据，且不包含远程调用。
    - 乐观锁用 `version` 检测冲突。死锁重试必须重跑整个事务，并设置上限、退避与幂等保护。

1. **Java 访问 MySQL**

    - 访问链路：`DataSource/连接池 -> Connection -> PreparedStatement/MyBatis -> ResultSet/对象映射 -> Service 事务`。

        | MySQL | Java | 注意 |
        | --- | --- | --- |
        | `DECIMAL` | `BigDecimal` | 金额指定精度和舍入规则；数值比较通常用 `compareTo` |
        | `INT` / `BIGINT` | `Integer` / `Long` | 可空列使用包装类；`BIGINT UNSIGNED` 的上界超过 Java `long` |
        | `DATE` / `DATETIME` / `TIMESTAMP` | `LocalDate` / `LocalDateTime` / `Instant` | `DATETIME` 不带时区；绝对时间点统一用 UTC |
        | `JSON` | `String` 或领域对象 | 统一序列化和演进规则；高频查询字段优先拆成普通列 |

    - SQL 值使用参数绑定；MyBatis 的 `${}` 是文本替换，只能接收白名单映射后的标识符。
    - [连接池原理与 Java 用法](../Java学习笔记/README.md#jdbc-与数据库访问演进)见 Java 学习笔记；数据库侧按“每实例连接池最大连接数 × 应用实例数 + 其他客户端连接”核算总量；结果应低于数据库的最大连接数，并为运维和故障处理预留余量。
    - Spring `@Transactional` 通常不会传播到新线程；跨数据库与 HTTP/MQ 的一致性需依靠 outbox、重试和消费幂等。

1. **生产可靠性：复制、迁移、备份与监控**

    - redo log 用于 InnoDB 崩溃恢复，binlog 用于复制和时间点恢复；两者都不能替代备份。
    - 复制默认异步，副本也会复制误删。强一致读走主库或等待目标 GTID，事务内不要切换到副本。
    - 应用账号使用最小权限和 TLS，密码不写入代码或日志。DDL 由迁移工具管理，大表变更提前评估锁、磁盘和复制延迟。
    - 备份需要明确范围、保留期和恢复目标，并定期恢复到隔离环境验证。
    - 监控连接等待、慢 SQL、扫描行数、锁等待、I/O 和复制延迟；先定位 SQL/事务并检查执行计划，再考虑扩容或分库分表。

### PostgreSQL

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

---

## NoSQL 数据库

NoSQL 不是一种固定的数据模型，而是键值、文档、列族、图等非关系型数据库的统称。本节只介绍 MongoDB 和 Redis。

### MongoDB

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

### Redis

Redis 是主要在内存中读写的 NoSQL 键值数据库。它不仅保存字符串，还提供多种数据结构和原子命令，常用于缓存、会话、计数器、排行榜、限流和消息处理。

- 常用数据结构：

    | 数据结构 | 特点 | 常见用途 |
    | --- | --- | --- |
    | String | 字符串、数字或二进制数据 | 缓存值、计数器、状态标记 |
    | Hash | 一个 key 下保存多个字段和值 | 用户信息、对象属性 |
    | List | 按插入顺序排列的字符串序列 | 简单队列、时间线 |
    | Set | 无序且不重复的字符串集合 | 标签、去重、交集和并集 |
    | Sorted Set | 成员不重复，并按分数排序 | 排行榜、按时间或优先级排序 |
    | Stream | 只追加的消息流，支持消费组和待处理消息 | 事件流、需要确认和重试的消息处理 |

    数据结构应匹配操作方式，不要把所有对象都序列化成大字符串。计数优先用 `INCR`（Redis里对String做原子递增的命令），集合运算使用 Set，排名使用 Sorted Set；需要可靠消费语义时再考虑 Stream。

- **原子操作、Pipeline、事务与脚本**

    >**原子**（并发视角）：对 Redis 单条命令而言，某次操作在服务端执行时不可分割——要么整步完成，要么不算完成；执行过程中不会被其他客户端的命令插队打断。它强调“不被插队”，不等于多步操作失败后自动回滚，也不等于数据已持久化。

    | 机制 | 解决的问题 | 边界 |
    | --- | --- | --- |
    | 单条命令 | 原子地完成一次数据结构操作 | 先查再改的多条命令仍可能被其他客户端穿插 |
    | Pipeline | 一次发送多条命令，减少网络往返 | 不是事务，不保证整批命令原子执行 |
    | [`MULTI` / `EXEC`](https://redis.io/docs/latest/develop/using-commands/transactions/) | 将一组命令排队后连续执行 | 运行期错误不会自动回滚已成功的命令；可配合 `WATCH` 做乐观并发控制 |
    | [Lua 脚本 / Redis Functions](https://redis.io/docs/latest/develop/programmability/) | 在服务端原子执行条件判断和多步操作 | 执行期间会阻塞其他活动，脚本必须短小且可控 |

    | 对比项 | Redis 原子操作 / 事务 | 关系型数据库事务 |
    | --- | --- | --- |
    | 基本保证 | 单条命令原子执行；`MULTI` / `EXEC` 中的命令按顺序连续执行，期间不被其他客户端插入 | 多条 SQL 组成一个事务，最终提交或回滚 |
    | 执行错误 | `EXEC` 后某条命令报错，其他命令仍会继续，已成功的命令不回滚 | 可用 `ROLLBACK` 撤销未提交事务的修改，并可用保存点部分回滚 |
    | 并发控制 | `WATCH` 在监视的 key 被修改后让 `EXEC` 放弃执行，由客户端重试 | 通过隔离级别、锁和 MVCC 等机制允许多事务并发执行 |
    | 持久性 | 取决于 RDB / AOF 及其配置，不是“原子执行”自带的保证 | 是 ACID 中的独立目标；实际强度受数据库引擎与持久化配置影响 |

    >一句话区分：Redis 更强调“这组命令执行时不被插队”；关系型数据库事务还提供“失败后回滚”和可配置的隔离级别。回滚以事务型存储引擎和可事务化语句为前提；MySQL 部分 DDL 会隐式提交。

- **过期、内存与持久化**

    - TTL 触发“过期”，内存达到 `maxmemory` 后按 `maxmemory-policy` 触发“淘汰”；过期 key 不保证到期瞬间立即释放。
    - 缓存实例应配置合理的 TTL、内存上限和淘汰策略；使用 `noeviction` 时，达到上限后新增数据的写命令可能报错。
    - RDB 保存时间点快照，AOF 记录并重放写命令；前者更紧凑，后者通常保留更多最近写入但成本更高。
    - Redis 可使用 RDB、AOF、两者组合或关闭持久化；任何配置都不能代替独立备份和恢复演练。

- **缓存风险与大 key**

    | 问题 | 含义 | 常用处理 |
    | --- | --- | --- |
    | 缓存雪崩 | 大量 key 在短时间内同时失效，请求集中转向数据库 | 错开过期时间并加入随机值、缓存预热、限流或降级 |
    | 缓存穿透 | 缓存和数据库都没有目标数据，重复请求持续查询数据库 | 参数校验、布隆过滤器、短时间缓存空结果 |
    | 缓存击穿 | 某个热点 key 失效时，大量并发请求同时查询数据库 | 互斥更新、逻辑过期、提前刷新热点数据 |
    | 缓存污染 | 低频或仅访问一次的数据长期占用内存 | 设置合理的 TTL、`maxmemory` 和淘汰策略 |
    | 热 key | 请求集中到单个 key，压满实例或分片 | 本地缓存、请求合并、限流或拆分 key |
    | 大 key | 单个值或集合过大，放大网络、删除和迁移成本 | 用 `MEMORY USAGE`、`--bigkeys` 排查，按业务拆分并用 `UNLINK` 或分批删除 |

    监控至少覆盖命中率、内存、淘汰与过期量、命令延迟、网络流量和复制状态；全量扫描应避开高峰。

- **缓存一致性与 Cache Aside**

    由 MySQL 保存事实数据、Redis 缓存热点结果时，常用 Cache Aside：读取先查 Redis，未命中再查 MySQL 并回填带 TTL 的缓存；更新先提交 MySQL，再删除缓存，让后续读取重新加载。

    该模式只能缩短不一致窗口，不能天然保证强一致。删除失败要有重试或异步补偿；热点失效要限制并发回源；对余额、库存等强一致读取，应直接查询事实数据或使用更明确的一致性方案。

- **分布式锁**

    简单互斥可使用 `SET 「lockKey」 「唯一令牌」 NX PX 「超时毫秒」`。解锁必须原子地“比较令牌后再删除”，避免误删其他请求后来取得的锁；可用短 Lua 脚本或成熟客户端实现。锁超时、业务执行过久、网络分区和进程暂停仍可能破坏互斥，需要续期或 fencing token 时应使用经过验证的方案，不能只靠一个 `SETNX`。

- **复制与高可用**

    | 方案 | 作用 | 需要注意 |
    | --- | --- | --- |
    | 主从复制 | 提供数据副本和读扩展基础 | 默认异步，复制本身不负责自动故障转移 |
    | Sentinel | 为非 Cluster 部署提供监控、服务发现和自动故障转移 | 客户端必须支持 Sentinel；故障期间不保证所有已确认写入都保留 |
    | Redis Cluster | 通过多个主分片扩展容量和吞吐，并结合副本故障转移 | 客户端需支持 Cluster，跨槽多 key 操作受限，扩缩容和故障处理更复杂 |

    高可用不等于不丢数据，也不等于备份。部署前应明确允许的数据丢失窗口，并演练故障转移、客户端重连和数据恢复。

---

### 选型总结

- 四种数据库的横向对比：

    | 维度 | MySQL | PostgreSQL | MongoDB | Redis |
    | --- | --- | --- | --- | --- |
    | 核心模型 | 关系表 | 关系表、丰富类型 | BSON 文档 | 键值与数据结构 |
    | 查询方式 | SQL、关联与聚合 | SQL、复杂查询与扩展 | 文档查询、聚合管道 | 按 key 和数据结构命令访问 |
    | 事务与约束 | 成熟，适合核心业务 | 成熟，标准 SQL 能力丰富 | 单文档原子，多文档事务按需使用 | 单命令原子，事务不提供关系库式回滚 |
    | 典型用途 | 用户、订单、支付、库存 | 复杂 SQL、地理/扩展类型、特定扩展 | 内容、配置、商品属性、事件 | 缓存、会话、计数、排行、限流、消息流 |
    | 主要代价 | 复杂查询和大规模扩展仍需设计 | 运维和特性使用需要对应经验 | 文档建模、约束和分片键需要设计 | 内存成本、数据淘汰与异步复制风险 |

- 选型时依次确认：

    1. 数据是关系表、完整文档，还是短期键值状态？
    2. 是否需要跨记录事务、外键约束、复杂关联或强一致读取？
    3. 主要访问路径、数据规模、恢复目标和团队运维能力是什么？
    4. 现有数据库是否已经满足需求？能满足就不要为单个功能增加一种数据库。

- 多数常规 Web 业务可先用 MySQL 或 PostgreSQL 保存事实数据；有明确热点和可接受的短暂不一致时，再用 Redis 加速。MongoDB 适合独立且天然呈文档形态的数据，不应只因为字段可能变化就引入。
