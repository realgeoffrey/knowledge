# Cron表达式

> 墙钟到点触发。不是「再等 N 分钟」（那是延时，用 MQ / 落库）。周尽量写 `MON`、`FRI`，少写数字。时区在表达式外配置。

### 方言（段数）

| 段数 | 顺序 | 常见场景 |
| --- | --- | --- |
| 5 | 分 时 日 月 周 | crontab、K8s CronJob、GitHub Actions |
| 6 | 秒 分 时 日 月 周 | Spring `@Scheduled`、Quartz（年可省） |
| 6 | 分 时 日 月 周 年 | AWS `cron(…)`，无秒 |
| 7 | 秒 分 时 日 月 周 年 | Quartz / XXL-JOB（省年 → 回到**秒在左**的 6 段） |

### 字段取值

| 字段 | 范围 | 别名 |
| --- | --- | --- |
| 秒 / 分 | 0–59 | — |
| 时 | 0–23 | — |
| 日 | 1–31 | — |
| 月 | 1–12 | `JAN`–`DEC` |
| 周 | 见下「两套数字」 | `SUN`–`SAT` |
| 年 | 取决于调度器；AWS EventBridge 为 1970–2199 | — |

### 通用符号（各家都认）

| 符号 | 含义 | 例 |
| --- | --- | --- |
| `*` | 任意 | `*` |
| `,` | 列举 | `1,15` |
| `-` | 范围 | `MON-FRI`、`9-17` |
| `/` | 字段内的步长 | 分钟位 `*/5`＝每小时的 0、5、…、55 分；`10-59/15`＝10、25、40、55 分 |

### 扩展符号（多见于 Quartz / XXL-JOB；日、周）

| 符号 | 字段 | 含义 | 例 |
| --- | --- | --- | --- |
| `?` | 日或周 | 一侧不指定 | `0 0 2 ? * MON` |
| `L` | 日、周 | last | 日：`L`＝月末，`L-1`＝倒数第 2 天；<br>周：最后一个周五在 Spring 写 `5L`，在 Quartz 写 `6L` |
| `W` | 仅日 | 离该日最近的工作日（月末边界因实现而异） | `15W`；`LW`＝月末最后一个工作日 |
| `#` | 仅周 | 第 n 个周几（n 一般 1–5） | `MON#2`＝每月第 2 个周一 |

Spring 5.3 起使用 `CronExpression`，支持上表的日、周扩展写法。这里的「工作日」均指周一到周五，忽略节假日和调休。[Spring 字段说明](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/support/CronExpression.html)

### 谁认什么

| | crontab / K8s / GHA | Spring `@Scheduled` | Quartz / XXL-JOB | AWS EventBridge |
| --- | --- | --- | --- | --- |
| 秒 | 无 | 有（最左） | 有（最左） | 无 |
| 年 | 无 | 无 | 可选（最右） | 有（最右） |
| `?` `L` `W` `#` | 常见 crontab、GHA 不支持；K8s 接受 `?`，等同 `*` | 是（5.3+，日/周的 `?` 等同 `*`） | 是 | 是（按字段使用） |
| `@hourly` 等别名 | 常见 crontab、K8s 支持；GHA 不支持 | 是（5.3+） | 否 | 否 |
| `@reboot` | 仅系统 cron | 否 | 否 | 否 |

GitHub Actions 的最短调度间隔为 5 分钟。[GitHub Actions 定时触发](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) · [Kubernetes CronJob 语法](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#schedule-syntax)

### 容易踩的坑

1. **段数抄错**：Unix 5 段贴进 Spring 会坏（对照上表）。
2. **周的数字两套**：Unix / Spring：`0`/`7`=周日、`1`=周一；Quartz / AWS：`1`=周日、`2`=周一。跨家复制用名字。
3. **日和周同时写具体值**：crontab 是**或**；Spring 是**与**（`?`≈`*`，两侧可都 `*`）；Quartz / AWS 必须一侧 `?`，否则拒。
4. **Spring ≠ Quartz**：classpath 有 Quartz 时，`@Scheduled(cron)` 仍按 Spring 解析。XXL-JOB 使用自己的 Quartz 风格解析器，日/周一侧须写 `?`。
5. **`W` 的月初和月末边界**：1 号是周六时，`1W` 落到 3 号（周一）。月末则要看实现：从 2026 年 5 月 1 日算起，`31W` 在 Quartz 2.3.2 / 2.5.2 命中 5 月 29 日，在 Spring 5.3.39 / 6.2.14 的下一次匹配是 7 月 31 日。要在每月最后一个工作日运行，两者都用 `LW`。
6. **夏令时**：墙钟表达式可能跳过或重复一小时；关键任务看调度器文档，别假设一年 365×24 次。

### 常用写法

| 意图 | crontab（5） | Spring（6） | Quartz / XXL-JOB |
| --- | --- | --- | --- |
| 每天 02:00 | `0 2 * * *` | `0 0 2 * * *` | `0 0 2 * * ?` |
| 每 5 分钟 | `*/5 * * * *` | `0 */5 * * * *` | `0 */5 * * * ?` |
| 工作日 09:30 | `30 9 * * MON-FRI` | `0 30 9 * * MON-FRI` | `0 30 9 ? * MON-FRI` |
| 每月 1 号 00:00 | `0 0 1 * *` | `0 0 0 1 * *` | `0 0 0 1 * ?` |
| 月末 23:00 | —（无 `L`） | `0 0 23 L * *` | `0 0 23 L * ?` |
| 倒数第 2 天 | — | `0 0 0 L-1 * *` | `0 0 0 L-1 * ?` |
| 每月第 2 个周一 | — | `0 0 0 * * MON#2` | `0 0 0 ? * MON#2` |
| 离 15 号最近工作日 | — | `0 0 0 15W * *` | `0 0 0 15W * ?` |

### 别名（crontab、Spring 认；Quartz 一般不认）

| 别名 | 等价 crontab（5） | 等价 Spring（6） | 含义 |
| --- | --- | --- | --- |
| `@hourly` | `0 * * * *` | `0 0 * * * *` | 每小时整点 |
| `@daily` / `@midnight` | `0 0 * * *` | `0 0 0 * * *` | 每天 00:00 |
| `@weekly` | `0 0 * * 0` | `0 0 0 * * 0` | 每周日 00:00 |
| `@monthly` | `0 0 1 * *` | `0 0 0 1 * *` | 每月 1 号 00:00 |
| `@yearly` / `@annually` | `0 0 1 1 *` | `0 0 0 1 1 *` | 每年 1 月 1 日 00:00 |
| `@reboot` | — | — | Cronie 和 Debian cron 在每次系统启动后首次启动守护进程时执行一次 |

在同一次系统启动期间重启 Cronie 或 Debian cron 不会再次触发 `@reboot`。[Cronie 实现](https://github.com/cronie-crond/cronie/blob/master/src/cron.c) · [Debian cron 实现](https://sources.debian.org/src/cron/3.0pl1-162/cron.c/)

**crontab**（用户 crontab，`crontab -e`）：

```cron
@hourly /path/to/script.sh
@daily  /usr/local/bin/backup.sh
@reboot /path/to/on-boot.sh
```

别名 = **整段表达式**，不能再拼字段（没有 `@hourly 0 0`、`@daily MON` 这种写法）。要改时刻就写完整 cron。表达式外的配置仍可用：crontab 顶部环境变量；Spring 的 `zone` 等。

**Spring**：

```java
@Scheduled(cron = "@daily", zone = "Asia/Shanghai")  // 别名 + 时区 OK
// 不能：@Scheduled(cron = "@hourly", fixedRate = …)  // cron 与 fixedRate/fixedDelay 互斥
void run() { /* ... */ }
```

`@Scheduled` 会在每个应用实例上独立触发。多副本部署且任务只需执行一次时，可交给调度平台统一触发，或使用分布式锁协调，并让任务可幂等重试。
