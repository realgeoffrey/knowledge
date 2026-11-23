# Rust学习笔记

## 目录
1. [核心软件](#核心软件)
1. [笔记](#笔记)
1. [语法](#语法)

---
### 核心软件
1. rustup

    Rust官方工具链管理器
1. rustc

    Rust的编译器
1. cargo

    Rust的构建系统和包管理器

    >项目使用的外部库是依赖（dependencies）。Rust 的编译单元叫 crate，一个 Cargo 包（package）可以包含多个 crate。
1. rustfmt

    Rust代码格式化工具

### 笔记
1. `.rs`Rust源文件名

    文件、文件夹命名用 蛇形命名法（字母全小写、下划线`_`分割单词），e.g. `hello_world.rs`。
1. `fn main() {}`

    `main` 是普通 Rust 可执行程序的入口函数。
1. `println!`调用了一个 Rust 宏（macro）

    `println!("hello")` 中名称后的 `!` 标识宏调用。普通函数调用写作 `函数名(参数)`。
1. Rust 是一种**静态类型**语言，通常采用**预先编译（ahead-of-time compilation）**

    1. 在编译时就必须知道所有变量的类型。

        每一个值都属于某一个 数据类型（data type）。根据值及其使用方式，编译器通常可以推断出我们想要用的类型，当多种类型均有可能时，必须增加类型注解。
    2. 可以用 `rustc main.rs` 将单文件程序编译为可执行文件；Cargo 项目通常用 `cargo run` 编译并运行。

        >对方的平台与目标架构兼容，并具备程序依赖的动态库时，就可以直接运行可执行文件，无需安装 Rust。
1. `rustc`

    `rustc 文件`：（在执行命令的位置，）输出一个二进制的可执行文件。
1. `cargo`

    1. `cargo new 文件夹名` 创建项目。
    1. `cargo build` 构建项目。
    1. `cargo run` 构建项目并运行项目。
    1. `cargo check` 检查项目中的编译错误，通常会创建构建目录，但不生成项目的最终可执行文件。

    >`rustc main.rs` 默认将可执行文件放在当前工作目录；`cargo build` 默认将开发构建产物放在 `target/debug/`。

    >`cargo build --release` 和 `cargo run --release` 默认在 `target/release/` 生成优化后的产物。`cargo check --release` 使用发布配置检查项目，不生成最终可执行文件。

    1. `cargo update` 在 `Cargo.toml` 的约束内更新依赖并写入 `Cargo.lock`。例如 `"1.2.3"` 默认允许 `>=1.2.3, <2.0.0`，而 `"0.2.3"` 允许 `>=0.2.3, <0.3.0`。[Cargo 版本规则](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#default-requirements)
    1. `cargo doc --open` 构建当前包及其依赖的文档，并在浏览器中打开当前包的文档。
1. Rust 代码中的 函数和变量名 使用 蛇形命名法（字母全小写、下划线`_`分割单词）
1. Rust 是一门 基于表达式（expression-based）的语言

   1. 语句（Statements）是执行一些操作但不返回值的指令。 表达式（Expressions）计算并产生一个值。

    >不同于其他语言的重要区别。
   2. 表达式的结尾没有分号`;`。如果在表达式的结尾加上分号，它就变成了语句，而语句不会返回值。
1. 代码块`{}`的值是其最后一个表达式的值

    正常执行到末尾时，块的值取自末尾未加分号的表达式；没有这种表达式时，块的值是单元值 `()`。
1. 所有权

    1. 规则

        1. Rust 中的每一个值都有一个 所有者（owner）。
        2. 默认采用独占所有权。需要共享同一份数据时，可用 `Rc<T>`，跨线程共享可用 `Arc<T>`；最后一个强引用释放时，内部值被丢弃。
        3. 当所有者（变量）离开作用域，这个值将被丢弃。

        将 `String` 赋给另一个变量时，所有权随之移动。新所有者离开作用域时释放字符串的堆内存。
    1. 如果一个类型实现了 Copy trait，那么一个旧的变量在将其赋值给其他变量后仍然可用。否则旧的变量会被 move

        自定义结构体实现 `Copy` 要求所有字段都实现 `Copy`，且该结构体不能实现 `Drop`。如下是一些 Copy 的类型：

        1. 所有整数类型，比如 u32。
        2. 所有浮点数类型，比如 f64。
        3. 布尔类型，bool，它的值是 true 和 false。
        4. 字符类型，char。
        5. 元组，当且仅当其包含的类型也都实现 Copy 的时候。比如，(i32, i32) 实现了 Copy，但 (i32, String) 就没有。
    1. 赋值、按值传参和返回值都遵循移动或复制规则。传入 `&值` 时传递的是引用，原值仍由调用方持有。
    1. 引用reference `&`

        使用值但不获取其所有权。

        1. 创建一个引用的行为称为 借用（borrowing），（默认）不允许修改引用的值。
        2. `&mut`允许修改引用的值。

            >从而避免 数据竞争（data race）。

            1. 对同一处数据，可以同时持有多个共享借用 `&T`，或者一个独占的可变借用 `&mut T`。
            2. 是否冲突取决于借用的使用区间。即使在同一代码块，前一个借用最后一次使用后也可以开始新的借用。
        3. <details>

            <summary>引用必须总是有效的</summary>

            ```rust
            fn dangle() -> &String { // dangle 返回一个字符串的引用
                let s = String::from("hello"); // s 是一个新字符串

                &s // 返回字符串 s 的引用
            } // 这里 s 离开作用域并被丢弃。其内存被释放。
              // 报错
            ```

            ```rust
            fn no_dangle() -> String {
                let s = String::from("hello");

                s   // 所有权被移动出去，所以没有值被释放。没有错误
            }
            ```
            </details>

        - `&变量[开始索引..结束索引]` 取左闭右开的切片。数组按元素索引，字符串按 UTF-8 字节索引；越界或切在一个字符的编码中间会 panic。
1. 模块系统

    1. 包（Packages）：Cargo 的一个功能，它允许你构建、测试和分享 crate。

        包（package）包含一个或多个 crate，最多一个库 crate，也可有多个二进制 crate。`Cargo.toml` 描述如何构建这些目标。
    1. Crates ：一个模块的树形结构，它形成了库或二进制项目。

        1. crate 是 Rust 在编译时最小的代码单位。
        1. crate 有两种形式：

            1. 二进制项 可以被编译为可执行程序，比如一个命令行程序或者一个 web server。它们必须有一个 main 函数来定义当程序被执行的时候所需要做的事情。

                默认二进制目标的 crate 根：`src/main.rs`（其他二进制目标可放在 `src/bin/`）。
            1. 库 并没有 main 函数，它们也不会编译为可执行程序，它们提供一些诸如函数之类的东西，使其他项目也能使用这些东西。

                crate根节点：`src/lib.rs`
    1. `mod` 声明模块，`use` 将路径引入当前作用域；模块与函数默认私有，`pub` 可公开它们。
    1. 路径（path）：一个命名例如结构体、函数或模块等项的方式。

### 语法
1. `let`变量

    1. 变量默认是不可改变的（immutable）

        ```rust
        let apples = 5;         // 不可变（默认）
        apples = 6;             // 报错


        let mut bananas = 5;    // 可变
        bananas = 6;            // 正确（变量值变化），但是类型不能改变
        bananas = '7';          // 报错
        ```
   2. 隐藏（Shadowing）

        我们可以定义一个与之前变量同名的新变量。这意味着当您使用变量的名称时，编译器将看到第二个变量。实际上，第二个变量“遮蔽”了第一个变量，此时任何使用该变量名的行为中都会视为是在使用第二个变量，直到第二个变量自己也被隐藏或第二个变量的作用域结束。可以用相同变量名称来隐藏一个变量，以及重复使用 let 关键字来多次隐藏。新变量不受被隐藏变量的任何影响（类型、值）。

        ```rust
        let x = 5;

        let x = x + 1;          // 隐藏（前一个同名变量的值没有变化，是隐藏了）

        {
            let x = x * 2;      // 隐藏（前一个同名变量的值没有变化，是隐藏了）
            println!("12: {}", x);
        }
        {
            let x = "字符串";     // 隐藏（前一个同名变量的值没有变化，是隐藏了）
            println!("字符串: {}", x);
        }

        println!("6: {}", x);
        ```
1. `const`常量

    与`let`变量的区别：

    1. 不允许对常量使用 `mut`。常量不光默认不可变，它总是不可变。
    2. 必须 注明值的类型。
    3. 可以在任何作用域中声明，包括全局作用域。（`let`变量不能在全局作用域定义）
    4. 只能被设置为常量表达式，而不可以是其他任何只能在运行时计算出的值。

    - Rust约定常量命名用 字母全大写、下划线`_`分割单词。

    ```rust
    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
    ```
1. `println!("{} {x} {}", y, y+1);`，变量可以写在`{}`里或后面参数，表达式只能写在后面参数。`{}`按顺序匹配后面的参数。
1. 数据类型

    1. 标量（scalar）

        整型、浮点型、布尔类型、字符类型

        >单引号`'`声明 char 字面量，而与之相反的是，使用双引号`"`声明字符串字面量。
    2. 复合（compound）

        元组（tuple）`()` `.0` 解构、数组（array）`[]` `[0]`

        >不带任何值的元组有个特殊的名称，叫做 单元（unit） 元组。这种值以及对应的类型都写作 `()`，表示空值或空的返回类型。如果表达式不返回任何其他值，则会隐式返回单元值。

    - 结构体struct

        ```rust
        // 先定义结构体
        struct User {
          active: bool,      // 字段（field）
          username: String,
          email: String,
          sign_in_count: u64,
        }

        fn main() {
            // 再使用
            let mut user1 = User {
                active: true,
                username: String::from("someusername123"),
                email: String::from("someone@example.com"),
                sign_in_count: 1,
            };

            user1.active = false;
        }
        ```

        若可变，则整个实例都是可变的；Rust 并不允许只将某个字段标记为可变。

        使用字段初始化简写语法（field init shorthand）。

        结构体更新语法 `..旧实例` 放在最后。未显式赋值的字段按类型复制或移动。若移动了字段，旧实例不能再整体使用，未移动的字段仍可访问。

        - 元组结构体

            ```rust
            struct Color(i32, i32, i32);

            fn main() {
                let black = Color(0, 0, 0);
            }
            ```
        - 类单元结构体（unit-like structs）

            ```rust
            struct AlwaysEqual;

            fn main() {
                let subject = AlwaysEqual;
            }
            ```
    - 枚举

        枚举的每个变体可以携带不同的数据。无字段变体直接写作 `Message::Quit`；元组变体按函数形式构造，如 `Message::Write(text)`；具名字段变体写作 `Message::Move { x, y }`。

        像impl定义结构体的方法一样，`impl`可以定义枚举的方法。

        标准库的 `Option<T>` 用 `Some(T)` 或 `None` 表示值是否存在。`Result<T, E>` 用 `Ok(T)` 或 `Err(E)` 表示成功或失败；在返回兼容 `Result` 的函数中，`结果?` 会取出成功值，遇到错误则提前返回。[可恢复错误与 Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
1. 函数（function）

    `fn`

    1. 在函数签名中，必须 声明每个参数的类型。
    2. 函数可以向调用它的代码返回值，但必须在箭头（`->`）后声明它的类型。每个可能的返回值都必须是这个类型；否则报错。

        在 Rust 中，函数的返回值等同于函数体最后一个表达式的值。使用 return 关键字和指定值，可从函数中提前返回；但大部分函数隐式的返回最后的表达式。
1. 方法（method）

    方法是带有接收者参数的关联函数，在 `impl` 或 trait 中用 `fn` 声明。第一个参数常写作 `self`、`&self` 或 `&mut self`，分别表示取得实例、共享借用或可变借用。

    `impl`（implementation）、`self`、`Self`

    所有在 impl 块中定义的函数被称为 关联函数（associated functions），因为它们与 impl 后面命名的类型相关。

    - 我们可以定义不以 self 为第一参数的关联函数（因此不是~~方法~~），因为它们并不作用于一个结构体的实例

        1. 使用结构体名和`::`语法来调用这个关联函数：比如 `let sq = Rectangle::square(3);`。

            >这个函数位于结构体的命名空间中：`::`语法用于关联函数和模块创建的命名空间。
        2. 关键字`Self`在函数的返回类型中代指在 `impl` 关键字后出现的类型。

    我们可以选择将方法的名称与结构中的一个字段相同。Rust 知道我们指的是方法 width。当我们不使用圆括号时，Rust 知道我们指的是字段 width。

    每个结构体都允许拥有多个`impl`块。

    <details>
    <summary>e.g.</summary>

    ```rust
    struct Rectangle {
        width: u32,
        height: u32,
    }

    impl Rectangle {
        fn area(&self) -> u32 {
            self.width * self.height
        }
    }
    // 允许多个
    impl Rectangle {
        // 允许与字段同名
        fn width(&self) -> bool {
            self.width > 0
        }
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width > other.width && self.height > other.height
        }
        // 不是方法
        fn square(size: u32) -> Self {
            Self {
                width: size,
                height: size,
            }
        }
    }

    fn main() {
        let rect1 = Rectangle {
            width: 30,
            height: 50,
        };
        let rect2 = Rectangle {
            width: 10,
            height: 40,
        };

        println!(
            "The area of the rectangle is {} square pixels.",
            rect1.area()
        );

        if rect1.width() {
            println!("The rectangle has a nonzero width; it is {}", rect1.width);
        }

        println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));

        let sq = Rectangle::square(3);
        println!("{}", sq.width)
    }
    ```
    </details>
1. if表达式`if-else`（`else if`）

    `if 条件 { 表达式1 } else { 表达式2 }` 的值取自执行的分支。

    1. 普通 `if` 的条件必须是 `bool` 值。

        >不像 Ruby 或 JavaScript 这样的语言，Rust 并不会尝试自动地将非布尔值转换为布尔值。必须总是显式地使用布尔值作为 if 的条件。
    2. if表达式 的每个分支的可能的返回值都必须是相同类型；否则报错。

        >Rust 需要在编译时就确切的知道 变量的类型，这样它就可以在编译时验证在每处使用的 变量的类型是有效的。如果 类型仅在运行时确定，则 Rust 无法做到这一点；且编译器必须跟踪每一个变量的多种假设类型，那么它就会变得更加复杂，对代码的保证也会减少。
1. `match`

    `match 表达式 { 值1 => 返回值, 值2 => { 其他语句; 返回值 } }`返回某一个分支中返回的值

    1. match表达式可以是任意类型
    2. match分支返回值，必须是相同类型；否则报错。
    3. match匹配必须被穷尽

        1. 各分支的模式必须覆盖被匹配类型的所有可能值。例如匹配 `Option<T>` 时，可用 `Some(x)` 和 `None` 覆盖两个变体。
        2. 通配模式（匹配余下的所有情况）：任意变量名

            若不需要使用匹配值，则用`_`占位符替代任意变量名。若也没有返回值的话，则用`_ => ()`。
    4. `if let`

        <details>

        <summary>e.g.</summary>

        ```rust
        let mut count = 0;
        match coin {
            Coin::Quarter(state) => println!("State quarter from {state:?}!"),
            _ => count += 1,
        }
        ```

        等价于

        ```rust
        let mut count = 0;
        if let Coin::Quarter(state) = coin {
            println!("State quarter from {state:?}!");
        } else {
            count += 1;
        }
        ```
        </details>
1. 循环`loop`、`while`、`for-in`

    1. `break` 退出当前循环；`continue` 跳到当前循环的下一次迭代。
    2. `loop` 可以用 `break 表达式` 返回值，例如 `let answer = loop { break 42; };`。`while` 和 `for` 循环的值是 `()`，不支持带值的 `break`。
    3. 循环标签可指定跳出的目标，例如给外层循环标记 `'outer: loop` 后，内层可用 `break 'outer;` 退出外层循环。
