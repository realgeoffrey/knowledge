# 装饰器（注解）对比

## 目录
1. [总览](#总览)
1. [JS 装饰器](#js-装饰器)
1. [TS 装饰器](#ts-装饰器)
1. [Java 注解](#java-注解)
1. [Python 装饰器](#python-装饰器)
1. [Rust 属性与过程宏](#rust-属性与过程宏)

---
## 总览
1. 共同点：都把“额外处理意图”写在声明附近；具体机制不同，可能是包装/替换对象、注册信息、结构化元数据、编译器指令或编译期代码生成。
1. JS 装饰器：当前文档记录为 TC39 提案语义，不等同于已经进入所有 JS 运行时的稳定标准；项目里通常通过 TypeScript、Babel 或框架编译链使用。
1. TS 装饰器：围绕类和类成员提供元编程钩子，可以替换、初始化或注册目标；TS 需要区分新版装饰器和旧版 `experimentalDecorators`。
1. Java 注解：写在声明或类型使用位置上的结构化元数据，本身不执行逻辑；逻辑来自编译器、注解处理器、框架或反射。
1. Python 装饰器：定义函数或类时执行装饰器表达式，装饰器返回值会绑定回原名字，核心是**包装或替换对象**。
1. Rust 属性/过程宏：`#[...]`、`#![...]` 在编译期处理；内置属性影响编译，过程宏能消费并生成 Rust 语法。
1. 按机制分类：

    - 偏运行期包装行为：JS/TS 方法装饰器、Python 装饰器。
    - 偏运行期元编程/注册：JS/TS 类和类成员装饰器、TS 运行时注册表或 `reflect-metadata` 生态、Java `RUNTIME` 注解配合反射或框架。
    - 偏结构化元数据：Java 注解、Rust 内置属性/工具属性。
    - 偏编译器/工具指令：Java `@Override`、`@SuppressWarnings`，Rust `#[cfg]`、`#[allow]`、`#[test]`。
    - 偏编译期生成代码：Java 注解处理器、Rust 过程宏。

1. 按用法归纳：

    - 包裹函数调用前后逻辑：JS/TS 方法装饰器、Python 装饰器、普通高阶函数。
    - 提供结构化配置：JS/TS 装饰器、Java 注解、Rust 属性；其中旧版 TS + `reflect-metadata` 生态常用于运行期元数据。
    - 参与编译器或工具检查：Java `@Override`、`@SuppressWarnings`，Rust `#[cfg]`、`#[allow]`、`#[test]`。
    - 编译期生成代码：Java 注解处理器、Rust 过程宏。
    - 运行期扫描并调用：TS 运行时注册表或 `reflect-metadata` 生态；Java `RUNTIME` 注解 + 反射/框架。
    - 表达横切能力：日志、权限、事务、缓存、校验、注册、序列化映射、路由、依赖注入、ORM、AOP。
    - 保持可读性：不要把核心业务流程藏进装饰器。

## JS 装饰器
1. JavaScript 装饰器：当前文档记录为 TC39 提案语义，不等同于已经进入所有 JS 运行时的稳定标准；项目里通常通过 TypeScript、Babel 或框架编译链使用。
1. 执行/处理时机：TS/Babel 场景通常编译到 JS 后运行；语义上是在类定义求值期间调用。
1. 行为能力：

    - 可以替换被装饰值，但通常只能替换为语义匹配的值，如方法替换为方法、类替换为类。
    - 可以读取 `context.kind`、`context.name`、`context.static`、`context.private` 等上下文信息。
    - 可以用 `context.addInitializer()` 注入初始化逻辑。
    - 可以用装饰器工厂传参，如 `@logged('prefix')`。

1. 常见用法：类元编程、注册、校验、初始化。
1. 多个装饰器：

    ```js
    @a
    @b
    method() {}
    ```

    同一元素上，装饰器表达式通常先自上而下求值，装饰器函数再按相反顺序应用；写装饰器时不要依赖难读的副作用顺序。

## TS 装饰器
1. TypeScript 装饰器需要区分两套语义：

    1. 新版装饰器：TS 5+ 不需要 `experimentalDecorators`；典型签名是 `(value, context) => value?`；不支持参数装饰器；不兼容 `emitDecoratorMetadata`。
    1. 旧版实验装饰器：通过 `experimentalDecorators: true` 开启；典型签名是 `target`、`propertyKey`、`descriptor` 等；支持参数装饰器；可配合 `emitDecoratorMetadata`、`reflect-metadata`。

1. 作用对象：

    - 新版：类、字段、方法、getter、setter、自动访问器（`accessor`）。
    - 旧版 TS：类和类成员之外，还常见参数装饰器，尤其在依赖注入框架里。

1. 执行/处理时机：TS/Babel 场景通常编译到 JS 后运行；语义上是在类定义求值期间调用。
1. 行为能力：

    - 可以替换被装饰值，但通常只能替换为语义匹配的值，如方法替换为方法、类替换为类。
    - 可以读取 `context.kind`、`context.name`、`context.static`、`context.private` 等上下文信息。
    - 可以用 `context.addInitializer()` 注入初始化逻辑。
    - 可以用装饰器工厂传参，如 `@logged('prefix')`。

1. 常见用法：Angular/Nest、依赖注入、ORM、AOP、路由、类元编程、注册、校验、初始化。
1. 新版装饰器核心模型：

    ```ts
    function logged<This, Args extends unknown[], Return>(
      method: (this: This, ...args: Args) => Return,
      context: ClassMethodDecoratorContext<This, (this: This, ...args: Args) => Return>,
    ) {
      return function (this: This, ...args: Args) {
        console.log(`enter ${String(context.name)}`);
        return method.call(this, ...args);
      };
    }

    class Service {
      @logged
      save() {}
    }
    ```

1. 多个装饰器：

    ```ts
    @a
    @b
    method() {}
    ```

    同一元素上，装饰器表达式通常先自上而下求值，装饰器函数再按相反顺序应用；写装饰器时不要依赖难读的副作用顺序。

1. 注意点：

    - 业务代码优先用普通函数、组合、显式调用；装饰器适合横切关注点和框架基础设施。
    - 新旧 TS 装饰器不要混写；迁移 Angular/Nest/TypeORM 等旧生态时，要先确认框架支持哪套语义。
    - 参数类型、返回类型需要显式建模，否则装饰器很容易退化成 `any`。

## Java 注解
1. 语法：`@Annotation`、`@Annotation(value)`、`@Annotation(key = value)`。
1. 作用对象：类、字段、方法、参数、构造器、类型使用等。
1. 执行/处理时机：由保留策略决定，可以是源码、编译期或运行期。
1. 行为能力：注解本身不改变业务逻辑；真正读取和执行规则的是编译器、注解处理器、框架或反射代码。
1. 常见用法：

    - 编译检查：`@Override`。
    - 过时提示：`@Deprecated`。
    - 抑制警告：`@SuppressWarnings`。
    - 编译期代码生成或校验：Lombok、MapStruct、Dagger。
    - 运行期框架配置：Spring、JUnit、Jackson。
    - 字节码/AOP：框架结合代理或字节码增强，让注解“看起来会执行逻辑”。

1. 基本示例：

    ```java
    @Override
    public String toString() {
        return "user";
    }
    ```

    `@Override` 不包装方法，只让编译器检查“确实覆盖了父类/接口方法”。

1. 自定义注解：

    ```java
    import java.lang.annotation.ElementType;
    import java.lang.annotation.Retention;
    import java.lang.annotation.RetentionPolicy;
    import java.lang.annotation.Target;

    @Target({ElementType.FIELD, ElementType.PARAMETER})
    @Retention(RetentionPolicy.RUNTIME)
    public @interface Label {
        String value();
        boolean required() default true;
    }
    ```

1. 元注解：

    - `@Target`：限定注解使用位置，如 `TYPE`、`FIELD`、`METHOD`、`PARAMETER`、`CONSTRUCTOR`、`TYPE_USE`。
    - `@Retention`：限定保留阶段，`SOURCE`、`CLASS`、`RUNTIME`。
    - `@Documented`：进入 Javadoc。
    - `@Inherited`：类级注解可被子类继承，不适用于方法/字段。
    - `@Repeatable`：允许同一位置重复使用同类注解。

1. 注解元素规则：

    - 元素写成无参数方法，可有 `default`。
    - 返回值只能是基本类型、`String`、`Class`、枚举、注解，或这些类型的一维数组。
    - 元素名为 `value` 且其他元素有默认值时，可省略 `value =`。

## Python 装饰器
1. 语法：`@decorator`、`@decorator(args)`。
1. 作用对象：函数、方法、类。
1. 执行时机：定义函数或类时执行装饰器表达式，不是每次调用时才创建。
1. 行为能力：装饰器接收原对象，返回值直接替换原对象；可以包装调用前后逻辑，也可以返回原对象、新函数或新类。
1. 常见用法：

    - 日志、鉴权、缓存、路由、注册。
    - 描述符封装，如 `@property`。
    - 方法绑定语义，如 `@classmethod`、`@staticmethod`。
    - 数据类或标准库工具，如 `@dataclass`、`@functools.cache`。

1. 基本等价关系：

    ```py
    @log
    def run():
        pass

    # 近似等价于：
    def run():
        pass
    run = log(run)
    ```

1. 多个装饰器从**下到上**包裹：

    ```py
    @a
    @b
    def f():
        pass

    # 近似等价于：
    f = a(b(f))
    ```

1. 装饰器工厂：`@decorator(args)` 会先调用工厂，返回真正的装饰器。

    ```py
    def retry(times):
        def deco(fn):
            def wrapper(*args, **kwargs):
                last_error = None
                for _ in range(max(1, times)):
                    try:
                        return fn(*args, **kwargs)
                    except Exception as err:
                        last_error = err
                raise last_error
            return wrapper
        return deco
    ```

1. 注意点：

    - 包装函数会改变 `__name__`、`__doc__` 等元信息，通常用 `functools.wraps(fn)` 保留。
    - 装饰器可以有副作用，如注册路由、写入全局表、修改类属性。
    - 类型标注可用 `ParamSpec`、`TypeVar` 保留参数和返回类型，但运行期不自动校验类型。

## Rust 属性与过程宏
1. 语法：外部属性 `#[...]`、内部属性 `#![...]`。
1. 作用对象：crate、模块、类型、函数、字段、语句等。
1. 执行/处理时机：编译期。
1. 行为能力：内置属性影响编译；过程宏能生成或替换代码；不是所有 `#[...]` 都是宏。
1. 常见用法：条件编译、lint、测试、derive、代码生成。
1. 基本示例：

    ```rust
    #[derive(Debug, Clone)]
    struct User {
        id: u64,
    }

    #[cfg(test)]
    mod tests {}
    ```

1. 两种位置：

    - 外部属性 `#[...]`：作用在后面的 item、语句或表达式上。
    - 内部属性 `#![...]`：作用在包含它的 crate、模块或函数体上。

1. 属性分类：

    - 内置属性：`#[derive]`、`#[test]`、`#[cfg]`、`#[allow]`、`#[deprecated]`、`#[inline]`、`#[repr]` 等。
    - 工具属性：`#[rustfmt::skip]`、`#[clippy::...]` 等，由工具解释。
    - 过程宏属性：`#[route(...)]`、`#[tokio::main]` 这类由宏展开。
    - derive 辅助属性：如 Serde 中常见的 `#[serde(rename = "...")]`，通常配合 `#[derive(...)]` 读取。

1. 过程宏三类：

    - 函数式过程宏：使用方式是 `my_macro!(...)`；作用是消费 token，生成 token。
    - derive 宏：使用方式是 `#[derive(MyTrait)]`；作用是为结构体、枚举、联合体生成实现或额外 item。
    - 属性宏：使用方式是 `#[my_attr(...)] item`；作用是读取属性参数和目标 item，并用返回 token 替换目标 item。

1. 与 Java 注解的关键差异：

    - Java 注解主要是元数据，Rust 过程宏能在编译期生成或替换代码。
    - Rust 没有 Java 那种普遍运行期反射模型；很多能力在编译期完成。
    - 不是所有 `#[...]` 都是宏；很多只是编译器内置属性或工具属性。
