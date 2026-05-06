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

### Java 概览
#### 版本演进
- 1.2 以前通常叫 JDK（Java Development Kit）。
- 1.2 到 1.4 常见叫法是 J2SE（Java 2 Platform, Standard Edition）。
- Java 5 以后统一叫 Java SE（Java Platform, Standard Edition）。
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

#### 平台体系
- **Java SE**：标准版，覆盖语言基础、标准类库、集合、IO/NIO、日期时间、并发、网络、反射、注解。
- **Java EE（Java Enterprise Edition） / Jakarta EE**：企业级规范体系，现已演进为 Jakarta EE。
- **Java ME**（Java Micro Edition）：面向早期嵌入式/移动设备，现在基本不是主流。

#### 运行体系：JDK / JRE / JVM
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

#### 核心优势
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

### Java SE 基础
#### 环境配置与运行
- 安装 JDK、Maven，并配置 `JAVA_HOME`、`PATH`。

    下载并安装 JDK、Maven，然后配置环境变量。例如 `~/.zshrc`：

    ```text
    # 方式1，手动管理版本
    # JDK版本
    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home
    export PATH=$JAVA_HOME/bin:$PATH
    # Maven版本
    export M2_HOME=/usr/local/apache-maven-3.9.14
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

#### 类型系统
- Java 是强类型语言，变量声明必须有确定类型。
- 小范围数值类型可以向大范围类型隐式转换。
- 反向收窄转换需要显式强转，并可能丢失精度或溢出。
- `boolean` 不能与数值类型互转。

<details>
<summary>类型转换示例</summary>

```java
int a = 10;
double b = a; // int→double：隐式拓宽（按拓宽顺序：byte/short/char<int<long<float<double）
int c = b; // 反过来不行。编译错误：double→int 不能隐式收窄，需 (int)
int c1 = (int) b; // 强制收窄：小数部分截断，非四舍五入
long L = a; // int→long：隐式拓宽
float F = a; // int→float：隐式拓宽（可能损失整数精度，大 int 时明显）
double D = F; // float→double：隐式拓宽
char ch = 'A';
int chAsInt = ch; // char→int：隐式拓宽，得到 UTF-16 代码单元数值
byte bt = (byte) a; // int→byte：必须强制；超范围时按低位截断
short sh = (short) 32768; // 字面量默认 int，赋给 short 需强制，值溢出则按位模式截断
double expr = a + 1.0f; // 二元运算数值提升：int 与 float/double 运算时先提升到较宽类型再算
// String.valueOf 不是 (T)x 语法，是方法调用，把基本类型格式化成字符串。
String s = String.valueOf(a);
// String s1 = (String) a; // 编译错误：基本类型不能 (String) 强转
// char→String 用 String.valueOf(ch) 或 "" + ch 或 Character.toString(ch)，不能 (String)ch。
```
</details>

#### 基本类型与引用类型
Java 的数据类型分为基本类型（Primitive Types）和引用类型（Reference Types）。

1. 基本类型一共 8 种：

    | 类型     | 大小 | 字段/数组元素默认值 | 取值范围                       | 说明     |
    | ------- | ---- | ------------ | ---------------------------- | ------- |
    | `byte`    | 1字节 | 0        | -128 ~ 127                     | 整数型   |
    | `short`   | 2字节 | 0        | -32,768 ~ 32,767               | 整数型   |
    | `int`     | 4字节 | 0        | -2,147,483,648 ~ 2,147,483,647 | 整数型（最常用） |
    | `long`    | 8字节 | 0L       | -2^63 ~ 2^63-1                 | 整数型 |
    | `float`   | 4字节 | 0.0f     | 约 ±3.4E+38（最小正非 0 约 1.4E-45） | 浮点型（单精度） |
    | `double`  | 8字节 | 0.0d     | 约 ±1.8E+308（最小正非 0 约 4.9E-324） | 浮点型（双精度） |
    | `char`    | 2字节 | '\u0000' | 0 ~ 65535（UTF-16 代码单元）     | 字符型   |
    | `boolean` | 未规定 | false    | true / false                   | 布尔型   |

    - 上表的默认值只适用于字段和数组元素：字段是声明在类里、方法外的变量，包括实例字段（实例变量）和静态字段（类变量）；局部变量不是字段，没有默认值，读取前必须明确赋值。
    - 浮点数有精度问题，金额计算优先用 `java.math.BigDecimal`。
    - `char` 不是“任意一个 Unicode 字符”，因为有些字符需要两个 UTF-16 代码单元表示。单引号是 `char`，双引号是 `String`。
    - 经过运算符后的类型变化（表达式里会先做数值提升，再计算）：

        - **二元数值提升**：两个数值操作数做二元运算时，Java 会先把两边提升到同一种类型再计算；规则是 `int`<`long`<`float`<`double`，`byte`/`short`/`char` 都会先变成 `int`。
        - **先记 2 条总规则**：

            - `byte`/`short`/`char` 参与大多数算术运算时，都会先提升为 `int`。
            - 表达式结果通常看“参与运算时最宽的数值类型”：`int`<`long`<`float`<`double`。
        - **一元运算** `+`、`-`、`~`：`byte`/`short`/`char` → `int`；`long`/`float`/`double` 保持原类型。
        - **二元算术 / 整型位运算** `+`、`-`、`*`、`/`、`%`、`&`、`|`、`^`：先做二元数值提升，再得到结果类型。
        - **比较运算** `<`、`>`、`<=`、`>=`、`==`、`!=`：两个都是数值基本类型时，也会先做二元数值提升；`boolean` 只能和 `boolean` 比较。
        - **位移运算** `<<`、`>>`、`>>>`：左右两边先做一元数值提升；结果类型看左操作数提升后的类型。
        - **复合赋值**：`+=`、`-=`、`*=`、`/=`、`%=`、`&=`、`|=`、`^=`、`<<=`、`>>=`、`>>>=` 会先按普通运算计算，再隐式转换为左值类型；普通 `=` 不会自动做这种窄化转换。
        - **字符串拼接**：只要一侧是 `String`，`+` 就表示字符串拼接，结果一定是 `String`；`boolean` 可以参与字符串拼接（不能参与数值运算）。

        <details>
        <summary>表达式类型提升示例</summary>

        ```java
        byte b1 = 1;
        byte b2 = 2;
        int r1 = b1 + b2;      // byte + byte -> int
        // byte r2 = b1 + b2;  // 编译错误，结果是 int，不能直接赋给 byte

        short s1 = 3;
        int r3 = -s1;          // 一元 - 后结果是 int

        char c = 'A';
        int r4 = c + 1;        // char 先提升为 int，结果是 66

        long l = 1L;
        long r5 = l + 2;       // int 与 long 运算，结果是 long

        float f = 1.5f;
        float r6 = f + 2;      // int 与 float 运算，结果是 float

        double d = 3.14;
        double r7 = d + f;     // float 与 double 运算，结果是 double

        int r8 = 5 / 2;        // 结果是 2，两个 int 相除仍是 int
        double r9 = 5 / 2.0;   // 有 double 参与，结果是 2.5

        byte b3 = 1;
        b3 += 1;               // 等价于 b3 = (byte)(b3 + 1)，会隐式转换为 byte
        // b3 = b3 + 1;        // 编译错误，b3 + 1 的结果是 int，普通 = 不会自动窄化为 byte

        String str = "sum=" + b1 + b2;    // "sum=12"
        String str2 = "sum=" + (b1 + b2); // "sum=3"
        ```
        </details>
2. 引用类型包括：

    - 类（Class），如 `String`、普通类；枚举（Enum）也是一种特殊类。
    - 接口（Interface）；注解（Annotation）是特殊接口。
    - 数组（Array），如 `int[]`、`String[]`。
    - 类型变量，如泛型形参 `T`、`E`。

    引用类型变量中保存的是对象引用，值要么是 `null`，要么指向某个对象。

#### 语法基础与面向对象
- Java 的 `变量` 含义

    ```text
    变量
    ├─ 字段 Field：声明在类里、方法外
    │  ├─ 实例字段：不带 static，也叫实例变量
    │  └─ 静态字段：带 static，也叫类变量
    ├─ 局部变量 Local Variable：声明在方法、代码块里
    └─ 参数 Parameter：声明在方法参数列表里
    ```

    >变量不包含方法（方法是行为，不是变量）。
- 变量

    先记住一句真理：**变量不是对象；引用也不是对象；`new` 出来的东西才是对象。**

    判断 Java 中堆和栈的位置，不要靠感觉，按下面三步走：

    1. **先看变量声明在哪里**：方法内是局部变量；类里不带 `static` 是实例变量；类里带 `static` 是类变量。
    2. **再看变量保存什么**：基本类型变量保存真实值；引用类型变量保存对象地址的引用值，可能是 `null`。
    3. **最后看对象从哪里来**：只要看到 `new`，创建出来的对象或数组通常就在堆里。

    >初学够用版：局部变量和参数看栈；`new` 出来的对象、数组看堆；实例字段属于对象，存放在对象内部；`static` 字段属于类，被所有对象共享。

    <details>
    <summary>堆、栈、引用、对象的细节</summary>

    1. 栈与堆到底各管什么？

        | 对比项 | 栈（JVM Stack） | 堆（Heap） |
        | --- | --- | --- |
        | 核心职责 | 管方法调用过程 | 管对象生命周期 |
        | 归属 | 线程私有 | 线程共享 |
        | 主要存放 | 每次方法调用产生的栈帧；栈帧里有局部变量表、操作数栈、动态链接、方法返回地址 | `new` 出来的对象、数组；对象里的实例字段、数组元素 |
        | 生命周期 | 方法调用开始入栈，方法结束出栈 | 对象不再被任何可达引用指向后，由 GC 回收 |
        | 常见错误 | 递归过深会导致 `StackOverflowError` | 对象太多或太大导致 `OutOfMemoryError` |

        所以不要把“变量名在哪里”和“对象在哪里”混在一起。变量名主要是源码里的概念；程序运行时更接近于栈帧里的槽位、堆里的对象、对象里的字段。

    1. 三类变量的本质

        | 变量类型 | 声明位置 | 存放位置 | 默认值 | 关键逻辑 |
        | --- | --- | --- | --- | --- |
        | 局部变量（Local Variable） | 方法、参数列表、代码块里 | 当前方法调用的栈帧 | 没有，必须先赋值再读取 | 方法结束后失效 |
        | 实例变量（Instance Variable） | 类里、方法外、不加 `static` | 属于对象，存放在堆里的对象内部 | 有默认值 | 每 `new` 一个对象，就有自己的一份实例变量 |
        | 静态字段 / 类变量（Static Field / Class Variable） | 类里、方法外、带 `static` | 类级共享，不属于某个对象 | 有默认值 | 所有对象共享同一份 |

        成员变量通常指字段，包括实例字段和静态字段。字段有默认值：整数是 `0`，浮点数是 `0.0`，`boolean` 是 `false`，引用类型是 `null`（Java 里面没有 ~~`undefined`~~）。

        ```java
        class User {
            int age;          // 实例变量：属于每个 User 对象
            String name;      // 实例变量：保存引用，引用指向 String 对象或 null
            static int total; // 类变量：所有 User 对象共享
        }

        public void test() {
            int count = 0;    // 局部变量：在当前方法的栈帧里
        }
        ```

    1. 基本类型和引用类型的区别

        同样是变量，里面装的东西不一样：

        | 写法 | 变量里保存什么 | 变量在哪里 | 对象在哪里 |
        | --- | --- | --- | --- |
        | `int x = 18;`（方法内） | 数字 `18` | 栈帧 | 没有对象 |
        | `User u = new User();`（方法内） | 指向 `User` 对象的引用 | 栈帧 | `new User()` 在堆里 |
        | `String s = "Tom";`（方法内） | 指向字符串对象的引用 | 栈帧 | 字符串对象在堆里；字面量通常来自字符串池 |
        | `class User { int age; }` | `age` 的真实整数值 | 堆里的 `User` 对象内部 | `User` 对象在堆里 |
        | `class User { String name; }` | `name` 这个引用值 | 堆里的 `User` 对象内部 | 被引用的 `String` 对象在堆里或为 `null` |

        这里最容易误解的是：**引用变量在栈里，不代表对象在栈里。** 栈里的 `u` 只是一个引用；真正的 `User` 对象在堆里。

    1. 数组不是例外

        数组本身也是对象。方法里声明的数组变量是局部变量，变量在栈帧；`new` 出来的数组对象在堆。

        ```java
        public void test() {
            int[] nums = new int[5];
            System.out.println(nums[0]); // 输出 0
        }
        ```

        这段代码可以拆开看：

        - `nums` 是局部变量，里面保存数组引用，所以 `nums` 在当前方法栈帧里。
        - `new int[5]` 创建数组对象，所以数组本体在堆里。
        - `nums[0]` 是数组对象内部的元素，所以也在堆里的数组对象内部。
        - 数组对象在堆里，数组元素会有默认值；`int` 数组元素默认是 `0`。

    1. 参数传递的真相

        Java 只有值传递。方法参数本质上也是局部变量。

        - 基本类型参数：拷贝的是具体值。
        - 引用类型参数：拷贝的是引用值，不是拷贝整个对象。

        ```java
        void change(User user) {
            user.age = 20;
        }

        void test() {
            User u = new User();
            change(u);
        }
        ```

        `test` 里的 `u` 和 `change` 里的 `user` 是两个局部变量，分别在各自方法的栈帧里。但它们保存了同一个堆对象的引用，所以 `user.age = 20` 修改的是同一个堆对象，`u` 后续也能看到变化。

    </details>

    - 最终结论

        - **栈管执行过程**：哪个方法正在执行、这个方法里的参数和局部变量是什么。
        - **堆管对象本体**：`new` 出来的对象、数组，以及对象内部的实例字段、数组元素。
        - **引用只是指路牌**：引用可以存在栈帧里，也可以存在堆对象的字段里，还可以存在数组元素里。
        - **字段看归属**：实例字段属于对象，对象在堆里，所以实例字段也在对象内部；`static` 字段属于类，不属于某个对象。
        - **多个引用可以指向同一个对象**：改的是对象本体，不是某个变量名。
        - **JVM 可能做逃逸分析、标量替换、锁消除优化**，但不改变 Java 语义；学习时按这套规则理解即可。

    **一句话总结：** 看声明位置判断变量归属；看类型判断变量里装的是值还是引用；看 `new` 判断对象本体在堆里。
- 常量与不可变：`final`

    `final` 的核心含义是“只能赋值一次”。

    - `final` 修饰局部变量、参数、字段：变量不能再次指向新值。
    - `final` 修饰引用变量：引用不能换对象，但对象内部状态仍可能被修改。
    - `final` 修饰方法：子类不能重写该方法。
    - `final` 修饰类：不能被继承，如 `String`。
    - 真正常量通常写成 `public static final`，命名用全大写加下划线，如 `MAX_SIZE`。
- 关键字修饰符

    出现在类型（或方法返回值类型）**之前**的**关键字修饰符**按声明位置不同而不同；常见分类如下（同一条声明里可组合，但受语法限制）：

    - **访问控制**：`public`、`protected`、（不写时是包访问权限package-private，没有对应关键字、）`private`
    - **通用**：`static`、`final`
    - **仅类 / 接口 / 方法**：`abstract`
    - **仅方法**：`synchronized`、`native`、`strictfp`（`strictfp` 自 Java 17 起已过时，不建议新代码使用）
    - **仅字段**：`transient`、`volatile`
    - **接口实例方法**：`default`
    - **封闭类型（Java 17+）**：`sealed`、`non-sealed`，以及类头上的 `permits` 子句

    说明：顶级类只能用 `public` 或包访问权限；`private`、`protected` 通常用于成员或嵌套类型。局部变量只能用 `final`；`var` 是局部变量类型推断，不是修饰符。注解 `@…` 可写在修饰符前，但不算上述关键字修饰符。模块上的 `open` 属于模块声明，不是成员/局部上的修饰符。
- 包机制

    包可以理解为 Java 的命名空间和目录组织方式，用来组织代码、避免同名冲突，并配合访问控制限制可见范围。

    ```java
    package com.example.demo.service; // package 只写包名；import 才写具体类名或 *
    ```

    - 核心规则：

        - 普通源文件中，`package` 写在源文件顶部（注释后、`import` 前）；一个 `.java` 文件最多声明一个包。
        - 有显式顶级类声明时（如 `public class 类名 {}`），通常写在 `package`、`import` 之后。
        - `package` 只写包名，不写类名。
        - 包名通常全小写，常见写法是公司域名倒置，如 `com.baidu.project`。
        - 包路径通常与目录结构一致，如 `com.example.demo.service` 对应 `com/example/demo/service`。
        - 不写 `package` 就是默认包（default package），意思是这个类不属于任何具名包；练习代码可以用，正式项目一般不要用。

            >默认包和包访问权限不是同一个概念：默认包说的是“源文件有没有声明包名”；包访问权限说的是类、字段、方法、构造器不写 `public` / `protected` / `private` 时，只能被同一个包里的代码访问。
    - `import` 规则：

        - 使用其他包下的类型且不写全限定名时，通常需要 `import`。
        - `java.lang` 下的类默认导入，如 `String`、`System`。
        - 同包下的类型可直接使用，不需要 `import`。
        - 也可以直接写全限定类名（FQN, Fully Qualified Name），如 `java.util.List`。
        - `import com.example.*;` 只导入当前包下的类型，不会导入子包。

            >`import com.example.*;` 不会把 `com.example.service.UserService` 一起导入。

        - `import` 只是简化类名书写，不会因为写了 `import` 就提前加载整个包或类；类加载常由首次主动使用触发，例如创建对象、访问静态成员、调用静态方法、反射访问。

            >`import` 是编译期语法，作用是把冗长的全限定类名简化为简单类名；它不像 JS 的 `import` 那样执行模块加载。
        - `import 包.类;`、`import 包.*;`、`import static 包.类.静态成员;`、`import static 包.类.*;`（导入所有静态成员，导入后可直接写成员名）
        - 除 `java.lang.*` 外，其他标准库包通常也要显式 `import`。
        - 常用判断顺序：同包类型可直接用 -> 显式 `import 具体类` -> 通配符 `import ...*`；`java.lang.*` 会自动参与解析。若多个来源出现同名类型，可能需要写全限定名或直接编译报歧义。

            >同包类型和显式 `import 具体类` 最明确；通配符 `import ...*` 与 `java.lang.*` 出现同名类型时可能产生歧义。
        - 如果两个包里有同名类，`import` 不能消除歧义，冲突时必须写全限定名。
    - 和访问权限的关系：

        - `public`：任何包都能访问。
        - `protected`：同包可访问；跨包时仅子类在继承访问语境中可访问。
        - 不写修饰符：只有同包可访问，叫包访问权限（package-private）。
        - `private`：只有当前类内部可访问。
    - 实际项目通常会按包分层，例如 `controller`、`service`、`mapper`、`entity`、`config`、`util`。
    - 常见坑：

        - 目录结构和 `package` 声明不一致，容易导致编译或 IDE 识别异常。
        - 默认包中的类不能被其他包 `import`。
        - 子包不是父包的一部分，`com.example` 和 `com.example.service` 是两个不同的包。

- Javadoc

    >类似于“去掉了 `{type}` 标注的 JSDoc”：类型来自 Java 方法签名，注释负责解释用途、参数含义、返回值和异常。

    ```java
    /**
     * 根据用户 id 查询用户。
     *
     * @param id 用户 id
     * @return 用户对象；不存在时返回 null
     * @throws IllegalArgumentException id 非法时抛出
     */
    User findById(long id) {
        return null;
    }
    ```

    - 常用标签：`@param`、`@return`、`@throws`、`@see`、`@deprecated`。
    - `javadoc 文件.java` 可生成 HTML 文档。
- 增强 `for`（for-each）：`for (元素类型 元素名 : 遍历对象) { ... }`

    - 元素类型：与元素实际类型一致，或其父类型/接口。
    - 遍历对象：数组，或实现 `Iterable` 的集合（如 `List`、`Set`）。
    - 常见纠错：`Map` 不能直接 for-each，通常遍历 `entrySet()` / `keySet()` / `values()`。
- 方法

    `可选修饰符 返回值类型 方法名(参数类型 参数名, ...) { 方法体 }`

    - 返回值类型写 `void` 表示没有返回值。
    - 有返回值的方法必须返回与声明类型兼容的值。
    - 参数列表里要同时写“类型 + 参数名”。

    - Java 参数传递一律是值传递：

        - 传基本类型：传的是值本身。
        - 传引用类型：传的是引用值的副本，不是对象拷贝。

    - 重载（Overload）：同一个类中，方法名相同且参数列表不同（参数个数、类型或类型顺序不同）。

        ```java
        int sum(int a, int b) { return a + b; }
        int sum(int a, int b, int c) { return a + b + c; }
        ```

        仅返回值类型不同，不算重载；仅访问修饰符不同，不算重载。
    - 可变参数：`类型... 变量名`（`...` 前后都可以加空格）

        ```java
        int sum(int... nums) {
            int total = 0;
            for (int num : nums) {
                total += num;
            }
            return total;
        }
        ```

        - 一个方法最多只能有一个可变参数。
        - 可变参数必须放在最后。
        - 调用时可传 0个或多个 同类型实参，也可传同类型数组。

            ```java
            sum();              // 传 0 个 int，nums 是长度为 0 的 int 数组
            sum(1);             // 传 1 个 int
            sum(1, 2, 3);       // 传多个 int
            sum(new int[]{1, 2, 3}); // 也可以直接传 int 数组
            ```
    - 调用方法的方式：`类.静态方法()`、`对象.实例方法()`（非静态方法 == 实例方法）。

        >“成员方法”容易产生歧义，可能包含静态方法，也可能狭义地指代实例方法。建议直接说“静态方法”或“实例方法”。
- 数组

    数组用于存放“一组相同类型的数据”。数组是引用类型，数组对象在堆里，长度创建后不能改变。

    1. 声明

        推荐写法：`int[] nums`。`int nums[]`也合法但不推荐。
    1. 初始化

        >初始化指第一次赋值；赋值是更大的概念，包含初始化和后续重新赋值。

        1. 动态初始化：只给长度，元素使用默认值。

            ```java
            int[] nums = new int[3]; // [0, 0, 0]
            ```

        >同一个 `new` 表达式里，不能既写长度又写初始化列表，如 ~~`new int[3]{1, 2, 3}`~~ 非法。

        2. 静态初始化：直接给内容。

            ```java
            int[] nums1 = {10, 20, 30};
            int[] nums2 = new int[]{10, 20, 30};
            ```
        - 声明与赋值分开时，右侧必须使用 `new 类型[]{...}`，不能只写 ~~`{...}`~~

            ```java
            int[] num1;
            num1 = new int[]{10, 20, 30}; // 合法
            // num1 = {10, 20, 30}; // 编译错误
            ```
    1. 访问和修改

        ```java
        int[] nums = {10, 20, 30};
        System.out.println(nums[0]); // 10
        nums[1] = 99;                // 修改第二个元素
        ```

        - 数组下标从 `0` 开始。
        - 最后一个下标是 `length - 1`。
        - 越界会报 `ArrayIndexOutOfBoundsException`。
    1. 长度

        数组长度固定，创建后不能改；通过 `.length` 获取长度。

        ```java
        int[] nums = {10, 20, 30};
        System.out.println(nums.length); // 3
        ```

    遍历数组最常见两种写法：

    ```java
    int[] nums = {10, 20, 30};

    for (int i = 0; i < nums.length; i++) {
        System.out.println(nums[i]);
    }

    for (int num : nums) {
        System.out.println(num);
    }
    ```

    - 多维数组

        Java 的多维数组本质上是“数组里的元素还是数组”，所以可以是不规则数组。

        >不规则数组（也叫“锯齿数组”）：每一行长度可以不一样的二维/多维数组。相对地，规则数组一般如 `new int[3][4]`，每行都是 4。

        ```java
        int[][] matrix = {
            {1, 2, 3},
            {4, 5}
        };

        int[][][] cube = {{{1, 2}}, {{3, 4}}};
        ```

    - <details>

        <summary>稀疏数组</summary>

        稀疏数组不是 Java 内置类型，而是一种压缩存储思路：当二维数组中大部分元素都是默认值（如 `0`）时，只保存有意义的数据。

        常见表示方式是 `int[][] sparse`，每行 3 列：`行下标`、`列下标`、`值`。通常第 0 行保存原数组信息：`总行数`、`总列数`、`有效值个数`。

        ```java
        int[][] sparse = {
            {11, 11, 2},
            {1, 2, 1},
            {2, 3, 2}
        };
        /*
          原数组是 11 行 11 列，一共有 2 个非 0 值
          这 2 个值分别在：
          array[1][2] = 1
          array[2][3] = 2
          其他位置默认都是 0
        */
        ```
        </details>

- Java 的面向对象包含关系

    ```text
    包 package
    └─ 类 class / 接口 interface / 枚举 enum / 注解 annotation
       └─ 类 class
          ├─ 静态成员：属于类本身
          │  ├─ 静态字段 / 类变量：static field
          │  ├─ 静态方法 / 类方法：static method
          │  └─ 静态代码块：static {}：类初始化时执行一次
          │
          ├─ 实例成员：属于实例对象
          │  ├─ 实例字段 / 实例变量：instance field
          │  └─ 实例方法：instance method
          │
          ├─ 构造器 constructor：负责创建对象时初始化
          ├─ 初始化代码块：{}，创建对象时执行
          └─ 嵌套类型 nested type：类里面再定义类、接口、枚举、注解

    实例对象 object / instance
    ├─ 由类 new 出来
    ├─ 拥有自己的一份实例字段
    ├─ 可以调用实例方法
    └─ 共享类里的 static 字段和 static 方法

    方法 method
    ├─ 参数 parameter：变量
    ├─ 局部变量 local variable：变量
    ├─ 局部类型 local type：可选；局部类，Java 16+ 还支持局部 record；不是类成员，只在该作用域可见
    └─ 代码逻辑 statement / expression
    ```
- 面向对象：类与对象、封装、继承、多态

    >OO = Object-Oriented，面向对象（一种思想/范式）；OOP = Object-Oriented Programming，面向对象编程。以类的方式组织代码，以对象的方式组织（封装）数据

    - 类与对象

        类是对象的模板，定义字段（属性）和方法（行为）；对象是类的实例，通常通过 `new` 创建。

        - 实例字段 / 实例方法属于对象；`static` 字段 / 方法属于类。
        - 使用对象前，通常要先有引用变量指向一个对象：`User user = new User();`。

    - 构造器

        构造器和类名相同，没有返回值，也不能写 `void`；通常在创建对象时被调用，常用于初始化实例字段。

        - 构造器可以重载；调用时实参必须匹配某个构造器的形参列表。
        - 如果一个构造器都不写，Java 会自动生成一个无参构造器。
        - 只要手写了任意构造器，Java 就不会再自动生成无参构造器；是否必须补写无参构造器，取决于代码是否需要 `new User()`，或框架是否需要通过反射创建对象。
        - `this.xxx` 表示当前对象的字段；构造器之间可以用 `this(...)` 调用，但必须写在第一行。
    - 初始化代码块

        直接写在类里的 `{}` 代码块，不属于某个方法；每次 `new` 对象时都会执行，执行时机早于构造器正文。`static {}` 是静态代码块，类初始化时执行一次。

        | 写法 | 执行时机 | 常见用途 |
        | --- | --- | --- |
        | 实例字段直接赋值 | 创建对象时，早于构造器正文 | 简单默认值 |
        | 实例初始化代码块 `{}` | 每次 `new` 对象时，早于构造器正文 | 多个构造器共享的实例初始化逻辑 |
        | 构造器 `User(...) {}` | 每次 `new` 对象时，按调用的构造器执行 | 根据参数初始化对象 |
        | 静态字段直接赋值 | 类初始化时执行一次 | 简单类级默认值 |
        | 静态代码块 `static {}` | 类初始化时执行一次 | 初始化静态字段或类级资源 |

        >同一类中，静态字段赋值和静态代码块按源码顺序执行；实例字段赋值和实例初始化代码块也按源码顺序执行，然后才进入构造器正文。

        ```java
        class User {
            String name; // 实际项目里更常见的是直接给字段赋值或写在构造器里，而不用初始化代码块
            static {
                System.out.println("类初始化时执行一次");
            }
            {
                name = "默认名"; // 初始化代码块
            }
            User() {
                System.out.println(name);
            }
        }
        ```

    - 封装

        把对象内部状态和实现细节收起来，只通过必要的方法暴露能力。

        - 字段通常用 `private`，通过 `public` 方法提供受控访问。
        - Getter / Setter 是访问入口，不是封装本身；Setter 可以做校验，也可以只提供 Getter 形成对外只读访问。
        - 封装的目标是减少外部代码对内部结构的依赖，后续修改实现时不影响调用方。

    - 继承 `extends`

        子类（派生类）复用父类（基类）的非 `private` 成员，并可以扩展或重写父类行为。

        - Java 类只能单继承（没有类的多继承）：一个类只能 `extends` 一个父类，但可以 `implements` 多个接口。
        - （除 `Object` 本身外，）所有类最终都继承自 `java.lang.Object`。
        - 继承表示 “is-a” 关系；若只是复用代码，则优先考虑组合“has-a”。

            1. `class Dog extends Animal {}`：狗是一种动物，is-a 合理，可以用继承。
            2. `class Engine extends Car {}`：发动机不是一辆车，is-a 不合理；应使用组合 has-a：`class Car { private Engine engine; }`，表示车有一个发动机。
        - 访问父类成员：`super.字段` 或 `super.方法()`；父类 `private` 成员不能直接访问。
        - 构造器

            - 子类构造器会先调用父类构造器；可以用 `super(...)` 明确选择父类构造器，也必须写在第一行。

                >因为 `this(...)` 和 `super(...)` 都必须在第一行，因此一个构造器里只能直接选择其中一个。
            - 如果父类没有无参构造器，子类构造器必须显式写 `super(...)` 并传入匹配参数。
    - `对象 instanceof 类或接口`：当对象的运行时类型 与该类型兼容（**即该类型本身、其子类或其实现类**）时，结果为 `true`

        允许：`父类 变量 = new 子类();`（向上转型）。反过来不行。

        ```java
        Animal a = new Dog();      // 向上转型：总是安全
        Dog d1 = (Dog) a;          // 向下转型：安全（a 真实指向 Dog）

        Animal b = new Animal();
        Dog d2 = (Dog) b;          // 编译能过，但运行时抛 ClassCastException

        // 更稳妥写法
        if (a instanceof Dog) {
            Dog d3 = (Dog) a;
        }
        ```

    - 多态

        >常见运行时多态的前提：①有继承或接口实现关系，②父类/接口引用指向子类/实现类对象，③调用可被重写的实例方法。

        多态指：同一个父类/接口类型的引用，指向不同子类/实现类对象时，同一段方法调用会在运行期执行不同实现。

        编译期看引用的声明类型，决定“能调用哪些成员”；运行期看真实对象类型，决定“执行哪个重写后的实例方法”。字段和 `static` 方法是隐藏，`private` 方法不能被重写，`final` 方法禁止重写：都不参与运行时多态。

        ```java
        Person p = new Student();
        p.talk(); // 编译期允许调用 Person 中声明的 talk；运行期执行 Student 重写后的 talk（若 Student 未重写，则调用 Person 的 talk）

        Object obj = new Student();
        // obj.talk(); // 编译错误：Object 类型中没有 talk()

        Person.printType();  // 若 printType 是 static 方法，按声明类调用；静态方法是隐藏，不是重写
        p.printType();  // p.printType() 能编译，但因为 printType 是 static 方法，所以它不会按 new Student() 的真实对象走多态，而是按 p 的声明类型 Person 解析，等价于 Person.printType()。不推荐这样写
        ```

        - 重写（Override）：子类重新实现父类实例方法，方法签名要兼容，访问权限不能更窄（`public` > `protected` > 包访问 > `private`），建议加 `@Override`，抛出的受检异常范围不能更宽。

            >概念总结：重载（Overload），同一类中方法（实例方法或静态方法）“参数列表不同”。重写，父子类中“同一实例方法的不同实现”。多态，用父类/接口引用调用该实例方法时，运行期执行真实对象的实现。
    - 抽象类、接口、枚举

        - 抽象类（`abstract class`）：不能直接 `new`，适合放共同状态和部分实现，子类继承后补全抽象方法。
        - 接口（`interface`）：定义能力或契约，一个类可以 `implements` 多个接口；接口中的抽象方法默认是 `public abstract`，字段默认是 `public static final`，也可以定义 `default` / `static` 方法，Java 9+ 还可以定义 `private` 辅助方法。
        - 枚举（`enum`）：表示固定有限的一组实例，适合状态码、类型码、开关选项、流程节点；枚举常量本质上是该枚举类型的固定对象。
        - 选择：有共同字段和部分实现用抽象类；只约定能力用接口；值集合固定用枚举。
- 嵌套、局部、匿名类型

    先按“声明位置”判断：

    - **成员位置**：直接写在类 / 接口 / 枚举 / 注解的 `{}` 第一层。可声明成员类、成员接口、成员枚举、成员注解；Java 16+ 还支持成员 `record`。
    - **局部位置**：写在方法、构造器、初始化代码块、普通代码块内部。可声明局部类；Java 16+ 还支持局部 `record`。
    - **表达式位置**：不是单独声明一个类型，而是在需要一个对象值的地方直接写 `new 父类或接口() { ... }`。这会创建匿名类对象，常见于赋值、传参、返回值。

    >严格说，字段、方法、嵌套类型是类的成员；构造器和初始化代码块不是成员，但它们也写在类体第一层。

    ```java
    class User {
        class Profile {}        // 成员类：非 static，也叫内部类
        static class Address {} // 静态嵌套类
        interface Validator {}  // 成员接口，隐式 static
        enum Role { ADMIN }     // 成员枚举，隐式 static
        @interface FieldName {} // 成员注解，隐式 static

        // Java 16+:
        // record Pair(String key, String value) {} // 成员 record，隐式 static

        void test() {
            class LocalHelper {} // 局部类

            // Java 16+:
            // record LocalPair(String key, String value) {} // 局部 record

            Runnable task = new Runnable() { // 匿名类
                public void run() {}
            };

            runTask(new Runnable() { // 匿名类作为方法实参
                public void run() {}
            });
        }

        void runTask(Runnable task) {}
    }
    ```

    | 类型形式 | 位置 | `static` 规则 | 重点 |
    | --- | --- | --- | --- |
    | 非静态成员类 | 成员位置 | 不默认 `static` | 会关联一个外部对象，也叫内部类 |
    | 静态嵌套类 | 成员位置 | 显式写 `static` | 不关联外部对象，常用于组织辅助类型 |
    | 成员接口 | 成员位置 | 隐式 `static` | 定义和外层类型强相关的能力规范 |
    | 成员枚举 | 成员位置 | 隐式 `static` | 定义和外层类型强相关的固定选项 |
    | 成员注解 | 成员位置 | 隐式 `static` | 定义和外层类型强相关的元数据标记 |
    | 成员 `record` | 成员位置 | 隐式 `static` | Java 16+，定义和外层类型强相关的只读数据结构 |
    | 局部类 | 局部位置 | 不适用 | 只在当前方法或代码块内可见 |
    | 局部 `record` | 局部位置 | 不适用 | Java 16+，适合方法内部临时数据结构 |
    | 匿名类 | 表达式位置 | 不适用 | 在需要对象值的位置直接 `new ... {}`，没有类名，通常一次性使用 |

    结论：**成员位置看是否属于外层类型；局部位置看是否只在当前代码块可见；匿名类看是否由 `new ... {}` 临时创建。** 局部位置不能直接声明 `interface`、`enum`、`@interface`。

- 异常处理：`try-catch-finally`、`throw`、`throws`

    - `try`：包住可能出错的代码。
    - `catch`：捕获并处理异常。
    - `finally`：无论是否异常，通常都会执行，常用于释放资源。
    - `throw`：在方法内部主动抛出一个异常对象。
    - `throws`：写在方法声明上，告诉调用方这个方法可能抛出哪些异常。
    - 受检异常（checked exception）必须捕获或继续 `throws`；运行时异常（runtime exception）通常表示代码逻辑问题，不强制捕获。

    ```java
    void read(String path) throws IOException {
        if (path == null) {
            throw new IllegalArgumentException("path 不能为空");
        }

        try {
            Files.readString(Path.of(path));
        } catch (IOException e) {
            throw e;
        } finally {
            System.out.println("清理资源");
        }
    }
    ```

    >实际读写资源优先用 `try-with-resources`，它会自动关闭实现了 `AutoCloseable` 的资源。

#### 常用 API 与进阶主题
业务开发里最常用的一批内容：

- `String`：不可变字符串；频繁拼接优先用 `StringBuilder`。
- 日期时间 API：优先用 `java.time`，如 `LocalDateTime`、`Instant`、`Duration`，少用旧的 `Date` / `Calendar`。
- 集合类：`List` 有序可重复；`Set` 不重复；`Map` 存键值对；遍历 `Map` 常用 `entrySet()`。
- 泛型：把类型变成参数，如 `List<String>`，主要用于编译期类型检查，运行期有类型擦除。
- 注解：给类、接口、枚举、字段、方法、构造器、参数、局部变量、类型使用位置添加元数据，常配合框架、反射、编译器使用。
- IO 流：字节流处理二进制，字符流处理文本；资源关闭优先用 `try-with-resources`。
- 反射：运行期读取类、构造器、字段、方法、参数、注解、泛型签名信息；框架常用，业务代码少滥用。
- 多线程基础：先掌握 `Thread`、`Runnable`、线程池、锁、可见性、原子性，再深入并发工具类。

### 后端工程与数据中间件
#### 构建与依赖管理
- **Maven**：最常见的 Java 项目构建与依赖管理工具。

    1. 配置 IDE 的 Maven 版本：

        1. 运行路径（如 Cursor 配置 `/usr/local/apache-maven-3.9.14/bin/mvn` 或 `~/.sdkman/candidates/maven/current/bin/mvn`；IDEA 配置 `/usr/local/apache-maven-3.9.14` 或 `~/.sdkman/candidates/maven/current`）
        2. 用户运行环境配置文件（如：`~/.m2/settings.xml`）

            >仓库地址（私服/镜像）、账号密码（私有仓库）、代理（proxy）、本地仓库路径。
    1. 项目内的 `pom.xml`：项目级构建配置

        >依赖（dependencies）、构建流程（build）、插件（plugins）、模块结构（modules）。
    1. 配置文件（Profiles）选择配置

        >这个配置通常保存在 IDE 本地配置中（如 `.idea` 或其他目录），注意跨设备、跨 IDE 不一定同步。
    1. 安装

        执行 Lifecycle（生存期）的 `clean`、`install`（相当于 `mvn clean install`），会先清理，再按 Maven 生命周期运行到 `install` 阶段；其中 `install` 会把当前项目产物安装到本地仓库（根据 Maven 用户运行环境配置文件设置，默认 `~/.m2/repository`）。

        >1. `clean`：执行清理生命周期，通常会删除当前项目的 `target` 目录，清理上一次构建产物；不会删除本地仓库 `~/.m2/repository` 中的依赖。
        >1. `install`：执行默认生命周期直到 `install` 阶段，关键阶段包括 `validate` -> `compile` -> `test` -> `package` -> `verify` -> `install`，并将当前项目产物安装到本地 Maven 仓库（默认 `~/.m2/repository`），供本机其他项目依赖。
        >
        >    同理，执行 `deploy` 就是执行默认生命周期直到 `deploy` 阶段，关键阶段包括 `validate`->`compile`->`test`->`package`->`verify`->`install`->`deploy`
        >1. `切换“跳过测试”模式`：切换 Maven 构建时是否跳过测试执行（Maven 生命周期的 `test` 阶段），类似 `mvn install -DskipTests`。（`-DskipTests` 跳过执行测试但仍编译测试代码；`-Dmaven.test.skip=true` 连测试编译也跳过）

    >建议用ide的可视化操作（配置文件（Profiles）选择配置、编辑配置、安装、运行或调试）来代替mvn命令行，如：`mvn -U -pl 项目路径 -am clean install -P环境 -Dmaven.test.skip=true`、`mvn -f 项目路径/pom.xml spring-boot:run -P环境 -Dmaven.test.skip=true`

    1. `同步所有Maven项目`（或`重新加载所有Maven项目`）

        >1. `同步所有Maven项目`：让 IDE 按最新 `pom.xml` 重新导入 Maven 项目，更新模块结构、依赖、源码目录、资源目录、插件配置等信息。
        >1. `重新加载所有Maven项目`：通常与“同步所有Maven项目”作用接近，本质上都是让 IDE 重新读取所有 `pom.xml`，刷新 Maven 项目模型和依赖解析状态。
    - Maven 跨项目依赖通常认构建产物（jar），不是直接认另一个项目的源码；被依赖项目改动后，需要重新 `package` / `install`，或用 `-pl` / `-am` 放到同一次 reactor 构建里。

- **Gradle**：更灵活，Android 和部分现代项目里较常见。

>对于多数后端初学者，先掌握 Maven 即可。

#### Web 框架与持久层
- **Java Web**：传统 Web 基础主要包括 Servlet、Filter、Listener、Session、Cookie。
- **Spring MVC**：处理 HTTP 请求映射、参数绑定、数据校验、异常处理、视图解析、JSON 响应。
- **MyBatis**：负责 SQL 映射、参数绑定、结果映射、动态 SQL、数据库访问。

可以简单理解为：

- Spring MVC 负责“接请求、回响应”
- MyBatis 负责“连数据库、执行 SQL”

#### Spring 生态
- **Spring Framework**：核心框架，提供 IoC、AOP、事务管理、资源访问、事件、类型转换、校验。
- **Spring Boot**：在 Spring 基础上做自动配置，简化项目搭建和开发。

    启动标配：`@SpringBootApplication`（一个组合注解，主要包含：`@SpringBootConfiguration`、`@EnableAutoConfiguration`、`@ComponentScan`；其中 `@SpringBootConfiguration` 可视为 Spring Boot 场景下的 `@Configuration`）

对业务开发来说，最重要的不是背概念，而是先理解常见分层：

- Controller：接收请求、返回响应
- Service：写业务逻辑
- Mapper / DAO：访问数据库

#### 关系型数据库：MySQL
- 最常见的关系型数据库。
- 先掌握建表、增删改查、索引、事务，再谈性能优化。
- 业务开发重点：表结构设计、主键、唯一约束、外键取舍、分页查询、慢 SQL、事务隔离级别。

#### 缓存与内存数据：Redis
- 常用作缓存，也可用于分布式锁、计数器、会话、排行榜、延迟队列场景。
- 要先理解缓存命中、过期、穿透、击穿、雪崩这些基础问题。
- 常见数据结构：String、Hash、List、Set、Sorted Set；先按业务场景选结构，不要只把 Redis 当 Map 用。

#### 消息队列：Kafka / RabbitMQ
- **Kafka**：偏日志流、吞吐高，常用于异步削峰、流式处理。
- **RabbitMQ**：偏传统消息队列，路由能力更丰富，业务系统里也很常见。
- 核心问题：消息是否丢失、是否重复消费、消费失败怎么重试、顺序性是否重要、是否需要死信队列。
