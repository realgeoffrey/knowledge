# 数据库使用

## 目录


1. [MySQL服务安装、启动与连接](#mysql服务安装启动与连接)
1. [PostgreSQL服务安装、启动与连接](#postgresql服务安装启动与连接)
1. [MongoDB服务安装、启动与连接](#mongodb服务安装启动与连接)
1. [Redis服务安装、启动与连接](#redis服务安装启动与连接)
1. [关系型数据库](#关系型数据库)

    1. [MySQL](#mysql)
    1. [PostgreSQL](#postgresql)
1. [NoSQL 数据库](#nosql-数据库)

    1. [MongoDB](#mongodb)
    1. [Redis](#redis)
1. [选型总结](#选型总结)

---

数据库是用于持久化、组织和查询数据的软件。广义的数据库既包括使用表和 SQL 的关系型数据库，也包括键值、文档等 NoSQL 数据库，因此 Redis 也属于数据库。

| 数据库 | 类型 | 数据组织方式 |
| --- | --- | --- | --- |
| MySQL | 关系型数据库 | 表、行、列 |
| PostgreSQL | 关系型数据库 | 表、行、列，并支持丰富的类型和扩展 |
| MongoDB | NoSQL 文档数据库 | BSON 文档、集合 |
| Redis | NoSQL 键值数据库 | 内存中的键和多种数据结构 |

关系型数据库适合结构稳定、关联和事务要求明确的数据；NoSQL 是多种非关系型数据模型的统称，通常针对特定访问方式简化存储和查询。两者不是替代关系，一个系统可以同时使用多种数据库。

## 服务安装、启动与连接

以下命令以 macOS 和 Homebrew 为例。先启动数据库服务，再使用对应客户端连接。

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

>`DROP`、`DELETE`、`UPDATE` 等语句会修改或删除数据。执行前先备份并确认当前环境、对象名称和 `WHERE` 条件；授权时遵循最小权限原则，`ALL PRIVILEGES` 仅用于明确需要完全管理权限的场景。

```sql
-- 查看、创建、删除和切换数据库
SHOW DATABASES;
CREATE DATABASE 「数据库名」 DEFAULT CHARACTER SET utf8mb4;
DROP DATABASE 「数据库名」;
SELECT DATABASE();
USE 「数据库名」;

-- 查看和修改表
SHOW TABLES;
DESCRIBE 「表名」;                    -- 等价于 SHOW COLUMNS FROM 「表名」;
SHOW FULL COLUMNS FROM 「表名」;      -- 额外显示权限、注释等信息
CREATE TABLE 「表名」 (「字段」 「类型」);
DROP TABLE 「表名」;
RENAME TABLE 「原表名」 TO 「新表名」;
ALTER TABLE 「表名」 「修改内容」;

-- 增删改查数据
SELECT * FROM 「表名」 WHERE 「条件」;
INSERT INTO 「表名」 (「字段」) VALUES (「值」);
UPDATE 「表名」 SET 「字段」 = 「值」 WHERE 「条件」;
DELETE FROM 「表名」 WHERE 「条件」;

-- 查看、创建、授权和删除用户
SELECT User, Host FROM mysql.user;
SHOW GRANTS;  -- 查看当前用户的权限
CREATE USER '「用户名」'@'「主机」' IDENTIFIED BY '「密码」';
GRANT 「所需最小权限，如 SELECT, UPDATE」 ON 「数据库名 或 *」.「表名 或 *」 TO '「用户名」'@'「主机」';
REVOKE 「要撤销的权限，如 UPDATE」 ON 「数据库名 或 *」.「表名 或 *」 FROM '「用户名」'@'「主机」';
DROP USER '「用户名」'@'「主机」';
```

>MySQL 中 `DATABASE` 与 `SCHEMA` 基本同义；连接后可用 `USE 「数据库名」;` 切换当前数据库。

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

>`DROP` 会删除对象，执行前先备份并确认当前环境和对象名称。`SUPERUSER` 可绕过常规权限检查，仅在明确需要时使用；通常应创建普通用户并按需授权。

```text
-- 查看数据库列表
\l
-- 创建数据库；shell 中可用：createdb my_test_db
CREATE DATABASE my_test_db;
-- 删除数据库；shell 中可用：dropdb my_test_db
DROP DATABASE my_test_db;
-- 查看和切换当前数据库
SELECT current_database();
\c my_test_db
-- 模式属于当前数据库，不能通过「数据库名.模式名」跨库创建
CREATE SCHEMA IF NOT EXISTS "模式名";
-- 只能直接删除空模式；若包含对象，需先删除对象或按需使用 CASCADE
DROP SCHEMA "模式名";

-- 查看用户列表；\du+ 额外展示描述
\du
-- 创建普通用户；shell 中可用：createuser -U "$(whoami)" -P 用户名
CREATE USER 用户名 WITH PASSWORD '密码';
-- 创建超级用户；用 \h CREATE USER 查看所有选项
CREATE USER 用户名 WITH SUPERUSER PASSWORD '密码';
-- 删除用户；shell 中可用：dropuser -U "$(whoami)" 用户名
DROP USER 用户名;
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
show collections

db.「集合名」.insertOne({ 「字段名」: 「值」 })
db.「集合名」.find({ 「字段名」: 「值」 }).sort({ 「排序字段」: -1 }).limit(「数量」)
db.「集合名」.countDocuments({ 「字段名」: 「值」 })
db.「集合名」.updateOne({ 「查询条件」 }, { $set: { 「字段名」: 「新值」 } })
db.「集合名」.deleteOne({ 「查询条件」 })
```

>`updateOne()` 和 `deleteOne()` 会修改数据，执行前先用同一查询条件运行 `find()` 确认目标文档。

### [Redis](https://redis.io/docs/latest/)服务安装、启动与连接

```shell
# 1. 安装
brew install redis      # 安装 Redis

# 2. 启动服务
# 后台运行：start 会立即启动并注册为登录时自动启动；run 只启动本次，不注册为登录时自动启动
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
redis-cli -a 「密码」 ping     # 带密码；也可用 -u 见下
# URL 形式：redis://[:密码@]主机:端口[/逻辑库序号]
redis-cli -u 'redis://:「密码」@「地址」:「端口」/「逻辑库序号」' ping
redis-cli INFO server          # 看版本、uptime 等；确认连的是哪台实例
```

>进入 `redis-cli` 后，可直接执行 Redis 命令；`HELP 「命令」` 查看帮助，`QUIT` 退出。

```text
SET 「key」 「value」
SET 「key」 「value」 EX 「秒数」 NX
GET 「key」
DEL 「key1」 「key2」
EXISTS 「key」
TTL 「key」
SCAN 0 MATCH '「匹配模式，如 user:*」' COUNT 「数量」
```

>`NX` 表示仅在 key 不存在时写入，`XX` 表示仅在 key 已存在时写入；`EX` 和 `PX` 分别以秒和毫秒设置过期时间。遍历键时将 `SCAN` 返回的游标传入下一次调用，直到游标再次为 `0`；生产环境避免使用可能长时间阻塞服务的 `KEYS *`。

## 关系型数据库

### MySQL

MySQL 是关系型数据库管理系统。一个 MySQL 服务可包含多个数据库（`DATABASE` 与 `SCHEMA` 在 MySQL 中基本同义）；数据库由表组成，约束保证数据规则，索引加快查询，SQL 用来读写和管理数据。

后端访问链路：`页面 -> HTTP API -> Controller -> Service -> Mapper/JDBC -> MySQL`。前端不应直接连接数据库。

学习主线：

- 基础：`表与约束 -> CRUD -> JOIN/聚合 -> 索引 -> 事务 -> Java 集成`
- 进阶：`执行计划 -> 并发与幂等 -> 连接池 -> 读写一致性 -> 生产诊断与容灾`

以下示例面向 **MySQL 8.0.16+**，该版本开始真正执行 `CHECK` 约束。

先在系统终端连接，再在 `mysql>` 提示符后执行 SQL：

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

```sql
SHOW DATABASES; -- SHOW SCHEMAS; 是同义写法
```

1. **表设计与约束**

    用用户、商品、订单和订单明细组成最小商城模型。建表顺序必须先主表、后引用它的子表。

    ```sql
    CREATE DATABASE shop
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_0900_ai_ci;
    USE shop;

    CREATE TABLE users (
        id BIGINT NOT NULL AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL,
        nickname VARCHAR(64) NOT NULL,
        created_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
        PRIMARY KEY (id),
        UNIQUE KEY uk_users_email (email)
    ) ENGINE=InnoDB;

    CREATE TABLE products (
        id BIGINT NOT NULL AUTO_INCREMENT,
        sku VARCHAR(64) NOT NULL,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        stock INT UNSIGNED NOT NULL DEFAULT 0,
        status TINYINT UNSIGNED NOT NULL DEFAULT 1,
        PRIMARY KEY (id),
        UNIQUE KEY uk_products_sku (sku),
        CONSTRAINT chk_products_price CHECK (price >= 0),
        CONSTRAINT chk_products_status CHECK (status IN (0, 1))
    ) ENGINE=InnoDB;

    CREATE TABLE orders (
        id BIGINT NOT NULL AUTO_INCREMENT,
        order_no VARCHAR(32) NOT NULL,
        user_id BIGINT NOT NULL,
        status VARCHAR(16) NOT NULL DEFAULT 'PENDING',
        total_amount DECIMAL(12,2) NOT NULL,
        version INT UNSIGNED NOT NULL DEFAULT 0,
        created_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
        PRIMARY KEY (id),
        UNIQUE KEY uk_orders_order_no (order_no),
        KEY idx_orders_user_created (user_id, created_at, id),
        CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users (id),
        CONSTRAINT chk_orders_total CHECK (total_amount >= 0)
    ) ENGINE=InnoDB;

    CREATE TABLE order_items (
        id BIGINT NOT NULL AUTO_INCREMENT,
        order_id BIGINT NOT NULL,
        product_id BIGINT NOT NULL,
        product_name VARCHAR(255) NOT NULL,
        unit_price DECIMAL(10,2) NOT NULL,
        quantity INT UNSIGNED NOT NULL,
        line_amount DECIMAL(12,2) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE KEY uk_order_items_order_product (order_id, product_id),
        KEY idx_order_items_product (product_id),
        CONSTRAINT fk_order_items_order FOREIGN KEY (order_id)
            REFERENCES orders (id) ON DELETE CASCADE,
        CONSTRAINT fk_order_items_product FOREIGN KEY (product_id)
            REFERENCES products (id),
        CONSTRAINT chk_order_items_quantity CHECK (quantity > 0),
        CONSTRAINT chk_order_items_amount CHECK (line_amount >= 0)
    ) ENGINE=InnoDB;
    ```

    ```sql
    SHOW TABLES;
    SHOW CREATE TABLE products;
    DESCRIBE products;
    ```

    | 需求 | 优先选择 | 关键点 |
    | --- | --- | --- |
    | ID、计数 | `BIGINT` / `INT` | 按真实范围选择 |
    | 金额 | `DECIMAL(p,s)` | 结算不要使用 `FLOAT` / `DOUBLE` |
    | 短文本 | `VARCHAR` | 长度是数据边界，不只是前端校验 |
    | 长文本 | `TEXT` | 索引方式和长度受限制 |
    | 时间 | `DATETIME` / `TIMESTAMP` | 明确时区和传输格式 |
    | 半结构化数据 | `JSON` | 不替代稳定、常查询的关系型列 |
    | 必填、唯一、关联 | `NOT NULL`、`UNIQUE`、`FOREIGN KEY` | 数据库约束是最终防线 |

    关系型数据库的关联通常这样落表：

    | 关系 | 常见建模方式 | 本例 |
    | --- | --- | --- |
    | 一对一 | 外键加 `UNIQUE`；生命周期完全一致时也可合并为一张表 | 用户与用户详情（本例未拆分） |
    | 一对多 | 在“多”的一方保存外键 | `users -> orders` |
    | 多对多 | 用中间表保存两侧外键，并根据业务加联合唯一约束 | `orders <-> products`，中间表为 `order_items` |

    - `utf8mb4` 可保存完整 Unicode；排序规则决定比较、排序及大小写/重音敏感性。
    - 表设计通常先减少重复存储；订单明细保存商品名和成交单价快照，是为了避免商品改名或调价后旧订单失真的有意冗余。
    - Java 校验负责尽早返回友好错误，数据库约束负责阻止绕过应用或并发造成的非法数据。
    - `NULL` 表示未知或不存在，不要用空字符串或 `0` 冒充。

1. **高频 SQL：增、查、改、关联与聚合**

    ```sql
    INSERT INTO users (email, nickname)
    VALUES ('alice@example.com', 'Alice');

    INSERT INTO products (sku, name, price, stock)
    VALUES ('BOOK-JAVA-001', 'Java 入门', 59.90, 100);

    SELECT id, name, price, stock
    FROM products
    WHERE status = 1 AND price BETWEEN 50.00 AND 100.00
    ORDER BY id DESC
    LIMIT 20;
    ```

    条件扣库存应合并为一条原子更新，并检查受影响行数：`1` 表示成功，`0` 表示商品不存在、不可售或库存不足。

    ```sql
    UPDATE products
    SET stock = stock - ?
    WHERE id = ? AND status = 1 AND stock >= ?;
    ```

    业务数据通常用状态实现逻辑删除；只有明确不再需要且已确认外键、审计和恢复要求时，才执行物理 `DELETE`。

    `JOIN` 组合关联表，`GROUP BY` 聚合，`HAVING` 筛选聚合结果。要保留左表全部行时，右表筛选条件通常放在 `ON`，否则可能把 `LEFT JOIN` 意外变成 `INNER JOIN`。

    ```sql
    SELECT u.id,
           u.nickname,
           COUNT(o.id) AS paid_order_count,
           COALESCE(SUM(o.total_amount), 0) AS paid_total
    FROM users AS u
    LEFT JOIN orders AS o
        ON o.user_id = u.id AND o.status = 'PAID'
    GROUP BY u.id, u.nickname
    HAVING COUNT(o.id) > 0;
    ```

    查询结果可按 `FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT` 理解（不代表实际执行顺序）。`WHERE` 过滤行，`HAVING` 过滤分组；没有 `ORDER BY` 时返回顺序不确定。

    判断空值用 `IS NULL`，不要写 `= NULL`；查询只取需要的列，避免无边界的 `SELECT *`。CTE、窗口函数、子查询和集合操作可在掌握上述主线后再学。

1. **索引与 `EXPLAIN`**

    InnoDB 普通索引通常使用 B+Tree。数据按主键组织在聚簇索引中，二级索引记录会携带主键值，因此主键宜短、稳定；索引越多，写入和存储成本越高。

    复合索引 `idx_orders_user_created (user_id, created_at, id)` 对应“查询某用户最近订单”：

    ```sql
    EXPLAIN
    SELECT id, order_no, total_amount, created_at
    FROM orders
    WHERE user_id = 1
    ORDER BY created_at DESC, id DESC
    LIMIT 20;
    ```

    - 复合索引优先利用最左前缀；跳过 `user_id` 只查 `created_at`，通常不能高效利用该索引的顺序。
    - 索引列顺序应由真实查询的过滤、排序和数据分布决定，不要机械套规则。
    - 查询所需列都在索引中称为覆盖索引；否则通常需要根据二级索引中的主键回表。
    - 前导通配符、隐式类型转换、对索引列套表达式等，都可能降低索引利用率；最终以执行计划和实测为准。

    | `EXPLAIN` 列 | 重点 |
    | --- | --- |
    | `type` | 访问方式；`ALL` 表示全表扫描，但不等于一定有问题 |
    | `key` | 实际选择的索引 |
    | `key_len` | 本次使用的索引键长度，可辅助判断复合索引利用范围 |
    | `rows` / `filtered` | 估计扫描行数与过滤比例，不是实际值 |
    | `Extra` | 额外操作，如排序、临时表、索引条件下推 |

    MySQL 8.0.18+ 的 `EXPLAIN ANALYZE` 会真正执行查询并显示实际时间、行数和循环次数，生产环境使用前必须评估查询成本与资源影响。

    优化顺序：`用代表性参数复现 -> 看执行计划 -> 减少扫描行和返回列 -> 只调整一个索引或一处 SQL -> 复测接口耗时`。不要同时乱改 SQL、索引和服务器参数。

    高级排查关注“估算”与“实际”的差异：

    - 估算行数偏差大：检查参数分布和统计信息，再评估 `ANALYZE TABLE` 或直方图。
    - 同一 SQL 耗时差异大：对比真实参数、锁等待、返回行数和 P95/P99。
    - 删除冗余索引：先设为不可见并观测；它仍占空间且有写入成本。
    - 优化器未选预期索引：先修正 SQL、索引和统计信息，`FORCE INDEX` 只作有回归测试的最后手段。

1. **分页与批量处理**

    `LIMIT offset, size` 简单，但深分页仍要跳过大量记录。连续翻页可用上一页最后一条记录作为游标：

    ```sql
    SELECT id, order_no, total_amount, created_at
    FROM orders
    WHERE user_id = ?
      AND (created_at < ?
           OR (created_at = ? AND id < ?))
    ORDER BY created_at DESC, id DESC
    LIMIT 20;
    ```

    游标分页适合“继续下一页”，不适合直接跳到任意页；具体索引利用情况仍要用 `EXPLAIN` 验证。批量写入应拆成可观测、可重试的批次，限制单批行数和事务时长，并观察锁等待、复制延迟和接口延迟。

1. **事务、隔离级别与锁**

    事务把多条 SQL 组成一个业务整体。ACID 分别是原子性、一致性、隔离性和持久性。MySQL 默认开启自动提交；需要多步一起成功或失败时，显式开启事务。

    下面是应用层伪 SQL，`?` 由 JDBC / MyBatis 绑定：

    ```sql
    START TRANSACTION;

    UPDATE products
    SET stock = stock - ?
    WHERE id = ? AND status = 1 AND stock >= ?;
    -- 应用检查受影响行数，不是 1 就 ROLLBACK

    INSERT INTO orders (order_no, user_id, total_amount)
    VALUES (?, ?, ?);

    INSERT INTO order_items
        (order_id, product_id, product_name, unit_price, quantity, line_amount)
    VALUES (LAST_INSERT_ID(), ?, ?, ?, ?, ?);

    COMMIT;
    ```

    任一步失败都应回滚；重试还要依靠唯一订单号等约束保证幂等。价格、名称和状态必须由服务端在事务内读取并校验，不能信任客户端提交的价格或总额。

    | 隔离级别 | 核心表现 |
    | --- | --- |
    | `READ UNCOMMITTED` | 可能读到未提交数据，业务中很少使用 |
    | `READ COMMITTED` | 每次一致性读看到当时已提交的数据 |
    | `REPEATABLE READ` | InnoDB 默认级别；同一事务的一致性读通常复用快照 |
    | `SERIALIZABLE` | 隔离最强，并发成本最高 |

    “脏读”是读到其他事务未提交的值；“不可重复读”是同一事务内两次读取同一行得到不同值；“幻读”是同一条件两次查询得到的记录集合发生变化。具体表现还取决于一致性读、当前读和加锁方式。

    - 普通 `SELECT` 通常读取 MVCC 快照；`UPDATE`、`DELETE`、`SELECT ... FOR UPDATE` 读取当前版本并加锁。
    - 能用单条条件 `UPDATE` 原子判断时，不要“先查再改”。
    - 唯一索引等值命中通常只锁记录；`REPEATABLE READ` 下的范围/非唯一索引可能使用 next-key lock（记录锁 + gap lock）。锁范围取决于扫描的索引，不是返回行数。
    - `SELECT ... FOR UPDATE` 必须放在明确事务中。事务应按固定顺序访问数据，且不包含远程调用或长时间计算。

    多个请求可能同时修改订单时，可用 `version` 实现乐观锁：

    ```sql
    UPDATE orders
    SET status = ?, version = version + 1
    WHERE id = ? AND version = ? AND status = ?;
    ```

    影响行数为 `0` 表示数据已变，应重新读取后重试或返回冲突。

    死锁出现时，InnoDB 会回滚其中一个事务。降低死锁的方法：所有流程按一致顺序更新表和行、缩短事务、使用合适索引。应用应对可重试错误重跑**整个事务**，设置次数上限和退避，并保证幂等；可用 `SHOW ENGINE INNODB STATUS` 查看最近一次死锁信息。

1. **Java 访问 MySQL**

    职责链：`DataSource/连接池 -> Connection -> PreparedStatement/MyBatis -> ResultSet/对象映射 -> Service 事务`。

    **类型映射**

    | MySQL | Java | 注意 |
    | --- | --- | --- |
    | `DECIMAL` | `BigDecimal` | 金额指定精度和舍入规则；数值比较通常用 `compareTo` |
    | `INT` / `BIGINT` | `Integer` / `Long` | 可空列使用包装类；`BIGINT UNSIGNED` 的上界超过 Java `long` |
    | `DATE` / `DATETIME` / `TIMESTAMP` | `LocalDate` / `LocalDateTime` / `Instant` | `DATETIME` 不带时区；绝对时间点统一用 UTC |
    | `JSON` | `String` 或领域对象 | 统一序列化和演进规则；高频查询字段优先拆成普通列 |

    **JDBC 与 MyBatis**

    - SQL 值使用参数绑定；MyBatis 的 `#{userId}` 是绑定参数，`${orderBy}` 是文本替换，只能接收经过白名单映射的表名、列名或排序方向。
    - `Connection`、`Statement`、`ResultSet` 必须由 `try-with-resources` 或框架关闭；连接池的 `close()` 通常表示归还连接。
    - 流式读取需正确配置 Connector/J `fetchSize` 和服务端预编译，且读完前不能归还连接。
    - 批量写入使用 `executeBatch()` / MyBatis `BATCH`，控制批次和事务时长；驱动优化参数需经过压测和语义校验。
    - MyBatis `fetchSize` 和 `timeout` 最终依赖 JDBC 驱动；二级缓存需显式评估失效与多实例一致性。

    **连接池与事务边界**

    - 按“单实例池大小 × 应用实例数”核算总连接，再根据 active/idle/pending/timeout 和数据库并发指标压测；连接池不是越大越快。
    - HikariCP 的 `maxLifetime` 应略短于基础设施连接寿命，且 `keepaliveTime < maxLifetime`。获取连接、SQL、事务和 HTTP 超时应分层设置。
    - Spring `@Transactional` 通常绑定当前线程和连接，不会自动传播到新线程；死锁重试应开启完整的新事务。
    - MySQL 事务不能保证 HTTP/MQ 同时成功；可用本地 outbox、异步投递和消费端幂等实现最终一致性。

1. **复制、读写分离与故障切换**

    - MySQL 复制默认异步。强一致读应走主库或等待目标 GTID 在副本执行，不用固定 `sleep` 猜延迟。
    - 路由必须感知事务：同一本地事务内的读写使用同一数据源和连接，不在事务中途把查询切到副本。
    - GTID 简化副本定位和故障切换，但不代替幂等、流量切换和旧主库隔离。半同步只保证日志已被副本接收，不代表已应用且可查。
    - 连接中断后 `COMMIT` 结果可能未知；重试前用幂等键、唯一约束或状态查询确认结果。

1. **安全、迁移、备份与监控**

    - 应用账号遵循最小权限；迁移账号与应用账号分开。连接使用 TLS，密码通过密钥管理或环境注入，日志不要记录密码、令牌和敏感参数。
    - 用 Flyway 或 Liquibase 管理可审查、可重复的 DDL。MySQL 大多数 DDL 会隐式提交，不能依赖业务事务的 `ROLLBACK` 撤销；破坏性变更应准备回退或恢复方案。
    - 生产结构变更宜按“先增加兼容字段/索引 -> 分批迁移数据并部署新代码 -> 确认旧代码停用后再删除旧结构”进行。大表 `ALTER TABLE` 前要评估执行算法、元数据锁、额外磁盘空间和复制延迟；即使是在线 DDL，也可能被长事务阻塞。
    - 副本不是备份，它也会复制误删。备份只有经过恢复演练才算可用；时间点恢复还依赖连续的二进制日志。下面的 `--single-transaction` 适用于 InnoDB 等事务表，导出期间应避免 DDL。

    ```bash
    mysqldump --single-transaction --routines --triggers shop > shop.sql

    # 仅恢复到预先创建的隔离测试库
    mysql shop_restore < shop.sql
    ```

    生产排障要从应用现象下钻到数据库证据：

    | 现象 | 应用侧先看 | MySQL 侧先看 |
    | --- | --- | --- |
    | 接口慢 | P50/P95/P99、具体 SQL 标识、返回行数 | `sys.statement_analysis`、`performance_schema.events_statements_summary_by_digest`、慢日志和 `EXPLAIN ANALYZE` |
    | 连接获取超时 | 池的 active/idle/pending/timeout、持有时长 | 当前连接/运行线程、慢 SQL、长事务；不先调大连接池 |
    | 锁等待或死锁 | 事务入参、SQL 顺序、重试次数 | `performance_schema.data_lock_waits`、`INFORMATION_SCHEMA.INNODB_TRX`、`SHOW ENGINE INNODB STATUS` |
    | DDL 长时间卡住 | 发布批次、迁移工具状态 | `sys.schema_table_lock_waits`、`performance_schema.metadata_locks`、未提交长事务 |
    | 副本读到旧值 | 读写路由、业务一致性级别 | 接收/应用线程、GTID 执行位置、复制延迟与错误 |

    - 监控连接池等待、P95/P99、扫描/返回行数、锁等待、I/O 和复制延迟。
    - 先修查询、索引和事务，再根据实测考虑读副本、分区或分库分表。

1. **常见错误与完成检查**

    常见错误：

    - 数据：拼接输入、金额用浮点数、漏唯一约束、忽略受影响行数。
    - 性能：无边界 `SELECT *`、N+1 查询、深分页、过度建索引、连接池盲目调大。
    - 可靠性：长事务、无限重试、忽略复制延迟、直接重放未知提交、不演练恢复。

    完成这一节后，应能：

    - [ ] 能建表并编写 CRUD、`JOIN` 和聚合查询；
    - [ ] 能用 `EXPLAIN ANALYZE` 和真实参数验证索引；
    - [ ] 能处理快照读、当前读、锁、死锁和幂等重试；
    - [ ] 能设置 Java 类型映射、连接池和分层超时；
    - [ ] 能处理写后读一致性、故障切换和未知提交；
    - [ ] 能根据 Performance Schema / `sys` 定位慢 SQL、锁等待和复制延迟。

### PostgreSQL

PostgreSQL 是开源的对象关系型数据库管理系统，与 MySQL 一样使用表和 SQL，适合事务、关联查询和结构化数据。它强调标准 SQL、复杂查询以及类型、函数和扩展机制；是否选择它，应由项目需求和团队经验决定，而不是简单比较“谁更强”。

PostgreSQL 的对象层级：

`集群（Cluster） -> 数据库（Database） -> 模式（Schema） -> 表、视图、函数等对象`

- 一个集群可包含多个数据库；角色等少数对象由整个集群共享。
- 一次客户端连接只能访问一个数据库。访问其他数据库时，需要重新连接或使用 `\c 「数据库名」` 切换。
- Schema 是数据库内的命名空间，可以组织对象，也允许不同 Schema 存在同名表。
- 未写 Schema 的对象名按 `search_path` 查找。默认通常包含 `"$user", public`；可用 `SHOW search_path;` 查看。

MySQL 与 PostgreSQL 都能处理常规 Web 业务。已有 MySQL 技术栈时通常继续使用 MySQL；明确需要 PostgreSQL 的复杂 SQL、扩展类型或特定扩展时，再选择 PostgreSQL。

## NoSQL 数据库

NoSQL 不是一种固定的数据模型，而是键值、文档、列族、图等非关系型数据库的统称。本节只介绍 MongoDB 和 Redis。

### MongoDB

MongoDB 是文档数据库：一条记录是一个 BSON 文档，多个文档组成集合（Collection）。文档类似 JSON 对象，可以包含数组和嵌套文档；同一集合中的文档不必拥有完全相同的字段。

MongoDB 适合：

- 数据天然呈文档结构，例如内容、配置、商品属性和事件记录；
- 字段会持续演进，希望减少频繁修改表结构；
- 相关数据适合嵌入同一文档，并经常作为整体读取。

灵活结构不等于不需要设计。仍要统一字段类型、建立必要索引，并决定相关数据是嵌入文档还是保存引用。如果业务依赖大量关联、严格约束和复杂事务，关系型数据库通常更直接。

### Redis

Redis 是主要在内存中读写的 NoSQL 键值数据库。它不仅保存字符串，还提供多种数据结构和原子命令，常用于缓存、会话、计数器、排行榜、限流和消息处理。

常用数据结构：

| 数据结构 | 特点 | 常见用途 |
| --- | --- | --- |
| String | 字符串、数字或二进制数据 | 缓存值、计数器、状态标记 |
| Hash | 一个 key 下保存多个字段和值 | 用户信息、对象属性 |
| List | 按插入顺序排列的字符串序列 | 简单队列、时间线 |
| Set | 无序且不重复的字符串集合 | 标签、去重、交集和并集 |
| Sorted Set | 成员不重复，并按分数排序 | 排行榜、按时间或优先级排序 |

**过期与内存**

- 可为 key 设置 TTL，到期后由 Redis 删除；缓存数据通常应设置合理的过期时间。
- 内存达到 `maxmemory` 后如何处理，取决于淘汰策略。不要默认 Redis 会无限保存数据。
- 遍历大量 key 使用渐进式 `SCAN`；生产环境避免直接使用可能阻塞服务的 `KEYS *`。

**持久化**

- RDB：按时间点生成数据快照，文件紧凑，但故障时可能丢失最近一次快照之后的数据。
- AOF：记录写命令并在启动时重放，通常比单独使用 RDB 保留更多最近写入，但文件和写入成本更高。
- Redis 可以使用 RDB、AOF、两者组合，也可以关闭持久化。重启后是否丢失数据取决于配置和故障时机；持久化不能代替独立备份和恢复演练。

**常见缓存问题**

| 问题 | 含义 | 常用处理 |
| --- | --- | --- |
| 缓存雪崩 | 大量 key 在短时间内同时失效，请求集中转向数据库 | 错开过期时间并加入随机值、缓存预热、限流或降级 |
| 缓存穿透 | 缓存和数据库都没有目标数据，重复请求持续查询数据库 | 参数校验、布隆过滤器、短时间缓存空结果 |
| 缓存击穿 | 某个热点 key 失效时，大量并发请求同时查询数据库 | 互斥更新、逻辑过期、提前刷新热点数据 |
| 缓存污染 | 低频或仅访问一次的数据长期占用内存 | 设置合理的 TTL、`maxmemory` 和淘汰策略 |

**MySQL 与 Redis 配合**

常见做法是由 MySQL 保存需要可靠持久化的事实数据，Redis 缓存热点结果：读取时先查 Redis，未命中再查 MySQL 并写入带 TTL 的缓存；更新时先保证 MySQL 写入成功，再删除或更新缓存。缓存一致性、并发回源和失败重试仍需按业务要求设计，不能把 Redis 缓存直接当作唯一事实来源。

### 选型总结

| 主要需求 | 优先考虑 | 原因 |
| --- | --- | --- |
| 订单、用户、支付等结构化核心业务 | MySQL | 事务、约束、关联查询和生态成熟 |
| 复杂 SQL、丰富类型或 PostgreSQL 特定扩展 | PostgreSQL | SQL 能力和扩展机制丰富 |
| 结构会演进、天然呈文档形态的数据 | MongoDB | 文档可包含嵌套对象和数组，结构较灵活 |
| 缓存、计数、排行榜和高频临时数据 | Redis | 内存访问快，并提供多种数据结构和原子命令 |

选型应从数据结构、访问方式、一致性、持久化和运维能力出发，优先使用能满足需求的最少数据库。常见组合是 **MySQL 保存核心数据，Redis 加速热点读取**；PostgreSQL 或 MongoDB 只在需求明确时引入。
