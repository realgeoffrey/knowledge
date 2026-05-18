# Java学习笔记

## 目录
1. [Java 概览](#java-概览)
1. [Java SE 基础](#java-se-基础)
1. [后端工程与数据中间件](#后端工程与数据中间件)

---

<details>
<summary>定位、资源与路线</summary>

1. 这份笔记面向“前端转全栈 Java”的学习场景；与 JS 基本一致的内容尽量少写，重点建立能做业务开发的知识骨架。

    - 第一阶段：会写 Java 基础语法，能看懂并修改常见后端代码。
    - 第二阶段：掌握 Spring Boot + MyBatis + MySQL，能独立完成基础 CRUD 接口。
    - 第三阶段：补 Redis、消息队列、JVM、并发、性能调优等进阶内容。

    <details>
    <summary>学习资源</summary>

    1. 视频

        1. 快速入门：[系列·狂神说Java系列（排序完毕）](https://space.bilibili.com/95256449/lists/393820?type=series)
        1. Java 基础：[【零基础 快速学Java】韩顺平 零基础30天学会Java](https://www.bilibili.com/video/BV1fh411y7R8)
        1. 补深度：[尚硅谷最新Java学习路线（AI赋能全新升级）](https://www.bilibili.com/opus/369163743450531164)
    1. 文本

        1. [廖雪峰：Java教程](https://liaoxuefeng.com/books/java/introduction/index.html)
    </details>
1. 学习路线

    推荐按下面顺序学习，不要一开始就陷入源码、JVM 参数、微服务治理这类细节。

    1. Java SE 基础
    2. Maven
    3. MySQL
    4. Spring / Spring Boot
    5. MyBatis
    6. Redis
    7. 消息队列
    8. 并发、JVM、性能优化

    前端转 Java 时，最容易卡住的点通常不是语法，而是下面三件事：

    - 类型系统更严格，编译期约束更多。
    - 后端代码更强调分层、事务、数据一致性。
    - 工程启动、依赖管理、数据库与中间件的协作成本更高。

</details>

## Java 概览
### 版本演进
- Java 1.0 / 1.1 常见称呼是 JDK 1.0 / 1.1（Java Development Kit）。
- 1.2 到 1.4 常见叫法是 J2SE（Java 2 Platform, Standard Edition）。
- Java 5 的正式品牌常见写作 J2SE 5.0，也常被称为 Java 5；Java 6 起通常叫 Java SE（Java Platform, Standard Edition）。
- 日常说版本时，Java SE 8 / Java 8 / JDK 8 / JDK 1.8 通常指同一代（2014年）。

    下载地址：[Java SE 8 Archive Downloads (JDK 8u202 and earlier)](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)、[Java SE 8 Archive Downloads (JDK 8u211 and later)](https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html)（[Java downloads](https://www.oracle.com/java/technologies/downloads/)、[Java Archive](https://www.oracle.com/java/technologies/downloads/archive/)）

    >JDK 8u202解析：`8`代表主版本号，也就是 Java 8（在早期命名规范中也叫 JDK 1.8）。`u`是 Update（更新） 的缩写。`202`是更新号。Oracle 会定期发布这些 Update，主要包含安全漏洞修复、Bug 修复以及一些微小的性能调优，不涉及语法层面的大改动。
- Java 9 起主版本号不再写成 `1.x`，而是直接使用 9、10、11、17、21、25 这种形式。
- <details>

    <summary>本地版本管理：<a href="https://github.com/sdkman/sdkman-cli">SDKMAN!</a></summary>

    ```
    sdk list            # 列出 SDKMAN! 支持管理的候选项（java、maven、gradle、...）
    sdk list java       # 列出 Java 可安装、本地、已安装和当前使用的版本（通常 `>>>` 表示当前正在使用，底部图例为准）
    sdk list java | grep -E "installed|local only"  # 查看已安装或通过本地路径接管的 Java
    ls -l ~/.sdkman/candidates/java/                # 查看安装目录
    # 不同候选项的 sdk list 展示格式可能不同，以输出底部图例为准
    # 针对maven，可以根据sdk list maven查看标志信息（如：`+`local version；`*`installed；`>`currently in use）

    sdk install java                # 安装 Java 最新稳定版
    sdk install java 「支持的版本标识」 # 安装指定版本，版本标识从 sdk list java 中复制
    sdk install java 8.0.192-local /Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home
    # 安装本地版本（sdk install java 「唯一的版本号」 「本地路径」）：先手动下载一个版本，然后让 SDKMAN! 接管（软链接）

    sdk use java 8.0.192-local          # 仅当前 shell 使用该 Java 版本

    sdk default java 8.0.192-local      # 设为默认版本，后续新 shell 生效

    sdk current             # 查看所有候选项当前使用的版本
    sdk current java        # 查看 Java 当前使用的版本

    sdk uninstall java 「已安装的版本号」

    sdk selfupdate  # 更新 SDKMAN! 自身
    ```
    </details>

### 平台体系
- **Java SE**：标准版，覆盖语言基础、标准类库、集合、IO/NIO、日期时间、并发、网络、反射、注解。
- **Java EE（Java Enterprise Edition） / Jakarta EE**：企业级规范体系，现已演进为 Jakarta EE。
- **Java ME**（Java Micro Edition）：面向早期嵌入式/移动设备，现在基本不是主流。

### 运行体系：JDK / JRE / JVM
- **JDK**：开发套件，包含 JVM、标准类库，以及 `$JAVA_HOME/bin` 下的开发和诊断工具；业务常用命令包括 `java`、`javac`、`jar`、`javadoc`、`jshell`、`jdeps`、`jlink`、`jcmd`、`jmap`、`jstack`。
- **JRE**（Java Runtime Environment）：运行环境，包含 JVM 和标准类库；Java 8 常见独立 JRE，现代 JDK 通常直接提供完整运行环境。
- **JVM**（Java Virtual Machine）：负责加载并执行 `.class` 字节码。

```mermaid
flowchart TD
    %% 定义外部输入
    Src["源代码 (.java)"]

    subgraph JDK ["JDK (开发套件 = 运行环境 + 开发工具)"]
        direction TB
        Tools["开发工具<br/>(java, javac, jar, javadoc, jcmd, jmap, jstack)"]

        subgraph JRE ["运行环境 (JVM + 标准类库)"]
            direction TB
            Lib["标准类库<br/>(Java SE API)"]
            JVM["JVM 虚拟机<br/>(类加载器, 执行引擎, 内存区, GC)"]

            Lib -.->|"提供基础类支撑"| JVM
        end
    end

    %% 核心流程
    BC["字节码 (.class)"]
    OS["底层操作系统<br/>(Windows, Linux, macOS)"]

    %% 节点连接关系
    Src -->|"1. 编译 (javac)"| Tools
    Tools -->|"2. 生成"| BC
    BC -->|"3. 加载与执行"| JVM
    JVM ==>|"4. 系统调用 / 本地接口"| OS
```

### 核心优势
- 跨平台：同一套字节码可以运行在不同平台的 JVM 上（一次编写，到处运行。Write Once, Run Anywhere。WORA）。
- 工程生态成熟：框架、数据库驱动、中间件集成非常完善。
- 垃圾回收：不需要像 C/C++ 那样手动管理内存。
- 稳定：在企业级业务系统里长期被验证。

>- “三高”是什么
>
>    - **高并发**：同一时间处理大量请求的能力。
>    - **高性能**：单机延迟和吞吐表现好。
>    - **高可用**：服务故障时仍能持续对外提供服务。
>
>“三高”主要是系统设计问题，语言和框架只是基础条件，不是全部答案。

## Java SE 基础
Java SE 基础按 8 个字回忆：**名、值、流、法、组、系、形、错**。

```text
名：包、import、访问控制、修饰符、Javadoc，解决名字从哪里来、谁能用。
值：变量、值、引用、内存、默认值、null、final、常量、事实不可变。
流：表达式、语句、代码块、if/switch、while/for、break/continue/return/throw。
法：方法、参数、返回、值传递、重载、可变参数、静态方法、实例方法、构造器。
组：数组、类、对象、字段、成员、初始化、this/super、封装。
系：继承、组合、转型、instanceof、多态、重写、字段隐藏、静态方法隐藏。
形：抽象类、接口、default 方法、枚举、记录、嵌套类、局部类、匿名类。
错：异常体系、受检/非受检、try-catch-finally、try-with-resources、throw/throws、自定义异常。
```

判断任何基础问题，只问三句：**名字能不能访问？编译期类型是什么？运行期对象和异常路径是什么？**

### 环境配置与运行
- 安装 JDK、Maven，并配置 `JAVA_HOME`、`PATH`。

    下载并安装 JDK、Maven，然后配置环境变量。例如 `~/.zshrc`：

    ```text
    # 方式1，手动管理版本
    # JDK版本
    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home
    export PATH=$JAVA_HOME/bin:$PATH
    # Maven版本
    export M2_HOME=/usr/local/apache-maven-3.9.15
    export PATH=$M2_HOME/bin:$PATH


    # 方式2，SDKMAN管理
    #THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
    export SDKMAN_DIR="$HOME/.sdkman"
    [[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
    ```

    - 配置 IDE 的 Java 版本：

        1. Cursor：`java.configuration.runtimes`
        2. IDEA：「文件」-「项目结构」-「项目」-「SDK」（「编辑」配置好需要的SDK）
- 初学期建议先用 LTS 版本；老项目常见 Java 8，新项目常见 Java 17/21，是否使用更高版本以团队基线为准（团队统一约定的技术标准下限/默认线）。

- `javac 文件.java` → `类名.class`，编译为字节码；运行 `java 类名`（不写 `.class`）后，由 JVM 解释执行或经 JIT 编译为机器码，再交给CPU执行。

    >字节码是源代码经过编译器编译生成的，但它并不直接运行在物理硬件上，而是运行在虚拟机上。虚拟机会解释执行字节码指令，并将其转化为机器码让CPU实际执行。

    >可通过 `java 类名 参数1 参数2` 向 `main` 传入命令行参数，如：`public class 类名 { public static void main(String[] args) {} }`。传统项目入口常用这个标准签名。只有要被 JVM 直接当作程序入口启动的类，才必须有可启动的 `main` 方法。
- 普通源文件中，`public` 顶级类的类名必须与文件名一致；一个 `.java` 文件最多只能有一个 `public` 顶级类。

### 类型转换与强类型规则
- Java 是强类型语言，变量和表达式都有编译期类型。
- 赋值、传参、返回值等上下文中的自动转换主要是**拓宽基本类型转换**：

    1. `byte` 可转为 `short/int/long/float/double`
    1. `short` 可转为 `int/long/float/double`
    1. `char` 可转为 `int/long/float/double`
    1. `int` 可转为 `long/float/double`
    1. `long` 可转为 `float/double`
    1. `float` 可转为 `double`
- 表达式运算中的规则叫**数值提升**：`byte`、`short`、`char` 参与大多数算术运算时先提升为 `int`，再按 `int -> long -> float -> double` 决定结果类型。
- 反向或不在拓宽规则内的转换是**收窄基本类型转换**，通常需要显式强转，可能截断、溢出或丢失精度。
- “拓宽”是 Java 官方转换规则，不等于完全无损；例如 `int -> float` 是拓宽转换，但大整数可能丢失低位精度。
- `boolean` 不能与数值类型互转。

<details>
<summary>类型转换示例</summary>

```java
int a = 10;
double b = a; // int -> double：拓宽基本类型转换，自动完成
// int c = b; // 编译错误：double -> int 是收窄转换，不能隐式完成
int c1 = (int) b; // 显式收窄：小数部分截断，非四舍五入
long L = a; // int -> long：拓宽转换
float F = a; // int -> float：拓宽转换，但大整数可能丢失精度
double D = F; // float -> double：拓宽转换
char ch = 'A';
int chAsInt = ch; // char -> int：拓宽转换，得到 UTF-16 代码单元数值
byte bt = (byte) a; // int -> byte：必须强转；超范围时按低位截断
short sh = (short) 32768; // 字面量默认 int，赋给 short 需强制，值溢出则按位模式截断
double expr = a + 1.0f; // 二元运算数值提升：int 与 float/double 运算时先提升到较宽类型再算
byte n = 1;
// char c2 = n; // 编译错误：byte -> char 不是拓宽转换，不能只按“范围大小”理解
char c3 = (char) n;
// String.valueOf 不是 (T)x 语法，是方法调用，把基本类型格式化成字符串。
String s = String.valueOf(a);
// String s1 = (String) a; // 编译错误：基本类型不能 (String) 强转
// char -> String 用 String.valueOf(ch) 或 "" + ch 或 Character.toString(ch)，不能 (String)ch。
```
</details>

### 基本类型与引用类型
Java 类型先分两类：**基本类型保存值本身**，**引用类型保存对象引用或 `null`**。变量具体在栈、堆还是对象内部，取决于它是局部变量、字段还是数组元素，不由“基本类型 / 引用类型”单独决定。

1. 基本类型一共 8 种

    | 类型 | 大小 | 字段 / 数组元素默认值 | 范围或含义 | 说明 |
    | --- | --- | --- | --- | --- |
    | `byte` | 1 字节 | `0` | -128 ~ 127 | 小整数 |
    | `short` | 2 字节 | `0` | -32768 ~ 32767 | 小整数 |
    | `int` | 4 字节 | `0` | -2^31 ~ 2^31 - 1 | 默认整数类型 |
    | `long` | 8 字节 | `0L` | -2^63 ~ 2^63 - 1 | 长整数，字面量常加 `L` |
    | `float` | 4 字节 | `0.0f` | 约 ±3.4E38 | 单精度浮点，字面量常加 `F` |
    | `double` | 8 字节 | `0.0d` | 约 ±1.8E308 | 默认浮点类型 |
    | `char` | 2 字节 | `'\u0000'` | 0 ~ 65535 | UTF-16 代码单元，不等于任意 Unicode 字符 |
    | `boolean` | 未规定 | `false` | `true` / `false` | 不能参与数值运算 |

    - 基本类型规则

        - 默认值只适用于字段和数组元素；局部变量没有默认值，读取前必须明确赋值。
        - 基本类型不是对象，不能为 `null`，不能直接调用方法；需要对象能力时使用包装类型，如 `Integer`、`Double`、`Boolean`。
        - 整数字面量默认是 `int`，浮点字面量默认是 `double`；`long` 常写 `1L`，`float` 常写 `1.0F`。
        - 单引号是 `char`，双引号是 `String`；`String` 是引用类型，不是基本类型。
        - 运算前会做数值提升：`byte`、`short`、`char` 参与大多数算术运算会先提升为 `int`；二元数值运算按 `int` < `long` < `float` < `double` 提升到较宽类型。
        - 位移运算结果看左操作数提升后的类型；复合赋值会隐式转回左值类型，普通 `=` 不会自动窄化。
        - 只要 `+` 的一侧是 `String`，结果就是字符串拼接；`boolean` 可以拼接成字符串，但不能参与数值运算。
        - 泛型不能使用基本数据类型，但是可以用基本类型的包装类型用于泛型

            >Java 泛型类型必须是引用类型，所以基本类型不能直接作为泛型类型参数。更底层的原因是：Java 泛型采用类型擦除实现，类型参数最终需要擦除成 Object 或某个引用类型上界，而基本类型不是引用类型，也不是 Object 的子类。

        - 浮点数规则

            - `float` / `double` 基于 IEEE 754，分别对应 binary32 / binary64。
            - 浮点字面量默认是 `double`；`1.0f` 是 `float`，`1e-3` 是科学计数法。
            - 浮点运算是有限精度近似计算，不适合金额；金额优先用 `java.math.BigDecimal`。
            - 浮点除以零不抛 `ArithmeticException`：`1.0 / 0.0` 是 `Infinity`，`-1.0 / 0.0` 是 `-Infinity`，`0.0 / 0.0` 是 `NaN`。
            - `NaN` 表示非法或未定义结果：有序比较遇到 `NaN` 都是 `false`，`NaN == NaN` 是 `false`，`NaN != NaN` 是 `true`；用 `Float.isNaN` / `Double.isNaN` 判断。
            - `+0.0 == -0.0` 为 `true`，但符号会影响 `1.0 / ±0.0` 等结果；浮点排序或统一比较用 `Float.compare` / `Double.compare`。
            - `Math` / `StrictMath` 对 `NaN`、无穷大、正负零有明确规则；需要跨平台可复现时优先看 `StrictMath`。

    <details>
    <summary>表达式类型提升示例</summary>

    ```java
    byte b1 = 1;
    byte b2 = 2;
    int r1 = b1 + b2;      // byte + byte 先提升为 int

    char c = 'A';
    int r2 = c + 1;        // char 先提升为 int，结果是 66

    long l = 1L;
    long r3 = l + 2;       // int 与 long 运算，结果是 long

    float f = 1.5f;
    float r4 = f + 2;      // int 与 float 运算，结果是 float

    int r5 = 5 / 2;        // 两个 int 相除仍是 int，结果是 2
    double r6 = 5 / 2.0;   // 有 double 参与，结果是 2.5

    byte b3 = 1;
    b3 += 1;               // 等价于 b3 = (byte)(b3 + 1)
    // b3 = b3 + 1;        // 编译错误：b3 + 1 是 int，普通 = 不自动窄化

    String str = "sum=" + b1 + b2;    // "sum=12"
    String str2 = "sum=" + (b1 + b2); // "sum=3"
    ```
    </details>

3. 引用类型包括

    | 类型 | 例子 | 说明 |
    | --- | --- | --- |
    | 类类型 | `String`、普通类、包装类、枚举、记录 | 枚举、记录是特殊类 |
    | 接口类型 | `List`、`Runnable`、注解接口 | 注解接口是特殊接口 |
    | 数组类型 | `int[]`、`String[]`、`int[][]` | 数组本身是对象，元素可以是基本类型或引用类型 |
    | 类型变量 | `T`、`E` | 泛型形参，编译期参与类型检查 |

    - 引用类型规则

        - 引用变量保存的是引用值；引用值要么是 `null`，要么指向对象或数组。
        - 字段和数组元素里的引用类型默认值是 `null`；局部引用变量仍然没有默认值。
        - 对 `null` 调用字段、方法或数组长度会抛 `NullPointerException`。
        - `==` 比较两个引用是否指向同一个对象；内容相等通常看类是否正确实现 `equals`。
        - 数组是引用类型：`int[]` 变量保存数组引用，数组对象里的元素才是 `int` 值。
        - 基本类型和引用类型不能互相强转；基本类型与包装类型之间可以自动装箱 / 拆箱，拆箱 `null` 会抛 `NullPointerException`。

    - 包装类

        | 基本类型 | 包装类 |
        | --- | --- |
        | `byte` | `Byte` |
        | `short` | `Short` |
        | `int` | `Integer` |
        | `long` | `Long` |
        | `float` | `Float` |
        | `double` | `Double` |
        | `char` | `Character` |
        | `boolean` | `Boolean` |
        | `void` | `Void`，表示 `void` 对应的类型对象，不能像普通值一样创建实例 |

        - 包装类是基本类型的引用类型版本，主要用于泛型、集合、可空值和工具方法。
        - 自动装箱：基本类型转包装类；自动拆箱：包装类转基本类型。拆箱 `null` 会抛 `NullPointerException`。
        - `List<Integer>` 合法，`List<int>` 不合法（泛型类型参数必须是引用类型）。
        - 包装类对象比较值优先用 `equals`；`==` 比较引用，只有判断 `null` 时稳定使用。
        - `Boolean`、`Byte`、部分 `Character`、`Short` / `Integer` / `Long` 的小范围值可能被缓存，不要依赖缓存结果写 `==` 值比较。
        - 常用方法：`Integer.parseInt("123")` 返回 `int`，`Integer.valueOf("123")` 返回 `Integer`，`String.valueOf(123)` 返回 `String`。
        - Java 可以有自定义包装类型，但它们只是普通类，不属于 Java 内置的 8 个基本类型包装类，也不支持自动装箱/拆箱。Void 是 void 的特殊占位类，主要用于泛型和反射场景。

    - <details>

        <summary><code>String</code>字面量与转义<code>\</code></summary>

        - 反斜杠 `\` 在源码字符串中表示“开始转义”，不是普通字符；如果字符串内容要包含反斜杠本身，写 `\\`。
        - 常见转义：`\\` 反斜杠，`\"` 双引号，`\n` 换行，`\r` 回车，`\t` 制表符，`\b` 退格，`\f` 换页。
        - `"\n"` 是一个换行字符；`"\\n"` 是两个字符：反斜杠和字母 `n`。
        - Unicode 转义写作 `\uXXXX`，如 `"\u0041"` 表示 `"A"`；它在 Java 源码词法处理早期生效，复杂场景下不要滥用。
        - 文本块（text block）用 `"""..."""` 表示多行字符串；Java 13/14 是预览功能，Java 15 起正式可用。
        - 文本块的起始 `"""` 后必须换行，适合 SQL、JSON、HTML 等多行文本；内部普通双引号通常不需要转义，反斜杠转义仍可用。
        </details>
    ```java
    int n = 10;             // 基本类型变量保存 int 值
    Integer boxed = n;      // 自动装箱：int -> Integer
    int m = boxed;          // 自动拆箱：Integer -> int

    String text = "hi";     // text 保存 String 对象引用
    String empty = null;    // null 可以赋给引用类型
    // empty.length();      // 运行期 NullPointerException

    String sql = """
            SELECT *
            FROM users
            WHERE name = "Tom"
            """;

    int[] nums = {1, 2, 3}; // nums 是引用，数组对象里的元素是 int
    ```

### 变量、值、引用与内存

变量不是对象；引用不是对象；对象是运行期存在的数据本体。

```text
变量 variable
├─ 局部变量 local variable：声明在方法、构造器、初始化代码块、普通代码块内部
├─ 参数 parameter：声明在方法、构造器、lambda、catch、增强 for 的参数位置
├─ 字段 field：声明在类、接口、枚举、记录、注解接口的成员位置
│  ├─ 实例字段 instance field：不带 static，属于每个对象
│  └─ 静态字段 static field / class variable：带 static，属于类型本身
└─ 数组元素 array component：数组对象内部的槽位，可通过下标访问
```

>变量不包含方法。方法是行为，字段、局部变量、参数、数组元素才保存值。

| 类别 | 声明位置 | 默认值 | 归属与生命周期 |
| --- | --- | --- | --- |
| 局部变量 | 方法体、构造器体、代码块内部 | 没有默认值，读取前必须明确赋值 | 随当前代码块级作用域结束而失效 |
| 参数 | 方法、构造器、lambda、catch、增强 for 参数位置 | 调用时由实参或运行时提供 | 本质是当前调用中的局部变量 |
| 实例字段 | 类型成员位置，不带 `static` | 有默认值 | 属于对象；每个对象有自己的一份 |
| 静态字段 | 类型成员位置，带 `static` | 有默认值 | 属于类型；同一个类加载器下共享一份 |
| 数组元素 | 数组对象内部 | 有默认值 | 属于数组对象；数组活着元素就存在 |

- 字段和数组元素的默认值

    | 类型 | 默认值 |
    | --- | --- |
    | `byte`、`short`、`int` | `0` |
    | `long` | `0L` |
    | `float` | `0.0f` |
    | `double` | `0.0d` |
    | `char` | `'\u0000'` |
    | `boolean` | `false` |
    | 引用类型 | `null` |

>Java 没有 `undefined`。变量只要属于局部变量或参数，读取前就必须让编译器确认它已经被赋值；变量只要属于字段或数组元素，创建所属对象时就会先填默认值。

| 写法 | 变量里保存什么 | 对象在哪里 |
| --- | --- | --- |
| `int x = 18;` | 数字 `18` | 没有对象 |
| `User u = new User();` | 指向 `User` 对象的引用值 | `new User()` 创建的对象在堆中 |
| `String s = "Tom";` | 指向字符串对象的引用值 | 字符串对象在堆中，字面量通常来自字符串池 |
| `User[] users = new User[3];` | 指向数组对象的引用值 | 数组对象在堆中；每个元素初始为 `null` |
| `class User { int age; }` | `age` 保存整数值 | `age` 在所属 `User` 对象内部 |
| `class User { String name; }` | `name` 保存引用值或 `null` | 被引用的字符串对象在堆中或不存在 |

>简化模型：栈管方法调用过程，堆管对象生命周期。局部变量和参数在当前方法调用的栈帧里；`new` 出来的对象和数组在堆里；实例字段在对象内部；静态字段属于类，不属于某个对象。JVM 可能做逃逸分析、标量替换、锁消除优化，但这些优化不改变 Java 语言语义。

```java
class User {
    int age;          // 实例字段：每个 User 对象一份，默认 0
    String name;      // 实例字段：每个 User 对象一份，保存引用值，默认 null
    static int total; // 静态字段：User 类型一份，默认 0
}

void demo(int input) {        // input 是参数
    int count = 0;            // count 是局部变量
    User u = new User();      // u 保存引用值，对象由 new 创建
    int[] scores = new int[3];// scores 保存数组引用，元素默认 0
}
```

Java 只有值传递。传基本类型时复制具体值；传引用类型时复制引用值，不复制对象本体。

- `var`

    - `var` 是局部变量类型推断，不是动态类型；编译器根据初始化表达式推断出确定类型，之后不能当成其他类型使用。
    - `var` 只能用于能推断出类型的局部声明，常见于普通局部变量、`for` 初始化变量、增强 `for` 元素变量、try-with-resources 资源变量；不能用于字段、方法返回类型、普通方法参数。
    - `var x;`、`var x = null;`、`var arr = {1, 2, 3};` 都不合法；数组要写 `var arr = new int[] {1, 2, 3};`。

    ```java
    void localScope(boolean ok) {
        int outer = 1;

        if (ok) {
            var text = "hi";        // 推断为 String
            int inner = outer + 1;  // 内层块可访问外层局部变量
        }

        // text 和 inner 已离开作用域，不能再访问
        // var value;       // 编译错误：var 必须有初始化表达式
        // var nothing = null; // 编译错误：无法从 null 推断类型
    }
    ```

- 作用域规则

    - 局部变量从声明处开始可见，到所在代码块结束失效（块级作用域）。
    - 字段在整个对象或类型中可用，但仍受访问权限控制。
    - 局部变量可以遮蔽字段；访问当前对象字段可写 `this.name`。
    - 同一方法的重叠局部作用域中，不能重新声明同名局部变量或同名参数。

### 常量、事实不可变与 `final`

`final` 的核心含义是“只能赋值一次”，不是“对象一定不可变”。

| 使用位置 | 含义 | 关键规则 |
| --- | --- | --- |
| 局部变量 | 只能赋值一次 | 可声明时赋值，也可稍后赋值一次 |
| 参数 | 方法体内不能重新给参数赋值 | 不能阻止调用方对象被修改 |
| 实例字段 | 每个对象内只能初始化一次 | 可在声明处、实例初始化代码块、构造器中完成初始化 |
| 静态字段 | 类型级变量只能初始化一次 | 可在声明处或静态代码块中完成初始化 |
| 引用变量 | 引用值不能换 | 被引用对象的字段仍可能变化 |
| 方法 | 子类不能重写 | 仍可被重载 |
| 类 | 不能被继承 | `String`、包装类、很多值类型设计会用它 |

```java
final int a = 1;
// a = 2; // 编译错误

final User user = new User();
user.name = "Li";       // 合法：对象状态变化
// user = new User();   // 编译错误：引用值变化
```

常量通常写成 `public static final`，命名用全大写加下划线：

```java
public static final int MAX_RETRY_COUNT = 3;
public static final String DEFAULT_CHARSET = "UTF-8";
```

- 更细的规则

    - `static final` 字段如果是基本类型或 `String`，并且用编译期常量表达式初始化，会成为编译期常量，使用方编译后可能直接内联该值。
    - `final` 字段不在声明处赋值时叫空白 final 字段，必须保证每条构造路径或静态初始化路径给它赋值一次。
    - 局部变量没有显式写 `final`，但赋值后再也不改，也叫事实不可变；lambda、局部普通类、匿名类读取外部局部变量时需要这种状态。
    - 不可变类需要同时控制类继承、字段可变性、构造时防御性拷贝、Getter 暴露方式；单独写 `final` 引用不够。

### 包、`import` 与访问控制

包（`package`）是 Java 组织类型的命名空间。一个类型的全限定名 = 包名 + 类型名，例如 `com.example.demo.service.UserService`。包负责命名隔离、源码组织、编译输出组织、包访问权限边界。

```java
package com.example.demo.service;   // package 只写包名

import java.util.List;              // import 写具体类型名或 *（class、interface、enum、注解接口、record）
import static java.lang.Math.PI;    // import static 写具体静态成员或 *（静态字段、静态方法、枚举常量、静态嵌套类型）
```

- 包声明规则

    - 普通 `.java` 源文件最多声明一个 `package`。
    - `package` 必须位于有效代码最前面：注释和包注解之后，`import` 与顶级类型声明之前。
    - 同一个源文件里的所有顶级类型属于同一个包。
    - 同一个包的类型可以分散在多个 `.java` 文件里，只要声明相同包名。
    - 包名通常全小写，常用公司域名倒置加项目模块名，例如 `com.baidu.mall.order`。
    - 包路径通常与目录结构一致，例如 `com.example.demo.service` 对应 `com/example/demo/service`。
    - 不写 `package` 是默认包。默认包适合临时练习；具名包中的代码不能 `import` 默认包类型，也不能直接引用默认包类型。
    - 一个 `.java` 文件可以放多个顶级类型：类、接口、枚举、注解接口、记录。
    - 一个 `.java` 文件最多只能有一个 `public` 顶级类型，文件名必须与这个 `public` 顶级类型同名。
    - 没有写 `public` 的顶级类型是包访问权限。
    - 子包不是父包的一部分：`com.example` 与 `com.example.service` 是两个不同的包，包访问权限不能互通。

- `import` 规则

    - `import` 是编译期语法，只负责简化名称书写，不会加载整个包，不会执行被导入类型的代码。
    - 同包类型、同源文件里的其他顶级类型、`java.lang` 包下的类型可以直接使用。
    - 使用其他包下的类型时，可以写全限定名，例如 `java.util.List`。
    - 想把 `java.util.List` 简写成 `List`，写 `import java.util.List;`。
    - 类型导入有两种：`import 包.类型;`、`import 包.*;`。
    - 静态导入有两种：`import static 包.类型.静态成员;`、`import static 包.类型.*;`。
    - `import com.example.*;` 只导入 `com.example` 当前包下的类型，不递归导入 `com.example.service.UserService`。
    - Java 没有 `import ... as ...` 别名语法。
    - 多个来源出现同名类型时，`import` 不能替你选择；冲突处写全限定名最清楚。
    - `import` 不改变访问权限。能不能访问只由访问修饰符、调用方所在包、继承关系共同决定。

- 访问控制表

    | 修饰符 | 顶级类型可用 | 成员可用 | 访问范围 |
    | --- | --- | --- | --- |
    | `public` | 可用 | 可用 | 任意包中的代码可访问 |
    | `protected` | 不可用 | 可用 | 同包可访问；跨包只允许子类在继承访问语境中访问 |
    | 不写 | 可用 | 可用 | 同包可访问，称为包访问权限 |
    | `private` | 不可用 | 可用 | 当前顶级类型及其嵌套类型内部可访问 |

    - 同一个源文件不会自动共享 `private` 权限；两个并列顶级类仍不能互相访问对方的 `private` 成员。
    - 外部类与嵌套类属于同一个 nest，可以互相访问 `private` 成员；这是嵌套类型的特殊规则。

### 关键字修饰符

关键字修饰符要看声明位置，不能只背单词。

| 声明位置 | 可用关键字 |
| --- | --- |
| 顶级普通类 | `public`、`abstract`、`final`、`sealed`、`non-sealed`、`strictfp` |
| 顶级接口 | `public`、`abstract`、`sealed`、`non-sealed`、`strictfp` |
| 顶级枚举 | `public`、`strictfp` |
| 顶级注解接口 | `public`、`abstract`、`strictfp` |
| 顶级记录 | `public`、`final`、`strictfp` |
| 成员普通类 | `public`、`protected`、`private`、`static`、`abstract`、`final`、`sealed`、`non-sealed`、`strictfp` |
| 成员接口 | `public`、`protected`、`private`、`static`、`abstract`、`sealed`、`non-sealed`、`strictfp` |
| 成员枚举 | `public`、`protected`、`private`、`static`、`strictfp` |
| 成员注解接口 | `public`、`protected`、`private`、`static`、`abstract`、`strictfp` |
| 成员记录 | `public`、`protected`、`private`、`static`、`final`、`strictfp` |
| 普通字段 | `public`、`protected`、`private`、`static`、`final`、`transient`、`volatile` |
| 接口字段 | `public`、`static`、`final` |
| 普通方法 | `public`、`protected`、`private`、`static`、`abstract`、`final`、`synchronized`、`native`、`strictfp` |
| 接口方法 | `public`、`private`、`abstract`、`default`、`static`、`strictfp` |
| 构造器 | `public`、`protected`、`private` |
| 局部普通类 | `abstract`、`final`、`strictfp` |
| 局部变量 | `final` |
| 参数 | `final` |

- 组合限制

    - 顶级类型只能是 `public` 或包访问权限，不能写 `protected`、`private`、`static`。
    - 同一声明中不能重复写同一个修饰符。
    - `abstract` 和 `final` 语义冲突，不能同时修饰同一个类或同一个方法。
    - `abstract` 方法不能同时是 `private`、`static`、`final`、`native`、`synchronized`、`strictfp`。
    - 字段不能同时是 `final` 和 `volatile`。
    - 构造器不是方法，不能写返回值类型，不能写 `static`、`final`、`abstract`。
    - 局部变量和普通方法参数只能写 `final`；`var` 是局部变量类型推断关键字，不是修饰符。
    - 接口中的 `default`、`static`、`private` 方法必须有方法体；接口抽象方法不能有方法体。
    - 接口体中直接声明的成员类型隐式是 `public static`，不能写 `protected` 或 `private`。
    - `sealed` 类型通过 `permits` 限制直接子类型；直接子类型必须声明为 `final`、`sealed`、`non-sealed` 三者之一。
    - `non-sealed` 只能用于直接继承或实现某个 `sealed` 类型的类或接口，不能作为普通“可继承”标记随意使用。
    - `strictfp` 自 Java 17 起没有实际必要，新代码不建议使用。
    - 注解 `@Override`、`@Deprecated`、`@SuppressWarnings` 可写在声明前，但注解不是关键字修饰符。

### Javadoc
<details>
<summary></summary>

Javadoc 的类型信息来自 Java 签名，注释负责说明用途、参数语义、返回语义、异常语义、使用约束。

```java
/**
 * 根据用户 id 查询用户。
 *
 * @param id 用户 id，必须大于 0
 * @return 用户对象；不存在时返回 null
 * @throws IllegalArgumentException id 不大于 0 时抛出
 */
User findById(long id) {
    return null;
}
```

| 常用标签 | 用途 |
| --- | --- |
| `@param` | 说明参数 |
| `@return` | 说明返回值，`void` 方法不写 |
| `@throws` / `@exception` | 说明可能抛出的异常 |
| `@see` | 关联参考类、方法、文档 |
| `@since` | 标记从哪个版本加入 |
| `@deprecated` | 标记不推荐继续使用，并说明替代方案 |
| `@author` | 标记作者，团队项目通常不用 |
| `@version` | 标记版本，现代项目通常交给 Git |
| `@apiNote` | 写 API 使用说明 |
| `@implSpec` | 写实现必须遵守的约束 |
| `@implNote` | 写当前实现的补充说明 |

`javadoc 文件.java` 可以生成 HTML 文档。项目里更常见的是由 Maven、Gradle、IDE 或 CI 调用 Javadoc 工具。
</details>

### 语句、表达式与控制流
<details>
<summary></summary>

Java 代码块用 `{}` 包起来。能单独执行的结构叫语句；能计算出值或触发副作用的结构叫表达式。

| 类别 | 写法 |
| --- | --- |
| 空语句 | `;` |
| 代码块 | `{ statement1; statement2; }` |
| 局部变量声明语句 | `int n = 1;` |
| 表达式语句 | 赋值、前置自增、前置自减、后置自增、后置自减、方法调用、对象创建 |
| 分支语句 | `if`、`if-else`、`switch` |
| 循环语句 | `while`、`do-while`、传统 `for`、增强 `for` |
| 跳转语句 | `break`、`continue`、`return`、`throw` |
| 标签语句 | `label: statement`，可配合带标签的 `break` 或 `continue` |

- `if` 的条件必须是 `boolean`，不能把数字当真假值

    ```java
    int count = 1;
    // if (count) {}      // 编译错误
    if (count > 0) {}     // 合法
    ```

- `switch` 先分传统语句和表达式

    ```java
    int level = 2;

    switch (level) {
        case 1:
            System.out.println("low");
            break;
        case 2:
            System.out.println("middle");
            break;
        default:
            System.out.println("unknown");
    }

    String label = switch (level) {
        case 1 -> "low";
        case 2 -> "middle";
        default -> "unknown";
    };
    ```

    - `switch` 规则

        - 传统 `case:` 写法会继续向下执行，通常需要 `break`。
        - `case ->` 写法不会向下穿透。
        - `switch` 表达式必须产生结果；代码块形式用 `yield` 返回分支结果。
        - 传统 `switch` 选择值支持 `byte`、`short`、`char`、`int`、`Byte`、`Short`、`Character`、`Integer`、`String`、枚举类型。
        - `long`、`float`、`double`、`boolean` 不能作为传统 `switch` 选择值。
        - `case` 标签不能重复；传统常量 `case` 必须是编译期常量或枚举常量。
        - `default` 最多写一个，可以放在任意位置；为了阅读，通常放最后。

- 循环规则

    ```java
    while (condition) {
        // 先判断，再执行
    }

    do {
        // 至少执行一次
    } while (condition);

    for (int i = 0; i < 3; i++) {
        // 初始化；条件；迭代
    }

    for (int value : values) {
        // 增强 for
    }
    ```

- 增强 `for` 规则

    - 格式：`for (元素类型 元素名 : 遍历对象) { ... }`。
    - 遍历对象只能是数组，或实现了 `Iterable` 的对象。
    - `List`、`Set` 可直接增强 `for`。
    - `Map` 不能直接增强 `for`；遍历键值对用 `entrySet()`，遍历键用 `keySet()`，遍历值用 `values()`。
    - 循环变量是每次迭代拿到的元素值副本；给循环变量重新赋值，不会替换数组或集合中的元素。
    - 遍历集合时不要直接改集合结构；需要删除元素时用 `Iterator.remove()` 或收集后统一删除。
</details>

### 方法

```java
可选修饰符 返回值类型 方法名(参数类型 参数名, 参数类型 参数名) 可选throws声明 {
    方法体
}
```

- 返回值规则

    - `void` 表示没有返回值；可以写 `return;` 提前结束。
    - 非 `void` 方法必须保证每条正常结束路径都 `return` 一个兼容值。
    - 方法可以通过 `throw` 异常结束，此时不需要再写正常返回值。
    - 返回引用类型时，返回的是引用值；不是对象拷贝。

- 方法签名只看方法名和参数类型列表

    ```java
    int sum(int a, int b) { return a + b; }
    int sum(int a, int b, int c) { return a + b + c; }
    long sum(long a, long b) { return a + b; }
    ```

- 重载（Overload）成立条件

    - 方法名相同。
    - 参数个数不同，或参数类型不同，或参数类型顺序不同。
    - 不构成重载

        - 返回值类型不同不构成重载。
        - 参数名不同不构成重载。
        - 访问修饰符不同不构成重载。
        - `throws` 声明不同不构成重载。

- 重载解析简化顺序

    1. 优先选择不需要装箱、拆箱、可变参数的普通调用；这里包含基本类型拓宽和引用向上转型。
    2. 再考虑需要装箱或拆箱的普通调用。
    3. 最后考虑可变参数调用。
    4. `null` 可匹配引用类型；多个互不隶属的引用类型同时匹配时会编译报“调用不明确”。

- 可变参数规则

    ```java
    int sum(int... nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        return total;
    }
    ```

    - 写法：`类型... 变量名`。
    - 一个方法最多只能有一个可变参数。
    - 可变参数必须放在参数列表最后。
    - 方法体内，可变参数按数组使用。
    - 调用时可传 0 个实参、1 个实参、多个实参、同类型数组。

        ```java
        sum();                    // nums 长度为 0
        sum(1);                   // nums 长度为 1
        sum(1, 2, 3);             // nums 长度为 3
        sum(new int[]{1, 2, 3});  // 直接传数组
        ```
    - 传 `null` 时要小心：`sum(null)` 会把 `nums` 变成 `null`，方法体内访问 `nums.length` 会抛 `NullPointerException`。

- 调用方式按归属区分

    - 静态方法属于类，推荐写 `类名.静态方法()`。
    - 实例方法属于对象，写 `对象引用.实例方法()`。
    - 构造器不是方法，只能通过 `new 类名(...)` 或构造器内部的 `this(...)`、`super(...)` 调用。
    - “成员方法”容易产生歧义，建议直接说“静态方法”或“实例方法”。

### 数组

数组是引用类型；数组对象在堆中；数组长度创建后不能改变；元素类型在编译期固定。

```java
int[] nums;   // 推荐
int nums2[];  // 合法，不推荐
```

- 初始化写法

    ```java
    int[] a = new int[3];           // 动态初始化：[0, 0, 0]
    int[] b = {10, 20, 30};         // 静态初始化简写
    int[] c = new int[]{10, 20, 30};

    int[] d;
    d = new int[]{10, 20, 30};      // 声明和赋值分开时必须写 new int[]{...}
    // d = {10, 20, 30};            // 编译错误
    // int[] e = new int[3]{1, 2, 3}; // 编译错误：长度和初始化列表不能同时写
    ```

- 访问、修改、长度

    ```java
    int[] nums = {10, 20, 30};
    System.out.println(nums[0]);     // 10
    nums[1] = 99;
    System.out.println(nums.length); // 3
    ```

    - 下标从 `0` 开始。
    - 最后一个下标是 `length - 1`。
    - 下标小于 `0` 或大于 `length - 1`，抛 `ArrayIndexOutOfBoundsException`。
    - 数组变量可以是 `null`；此时访问元素或 `.length` 会抛 `NullPointerException`。
    - 长度可以是 `0`，例如 `new int[0]`。

- 遍历数组

    ```java
    int[] nums = {10, 20, 30};

    for (int i = 0; i < nums.length; i++) {
        nums[i] = nums[i] + 1; // 需要下标时用传统 for
    }

    for (int num : nums) {
        System.out.println(num); // 只读取元素时用增强 for
    }
    ```

- 复制数组

    - `arr.clone()`：浅拷贝一维数组。
    - `Arrays.copyOf(arr, newLength)`：复制并可改变长度。
    - `System.arraycopy(src, srcPos, dest, destPos, length)`：把一段元素复制到目标数组。
    - 二维数组复制时，外层数组复制后，内层数组引用仍可能指向原来的内层数组。

- 多维数组

    ```java
    int[][] matrix1 = new int[3][4]; // 3 行，每行 4 列
    int[][] matrix2 = new int[3][];  // 先建外层，内层稍后单独建

    matrix2[0] = new int[]{1, 2, 3};
    matrix2[1] = new int[]{4, 5};
    matrix2[2] = new int[]{6};

    int[][][] cube = {{{1, 2}}, {{3, 4}}};
    ```

    Java 的多维数组本质是“数组里的元素还是数组”，所以可以是不规则数组，也叫锯齿数组。

- 数组协变陷阱

    ```java
    String[] names = {"A"};
    Object[] objects = names;       // 合法：数组协变
    // objects[0] = new Object();   // 运行时抛 ArrayStoreException
    ```

    数组知道自己的运行时元素类型。`String[]` 可以赋给 `Object[]`，但不能真的存入非 `String` 对象。

- <details>

    <summary>稀疏数组</summary>

    稀疏数组不是 Java 内置类型，而是一种压缩存储思路：当二维数组中大部分元素都是默认值 `0` 时，只保存有意义的数据。

    一种表示方式是 `int[][] sparse`，每行 3 列：`行下标`、`列下标`、`值`。第 0 行保存原数组信息：`总行数`、`总列数`、`有效值个数`。

    ```java
    int[][] sparse = {
        {11, 11, 2},
        {1, 2, 1},
        {2, 3, 2}
    };
    /*
        原数组是 11 行 11 列，一共有 2 个非 0 值：
        array[1][2] = 1
        array[2][3] = 2
        其他位置默认值是 0
    */
    ```
    </details>

### 面向对象

OO = Object-Oriented，面向对象思想。OOP = Object-Oriented Programming，面向对象编程。Java 的 OOP 重点是：用类型组织代码，用对象承载状态，用方法表达行为，用继承和接口表达可替换关系。

```text
包 package
└─ 顶级类型 top-level type
    ├─ class：类
    ├─ interface：接口
    ├─ enum：枚举（特殊类）
    ├─ @interface：注解接口
    └─ record：记录（特殊类）

类 class
├─ 字段 field
│  ├─ 实例字段：属于对象
│  └─ 静态字段：属于类
├─ 方法 method
│  ├─ 实例方法：通过对象调用，可参与运行时多态
│  └─ 静态方法：通过类调用，不参与运行时多态
├─ 构造器 constructor：创建对象时初始化对象
├─ 实例初始化代码块 {}：每次 new 对象时执行
├─ 静态初始化代码块 static {}：类初始化时执行一次
└─ 嵌套类型 nested type：写在类型内部的类型

对象 object / instance
├─ 由 new 创建
├─ 拥有实例字段
├─ 可调用实例方法
└─ 可通过类共享静态字段和静态方法
```

- 类、对象、成员与初始化

    类是对象的模板，定义状态和行为；对象是类在运行期创建出来的实例。

    ```java
    class User {
        private String name;          // 实例字段
        private long createdAt;       // 实例字段
        private static int total;     // 静态字段

        static {                      // 静态初始化代码块：类初始化时执行一次
            total = 0;
        }

        {                             // 实例初始化代码块：每次 new 对象时执行
            createdAt = System.currentTimeMillis();
        }

        User(String name) {           // 构造器
            this.name = name;
            total++;
        }

        String getName() {            // 实例方法
            return name;
        }

        static int getTotal() {       // 静态方法
            return total;
        }
    }
    ```

    - 成员归属

        | 成员 | 归属 | 调用方式 |
        | --- | --- | --- |
        | 实例字段 | 对象 | `对象引用.字段`，通常字段设为 `private` |
        | 实例方法 | 对象 | `对象引用.方法()` |
        | 静态字段 | 类 | `类名.字段` |
        | 静态方法 | 类 | `类名.方法()` |
        | 构造器 | 类的创建逻辑 | `new 类名(...)` |
        | 实例初始化代码块 | 对象初始化过程 | 不手动调用 |
        | 静态初始化代码块 | 类初始化过程 | 不手动调用 |

    - 构造器规则

        - 构造器名必须与类名相同。
        - 构造器没有返回值类型，不能写 `void`。
        - 构造器可以重载。
        - 没写任何构造器时，编译器生成一个无参构造器。
        - 手写任意构造器后，编译器不再生成无参构造器。
        - 构造器第一行可以写 `this(...)` 调用本类其他构造器。
        - 构造器第一行可以写 `super(...)` 调用父类构造器。
        - 没写 `this(...)` 或 `super(...)` 时，编译器默认插入 `super()`（没有默认调用`this(...)`的场景）。
        - `this(...)` 与 `super(...)` 都要求第一行，所以一个构造器不能同时直接写这两个调用。
        - 父类没有无参构造器时，子类构造器必须显式写 `super(...)` 并传入匹配参数。

    - 初始化顺序按这条链记

        1. 首次主动使用某个类时，先初始化父类，再初始化当前类。
        2. 同一个类中，静态字段赋值和静态代码块按源码顺序执行一次。
        3. `new` 对象时，先为整条继承链上的实例字段填默认值。
        4. 构造器链从子类构造器入口开始，最终先进入最顶层父类构造。
        5. 对继承链上的每一层类：先执行父类构造流程；回到当前类后，按源码顺序执行当前类的实例字段赋值和实例初始化代码块；最后执行当前类构造器正文。

        ```java
        class Parent {
            static { System.out.println("Parent static"); }
            { System.out.println("Parent init"); }
            Parent() { System.out.println("Parent constructor"); }
        }

        class Child extends Parent {
            static { System.out.println("Child static"); }
            { System.out.println("Child init"); }
            Child() { System.out.println("Child constructor"); }
        }
        ```

        执行 `new Child()` 时，输出顺序是：

        ```text
        Parent static
        Child static
        Parent init
        Parent constructor
        Child init
        Child constructor
        ```

    - `this` 与 `super`

        - `this` 表示当前对象。
        - `this.field` 访问当前对象字段，可解决局部变量遮蔽字段的问题。
        - `this(...)` 调用本类其他构造器，只能写在构造器第一行。
        - `super` 表示父类视角。
        - `super.field`、`super.method()` 访问父类中可见的成员。
        - `super(...)` 调用父类构造器，只能写在构造器第一行。

- 封装

    封装不是“写 Getter / Setter”本身，而是把对象内部状态和实现细节收起来，只暴露稳定、必要、可校验的操作。

    - 字段通常写 `private`。
    - 需要外部读取时提供 Getter。
    - 需要外部修改时提供 Setter，并在 Setter 中做校验。
    - 不希望外部修改时只提供 Getter，或返回防御性拷贝。
    - 对集合字段，不要直接返回内部可变集合引用；可返回不可变视图或拷贝。
    - 封装目标是降低调用方对内部结构的依赖，使字段名、存储方式、校验逻辑变化时不影响外部代码。

- 继承、组合、转型与 `instanceof`

    继承表达 is-a 关系；组合表达 has-a 关系。只为复用代码而继承，后期容易让父子类语义变形。

    ```java
    class Animal {}
    class Dog extends Animal {}          // 狗是动物：is-a

    class Engine {}
    class Car {
        private Engine engine;           // 车有发动机：has-a
    }
    ```

    - 继承规则

        - Java 类是单继承：只能 `extends` 一个直接父类，不能 `extends` 接口。
        - Java 类可 `implements` 多个接口；接口可 `extends` 多个接口。
        - 除 `Object` 自身外，所有类最终继承自 `java.lang.Object`。
        - 构造器不会被继承。
        - 父类 `private` 成员不能被子类直接访问。
        - 子类可以继承父类可见的实例方法，并可重写其中可重写的方法。
        - 子类可以定义与父类同名字段，这叫字段隐藏，不建议滥用。

            >隐藏：子类同名字段，子类同签名静态方法。

    - 转型

        ```text
        类型转换：大概念
        ├─ 基本类型转换：int -> long、double -> int
        ├─ 装箱 / 拆箱：int <-> Integer
        ├─ 引用类型转换
        │  ├─ 转型：继承 / 接口 / 多态，如 Dog -> Animal、Animal -> Dog
        │  └─ 其他：数组、泛型、null 有各自规则，不都叫“转型”
        └─ 字符串转换：任意值 -> String 表示，常见于字符串拼接；不是对象转型
        ```

        - 向上转型总是安全

            ```java
            Dog dog = new Dog();
            Animal animal = dog;
            Object obj = dog;
            ```

        - 向下转型需要真实对象支持

            ```java
            Animal animal = new Dog();
            Dog d1 = (Dog) animal; // 安全

            Animal other = new Animal();
            // Dog d2 = (Dog) other; // 运行时抛 ClassCastException
            ```

    - `instanceof` 规则

        - 左侧必须是引用类型表达式或 `null`。
        - 右侧必须是可在运行期检查的类型。
        - 基本类型不能直接用 `instanceof`。
        - 左侧为 `null` 时结果为 `false`。
        - 编译器会先检查两边是否可能兼容，不可能兼容时直接编译错误。
        - 运行期看左侧对象真实类型；真实类型是右侧类本身、右侧类的子类、右侧接口的实现类、右侧接口子接口的实现类时，结果为 `true`。
        - 右侧不能写不可运行期检查的泛型实参，例如 `obj instanceof List<String>` 不合法；通常写 `obj instanceof List<?>`。

        ```java
        interface Living {}
        interface Pet extends Living {}
        class Dog extends Animal implements Pet {
            void bark() {}
        }

        Animal a = new Dog();

        a instanceof Animal; // true
        a instanceof Dog;    // true
        a instanceof Pet;    // true
        a instanceof Living; // true
        null instanceof Dog; // false

        if (a instanceof Dog dog2) { // Java 16+ 模式匹配
            dog2.bark();
        }
        ```

- 多态与重写

    运行时多态成立需要三件事：存在继承或接口实现关系；父类或接口引用指向子类或实现类对象；调用的是可被重写的实例方法。

    ```java
    class Person {
        String name = "person";
        void talk() { System.out.println("person"); }
        static void type() { System.out.println("Person"); }
    }

    class Student extends Person {
        String name = "student";
        @Override
        void talk() { System.out.println("student"); }
        static void type() { System.out.println("Student"); }
    }

    Person p = new Student();
    p.talk();              // student：实例方法运行期看真实对象
    System.out.println(p.name); // person：字段编译期看声明类型
    p.type();              // Person：静态方法编译期看声明类型，不推荐用对象调用静态方法
    ```

    - 编译期和运行期的分工

        - 编译期看引用的声明类型，决定能不能访问某个成员。
        - 运行期看真实对象类型，决定重写后的实例方法执行哪一个实现。
        - 字段不参与运行时多态。
        - 静态方法不参与运行时多态；子类同名静态方法叫隐藏。

            >隐藏：子类同名字段，子类同签名静态方法。
        - `private` 方法不能被重写。
        - `final` 方法不能被重写。
        - 构造器不能被重写。

    - 重写（Override）规则

        - 发生在父子类或接口实现关系中。
        - 方法名相同。
        - 参数类型列表相同。
        - 返回类型相同，或返回父方法返回类型的子类型。
        - 访问权限不能比父方法更窄。
        - 受检异常范围不能比父方法更宽；运行时异常（RuntimeException 及其子类）不受这条限制。
        - 建议总是写 `@Override`，让编译器帮你检查。

- 抽象类、接口、枚举与记录

    - 抽象类（`abstract class`）

        抽象类是不能直接实例化的父类模板，适合给子类提供共同状态、共同实现，并把差异行为留给子类补全。

        | 分类 | 知识点 |
        | --- | --- |
        | 创建规则 | 不能直接 `new` 抽象类 |
        | 成员能力 | 可以有实例字段、静态字段、普通实例方法、静态方法、`final` 方法、构造器、实例初始化代码块、静态初始化代码块 |
        | 抽象方法 | 可以有抽象方法，也可以没有抽象方法；抽象方法只有方法签名，没有方法体 |
        | 类声明规则 | 只要类中声明抽象方法，这个类必须声明为 `abstract` |
        | 子类实现规则 | 具体子类必须实现继承到的所有抽象方法；抽象子类可以不实现、部分实现或全部实现继承到的抽象方法 |
        | 构造规则 | 抽象类可以有构造器；创建子类对象时，父类抽象类部分仍会先初始化 |
        | 修饰符限制 | 抽象方法不能写 `private`、`static`、`final`，因为 `private` 无法被子类重写，`static` 属于类本身不走重写，`final` 禁止重写 |
        | 接口关系 | 抽象类可以实现接口；它可以不实现、部分实现或全部实现接口中的抽象方法 |
        | 默认方法关系 | 抽象类实现接口时，接口的 `default` 方法可按需重写；未实现的抽象方法留给具体子类 |
        | 使用边界 | 适合表达“有共同状态和部分共同实现”的父类型 |

    - 接口（`interface`）

        接口定义能力、契约和多态边界，强调“对象能做什么”，用于解耦调用方与具体实现。

        | 分类 | 知识点 |
        | --- | --- |
        | 创建规则 | 不能直接 `new` 接口 |
        | 实现方式 | 通常由普通类或抽象类通过 `implements` 实现；也可以通过匿名类创建接口实现对象 |
        | 函数式创建 | 函数式接口可以用 lambda 表达式或方法引用创建实现对象 |
        | 状态限制 | 没有构造器；没有普通初始化代码块；不能声明实例字段 |
        | 字段规则 | 字段默认且只能是 `public static final`，必须显式初始化 |
        | 抽象方法 | 抽象方法默认是 `public abstract`；实现类重写时必须写成 `public` |
        | 默认方法 | 可声明 `default` 方法，供实现类继承默认实现；`default` 方法是实例方法，可被实现类重写 |
        | 静态方法 | 可声明 `static` 方法，通过 `接口名.方法名()` 调用 |
        | 私有方法 | Java 9+ 可声明 `private` 方法和 `private static` 方法，供接口内部复用 |
        | 类实现接口 | 一个类可以实现多个接口；普通类必须实现接口中所有未实现的抽象方法 |
        | 抽象类实现接口 | 抽象类可以不实现、部分实现或全部实现接口中的抽象方法 |
        | 接口继承接口 | 一个接口可以继承一个或多个接口 |
        | 默认方法冲突 | 多个接口的 `default` 方法冲突时，实现类必须重写并明确选择行为 |
        | 类优先规则 | 类继承来的实例方法优先于接口默认方法 |
        | 函数式接口 | 只有一个抽象方法的接口叫函数式接口，可用 `@FunctionalInterface` 标注 |
        | 标记接口 | 没有抽象方法的接口可以作为标记接口，例如 `Serializable` |
        | 封闭接口 | Java 17+ 的 `sealed interface` 可以限制允许实现它的类型 |
        | 使用边界 | 只表达能力规范时，优先考虑接口；需要共享状态、构造逻辑或较多部分实现时，优先考虑抽象类 |

        <details>
        <summary>多个接口的<code>default</code>方法冲突时，实现类必须重写并明确选择行为</summary>

        ```java
        interface A {
            default void hello() {
                System.out.println("A");
            }
        }

        interface B {
            default void hello() {
                System.out.println("B");
            }
        }

        class User implements A, B {
            @Override
            public void hello() {
                A.super.hello(); // 明确选择 A 的默认实现
                // 或者 B.super.hello();
                // 或者自己写全新的逻辑
            }
        }
        ```
        </details>

    | 抽象类与接口对比项 | 抽象类 | 接口 |
    | --- | --- | --- |
    | 直接实例化 | 不能直接 `new` | 不能直接 `new` |
    | 继承 / 实现数量 | 类只能 `extends` 一个父类 | 类可以 `implements` 多个接口 |
    | 继承其他类型 | 抽象类可以继承一个类、实现多个接口 | 接口可以继承一个或多个接口 |
    | 实例字段 | 可以有 | 不能有 |
    | 构造器 | 可以有，供子类初始化父类部分 | 没有 |
    | 普通实例方法 | 可以有 | 通过 `default` 提供默认实例方法 |
    | 静态方法 | 可以有 | 可以有，通过接口名调用 |
    | 私有辅助方法 | 可以有 | Java 9+ 可以有 |
    | 抽象方法实现压力 | 具体子类必须实现未实现的抽象方法 | 普通实现类必须实现未实现的抽象方法 |
    | 主要用途 | 复用共同状态、构造逻辑、部分实现 | 定义能力、契约、多实现多态边界 |

    - 枚举（`enum`）

        | 分类 | 知识点 |
        | --- | --- |
        | 定位 / 边界 | 枚举是特殊类，用于表达编译期固定、运行期不动态增删的一组实例：状态、类型、选项、策略分支；<br>不适合直接写死成枚举的场景：值需要运行期动态增删、频繁配置或来自数据库字典时 |
        | 声明 / 类关系 | `enum Status { NEW, DONE }`；枚举不能声明类型参数（~~enum Status<T> { NEW, DONE }~~），方法可以声明自己的泛型；隐式继承 `java.lang.Enum<本枚举>`，不能再 `extends` 其他类，可 `implements` 接口，外部都不能继承枚举 |
        | 常量 / 实例本质 | 常量必须写在枚举体最前，逗号分隔；每个常量都是 `public static final` 固定实例，类加载时创建一次；外部只能引用，不能 `new`、继承或重新赋值 |
        | 分号 / 构造参数 | 只有常量时 `;` 可省略；后面还有字段、构造器、方法或静态块时必须写 `;`；<br>常量可不带参数，也可带构造参数；构造器可重载，实参必须匹配某个构造器 |
        | 构造 / 初始化 | 构造器只能 `private` 或省略；每个常量初始化时调用一次；构造器/实例初始化中不能直接访问本枚举的非编译期常量静态字段，静态索引、缓存放 `static` 块 |
        | 成员 / 常量类体 | 可有实例字段/方法、静态字段/方法、静态初始化块、嵌套类型；<br>常量状态通常用 `private final` 字段保存；常量后可写 `{}` 覆盖方法或实现抽象方法，枚举声明抽象方法时每个常量都必须实现 |
        | 内置 API / 顺序 | 编译器生成 `values()`、`valueOf(String)`；`java.lang.Enum` 提供 `name()`、`ordinal()`、`compareTo()`、`getDeclaringClass()`；`values()` 返回一个新的数组，数组元素是按声明顺序排列的枚举常量引用 |
        | 比较 / 分支 / 集合 | 枚举常量是固定单例，比较优先用 `==`；`switch` 支持枚举；自然顺序、`compareTo()`、`ordinal()` 都按声明顺序；多选用 `EnumSet`，枚举 key 用 `EnumMap` |
        | 输出 / 持久化 | `name()` 来自常量名；`toString()` 可覆盖，仅适合展示；持久化优先存业务码或 `name()`，不要存 `ordinal()`（返回枚举常量在声明时的顺序下标，从 0 开始）；单常量枚举可实现单例，反序列化仍回到同一个常量 |
        | 异常 / 易错点 | `valueOf(String)` 按常量名精确匹配，大小写敏感，不认 `toString()` 或业务码；找不到名称抛 `IllegalArgumentException`，传 `null` 抛 `NullPointerException`；`switch` 未显式处理 `null` 时会抛空指针异常；`EnumSet` 不允许 `null` 元素，`EnumMap` 不允许 `null` key、允许 `null` value；常量类体会生成特殊子类，判断声明枚举类型用 `getDeclaringClass()` |

        <details>
        <summary>e.g. </summary>

        ```java
        import java.util.EnumMap;
        import java.util.EnumSet;

        // 约定实现类必须提供展示名称；枚举可以 implements 接口。
        interface Labeled {
            String label();
        }

        // OrderStatus 是一组固定订单状态：外部只能使用这些常量，不能 new 新状态。
        enum OrderStatus implements Labeled {
            // UNKNOWN 不写构造参数，会调用无参构造器。
            UNKNOWN {
                @Override
                boolean canCancel() { return false; } // 未知状态不可取消
            },

            // NEW/PAID/SHIPPED/REFUNDED 写了构造参数，会调用 OrderStatus(String label)。
            NEW("新建") {
                @Override
                boolean canCancel() { return true; } // 新建状态可取消
            },
            PAID("已支付") {
                @Override
                boolean canCancel() { return true; } // 已支付但未发货，仍可取消
            },
            SHIPPED("已发货") {
                @Override
                boolean canCancel() { return false; } // 已发货后不可取消
            },
            REFUNDED("已退款") {
                @Override
                boolean canCancel() { return false; } // 已退款后不可取消
            };

            // 每个枚举常量各保存一份 label；通常用 final 表示创建后不再改变。
            private final String label;

            OrderStatus() { // 无参构造器：供 UNKNOWN 使用
                this("未知");
            }

            OrderStatus(String label) { // 枚举构造器默认 private，只能由枚举常量调用
                this.label = label;
            }

            // 实现 Labeled 接口，返回展示名称。
            @Override
            public String label() { return label; }

            // 抽象方法：每个枚举常量都必须在自己的常量类体中实现。
            abstract boolean canCancel();

            // 普通实例方法：所有常量都能调用。
            public boolean terminal() {
                return this == SHIPPED || this == REFUNDED;
            }

            // 自定义展示文本；不要把 toString() 当作稳定持久化值。
            @Override
            public String toString() { return "OrderStatus:" + label; }
        }

        class EnumDemo {
            public static void main(String[] args) {
                // 1. 最基础用法：直接引用枚举常量。
                OrderStatus status = OrderStatus.PAID;
                System.out.println(status); // OrderStatus:已支付，println 会调用 toString()

                // 2. 枚举常量是固定单例，比较优先用 ==。
                System.out.println(status == OrderStatus.PAID); // true

                // 3. valueOf(String) 按常量名解析，字符串必须精确匹配 PAID。
                OrderStatus parsed = OrderStatus.valueOf("PAID");
                System.out.println(status == parsed); // true

                // 4. name() 是代码里的常量名；label() 是业务展示文案。
                System.out.println(status.name());  // PAID
                System.out.println(status.label()); // 已支付

                // 5. 枚举实现接口后，可以按接口类型统一调用方法。
                Labeled labeled = status;
                System.out.println(labeled.label()); // 已支付

                // 6. values() 遍历所有枚举常量，顺序就是声明顺序。
                for (OrderStatus item : OrderStatus.values()) {
                    System.out.println(item.name() + " -> " + item.label());
                }
                // UNKNOWN -> 未知
                // NEW -> 新建
                // PAID -> 已支付
                // SHIPPED -> 已发货
                // REFUNDED -> 已退款

                // 7. switch 支持枚举，适合按状态分支。
                String action;
                switch (status) {
                    case NEW:
                    case PAID:
                        action = "allow cancel";
                        break;
                    case SHIPPED:
                        action = "track";
                        break;
                    case REFUNDED:
                        action = "refund finished";
                        break;
                    case UNKNOWN:
                    default:
                        action = "unknown";
                        break;
                }
                System.out.println(action); // allow cancel

                // 8. 调用每个常量自己的行为：PAID 的 canCancel() 返回 true。
                System.out.println(status.canCancel()); // true

                // 9. 调用普通实例方法：PAID 还不是终态。
                System.out.println(status.terminal()); // false

                // 10. ordinal() 是声明顺序下标，从 0 开始；只适合临时查看，不适合存数据库。
                System.out.println(status.ordinal()); // 2

                // 11. compareTo() 按声明顺序比较；NEW 在 SHIPPED 前面，所以结果为负数。
                System.out.println(OrderStatus.NEW.compareTo(OrderStatus.SHIPPED)); // -2

                // 12. EnumSet 存一组枚举值，适合表达“哪些状态属于同一类”。
                EnumSet<OrderStatus> cancellable = EnumSet.of(OrderStatus.NEW, OrderStatus.PAID);
                System.out.println(cancellable.contains(status)); // true

                // 13. EnumMap 用枚举当 key，适合给不同状态配置额外信息。
                EnumMap<OrderStatus, String> labels = new EnumMap<>(OrderStatus.class);
                labels.put(OrderStatus.NEW, "待处理");
                labels.put(OrderStatus.SHIPPED, "配送中");
                System.out.println(labels.get(OrderStatus.SHIPPED)); // 配送中
            }
        }
        ```
        </details>

    - <details>

        <summary>记录（<code>record</code>，Java 16+）</summary>

        | 分类 | 知识点 |
        | --- | --- |
        | 定位 | 固定组件的数据值：DTO、配置值、返回值、复合键、不可变值对象 |
        | 声明 | `record User(String name, int age) {}`；可泛型/可变参数，组件不写访问修饰符 |
        | 组件 / 生成 | 组件生成 `private final` 字段、同名访问器、规范构造器、`equals`、`hashCode`、`toString`；无 `getXxx()` |
        | 构造器 | 可写紧凑或完整规范构造器；额外构造器首行必须 `this(...)` |
        | 成员 / 字段 | 可有实例方法、静态字段方法、静态块、嵌套类型；不能有额外实例字段和实例初始化块 |
        | 可变性 | 组件引用不可重新赋值，但指向对象可能可变；集合/数组组件通常做防御性拷贝 |
        | 接口 / 继承 | 可实现接口、重写组件访问器；隐式 `final`、继承 `java.lang.Record`，不能 `extends` 其他类或 `abstract` |
        | 嵌套 / 模式 | 可顶级、成员、局部；嵌套记录隐式 `static`；Java 21+ record pattern 可解构 |
        | 使用边界 | 不适合可变生命周期、对象身份、复杂继承层级的实体模型 |

        ```java
        import java.util.*;

        interface HasCode { String code(); }

        record Product<T>(String code, String name, int cents, List<T> tags) implements HasCode {
            public static final String CURRENCY = "CNY";

            public Product {
                code = Objects.requireNonNull(code, "code").trim();
                name = Objects.requireNonNull(name, "name").trim();
                if (code.isEmpty() || name.isEmpty() || cents < 0) throw new IllegalArgumentException();
                tags = List.copyOf(tags);
            }

            public Product(String code, String name, int cents) {
                this(code, name, cents, List.of());
            }

            @Override
            public String code() { return code; }

            public boolean free() { return cents == 0; }

            public static Product<String> sample(String code) {
                return new Product<>(code, "sample", 0, List.of("demo"));
            }

            record Snapshot(String code, int cents) {}
        }

        record Point(int x, int y) {}

        class RecordDemo {
            public static void main(String[] args) {
                Product<String> p = Product.sample("A001");
                String code = p.code();
                int cents = p.cents();
                boolean same = p.equals(new Product<>("A001", "sample", 0, List.of("demo")));
                String text = p.toString();
                Product.Snapshot snapshot = new Product.Snapshot(p.code(), p.cents());

                Object obj = new Point(1, 2);
                if (obj instanceof Point(int x, int y)) {
                    System.out.println(x + y);
                }
            }
        }
        ```
    </details>

    | 需求 | 选择建议 |
    | --- | --- |
    | 有共同状态和部分实现 | 抽象类 |
    | 只约定能力或协议 | 接口 |
    | 值集合固定 | 枚举 |
    | 只承载一组不可重新赋值的数据 | 记录 |

- 嵌套类型

    嵌套类型是声明在另一个类型内部，或声明在方法、构造器、代码块内部的类型；顶级类型写在源文件第一层，不算嵌套类型。

    按“声明位置 + 是否绑定外部对象”穷举：

    | 大类 | 类型形式 | 写法 / 位置 | 外部对象 | 局部变量捕获 |
    | --- | --- | --- | --- | --- |
    | 成员类型 | 非静态成员类 | 类型成员位置：`class Inner {}` | 有 | 不涉及 |
    | 成员类型 | 静态成员类 | 类型成员位置：`static class Nested {}` | 无 | 不涉及 |
    | 成员类型 | 成员接口 | 类型成员位置：`interface I {}` | 无，隐式 `static` | 不涉及 |
    | 成员类型 | 成员枚举 | 类型成员位置：`enum E {}` | 无，隐式 `static` | 不涉及 |
    | 成员类型 | 成员注解接口 | 类型成员位置：`@interface A {}` | 无，隐式 `static` | 不涉及 |
    | 成员类型 | 成员记录 | 类型成员位置：`record R(...) {}` | 无，隐式 `static` | 不涉及 |
    | 局部类型 | 局部普通类 | 块内：`class L {}` | 可能有 | 可捕获 `final` 或事实不可变变量 |
    | 局部类型 | 局部接口 | 块内：`interface I {}` | 无，隐式 `static` | 不捕获 |
    | 局部类型 | 局部枚举 | 块内：`enum E {}` | 无，隐式 `static` | 不捕获 |
    | 局部类型 | 局部记录 | 块内：`record R(...) {}` | 无，隐式 `static` | 不捕获 |
    | 匿名类 | 匿名类 | `new 父类或接口(...) { ... }` 表达式 | 可能有 | 可捕获 `final` 或事实不可变变量 |

    >字段、方法、成员类型是成员；构造器和初始化代码块写在类体第一层，但不是成员。

    ```java
    class User {
      private String name;

      class Profile {
        String ownerName() {
          return User.this.name; // 非静态成员类访问外部对象
        }
      }

      static class Address {
      }

      interface Validator {
        boolean ok(String value);
      }

      enum Role {
        ADMIN, MEMBER
      }

      @interface FieldName {
      }

      record Pair(String key, String value) {
      }

      void test() {
        int base = 10;

        class LocalHelper {
          int value() {
            return base; // 局部普通类读取外部局部变量，base 必须是 final 或事实不可变
          }
        }

        enum LocalRole {
          TEMP
        }

        record LocalPair(String key, String value) {}

        interface LocalValidator {
          boolean ok(String value);
        }

        Runnable task = new Runnable() {
          @Override
          public void run() {
            System.out.println(base); // 匿名类也要求 base 是 final 或事实不可变
          }
        };

        task.run();
      }

      public static void main(String[] args) {
        // 创建方式
        User user = new User();
        User.Profile profile = user.new Profile(); // 外部对象.new 内部类()：绑定到 user

        User.Address address = new User.Address(); // 静态嵌套类：不需要外部对象
      }
    }
    ```

    - 创建或使用语法单独记

        | 目标 | 写法 | 含义 |
        | --- | --- | --- |
        | 非静态成员类，在外部类外创建 | `outer.new Inner()` | 先有外部对象，再创建绑定到它的内部类对象 |
        | 非静态成员类，在外部类实例代码中创建 | `new Inner()` | 默认绑定当前 `this` |
        | 静态成员类 / 成员记录 | `new Outer.Nested(...)` | 只用外部类型名限定类型，不绑定外部对象 |
        | 成员枚举 | `Outer.Role.ADMIN` | 通过外部类型名访问枚举常量 |
        | 局部普通类 / 局部记录 | 当前块内 `new LocalType(...)` | 只在声明所在块内可见 |
        | 局部枚举 | 当前块内 `LocalEnum.VALUE` | 只在声明所在块内可见 |
        | 接口 | 用类、匿名类或 lambda 实现 | 接口本身不直接创建对象 |
        | 匿名类 | `new 父类或接口(...) { ... }` | 声明匿名子类或接口实现类，并立刻创建对象 |

    - 细节规则

        - 内部类不是所有嵌套类型，只包括非 `static` 的嵌套类：非静态成员类、局部普通类、匿名类。
        - 非静态成员类一定持有关联外部对象；用 `Outer.this` 指明外部对象。
        - `outer.new Inner()` 里的 `outer` 是外部对象引用；如果是 `null`，运行期抛 `NullPointerException`。
        - 静态成员类、成员接口、成员枚举、成员注解接口、成员记录不持有关联外部对象，不能直接访问外部对象的实例字段或实例方法。
        - 成员接口、成员枚举、成员注解接口、成员记录隐式是 `static`；写在接口体内的成员类型还隐式是 `public`。
        - 外部类型和嵌套类型属于同一个 nest，可以互相访问对方的 `private` 成员。
        - 局部普通类和匿名类可以读取外部局部变量，但变量必须是 `final` 或事实不可变。
        - 局部接口、局部枚举、局部记录隐式是 `static`，不捕获外部局部变量，也不绑定外部对象。
        - 局部类型不能写访问控制修饰符、`static`、`sealed`、`non-sealed`。
        - 局部位置可以声明普通 `class`、`interface`、`enum`、`record`；不能声明局部`@interface`。
        - 匿名类没有类名，不能显式声明构造器；需要初始化逻辑时写实例初始化代码块。
        - 匿名类只能继承一个父类或实现一个接口；用于一次性实现，单抽象方法接口优先用 lambda。

### 异常处理：`try-catch-finally`、`throw`、`throws`
<details>
<summary></summary>

```text
Throwable
├─ Error：严重问题，通常不在业务代码中捕获
└─ Exception
    ├─ RuntimeException：运行时异常，不强制捕获
    └─ 非 RuntimeException 的 Exception：受检异常，必须捕获或继续声明 throws
```

- 编译器检查规则

    - 受检异常：`Throwable` 中不属于 `RuntimeException` 子类、也不属于 `Error` 子类的类型。
    - 非受检异常：`RuntimeException` 子类和 `Error` 子类。
    - 受检异常必须在当前方法内 `catch`，或在方法签名上 `throws`。
    - 非受检异常可以捕获，但编译器不强制。

- 常见运行时异常

    | 异常 | 常见原因 |
    | --- | --- |
    | `NullPointerException` | 对 `null` 调用字段、方法、数组长度 |
    | `ArrayIndexOutOfBoundsException` | 数组下标越界 |
    | `ClassCastException` | 向下转型时真实对象类型不匹配 |
    | `IllegalArgumentException` | 方法参数非法 |
    | `IllegalStateException` | 对象状态不允许当前操作 |
    | `NumberFormatException` | 字符串转数字失败 |
    | `ArithmeticException` | 整数除以 0 |
    | `UnsupportedOperationException` | 当前对象不支持该操作 |

- `try` 组合形式

    ```java
    try {
        risky();
    } catch (IOException e) {
        handle(e);
    }

    try {
        risky();
    } finally {
        cleanup();
    }

    try {
        risky();
    } catch (IOException e) {
        handle(e);
    } finally {
        cleanup();
    }

    try (BufferedReader reader = Files.newBufferedReader(path)) {
        return reader.readLine();
    } catch (IOException e) {
        throw new UncheckedIOException(e);
    }
    ```

- `catch` 规则

    - 多个 `catch` 时，子类异常写前面，父类异常写后面。
    - 如果先写 `catch (Exception e)`，后面再写 `catch (IOException e)` 会编译错误。
    - 多异常捕获可写 `catch (IOException | SQLException e)`。
    - 多异常捕获里的异常类型不能有父子关系。
    - 捕获后只记录日志但继续运行，要确认调用方能接受这个失败结果。
    - 捕获后重新抛出时，优先保留原异常作为 cause。

- `throw` 与 `throws`

    | 写法 | 位置 | 作用 |
    | --- | --- | --- |
    | `throw new IllegalArgumentException("id");` | 方法体内部 | 主动抛出一个异常对象 |
    | `void read() throws IOException` | 方法声明处 | 告诉调用方该方法可能抛出异常 |

    ```java
    void read(Path path) throws IOException {
        if (path == null) {
            throw new IllegalArgumentException("path 不能为空");
        }
        Files.readString(path);
    }
    ```

- `finally` 规则

    - `finally` 通常在 `try` 或 `catch` 结束后执行。
    - `finally` 常用于释放资源、恢复状态、清理临时数据。
    - 不建议在 `finally` 中写 `return`，因为它会覆盖 `try` 或 `catch` 中的返回值。
    - 不建议在 `finally` 中抛新异常，除非明确要覆盖原异常。
    - `System.exit(...)`、`Runtime.getRuntime().halt(...)`、JVM 崩溃、操作系统杀进程、机器断电、线程永远卡在 `try` 中时，`finally` 无法完成执行。

- `try-with-resources` 规则

    - 资源类型必须实现 `AutoCloseable`。
    - 小括号里声明的资源会自动关闭。
    - 多个资源按声明的反向顺序关闭。
    - `try` 中抛异常且关闭资源也抛异常时，关闭异常会作为 suppressed exception 挂到主异常上，可通过 `getSuppressed()` 读取。
    - 文件、网络连接、数据库连接、输入输出流优先使用这种写法。

- 自定义异常

    ```java
    class UserNotFoundException extends RuntimeException {
        UserNotFoundException(long id) {
            super("User not found: " + id);
        }
    }

    class ConfigLoadException extends Exception {
        ConfigLoadException(String message, Throwable cause) {
            super(message, cause);
        }
    }
    ```

- 业务参数错误通常用 `IllegalArgumentException`。
- 对象状态不允许操作通常用 `IllegalStateException`。
- 希望调用方被迫处理时继承 `Exception`。
- 希望调用方按业务需要选择处理时继承 `RuntimeException`。
</details>

### 泛型
泛型把“可变化的类型”抽象成参数，让类、接口、记录、方法和构造器在保持复用的同时获得编译期类型检查。Java 泛型主要靠**类型擦除**实现：编译期检查类型关系，编译后通常擦除成 `Object` 或第一个上界，运行期不会为 `List<String>`、`List<Integer>` 生成两套类。

- 核心术语

    | 术语 | 例子 | 含义 |
    | --- | --- | --- |
    | 类型形参 | `T`、`E`、`K`、`V` | 声明泛型时定义的类型变量 |
    | 类型实参 | `String`、`Integer`、`User` | 使用泛型时传入的具体引用类型 |
    | 参数化类型 | `List<String>` | 带具体类型实参的泛型类型 |
    | 原始类型 | `List` | 不带类型实参的兼容旧代码写法，会绕开泛型检查 |
    | 通配符 | `?`、`? extends Number` | 表示某个未知类型，只用于使用泛型的位置 |
    | 上界 | `<T extends Number>` | 限制 `T` 至少是某个父类型的子类型 |
    | 下界 | `? super Integer` | 只存在于通配符，表示未知类型是某个类型的父类型 |
    | 类型擦除 | `T -> Object` 或 `T -> 上界` | 编译后移除大多数泛型实参信息 |
    | 可具体化类型 | `String`、`int[]`、`List<?>` | 运行期能完整或足够确定表示的类型 |
    | 不可具体化类型 | `List<String>`、`T` | 运行期无法完整知道泛型实参的类型 |
    | 堆污染 | `List<String>` 中混入非 `String` | 常由原始类型、未经检查强转、泛型可变参数导致 |

- 泛型能力边界

    | 维度 | 规则 |
    | --- | --- |
    | 解决什么 | 编译期类型安全、API 复用、减少强转、表达输入输出类型关系 |
    | 不解决什么 | 运行期按泛型实参分派逻辑、运行期保存对象的具体泛型实参 |
    | 类型实参 | 只能是引用类型；`List<Integer>` 合法，`List<int>` 不合法 |
    | 类型形参命名 | 常用 `T`=type、`E`=element、`K/V`=key/value、`R`=return/result、`ID`=标识类型 |
    | 与继承关系 | `String extends Object` 不代表 `List<String> extends List<Object>` |
    | 与数组关系 | 数组协变且运行期检查；泛型默认不协变且主要编译期检查 |

- 声明位置穷举

    | 位置 | 写法 | 说明 |
    | --- | --- | --- |
    | 泛型类 | `class Box<T> {}` | 类型参数属于这个类的实例类型 |
    | 泛型接口 | `interface Repository<T, ID> {}` | 实现类可固定类型实参，也可继续保留类型参数 |
    | 泛型记录 | `record Pair<K, V>(K key, V value) {}` | 记录可以声明类型参数，Java 16+ 可用 |
    | 泛型方法 | `<T> T first(List<T> list) {}` | 类型参数写在返回值类型前，只在本方法内有效 |
    | 静态泛型方法 | `static <T> T id(T value) {}` | 静态方法不能使用类上的 `T`，需要自己声明 `<T>` |
    | 泛型构造器 | `<T> Holder(T value) {}` | 类型参数只属于本次构造调用，少见但合法 |
    | 泛型异常声明 | `<E extends Exception> void run() throws E` | 类型变量可用于 `throws`，但泛型类不能继承 `Throwable` |
    | 通配符类型 | `List<?>`、`List<? extends Number>` | 不是声明新类型形参，而是在使用处表达未知类型 |

    - 枚举和注解接口不能声明自己的泛型类型参数。
    - 类级类型参数可用于实例字段、实例方法、构造器、实例初始化块、成员类型声明；不能直接用于静态字段、静态初始化块、静态方法签名。
    - 方法级类型参数作用域只在该方法内；方法级 `<T>` 可以遮蔽类级 `T`，但不建议这样写。

- 使用位置穷举

    | 位置 | 例子 | 说明 |
    | --- | --- | --- |
    | 字段 | `private List<User> users;` | 约束字段保存的元素类型 |
    | 局部变量 | `List<String> names = new ArrayList<>();` | 左侧提供目标类型，右侧 diamond 可推断 |
    | 方法参数 | `void save(List<User> users)` | 调用方必须传入匹配的泛型类型 |
    | 方法返回值 | `Optional<User> findById(Long id)` | 调用方拿到带泛型约束的返回值 |
    | 构造调用 | `new Box<String>("A")`、`new Box<>("A")` | 可显式写类型实参，也可用 diamond 推断 |
    | 继承父类 | `class StringBox extends Box<String>` | 子类固定父类的类型实参 |
    | 实现接口 | `class UserRepository implements Repository<User, Long>` | 实现类固定接口的实体类型和 ID 类型 |
    | 显式方法类型实参 | `GenericExamples.<String>first(names)` | 也叫 type witness，通常可省略 |
    | 类型令牌 | `Class<User> type` | 常用于反射、反序列化、工厂方法 |
    | 通配符参数 | `List<? extends Number>` | 提高参数兼容性，但会限制读写能力 |

- 类型推断

    | 写法 | 推断方向 | 结果 |
    | --- | --- | --- |
    | `Box<String> b = new Box<>("A");` | 左侧目标类型 + 构造器参数 | `<>` 推断为 `String` |
    | `var b = new Box<String>("A");` | 右侧表达式 | `var` 推断为 `Box<String>` |
    | `var b = new Box<>("A");` | 构造器参数 | `<>` 推断为 `String`，`var` 推断为 `Box<String>` |
    | `var list = new ArrayList<>();` | 没有目标类型、没有元素参数 | 通常推断为 `ArrayList<Object>` |
    | `List<String> list = new ArrayList<>();` | 左侧目标类型 | 右侧推断为 `ArrayList<String>` |
    | `var list = new ArrayList<String>();` | 右侧显式类型实参 | `var` 推断为 `ArrayList<String>` |

    - `var` 推断的是**局部变量类型**；`<>` 推断的是**构造调用的泛型实参**。
    - 方法调用也会做类型推断：`first(List.of("A"))` 可推断返回 `String`。
    - lambda、方法引用、泛型方法常依赖目标类型；目标类型不足时，需要显式类型实参或显式变量类型。
    - diamond `<>` Java 7 起可用于普通构造调用；Java 9 起也可更好地用于匿名类场景。

- 上界、多重边界与递归边界

    | 写法 | 含义 | 典型用途 |
    | --- | --- | --- |
    | `<T>` | 等价于 `<T extends Object>` | 无特殊约束 |
    | `<T extends Number>` | `T` 必须是 `Number` 或子类 | 方法内可按 `Number` 使用 |
    | `<T extends Comparable<T>>` | `T` 能与同类对象比较 | 排序、最大值、最小值 |
    | `<T extends Number & Comparable<T>>` | 多重上界 | 同时需要数值能力和比较能力 |
    | `<T extends Comparable<? super T>>` | 更宽的递归比较边界 | 兼容父类型定义的比较能力 |

    - 多重边界用 `&`，如果包含类上界，类必须写第一个；接口上界可以多个。
    - 类型形参没有 `super` 下界写法；`super` 只用于通配符。
    - 上界决定擦除结果：`T extends Number` 擦除后主要按 `Number` 处理。

- 泛型不变、通配符与 PECS

    | 类型关系 | 是否成立 | 说明 |
    | --- | --- | --- |
    | `String extends Object` | 成立 | 普通类继承关系 |
    | `List<String> extends List<Object>` | 不成立 | 泛型默认不协变 |
    | `List<String> extends List<?>` | 成立 | `?` 接收任意元素类型 |
    | `List<Integer> extends List<? extends Number>` | 成立 | 上界通配符接收 `Number` 子类型列表 |
    | `List<Number> extends List<? super Integer>` | 成立 | 下界通配符接收 `Integer` 父类型列表 |

    | 写法 | 读能力 | 写能力 | 适合场景 |
    | --- | --- | --- | --- |
    | `List<T>` | 读出 `T` | 写入 `T` | 既读又写同一种类型 |
    | `List<?>` | 读出 `Object` | 只能写入 `null` | 只关心大小、遍历、清空等与元素类型无关的操作 |
    | `List<? extends Number>` | 读出 `Number` | 不能安全写入具体数值，`null` 除外 | 生产者，只读为主 |
    | `List<? super Integer>` | 读出 `Object` | 可写入 `Integer` 及其子类对象 | 消费者，写入为主 |

    - PECS：Producer Extends, Consumer Super。只从数据源取，用 `? extends T`；只向目标写，用 `? super T`。
    - 通配符表达的是“我不知道具体类型”；类型参数 `<T>` 表达的是“多个位置是同一个类型”。
    - 通配符捕获：编译器可把 `List<?>` 的未知类型临时捕获成某个类型；复杂场景可用私有泛型 helper 方法辅助。

- 类型擦除、桥接方法与反射

    - 无上界类型变量通常擦除为 `Object`；有上界时擦除为第一个上界。
    - 编译器会在必要位置插入强制类型转换，例如从 `List<String>` 取值后转成 `String`。
    - 子类重写泛型父类方法时，擦除后签名可能变化；编译器可能生成桥接方法保持多态正确。
    - 两个方法如果擦除后签名相同，不能只靠不同泛型实参重载，例如 `m(List<String>)` 和 `m(List<Integer>)` 不能同时存在。
    - class 文件可保留泛型签名元数据；反射能读到字段、方法、父类、接口声明上的泛型签名，但普通对象本身通常不知道自己是 `List<String>` 还是 `List<Integer>`。
    - `Class<T>` 常作为类型令牌使用，但 `List<String>.class` 不存在；只能写 `List.class` 或借助框架的 `TypeReference` 思路保存泛型签名。

- 运行期限制与非法写法

    | 限制 | 非法或不推荐写法 | 原因 |
    | --- | --- | --- |
    | 基本类型不能作为类型实参 | `List<int>` | 类型实参必须是引用类型 |
    | 不能直接创建类型变量对象 | `new T()` | 擦除后不知道要创建哪个类 |
    | 不能取类型变量 class | `T.class` | 运行期没有具体 `T` |
    | 不能精确判断参数化类型 | `obj instanceof List<String>` | 泛型实参被擦除 |
    | 不能创建参数化类型数组 | `new List<String>[10]` | 数组运行期检查与泛型擦除冲突 |
    | 静态成员不能用类级 `T` | `static T value;` | 类级 `T` 属于实例类型，不属于类静态区 |
    | 泛型类不能继承异常 | `class X<T> extends Exception` | 异常捕获需要运行期确定类型 |
    | `catch` 不能捕获类型变量 | `catch (T e)` | 捕获类型必须运行期可检查 |
    | 不能只按泛型实参重载 | `m(List<String>)` / `m(List<Integer>)` | 擦除后签名冲突 |

    - `List<?>[] array = new List<?>[10]` 这类“无界通配符数组”可以创建，因为 `List<?>` 是可具体化类型；但业务中仍要谨慎使用。
    - `List<String>[]` 不能直接创建；优先用 `List<List<String>>`。

- 原始类型、未经检查警告与堆污染

    - 原始类型 `List` 主要为兼容 Java 5 之前的旧代码保留；新代码应写 `List<T>`、`List<?>` 或具体参数化类型。
    - 原始类型赋给参数化类型、未经检查强转、泛型数组和泛型可变参数都可能触发 unchecked 警告。
    - `@SuppressWarnings("unchecked")` 只能压在最小作用域，并且要确认数据来源真的满足目标泛型类型。
    - 泛型可变参数如 `List<String>... lists` 可能产生堆污染；只有确认方法不会写入错误类型、不会暴露参数数组时，才使用 `@SafeVarargs`。
    - `@SafeVarargs` 可用于构造器，以及 `static`、`final`、`private` 等不会被不安全重写的方法。

- 设计原则

    - 集合、缓存、仓储、结果包装、分页结果、树节点、事件、回调等“同一结构承载不同类型”的场景适合泛型。
    - 类型参数要表达真实关系：如果入参、返回值、字段之间没有类型关联，泛型可能只是增加噪声。
    - 只在一个方法内相关，用泛型方法；对象整个生命周期都绑定某个类型，用泛型类或泛型接口。
    - 入参需要更灵活时使用通配符；返回值通常避免返回 `? extends T`、`? super T`，除非调用方确实只需要受限能力。
    - API 返回值、字段、集合元素尽量写具体泛型类型，不要退化成原始类型。
    - 边界写到刚好够用：能用 `<T extends Number>` 就不要写无界 `<T>` 后再强转。
    - 优先用 `List<T>`、`Map<K, V>` 等集合抽象承载泛型数据；少用泛型数组。

<details>
<summary>Java 泛型例子</summary>

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GenericExamples {
    public static void main(String[] args) {
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Tom", 90);
        scores.put("Jerry", 85);
        Integer tomScore = scores.get("Tom");

        Box<String> nameBox = new Box<>("Alice"); // diamond 推断 String
        String name = nameBox.get();

        var inferredBox = new Box<>("Bob");       // var 推断 Box<String>
        Box<String> explicitBox = new Box<>("Cat");

        // var emptyList = new ArrayList<>();      // 推断为 ArrayList<Object>
        var stringList = new ArrayList<String>();  // 推断为 ArrayList<String>

        Repository<User, Long> repository = new UserRepository();
        User user = repository.findById(1L);
        repository.save(user);

        String firstName = first(Arrays.asList("A", "B"));
        Integer firstNumber = GenericExamples.<Integer>first(Arrays.asList(1, 2));

        String biggerName = max("Tom", "Jerry");
        Integer biggerNumber = max(10, 20);

        List<Integer> integers = new ArrayList<>();
        addDefaults(integers);                     // ? super Integer：写入
        double total = sum(integers);              // ? extends Number：读取

        List<Integer> src = Arrays.asList(1, 2, 3);
        List<Number> dest = new ArrayList<>();
        copy(src, dest);

        System.out.println(tomScore + ", " + name + ", " + inferredBox.get() + ", " + explicitBox.get());
        System.out.println(firstName + ", " + firstNumber + ", " + biggerName + ", " + biggerNumber);
        System.out.println(user.name() + ", " + stringList.size() + ", " + total + ", " + dest);
    }

    static class Box<T> {
        private final T value;

        Box(T value) {
            this.value = value;
        }

        T get() {
            return value;
        }
    }

    interface Repository<T, ID> {
        T findById(ID id);
        void save(T entity);
    }

    static class User {
        private final Long id;
        private final String name;

        User(Long id, String name) {
            this.id = id;
            this.name = name;
        }

        Long id() {
            return id;
        }

        String name() {
            return name;
        }
    }

    static class UserRepository implements Repository<User, Long> {
        @Override
        public User findById(Long id) {
            return new User(id, "Alice");
        }

        @Override
        public void save(User entity) {
            System.out.println(entity.name());
        }
    }

    static <T> T first(List<T> list) {
        if (list.isEmpty()) {
            throw new IllegalArgumentException("list is empty");
        }
        return list.get(0);
    }

    static <T extends Comparable<? super T>> T max(T a, T b) {
        return a.compareTo(b) >= 0 ? a : b;
    }

    static double sum(List<? extends Number> numbers) {
        double total = 0;
        for (Number number : numbers) {
            total += number.doubleValue();
        }
        return total;
    }

    static void addDefaults(List<? super Integer> target) {
        target.add(0);
        target.add(1);
    }

    static <T> void copy(List<? extends T> src, List<? super T> dest) {
        for (T item : src) {
            dest.add(item);
        }
    }

    // 类型擦除相关限制：下面写法不合法
    // List<int> ids = new ArrayList<>();              // 基本类型不能作为类型实参
    // T value = new T();                              // 不能直接创建类型变量对象
    // if (src instanceof List<Integer>) {}            // 不能检查具体泛型实参
    // List<String>[] array = new List<String>[10];    // 不能创建参数化类型数组
}
```
</details>

### 注解、反射
1. 注解（Annotation）

    注解是写在声明或类型使用位置上的元数据，本身不直接改变业务逻辑；真正读取和执行规则的是编译器、注解处理器、框架或反射代码。

    ```java
    @注解名
    @注解名(值)
    @注解名(参数名 = 值)
    ```

    - 常见用途：编译器检查（`@Override`）、过时提示（`@Deprecated`）、抑制警告（`@SuppressWarnings`）、编译期代码生成（Lombok、MapStruct）、运行期框架配置（Spring、JUnit）、文档说明（`@Documented`）。
    - 常见内置注解：`@Override`、`@Deprecated`、`@SuppressWarnings`、`@SafeVarargs`、`@FunctionalInterface`、`@Serial`、`@Native`。
    - 元注解：`@Target` 限定使用位置；`@Retention` 限定保留阶段；`@Documented` 写入 Javadoc；`@Inherited` 只让类上的注解可被子类继承；`@Repeatable` 允许同一位置重复使用。
    - `@Retention`：`SOURCE` 只保留源码；`CLASS` 写入 `.class` 但运行期一般不可读，是默认策略；`RUNTIME` 运行期可通过反射读取。
    - `@Target`：常用 `TYPE`、`FIELD`、`METHOD`、`PARAMETER`、`CONSTRUCTOR`、`LOCAL_VARIABLE`、`ANNOTATION_TYPE`、`PACKAGE`、`MODULE`、`RECORD_COMPONENT`、`TYPE_PARAMETER`、`TYPE_USE`。
    - 注解接口用 `@interface` 定义；`@interface` 是定义语法，不是使用注解；`@注解名` 才是使用注解。

    ```java
    import java.lang.annotation.ElementType;
    import java.lang.annotation.Retention;
    import java.lang.annotation.RetentionPolicy;
    import java.lang.annotation.Target;

    @Target({ElementType.FIELD, ElementType.PARAMETER})
    @Retention(RetentionPolicy.RUNTIME)
    @interface Label {
        String value();                  // 使用时可写 @Label("用户名")
        boolean required() default true;
    }

    class User {
        @Label(value = "用户名", required = false)
        private String name;
    }
    ```

    - 注解元素规则：元素写成无参数方法；不能写方法体；可用 `default`；返回值只能是基本类型、`String`、`Class`、枚举、注解接口，或这些类型的一维数组；元素名为 `value` 且其他元素有默认值时，可省略 `value =`。
    - 反射读取：只有 `@Retention(RetentionPolicy.RUNTIME)` 的注解才能稳定通过 `getAnnotation()`、`getDeclaredAnnotations()` 读取。
    - 使用边界：注解适合描述元数据，不适合承载复杂业务流程；框架能读到注解，不代表 Java 语言会自动执行逻辑。
1. 反射（Reflection）

    反射是在运行期以 `Class` 为入口读取类型元信息，并通过 `Field`、`Method`、`Constructor` 等对象间接访问成员的机制。它把原本需要在编译期写死的类型操作延迟到运行期，常被框架用于扫描类、按配置创建对象、依赖注入、序列化 / 反序列化、ORM 映射、测试工具、插件系统和动态代理；代价是破坏封装、降低可读性、增加运行期开销，普通业务代码应少用。

    - 核心模型

        | 层级 | 含义 | 关键点 |
        | --- | --- | --- |
        | 类型元信息 | `Class<T>` 表示 JVM 中已加载类型的运行期描述 | 同一个类型在同一个类加载器下通常只有一个 `Class` 对象；不同类加载器加载的同名类不是同一个运行期类型 |
        | 成员元信息 | `Field`、`Method`、`Constructor` 描述字段、方法、构造器 | 这些对象只是成员描述，不等于字段值、方法执行结果或对象实例 |
        | 运行期操作 | 通过 `Field#get/set`、`Method#invoke`、`Constructor#newInstance` 执行访问、调用、创建 | 实例字段和实例方法必须传入目标对象；构造器只能创建新对象，不能反向找到堆里已有对象 |

    - 获取 `Class` 的入口

        | 入口 | 示例 | 含义 |
        | --- | --- | --- |
        | 类字面量 | `String.class` | 编译期已知类型，直接拿类型对应的 `Class` |
        | 类名加载 | `Class.forName("java.lang.String")` | 通过全限定类名查找并加载类型，默认会触发类初始化 |
        | 数组类型 | `int[].class`、`String[][].class` | 数组本身也是类型，元素类型和维度共同决定数组 `Class` |
        | 基本类型 | `int.class`、`void.class` | 基本类型和 `void` 也有 `Class`，但没有普通对象实例成员 |
        | 对象实例 | `"abc".getClass()` | 通过已有对象拿它的运行期实际类型；这只是拿 `Class`，不是已经对实例字段或方法做了反射操作 |

        ```java
        // 从类型入口拿 Class
        Class<String> c1 = String.class;
        Class<?> c3 = Class.forName("java.lang.String");
        Class<int[]> c4 = int[].class;
        Class<Integer> c5 = int.class;

        // 从实例入口拿运行期 Class
        Class<?> c2 = "abc".getClass();
        ```

        >`Class` 描述类型结构，例如字段、方法、构造器、注解、父类和接口；但 `Class` 不持有对象实例，也不能自动枚举 JVM 堆中已经存在的对象。要反射操作某个实例，必须先拿到目标对象引用，再结合成员元信息操作这个对象。

    - <details>

        <summary>常用能力</summary>

        | 能力 | 常用 API | 使用边界 |
        | --- | --- | --- |
        | 判断类型关系 | `getClass()`、`isInstance()`、`isAssignableFrom()` | 适合运行期分派和框架校验；普通业务优先用多态和接口 |
        | 读取类结构 | `getName()`、`getSuperclass()`、`getInterfaces()`、`getModifiers()` | 只能读到 JVM 保存的类型信息，不能读取源码注释和局部变量名等编译后不存在的信息 |
        | 读取成员 | `getFields()`、`getMethods()`、`getConstructors()` | 只取 `public`，并包含继承成员；构造器不继承 |
        | 读取本类声明 | `getDeclaredFields()`、`getDeclaredMethods()`、`getDeclaredConstructors()` | 只取本类声明成员，包含 `private`，不包含继承成员 |
        | 创建对象 | `getDeclaredConstructor(...).newInstance(...)` | 调用构造器创建新对象，不是查找已有对象 |
        | 访问字段 | `Field#get(obj)`、`Field#set(obj, value)` | 实例字段要传目标对象；静态字段可传 `null` |
        | 调用方法 | `Method#invoke(obj, args...)` | 实例方法要传目标对象；静态方法可传 `null`；被调用方法抛出的异常会被包进 `InvocationTargetException` |
        | 读取注解 | `getAnnotation()`、`getDeclaredAnnotations()` | 只有 `@Retention(RetentionPolicy.RUNTIME)` 的注解才能在运行期稳定读取 |
        | 读取泛型签名 | `getGenericSuperclass()`、`getGenericInterfaces()`、`getGenericType()` | 能读声明处保留的泛型签名，不能恢复普通对象被类型擦除后的运行期实参 |
        | 处理数组 | `Array.newInstance()`、`Array.get()`、`Array.set()` | 适合运行期才知道元素类型或维度的场景 |
        | 动态代理 | `Proxy.newProxyInstance()`、`InvocationHandler` | JDK 动态代理主要代理接口；类代理通常依赖 CGLIB、Byte Buddy 等字节码工具 |

        </details>

    ```java
    import java.lang.reflect.Constructor;
    import java.lang.reflect.Field;
    import java.lang.reflect.Method;

    class User {
        private String name;

        public User(String name) {
            this.name = name;
        }

        public String hello(String prefix) {
            return prefix + name;
        }
    }

    Class<User> type = User.class;
    Constructor<User> constructor = type.getDeclaredConstructor(String.class);
    User user = constructor.newInstance("Tom");

    Field field = type.getDeclaredField("name");
    field.setAccessible(true);          // 尝试绕过访问检查，模块边界下不一定成功
    field.set(user, "Jerry");

    Method method = type.getDeclaredMethod("hello", String.class);
    Object result = method.invoke(user, "Hi, ");
    ```

    - 关键边界：`setAccessible(true)` / `trySetAccessible()` 只是尝试放开 Java 语言访问检查；Java 9 之后模块系统会加强封装，跨模块反射访问不一定成功。反射也不能绕过类型擦除、不能凭 `Class` 找到已有对象、不能自动保证编译期类型安全。
    - 常见异常：`ClassNotFoundException`、`NoSuchFieldException`、`NoSuchMethodException`、`InstantiationException`、`IllegalAccessException`、`InvocationTargetException`、`IllegalArgumentException`、`SecurityException`。
    - 使用哲学：反射适合写通用框架、工具和基础设施，不适合替代正常业务建模。业务逻辑优先使用接口、多态、泛型、枚举、注解配置和显式 API；确实要用反射时，应把反射代码隔离在少数边界层，缓存重复查询到的 `Class` / `Field` / `Method`，集中处理异常，尽早失败，并用测试覆盖字段名、方法名、构造器签名这类运行期才暴露的问题。

### 常用 API 与进阶主题

- `String`：不可变字符串；频繁拼接优先用 `StringBuilder`。
- 日期时间 API：优先用 `java.time`，如 `LocalDateTime`、`Instant`、`Duration`，少用旧的 `Date` / `Calendar`。
- 集合类：`List` 有序可重复；`Set` 不重复；`Map` 存键值对；遍历 `Map` 常用 `entrySet()`。
- IO 流：字节流处理二进制，字符流处理文本；资源关闭优先用 `try-with-resources`。
- 多线程基础：先掌握 `Thread`、`Runnable`、线程池、锁、可见性、原子性，再深入并发工具类。

## 后端工程与数据中间件
### 构建与依赖管理
- **Maven**：Java 生态最常见的项目构建、依赖解析、插件执行和发布工具。

    1. 配置入口

        - Maven 的最终行为由三类入口共同决定：`settings.xml` 负责本机/用户运行环境，`pom.xml` 负责项目构建模型，`mvn` 命令或 IDE 操作决定本次执行。

            1. `settings.xml` 和 `pom.xml` 都是 XML，但根标签、schema、允许配置项和作用范围不同；不要把账号、代理、镜像等本机配置写进项目公共 `pom.xml`，也不要把依赖、插件构建规则放进 `settings.xml`。
            1. IDE 的 Maven 版本、Profiles 选择、运行/调试配置通常保存在 IDE 本地配置中（如 `.idea` 或其他目录），跨设备、跨 IDE 不一定同步；`同步所有Maven项目` / `重新加载所有Maven项目` 本质是让 IDE 重新读取 `pom.xml`，刷新项目模型和依赖解析状态。
        1. 运行环境配置：[`settings.xml`](./settings.xml)

            >参考：<https://maven.apache.org/ref/3.9.15/maven-settings/settings.html>

            1. 配置文件层级：用户级 `settings.xml` 通常位于 `${user.home}/.m2/settings.xml`；全局级 `settings.xml` 通常位于 Maven 安装目录的 `conf/settings.xml`；最终配置会合并生效，用户级配置优先级更高。
            1. 根级配置：`localRepository` 指定本地仓库路径，默认 `${user.home}/.m2/repository`；`interactiveMode` 控制是否允许交互输入，默认 `true`；`offline` 控制是否离线构建，默认 `false`。
            1. 仓库访问配置：`mirrors` 做远程仓库重定向；`servers` 保存仓库、镜像、发布目标认证；`proxies` 保存网络代理；这些配置属于本机运行环境，不应提交到公共项目 POM。

                >私服可以设置“下载需要账号密码”，也可以只让发布需要账号密码；这是私服服务端权限控制决定的。仓库、镜像、发布目标认证使用 `servers/server` 凭证，Maven 按实际访问的仓库或镜像 `id` 匹配；网络代理认证才使用 `proxies/proxy` 凭证。
            1. 本地环境扩展：`pluginGroups` 用于解析插件前缀；`profiles` / `activeProfiles` 用于注入本机差异，通常只适合放 `repositories`、`pluginRepositories` 和本地变量类 `properties`。
        1. 项目构建模型：[`pom.xml`](./pom.xml)

            >参考：<https://maven.apache.org/ref/3.9.15/maven-model/maven.html>

            1. 项目坐标：`groupId`、`artifactId`、`version`、`packaging`，用于唯一定位项目产物。
            1. 核心区域：`properties` 管公共变量；`dependencies` 声明依赖；`dependencyManagement` 集中管理依赖元信息但不直接引入依赖；`build` / `plugins` / `pluginManagement` 管构建插件；`modules` 管多模块；`repositories` 管依赖拉取仓库；`distributionManagement` 管发布目标。
            1. Maven 默认目录约定

                <details>
                <summary>“约定大于配置”</summary>

                1. 标准场景下，遵守 Maven 约定，少写甚至不写配置。
                1. Maven 用统一目录结构、生命周期、插件规则降低项目复杂度。
                1. 偏离默认约定时，再通过 pom.xml 显式配置。
                1. 它不是“不能配置”，而是“优先使用默认约定，配置只处理特殊情况”。
                </details>

                1. `pom.xml` 在项目根目录
                1. `src/main/java` 放主程序 Java 源码
                1. `src/main/resources` 放主程序资源配置（编译后进入 classpath）
                1. `src/test/java` 放测试源码
                1. `src/test/resources` 放测试资源
                1. `target` 是构建输出目录。

                <details>
                <summary>Maven 默认目录</summary>

                ```text
                my-maven-project/
                ├── pom.xml                  # Maven 项目配置文件，项目根配置
                │
                ├── src/
                │   ├── main/                # 主程序代码
                │   │   ├── java/            # 主程序 Java 源码
                │   │   │   └── com/
                │   │   │       └── example/
                │   │   │           └── App.java
                │   │   │
                │   │   └── resources/       # 主程序配置文件资源文件，编译后进入 classpath
                │   │       ├── application.properties
                │   │       ├── logback.xml
                │   │       └── static/
                │   │
                │   └── test/                # 测试代码
                │       ├── java/            # 测试 Java 源码
                │       │   └── com/
                │       │       └── example/
                │       │           └── AppTest.java
                │       │
                │       └── resources/       # 测试配置文件资源文件测试数据，测试时进入 test classpath
                │           └── test-data.json
                │
                └── target/                  # Maven 构建输出目录，执行 mvn compile/package 后生成
                    ├── classes/             # main/java 和 main/resources 编译后的结果
                    ├── test-classes/        # test/java 和 test/resources 编译后的结果
                    └── my-maven-project.jar # 打包产物，例如 jar/war
                ```
                </details>

                >Classpath（类路径）就是 Java 虚拟机（JVM）在运行程序时，用来寻找类（.class 文件）和资源文件（如 .xml、.yml、.properties、图片等）的“搜索目录”或“导航地图”。类似操作系统的`PATH`环境变量

            1. 多模块项目通常用父 `pom.xml` 的 `modules` 组织子模块，父工程常用 `packaging=pom` 并集中管理版本和公共插件配置；每个子模块再各自包含 `pom.xml` 与 `src/main` / `src/test` 目录；传统 `war` 项目还可能有 `src/main/webapp`。
    1. 依赖、仓库与版本管理

        1. 仓库类型

            按解析机制，Maven 仓库先分为 **本地仓库** 和 **远程仓库**；中央仓库、第三方仓库、私服、依赖仓库、插件仓库、发布仓库都是远程仓库按来源或用途的细分；镜像仓库是访问重定向规则，不是新增依赖来源。

            1. **本地仓库**：本机缓存和本机安装目录，默认 `${user.home}/.m2/repository`；远程下载的依赖、插件，以及 `mvn install` 安装的当前项目产物都会进入本地仓库。可在 `settings.xml` 的 `localRepository` 修改，也可用 `-Dmaven.repo.local=路径` 临时指定。
            1. **远程仓库**：本地仓库之外、通过 URL 访问的 Maven 仓库统称，常见协议是 `https`，也可以是 `file` 等。
            1. **中央仓库**：Maven 默认内置的公共远程仓库，仓库 `id` 通常是 `central`，地址是 `https://repo.maven.apache.org/maven2`；未额外配置仓库时，开源依赖通常从这里解析。
            1. **第三方仓库**：中央仓库和本团队私服之外，由厂商、开源组织或其他平台维护的远程仓库；它是新的依赖来源，通常需要在 `repositories` / `pluginRepositories` 中显式配置，可能要求认证，也可能托管中央仓库没有的包。
            1. **私服 / 内部仓库**：公司或团队自建的远程仓库，如 Nexus、Artifactory、Archiva；常用于缓存中央仓库、托管公司内部 jar、统一依赖来源和权限控制。
            1. **依赖仓库**：解析普通项目依赖的远程仓库，由 `repositories` 配置。
            1. **插件仓库**：解析 Maven 插件及插件依赖的远程仓库，由 `pluginRepositories` 配置。
            1. **发布仓库**：`mvn deploy` 的上传目标，由 `distributionManagement` 配置；正式版本通常发布到 `repository`，快照版本通常发布到 `snapshotRepository`，不等同于拉取依赖用的 `repositories`。
            1. **镜像仓库**：`settings.xml` 中 `mirrors` 配置的远程仓库替身；它用 `mirrorOf` 把匹配到的仓库请求改到镜像地址，常见值有 `central`、`*`、`external:*`、`*,!repoId`；同一个仓库最终只会选中一个镜像，聚合多个上游通常交给私服或仓库管理器。

        1. 依赖解析逻辑与优先级

            1. 解析顺序：先查本地仓库；本地没有，或 `SNAPSHOT` / 元数据按策略需要更新时，再查最终生效的远程仓库列表。
            1. 远程仓库候选来自当前 POM、父 POM、激活的 profile、全局/用户 settings，以及 Super POM 内置的 `central`；最终结果用 `mvn help:effective-pom` 和 `mvn help:effective-settings` 查看。
            1. 访问远程仓库前会先应用 `mirrors`：如果 `mirrorOf` 命中仓库 `id`，实际访问镜像地址；此时认证凭证匹配 `mirror.id`，不是原仓库 `id`。
            1. `releases` / `snapshots` 控制仓库是否用于正式版本或快照版本；`updatePolicy` 控制检查频率；离线模式 `-o` 或 `offline=true` 只使用本地仓库；`-U` 强制检查快照依赖和远程元数据更新。

        1. 配置方式

            1. 只使用中央仓库：通常不需要写 `repositories`，Maven 会从 Super POM 内置的 `central` 解析依赖。
            1. 项目共享依赖源：团队共同需要的第三方仓库或私服可写进项目 `pom.xml` 的 `repositories` / `pluginRepositories`；个人或机器差异更适合写在 `settings.xml` profile。
            1. 镜像统一出口：写在用户级或全局级 `settings.xml` 的 `mirrors`；公司统一入口常用 `mirrorOf=*` 或 `external:*`，只替换中央仓库可用 `mirrorOf=central`。
            1. 仓库认证：账号、密码、token、SSH key 写在 `settings.xml` 的 `servers`；拉取私服依赖、访问需登录镜像、`mvn deploy` 发布产物时才需要；`server.id` 必须匹配实际访问的 `repository`、`pluginRepository`、`distributionManagement` 或 `mirror` 的 `id`。
            1. 发布目标：`mvn deploy` 不看 `repositories`，发布地址由 `pom.xml` 的 `distributionManagement` 决定；正式版本用 `repository`，快照版本用 `snapshotRepository`，认证仍由 `settings.xml` 的 `servers` 提供。

        1. 依赖声明：普通依赖写在 `dependencies`；统一版本、scope、exclusions 等元信息写在父 POM、`dependencyManagement` 或 BOM（`type=pom`、`scope=import`）；`dependencyManagement` 不会自动引入依赖。
        1. 依赖范围：常见有 `compile`、`provided`、`runtime`、`test`，少用 `system`；可用 `optional` 控制传递，用 `exclusions` 排除冲突依赖。
        1. 版本仲裁：冲突通常按“路径最近优先”，路径相同再按声明顺序靠前优先；排查依赖冲突常用 `mvn dependency:tree`。
        1. `SNAPSHOT` 表示开发中版本，Maven 可按策略检查更新；正式版本应尽量不可变，便于复现构建。
        1. Maven 跨项目依赖通常认构建产物（jar），不是直接认另一个项目的源码；被依赖项目改动后，需要重新 `package` / `install`，或放到同一次 reactor 构建里。

    1. 构建执行、生命周期与问题排查

        1. Maven 有 `clean`、`default`、`site` 三套生命周期；常用默认生命周期阶段是 `validate`、`compile`、`test`、`package`、`verify`、`install`、`deploy`。
        1. 生命周期阶段只定义顺序，真正执行编译、测试、打包、发布的是插件 goal；`packaging` 会影响默认插件绑定，如 `jar` 绑定 `jar:jar`，`war` 绑定 `war:war`，常见阶段还会绑定 `surefire:test`、`install:install`、`deploy:deploy` 等目标。
        1. 常见构建配置包括 JDK 版本、编码、资源过滤、测试插件、打包插件、Spring Boot 插件、代码生成插件、静态检查插件；`jar` 常用于普通库或 Spring Boot 可执行包，`war` 常用于传统 Web 容器部署，`pom` 常用于父工程或 BOM。
        1. `mvn` 基本格式：`mvn [全局选项] [生命周期阶段或插件目标] [系统属性]`，如 `mvn clean install`、`mvn dependency:tree`、`mvn spring-boot:run`。
        1. 常用参数：`-s` 指定用户级 `settings.xml`，`-gs` 指定全局级 `settings.xml`，`-f` 指定 POM，`-P` 激活 profile，`-D` 传系统属性，`-o` 离线构建，`-U` 强制检查快照依赖更新。
        1. 多模块 reactor 构建会按模块依赖关系排序；`-pl` 选择模块，`-am` 同时构建所选模块需要的依赖模块，常用于跨模块改动后的同次构建。
        1. 阶段效果：`clean` 通常删除当前项目的 `target` 目录；`package` 生成 jar/war；`verify` 做集成测试或质量校验；`install` 把当前项目产物安装到本地仓库；`deploy` 发布到远程仓库，地址由 `distributionManagement` 决定，认证由 `settings.xml` 的 `servers` 提供。
        1. 跳过测试：`-DskipTests` 跳过测试执行但仍编译测试代码；`-Dmaven.test.skip=true` 连测试编译也跳过。
        1. 常用示例：`mvn -U -pl 项目路径 -am clean install -P环境 -Dmaven.test.skip=true`；`mvn -f 项目路径/pom.xml spring-boot:run -P环境 -Dmaven.test.skip=true`。日常优先用 IDE 的可视化操作（Profiles 选择、编辑配置、安装、运行或调试），排查或 CI 场景再显式写命令。
        1. 问题排查：最终 POM 看 `mvn help:effective-pom`，最终 Maven 配置看 `mvn help:effective-settings`，构建异常重点看 lifecycle phase、plugin goal、profile、JDK 版本和仓库解析结果。项目可使用 Maven Wrapper（`mvnw` / `mvnw.cmd`）固定 Maven 版本。

- **Gradle**：更灵活，Android 和部分现代项目里较常见。

>对于多数后端初学者，先掌握 Maven 即可。

### Spring 生态

>Java Web 是 Java 后端处理 HTTP 请求的基础体系，核心包括 Servlet、Filter、Listener、Session、Cookie；Spring 做 Web 开发时并不是绕开 Java Web，而是在 Java Web/Servlet 基础上进一步封装：SpringMVC 通过 `DispatcherServlet` 接收请求并分发到 `Controller`，Spring Boot 又建立在 Spring Framework/SpringMVC 之上，通过自动配置和内嵌 Servlet 容器简化项目启动。

1. Spring（Spring Framework）

    核心框架，提供 IoC、AOP、事务管理、资源访问、事件、类型转换、校验。

    >Spring Boot 是建立在 Spring Framework 之上的，Spring 的核心是容器管理对象和依赖注入。

    1. SpringMVC

        处理 HTTP 请求映射、参数绑定、数据校验、异常处理、视图解析、JSON 响应。

        >Spring Framework 里的 Web 模块。HTTP 请求 → Controller 方法 → Service → 返回 JSON
1. MyBatis

    负责 SQL 映射、参数绑定、结果映射、动态 SQL、数据库访问。

    >UserController -> UserService -> UserMapper -> user 表
1. SpringBoot

    在 Spring 基础上做自动配置，简化项目搭建和开发。

    >Spring Boot = Spring + SpringMVC + 数据库访问 + 自动配置 + 快速启动

    启动标配：`@SpringBootApplication`（一个组合注解，主要包含：`@SpringBootConfiguration`、`@EnableAutoConfiguration`、`@ComponentScan`；其中 `@SpringBootConfiguration` 可视为 Spring Boot 场景下的 `@Configuration`）

### 关系型数据库：MySQL
- 最常见的关系型数据库。
- 先掌握建表、增删改查、索引、事务，再谈性能优化。
- 业务开发重点：表结构设计、主键、唯一约束、外键取舍、分页查询、慢 SQL、事务隔离级别。

### 缓存与内存数据：Redis
- 常用作缓存，也可用于分布式锁、计数器、会话、排行榜、延迟队列场景。
- 要先理解缓存命中、过期、穿透、击穿、雪崩这些基础问题。
- 常见数据结构：String、Hash、List、Set、Sorted Set；先按业务场景选结构，不要只把 Redis 当 Map 用。

### 消息队列：Kafka / RabbitMQ
- **Kafka**：偏日志流、吞吐高，常用于异步削峰、流式处理。
- **RabbitMQ**：偏传统消息队列，路由能力更丰富，业务系统里也很常见。
- 核心问题：消息是否丢失、是否重复消费、消费失败怎么重试、顺序性是否重要、是否需要死信队列。
