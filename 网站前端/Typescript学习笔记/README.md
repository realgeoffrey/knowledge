# [Typescript](https://github.com/microsoft/TypeScript)学习笔记

## 目录
1. [类型](#类型)
1. [语法](#语法)

    1. [类型推论（Type Inference）](#类型推论type-inference)
    1. [类型断言（Type Assertion）](#类型断言type-assertion)
    1. [类型保护/类型守卫（Type Guards）](#类型保护类型守卫type-guards)
    1. [联合类型（Union Types）](#联合类型union-types)
    1. [交叉类型（Intersection Types）](#交叉类型intersection-types)
    1. [`表达式!`](#表达式)
    1. [`typeof 值`](#typeof-值)
    1. [`keyof 数据类型`（输入索引类型查询）](#keyof-数据类型输入索引类型查询)
    1. [`类型[键名]`（索引访问类型）](#类型键名索引访问类型)
    1. [`in`](#in)
    1. [装饰器（Decorators）](#装饰器decorators)
    1. [`readonly`](#readonly)
    1. [`this`](#this)
    1. [`类型1 extends 类型2 ? 类型3 : 类型4`（条件类型）](#类型1-extends-类型2--类型3--类型4条件类型)
    1. [`infer`](#infer)
    1. [`///`（三斜线指令）](#三斜线指令)
    1. [`namespace`（命名空间）](#namespace命名空间)
    1. [模块化](#模块化)
    1. [`名字.d.ts`（声明文件）](#名字dts声明文件)
    1. [协变与逆变](#协变与逆变)
1. [其他](#其他)

---

>参考：[TypeScript 入门教程](https://github.com/xcatliu/typescript-tutorial)、[TypeScript 使用手册（中文版）翻译](https://github.com/zhongsp/TypeScript)、[TypeScript Deep Dive 中文版](https://github.com/jkchao/typescript-book-chinese)。

- TypeScript是JS的一个超集，主要提供了类型系统和对ES6的支持。

    1. TS的类型系统被设计为可选的，因此，JS就是TS。
    2. TS不会阻止JS的运行，即使存在类型错误也不例外，这能让JS逐步迁移至TS。

### 类型
1. 数据类型

    >1. `Number`、`String`、`Boolean`、`Symbol`、`BigInt`、`Object`：（大写的）几乎在任何时候都不应该被用作一个类型。
    >
    >    `Object`类型：匹配任何值（基本数据类型+引用数据类型）。
    >2. 除了`Object`之外的引用类型（如：`Function`、`Date`），他们的实例类型用（大写的）构造函数名称（如：`: Function`、`: Date`）。

    1. 基本数据类型

        1. `number`
        2. `string`
        3. `boolean`
        4. `symbol`
        5. `bigint`
        6. `undefined`

            `undefined`可以赋值给可选参数（`?:`）。

            >1. `a?: 某类型`表示：`a`不存在或不传参，也可以是`某类型`或`undefined`。
            >2. `a: 某类型 | undefined`表示：`a`必须存在或必传参，类型是`某类型`或`undefined`。
        7. `null`

        >1. `undefined`和`null`值 可以赋值给所有类型的变量（除了`never`类型）；`undefined`和`null`类型 是所有类型的子类型（除了`never`类型）。
        >2. 若配置`strictNullChecks`，则：`undefined`只能赋值给类型`any`、`undefined`、`void`；`null`只能赋值给类型`any`、`null`。
    2. `void`

        1. 变量类型void，表示：仅允许被`null`（只在配置`strictNullChecks`未指定时）或`undefined`赋值。
        2. 函数返回值类型void，表示：`return null`（只在配置`strictNullChecks`未指定时）、`return undefined`、`return`、没有`return`。

            - 函数返回值类型void的变量，可以被赋值任何返回类型的函数（函数`返回值类型`是协变的）

            ><details>
            ><summary>Promise的默认返回可以用<code>void</code>（不能用<del><code>undefined</code></del>）</summary>
            >
            >e.g.
            >
            >```typescript
            >function a (): Promise<void> {
            >  return new Promise((resolve, reject) => {
            >    resolve();
            >  }).then(() => {
            >       // 支持：`return null`（只在配置`strictNullChecks`未指定时）、`return undefined`、`return`、没有`return`。
            >  });
            >}
            >
            >
            >function b (): Promise<undefined> {
            >  return new Promise((resolve, reject) => {
            >    resolve();
            >  }).then(() => {
            >    return undefined   // 或：return null（只在配置`strictNullChecks`未指定时）
            >  });
            >}
            >```
            ></details>
    3. `never`

        1. 表示永不存在的值的类型

            >e.g. 总是会抛出异常 或 根本就不会有返回值 的函数表达式；变量也可能是never类型，当它们被永不为真的类型保护所约束时。
        2. 当类型不存在时通常返回`never`

            >e.g. `number & string`、`Extract<string | number , boolean>`）。

        `never`可以赋值给所有类型的变量（包括`undefined`和`null`），`never`是所有类型的子类型。`never`类型的变量仅能被`never`类型的值赋值。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >// 返回never的函数必须存在无法达到的终点
        >function error (message: string): never {
        >  throw new Error(message)
        >}
        >
        >// 推断的返回值类型为never
        >function fail () {
        >  return error('Something failed')
        >}
        >
        >// 返回never的函数必须存在无法达到的终点
        >function infiniteLoop (): never {
        >  while (true) {
        >  }
        >}
        >
        >
        >// 变量
        >let x: never
        >let y: number
        >let z: undefined
        >
        >x = 123        // 报错，number 类型不能转为 never 类型
        >x = undefined  // 报错，undefined 类型不能转为 never 类型
        >x = (() => { throw new Error('exception')})() // never 类型可以赋值给 never 类型
        >y = (() => { throw new Error('exception')})() // never 类型可以赋值给 number 类型
        >z = (() => { throw new Error('exception')})() // never 类型可以赋值给 undefined 类型
        >```
        ></details>
    4. `any`

        能够兼容所有的类型（包括它自己）。当使用`any`时，基本上是在告诉TS编译器不要进行任何的类型检查，TS将会把类型检查关闭。

        >未声明类型的（且没有类型推论的）被认为是`any`。
    5. `unknown`

        1. 任何值都可以赋给`unknown`。
        2. 当没有类型断言或基于控制流的类型细化时`unknown`不可以赋值给其它类型，除了它自己和`any`之外。
        3. 在`unknown`没有被类型断言或js代码细化到一个确切类型之前，不允许在其上进行任何操作。
        4. `try-catch`抓到的是`unknown`，需要类型保护（e.g. `if (err instanceof Error) {){}`）之后才能认为`err`是`Error`类型。
        5. 用`?.`无效，只能用类型保护才能使用其属性。
    6. `object`或`{}`

        表示非原始类型/非基本数据类型（除了`boolean`、`number`、`string`、`symbol`、`bigint`、`undefined`、`null`之外的类型）。允许给它赋任意值和访问`Object.prototype`上的属性，但不能调用任意其他方法，即便它真的有这些方法。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >let obj1: object
        >
        >obj1 = []
        >
        >obj1.toString()  // 允许访问Object.prototype上的属性
        >obj1.a()         // 报错，只允许使用Object.prototype上的属性
        >obj1.length      // 报错，只允许使用Object.prototype上的属性
        >
        >
        >let obj2: { a }
        >
        >obj2 = { a: () => {} }
        >
        >obj2.toString()  // 允许访问Object.prototype上的属性
        >obj2.a()         // 允许访问定义的属性a
        >obj2.length      // 报错，只允许使用Object.prototype上的属性
        >```
        ></details>
    7. 对象类型

        1. 用`接口`定义。

            1. 确定属性（`属性名: 数据类型`），对象不允许多于或少于约定的属性数量（若有`索引签名`时，则允许多定义属性）。
            2. 可选属性（`属性名?: 数据类型`）。
            3. 只读类型（`readonly 属性名: 数据类型`），创建对象时必须给此属性赋值，并且之后不能修改此属性。

                >作为变量使用用`const`，作为属性使用用`readonly`。
            4. `索引签名`（`[任意名: string]: 数据类型`），确定属性、可选属性、只读属性的类型都必须是`索引签名`的类型的子集。

                1. 尽量不要把 `索引签名` 与 属性 混合使用。若属性名称中有拼写错误，则这个错误不会被捕获到

                    <details>
                    <summary>e.g.</summary>

                    ```typescript
                    // 错误示范：
                    interface NestedCSS1 {
                      color?: string;
                      [selector: string]: string | undefined | NestedCSS1;
                    }
                    const example: NestedCSS1 = {
                      color: 'red',
                      colorxxx: 'red',      // 无法检查出错误

                      '.subclass': {
                        color: 'blue',
                        colorxxx: 'red'     // 无法检查出错误
                      },
                    };


                    // 取而代之，把`索引签名`分离到自己的属性里，如命名为nest（或children、subnodes、等）：
                    interface NestedCSS2 {
                      color?: string;
                      nest?: {
                        [selector: string]: NestedCSS2;
                      };
                    }
                    const example: NestedCSS2 = {
                      color: 'red',
                      colorxxx: 'red'       // TS Error: 未知属性 'colorxxx'

                      nest: {
                        '.subclass': {
                          color: 'blue',
                          colorxxx: 'red'   // TS Error: 未知属性 'colorxxx'
                        }
                      }
                    }
                    ```
                    </details>
                2. 当 属性 和 `索引签名` 直接合并会出错的情况（当 属性的类型 并非 `索引签名`的类型 的子集时），也可以用`&`，只是不能用这个交叉类型创建对象

                    <details>
                    <summary>e.g.</summary>

                    ```typescript
                    type FieldState = {
                      value: string;
                    };

                    type FormState = { isValid: boolean } & { [fieldName: string]: FieldState };

                    // 将它用于从某些地方获取的 JavaScript 对象
                    declare const foo: FormState;

                    const isValidBool = foo.isValid;
                    const somethingFieldState = foo['something'];

                    // 使用它来创建一个对象时，将必然报错
                    const bar: FormState = {
                      // isValid 不能设置值类型 FieldState、也不能设置值类型 boolean
                      // isValid: { value: '' },    // 类型错误
                      // isValid: true              // 类型错误
                    };
                    ```
                    </details>

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface Person {
            >  name: string
            >
            >  func(): string
            >
            >  score?: number   // -> 不存在 或 number | undefined
            >
            >  readonly id: number
            >
            >  // 索引签名：描述对象的属性
            >  [任意名: string]: string | Function | number | undefined | boolean // 必须包含：所有其他属性的类型的联合类型（|）
            >}
            >
            >let tom: Person = {
            >  name: 'Tom',
            >
            >  func(){ return '' },
            >
            >  id: 1,
            >
            >  xx: 22
            >}
            >
            >tom.id = 2   // 报错，readonly
            >tom.x = 'x'
            >tom.xx = 'xx'
            >tom.xxx = 1n // 报错，1n不是 string | Function | number | undefined | boolean
            >```
            ></details>
        2. `: { 属性: 数据类型, }`（内联类型注解）

            >`{ [任意名: string]: any }`等价于`Record<string, any>`，表示对象类型，比 ~~`object`~~、~~`{}`~~ 更严格定义对象类型。
        3. `: 类名`

            取**实例**的类型，而不是~~类~~的类型，不包含类的所有 ~~`静态属性/方法`~~ 和 ~~`构造函数`~~。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >class A {
            >  a: number = 2;
            >  aa?: number = 2;
            >  b: () => void = () => {};
            >  bb?: () => void = () => {};
            >
            >  c() {}
            >  cc?() {}
            >
            >  static d: any;
            >}
            >
            >let a1: A = new A();
            >let a2: A = { a: 1, b() {}, c() {} };
            >let a3: A = {};                       // 报错，需要a、b、c属性
            >```
            ></details>

        - Freshness（更严格的`对象字面量`检查）

            只会发生在`对象字面量`上的错误提示。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >function logName(something: { name: string }) {
            >  console.log(something.name);
            >}
            >
            >const person = { name: 'matt' };
            >const animal = { name: 'cow', diet: 'vegan, but has milk of own specie' };
            >const randow = { note: `I don't have a name property` };
            >
            >logName(person); // ok
            >logName(animal); // ok
            >logName(randow); // Error: 没有 `name` 属性
            >
            >logName({ name: 'matt' });                          // ok
            >logName({ name: 'matt', job: 'being awesome' });    // Error: 对象字面量只能指定已知属性，`job` 属性在这里并不存在。
            >logName({});                                        // Error: 对象字面量只能指定已知属性，非可选
            >```
            ></details>
    8. 数组类型

        1. `数据类型[]`

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >let arr1: (number | string)[] = [1, "1"];
            >let arr2: { name: string; age: number }[] = [
            >  { name: "", age: 0 },
            >  { name: "1", age: 1 },
            >];
            >
            >class A {
            >  name: string = "";
            >  age: number = 0;
            >  sex?: boolean = true;
            >}
            >
            >let arr3: A[] = [
            >  { name: "", age: 0, sex: false },
            >  { name: "1", age: 1 },
            >];
            >```
            ></details>
        2. 泛型`Array<数据类型>`

            >e.g. `let arr: Array<number | string> = [1, '1']`

            - `ReadonlyArray<数据类型>`

                与`Array<数据类型>`相似，只是把所有可变方法去掉了，因此可以确保数组创建后再也不能被修改（readonly）。

                ><details>
                ><summary>e.g.</summary>
                >
                >```typescript
                >let a: number[] = [1, 2, 3, 4]
                >let ro: ReadonlyArray<number> = a  // 允许，普通数据类型 赋值给 ReadonlyArray
                >
                >ro[0] = 12      // 报错
                >ro.push(5)      // 报错
                >ro.length = 100 // 报错
                >
                >let b: number[] = ro               // 报错，ReadonlyArray赋值给一个普通数组也是不可以的
                >let c: number[] = ro as number[]   // 允许，类型断言重写
                >```
                ></details>
        3. 用`接口`定义

            用`索引签名`来定义索引和项。

            ```typescript
            interface NumberArray {
              [任意名: number]: number | string
            }

            let arr: NumberArray = [1, '1']
            ```
        4. 元组（Tuple）

            1. 规定`数组`每一项的数据类型：

                1. 直接赋值不能少于或多于约定长度。
                2. 下标赋值或`push`等可以大于规定长度，但要用前面所有数据类型的联合类型。
            2. `元组[数字]`可以获取内部某一项的类型

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >let arr1: [string, number] = ['string', 1]
            >arr1.push(2)
            >arr1.push(true)                                  // 报错，只能添加联合类型
            >
            >let arr2: [string, number] = ['string', 1, '啊'] // 报错，直接赋值不能多于约定长度
            >
            >let arr3: [string, number] = ['string']          // 报错，直接赋值不能少于约定长度
            >
            >type A = [number, string]
            >type B = A[0]                                    // -> number
            >```
            ></details>

        - 将`索引签名`设置为只读

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface ReadonlyStringArray {
            >  readonly [任意名: number]: string;
            >}
            >
            >let myArray: ReadonlyStringArray = ["Alice", "Bob"];
            >myArray[2] = "Mallory"; // error。readonly
            >```
            ></details>

        >枚举被编译为.js是数组。
    9. 函数类型

        1. 输入的参数、输出的返回值都需要设置类型。
        2. 支持：函数声明、函数表达式。

            1. 函数表达式定义类型方式：`Function` 或 `参数类型 => 返回类型` 或 `接口`（、类型别名、内联类型注解）

                若函数表达式需要表示重载，则只能通过 `接口`（、类型别名、内联类型注解） 定义。
            2. 函数声明使用定义类型方式：内联类型注解
        3. 支持：可选参数、默认参数、剩余参数。

            1. 可选参数 和 默认参数 不能同时设置（默认参数有可选参数的含义）。

                >e.g. 不允许：~~`x?: number = 1`~~；`x: number = 1`，可以传`number`或`undefined`，或不传参。
            2. 设置 所有参数类型（空参数也满足）：`(...args: 数组类型)`。
        4. 引用函数传入的参数不允许多于或少于约定的参数数量（若有可选参数`?`、或默认参数`=`、或剩余参数`...`，则允许少传入参数）。
        5. 函数的参数和返回值可以自动进行类型推论。
        6. `new`可实例化

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface A1 {     // 或：类型别名、内联类型注解
            >  new (): string;
            >}
            >// 使用
            >declare const A1Func: A1;
            >const bar1 = new A1Func(); // bar1 被推断为 string 类型
            >
            >
            >type A2 = new () => string
            >// 使用
            >declare const A2Func: A2
            >const bar2 = new A2Func(); // bar2 被推断为 string 类型
            >```
            ></details>
        7. 函数类型的[协变与逆变](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Typescript学习笔记/README.md#协变与逆变)

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >// 函数声明
        >
        >// 可选参数
        >function sum1 (x: number, y?: number): string {
        >  if (y) {
        >    return x + ''
        >  } else {
        >    return x + y + ''
        >  }
        >}
        >
        >// 默认参数
        >function sum2 (x: number = 1, y: number = 2): string { // 参数要使用默认参数：不传 或 传`undefined`
        >  return x + y + ''
        >}
        >
        >// 剩余参数
        >function sum3 (x: number, ...items: number[]): string {
        >  return x + items.reduce((a, b) => a + b, 0) + ''
        >}
        >
        >
        >// 函数表达式
        >
        >// 类型推论
        >let mySum1 = function (x: number, y: number): string {
        >  return x + y + ''
        >}
        >
        >// 显式定义（不是类型推论）
        >let mySum2: (xx: number, yy: number) => string = function (x: number, y: number): string { // 定义的参数名和实现的函数参数名不用一致
        >  return x + y + ''
        >}
        >
        >// 接口（或 类型别名）
        >interface mySum {
        >  // 描述方法（没有属性名）
        >  (xx: number, yy: number): string   // 定义的参数名和实现的函数参数名不用一致
        >}
        >let mySum3: mySum  // 显式定义（不是类型推论）
        >mySum3 = function (x, y) { // 类型推论
        >// 或：mySum3 = function (x: number, y: number): string {    // 显式定义（不是类型推论）
        >  return x + y + ''
        >}
        >
        >// 内联类型注解
        >function identity<T>(arg: T): T {
        >    return arg;
        >}
        >let myIdentity: {<T>(arg: T): T} = identity;
        >```
        ></details>

        >仅定义数据类型、不实现的方法都只有`()`、没有`{}`（`(参数: 类型): 类型`）：函数声明的重载、`interface/type/内联类型注解 中的方法`、`declare class 中的 方法`、`abstract class 中的 abstract 方法`。

        - 支持：重载

            1. 优先从最前面的函数定义开始匹配，因此若多个函数定义有包含关系，则需优先把精确的定义写在前面。
            2. 函数实现签名，它并不是重载的一部分。当至少具有一个函数重载的签名时，只有重载是可见的。最后一个声明签名（也可以被称为签名的实现）对签名的形状并没有贡献。
            3. 最终函数体及其函数形状需要兼容前面的所有重载。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >// 函数声明
            >function reverse1(x: number): number;
            >function reverse1(x: string): string;
            >
            >function reverse1(x: number | string): number | string {
            >  if (typeof x === "number") {
            >    return Number(x.toString().split("").reverse().join(""));
            >  } else {
            >    return x.split("").reverse().join("");
            >  }
            >}
            >
            >
            >// 函数表达式
            >interface FuncType  {
            >  (a: number): number;
            >  (a: string): string;
            >};
            >
            >const a: FuncType = <T extends string | number>(a: T): T => a
            >```
            ></details>

            >TS中的函数重载没有任何运行时开销。
    10. 内置对象类型

        1. 浏览器环境

            [TypeScript核心库的定义文件](https://github.com/Microsoft/TypeScript/tree/main/src/lib)定义了所有浏览器环境需要用到的类型（预置在TypeScript中）。

            1. [ECMAScript标准提供的内置对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects)
            2. 文档对象模型（DOM）、浏览器对象模型（BOM）的内置对象

        - ~~Node.js~~

            Node.js不是内置对象的一部分，需引入第三方声明文件：`npm install @types/node --save-dev`。

    - 返回Promise类型

        `Promise<resolve的类型>`仅能定义完成的Promise实例，不能定义失败的。失败的Promise实例总是认为是`unknown`（与`try-catch`中`catch`的参数类型一致）。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >function a(): Promise<number | string> {  // 仅能定义resolve
        >  return new Promise((resolve, reject) => {
        >    const random = Math.random();
        >    if (random < 0.3) {
        >      resolve(1);               // number
        >    } else if (random < 0.6) {
        >      resolve("1");             // string
        >    } else {
        >      reject(false);            // 完全忽略reject
        >    }
        >  });
        >}
        >
        >function b(): Promise<string> {
        >  return Promise.resolve(123);  // 报错，要求 string
        >}
        >
        >function c(): Promise<string> {
        >  return Promise.reject(123);   // 没问题，完全忽略reject
        >}
        >```
        ></details>
2. 类

    1. 访问修饰符（Access Modifiers）

        规定类的属性/方法的访问权限。

        1. `public`（默认）：公有的，在任何地方都可以被访问。
        2. `private`：私有的，只能在声明的类中访问。（继承和实例化对象不能访问）

            >若类的构造函数设置为`private`，则这个类不能实例化、也不能够被继承。
        3. `protected`：受保护的，只能在声明的类中、声明的继承子类中访问。（实例化对象不能访问）

            ><details>
            ><summary>若类的构造函数设置为<code>protected</code>，则这个类不能实例化，但继承的子级能够调用这个构造函数（<code>super()</code>）。</summary>
            >
            >e.g.
            >
            >```typescript
            >class Person {
            >  protected constructor () {}
            >}
            >
            >class Employee extends Person {
            >  constructor () {
            >    super()
            >  }
            >}
            >
            >let john = new Person()     // 报错，Person的构造函数是protected，只能够被子类调用
            >let howard = new Employee()
            >```
            ></details>

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >class Animal {
        >  public constructor (name, age, sex) {
        >    // （默认值会在编译后的.js的构造函数最前面加上：）this.age = 100
        >
        >    this.name = name
        >    this.age = age // 类的只读属性在构造函数里初始化
        >    this.sex = sex
        >  }
        >
        >  public name: string
        >  // 类的只读属性，必须在声明时默认赋值 或 在构造函数里初始化。
        >  private readonly age: number = 100   // 类的只读属性在声明时默认赋值
        >  protected sex: boolean
        >
        >  public getName (): string {
        >    return this.name
        >  }
        >
        >  private getAge (): number {
        >    return this.age
        >  }
        >
        >  protected getSex (): boolean {
        >    return this.sex
        >  }
        >}
        >
        >let a = new Animal('Jack', 5, true)
        >a.name = 'Tom'
        >console.log(a.age)               // 报错，private
        >console.log(a.sex)               // 报错，protected
        >console.log(a.getName())
        >console.log(a.getAge())          // 报错，private
        >console.log(a.getSex())          // 报错，protected
        >
        >class Cat extends Animal {
        >  constructor (name, age, sex) {
        >    super(name, age, sex)
        >
        >    console.log(this.name)
        >    console.log(this.age)        // 报错，private
        >    console.log(this.sex)
        >    console.log(super.getName())
        >    console.log(super.getAge())  // 报错，private
        >    console.log(super.getSex())
        >  }
        >}
        >
        >let b = new Cat('Jacky', 10, false)
        >b.name = 'Tomy'
        >console.log(b.age)               // 报错，private
        >console.log(b.sex)               // 报错，protected
        >console.log(b.getName())
        >console.log(b.getAge())          // 报错，private
        >console.log(b.getSex())          // 报错，protected
        >```
        ></details>

        - 参数属性

            若在类的构造函数的**参数**上设置访问修饰符（`private/public/protected`），则在实例化时会用参数名新建一个实例属性/方法。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >// A1和A2编译出的.js结果一致
            >
            >class A1 {
            >  private a: string
            >  protected readonly b: number
            >
            >  constructor (临时属性1: string, 临时属性2: number) {
            >    this.a = 临时属性1
            >    this.b = 临时属性2
            >  }
            >}
            >
            >class A2 {
            >  constructor (private a: string, protected readonly b: number) { }
            >}
            >```
            ></details>

        - `class-extends`重载属性

            1. `public`仅可被`public`重载
            2. `private`不可被重载
            3. `protected`仅可被`public`或`protected`重载
    2. `typeof 类名`

        取**类**的类型，而不是~~实例~~的类型，包含类的所有`静态属性/方法`和`prototype`。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >class Greeter {
        >  static staticGreeting = 'Hello, there'
        >  greeting: string
        >
        >  greet () {
        >    return Greeter.staticGreeting
        >  }
        >}
        >
        >let greeter1: Greeter // 实例（实例属性/方法、类.prototype.属性/方法）
        >greeter1 = new Greeter()
        >console.log(greeter1.greet(), greeter1.greeting)
        >
        >let greeterMaker: typeof Greeter  // 类（静态属性/方法、`prototype`）
        >greeterMaker = Greeter
        >greeterMaker.staticGreeting = 'Hey there'
        >
        >let greeter2: Greeter
        >greeter2 = new greeterMaker()
        >console.log(greeter2.greet(), greeter2.greeting)
        >
        >type A = keyof typeof Greeter  // -> 'prototype' | 'staticGreeting'
        >type B = keyof Greeter         // -> 'greeting' | 'greet'
        >```
        ></details>
    3. `abstract`

        抽象类、抽象方法。

        1. 抽象类不能实例化
        2. 抽象方法**必须**被子类实现（抽象类自己不能定义自己的抽象方法的实现）

            抽象方法仅允许出现在抽象类中。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >abstract class Animal {    // 抽象类
        >  public name: string
        >
        >  public constructor (name: string) {
        >    this.name = name
        >  }
        >
        >  public abstract sayHi () // 抽象方法
        >  public func () {}
        >}
        >
        >class Cat extends Animal {
        >  public sayHi (): void {
        >    console.log(`Meow, My name is ${this.name}`)
        >  }
        >}
        >
        >let cat: Cat = new Cat('Tom')
        >cat.sayHi()
        >```
        ></details>
    4. `implements`

        `class`实现`interface`（仅对`class`的实例属性/方法进行类型检查、不检查`class`的静态属性/方法）

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >interface Alarm {
        >  alert(num: number): void;  // 接口上的属性 被class实现必须是public
        >}
        >
        >interface Light {
        >  lightOn(str: string): boolean;
        >
        >  lightOff?(): void;
        >}
        >
        >class Car1 implements Light {
        >  public lightOn(str: string) {
        >    console.log("Car1 light on", str, this.x1, this.x2);
        >    return true;
        >}
        >
        >  protected x1() {}
        >  private x2() {}
        >}
        >
        >class Car2 extends Car1 implements Alarm, Light {
        >  alert(num: number) {
        >    console.log("Car2 alert", num);
        >  }
        >
        >  public lightOn(str: string) {
        >    console.log("Car2 light on", str,this.xx1, this.xx2);
        >    return true;
        >  }
        >
        >  lightOff() {
        >    console.log("Car2 light off");
        >  }
        >
        >  protected xx1() {}
        >  private xx2() {}
        >}
        >```
        ></details>

    - 类型兼容性

        1. 仅有 实例属性/方法 会相比较，构造函数和静态成员 不会被检查。
        2. private/protected的成员 必须来自于相同的类。
3. 接口（Interfaces）

    `interface`

    1. 定义`对象`、`数组`、`函数`的形状（Shape：数量和数据类型）

        >e.g.
        >
        >1. 对象类型：`interface X { a(): any, b: any }`
        >2. 函数类型：`interface Y { (): any }`
        >3. 数组类型：`interface Z { [任意名: number]: any }`

        - 还可以定义混合类型（一个对象同时作为函数和对象使用）。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface Counter {
            >  (start: number): string  // 描述方法（没有属性名）
            >
            >  interval: number         // 描述对象的属性
            >
            >  reset (): void           // 描述对象的方法（有属性名）
            >}
            >
            >function getCounter (): Counter {
            >  let counter = <Counter>function (start: number) { }
            >  counter.interval = 123
            >  counter.reset = function () { }
            >  return counter
            >}
            >
            >let c = getCounter()
            >c(10)            // 作为函数使用
            >c.reset()        // 作为对象使用
            >c.interval = 5.0 // 作为对象使用
            >```
            ></details>
    2. 对`类`的一部分行为进行抽象（`类`实现`接口`）

    - `extends`

        >与`class-extends`的不完全一致。

        接口继承。`interface B extends A`满足：B可以赋值给A（概括下面的`继承`+`重载`）。

        1. 接口继承`接口`

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface Alarm {
            >  alert ()
            >}
            >
            >interface LightableAlarm extends Alarm {
            >  lightOn ()
            >
            >  lightOff ()
            >}
            >
            >const obj: LightableAlarm = {
            >  alert(){},
            >  lightOn(){},
            >  lightOff(){}
            >}
            >```
            ></details>
        2. 接口继承`类`

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >class Point {
            >  x?: number
            >  y: number
            >}
            >
            >interface Point3d extends Point {
            >  z: number
            >}
            >
            >let point3d: Point3d = { y: 2, z: 3 }
            >```
            ></details>

            - 接口会继承类的访问修饰符（`public`、`private`、`protected`）

                当一个接口继承了一个拥有`private`或`protected`的成员的类时，这个接口类型只能被这个类或其子类所实现（implement）。

                ><details>
                ><summary>e.g.</summary>
                >
                >```typescript
                >class Control {
                >  private state: any;
                >}
                >
                >interface SelectableControl extends Control {
                >  select(): void;
                >}
                >
                >class Button extends Control implements SelectableControl {
                >  select() {}
                >}
                >
                >class TextBox extends Control {
                >  select() {}
                >}
                >
                >class ImageControl implements SelectableControl {
                >  // Error: Class 'ImageControl' incorrectly implements interface 'SelectableControl'.
                >  //  Types have separate declarations of a private property 'state'.
                >  private state: any;
                >
                >  select() {}
                >}
                >```
                ></details>
        3. 接口继承`别名`

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >type Name = {
            >  name: string;
            >}
            >interface User extends Name {
            >  age: number;
            >}
            >```
            ></details>

    - 支持：合并

        同名的interface会自动合并（`type`不可以有同名的定义）。

        1. 接口中的属性在合并时会简单的合并到一个接口中

            >合并的相同属性的类型必须是相同的。
        2. 接口中方法的重载，与函数的重载一样，支持：重载。
        3. 接口中属性的 内联类型注解 可以重载覆盖，但是需要用更多属性的对象（协变），不能用更少属性的对象

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface a {
            >  aa: { a: string; b: string }
            >}
            >
            >interface b extends a {
            >  aa: { a: string; b: string; c: string };
            >}
            >
            >interface c extends a {            // 报错，不能用更少的属性覆盖
            >  aa: { a: string; c: string };
            >}
            >```
            ></details>
4. 类型别名（Type Alias）

    >类型别名和`接口`有时很像，区别：
    >
    >1. 类型别名可以作用于：原始值、联合类型、交叉类型、元组以及其它任何需要手写的类型，只需要给它一个语义化的名字即可；
    >2. `接口`仅定义：对象、数组、函数，但有层次结构，能使用`implements`、`extends`。

    `type`：与其原始的类型完全一致；它们只是简单的替代名。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >type Name = string
    >type NameResolver = () => string
    >type NameOrResolver = Name | NameResolver
    >function getName(n: NameOrResolver): Name {
    >    if (typeof n === 'string') {
    >        return n
    >    } else {
    >        return n()
    >    }
    >}
    >```
    ></details>

    1. 起别名不会新建一个类型，仅创建了一个新名字来引用那个类型
    2. 可以使用类型别名来在属性里引用自己（~~`接口`~~ 不可以）

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type Tree<T> = {
        >  value: T;
        >  left: Tree<T>;
        >  right: Tree<T>;
        >}
        >
        >type LinkedList<T> = T & { next: LinkedList<T> };
        >```
        ></details>
    3. 扩展用`&`（`接口`用`extends`）

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type Name1 = {
        >  name: string;
        >}
        >type User1 = Name1 & { age: number; };
        >
        >
        >interface Name2 {
        >  name: string;
        >}
        >type User2 = Name2 & { age: number; };
        >```
        ></details>
5. 字面量类型

    一个字面量是一个集体类型（字符串、数字、布尔值、大数）中更为具体的一种子类型。通过使用字面量类型，可以规定一个字符串、数字、布尔值或大数必须含有的确定值。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >type aa = "ease-in" | "ease-out" | "ease-in-out";
    >type bb = 8 | 16 | 32;
    >type cc = { c1: true; c2: string } | { c1: false; c2: number };
    >
    >interface MapType {
    >  a: "ease-in" | "ease-out" | "ease-in-out";
    >  aa: aa;
    >  b: 8 | 16 | 32;
    >  bb: bb;
    >  c: { c1: true; c2: string } | { c1: false; c2: number };
    >  cc: cc;
    >}
    >
    >const obj: MapType = {
    >  a: "ease-in",
    >  aa: "ease-in",
    >  b: 8,
    >  bb: 8,
    >  c: { c1: true, c2: "123" },
    >  cc: { c1: false, c2: 13 },
    >};
    >```
    ></details>

    - 模版字面量类型

        若在替换字符串的位置是联合类型，则结果类型是由每个联合类型成员构成的字符串字面量的集合。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type World = 'world';
        >type Greeting = `hello ${World}`;  // -> 'hello world'
        >
        >
        >type EmailLocaleIDs = 'welcome_email' | 'email_heading';
        >type FooterLocaleIDs = 'footer_title' | 'footer_sendoff';
        >type Id = 'id1' | 'id2'
        >type AllLocaleIDs = `${EmailLocaleIDs | FooterLocaleIDs}_${Id}`;
        >// -> "welcome_email_id1" | "email_heading_id1" | "footer_title_id1" | "footer_sendoff_id1" | "welcome_email_id2" | "email_heading_id2" | "footer_title_id2" | "footer_sendoff_id2"
        >```
        ></details>
6. 枚举（Enum）

    用于取值被限定在一定范围内的场景。语义化、限制值的范围（只允许使用已定义的枚举名）。

    >使用枚举类型可以为一组数值赋予友好的名字。

    <details>
    <summary>e.g.</summary>

    ```typescript
    enum E {
      aa,
      bb = 123,
      cc,
      dd = 222,
      ee,
    }

    console.log(E.aa, E.bb, E.cc, E.dd, E.ee);                  // => 0 123 124 222 223
    console.log(E[E.aa], E[E.bb], E[E.cc], E[E.dd], E[E.ee]);   // => "aa" "bb" "cc" "dd" "ee"
    ```
    </details>

    1. 普通枚举 及 枚举成员的类型

        （除了~~常数枚举、外部枚举~~之外，）枚举名映射到枚举值，枚举值也映射到枚举名。

        1. 常数项（constant member）

            1. 枚举成员会被赋值为从`0`开始递增的数字。

                ><details>
                ><summary>e.g.</summary>
                >
                >```typescript
                >// .ts
                >enum Days {Sun, Mon, Tue, Wed, Thu, Fri, Sat}
                >
                >
                >// 被编译为.js
                >var Days;
                >(function (Days) {
                >    Days[Days["Sun"] = 0] = "Sun";
                >    Days[Days["Mon"] = 1] = "Mon";
                >    Days[Days["Tue"] = 2] = "Tue";
                >    Days[Days["Wed"] = 3] = "Wed";
                >    Days[Days["Thu"] = 4] = "Thu";
                >    Days[Days["Fri"] = 5] = "Fri";
                >    Days[Days["Sat"] = 6] = "Sat";
                >})(Days || (Days = {}));
                >
                >
                >/* 使用测试 */
                >console.log(Days["Sun"] === 0); // => true
                >console.log(Days["Mon"] === 1); // => true
                >console.log(Days["Tue"] === 2); // => true
                >console.log(Days["Sat"] === 6); // => true
                >
                >console.log(Days[0] === "Sun"); // => true
                >console.log(Days[1] === "Mon"); // => true
                >console.log(Days[2] === "Tue"); // => true
                >console.log(Days[6] === "Sat"); // => true
                >```
                ></details>
            2. 枚举项可以手动赋值（仅可赋值为数字或字符串），未手动赋值的枚举项会接着上一个枚举项递增。

                1. 若未手动赋值的枚举项与手动赋值的重复了，则编译器不会察觉到（易产生错误，应避免）。
                2. 手动赋值的枚举项允许不是数字，此时需要使用类型断言`<any>`来让编译器无视类型检查。

                    若紧接在不是数字的枚举项后面的是未手动赋值的项，则会因为无法获得初始值而报错。

                    ><details>
                    ><summary>e.g.</summary>
                    >
                    >```typescript
                    >// .ts
                    >enum Days {Sun = 7, Mon, Tue, Wed, Thu, Fri, Sat = <any>'S', a = 13, b}
                    >
                    >
                    >// 被编译为.js
                    >var Days;
                    >(function (Days) {
                    >    Days[Days["Sun"] = 7] = "Sun";
                    >    Days[Days["Mon"] = 8] = "Mon";
                    >    Days[Days["Tue"] = 9] = "Tue";
                    >    Days[Days["Wed"] = 10] = "Wed";
                    >    Days[Days["Thu"] = 11] = "Thu";
                    >    Days[Days["Fri"] = 12] = "Fri";
                    >    Days[Days["Sat"] = 'S'] = "Sat";
                    >    Days[Days["a"] = 13] = "a";
                    >    Days[Days["b"] = 14] = "b";
                    >})(Days || (Days = {}));
                    >```
                    ></details>
                3. 手动赋值的枚举项也可以为小数或负数，此时后续未手动赋值的项的递增步长仍为`1`。
        2. 计算所得项（computed member）

            1. 若紧接在计算所得项后面的是未手动赋值的项，则会因为无法获得初始值而报错。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >// .ts
            >enum Color {Red, Green, Blue = "blue".length, Yellow = 5, White}
            >
            >
            >// 被编译为.js
            >var Color;
            >(function (Color) {
            >    Color[Color["Red"] = 0] = "Red";
            >    Color[Color["Green"] = 1] = "Green";
            >    Color[Color["Blue"] = "blue".length] = "Blue";
            >    Color[Color["yellow"] = 5] = "yellow";
            >})(Color || (Color = {}));
            >```
            ></details>
    2. 常数枚举、外部枚举

        与普通枚举的区别是：①在编译阶段被删除、②不能包含计算所得项、③若手动赋值则枚举值必须是数字。

        1. 常数枚举（Const Enums）

            使用`const enum`定义的枚举类型。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >// .ts
            >const enum Directions {
            >  Up,
            >  Down,
            >  Left,
            >  Right
            >}
            >let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right]
            >
            >
            >// 被编译为.js（不会生成枚举的变量）
            >var directions = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
            >```
            ></details>

            （外部）常数枚举 生成的.js，不会生成~~枚举的变量~~，而是直接把枚举的值硬编码出来。配置`preserveConstEnums`可保持编译出枚举的变量。
        2. 外部枚举（Ambient Enums）

            使用`declare enum`定义的枚举类型。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >// .ts
            >declare enum Directions1 {
            >  Up,
            >  Down,
            >  Left,
            >  Right
            >}
            >let directions1 = [Directions1.Up, Directions1.Down, Directions1.Left, Directions1.Right]
            >
            >
            >// 被编译为.js
            >var directions1 = [Directions1.Up, Directions1.Down, Directions1.Left, Directions1.Right];
            >```
            ></details>
        3. 外部枚举 + 常数枚举

            使用`declare const enum`定义的枚举类型。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >// .ts
            >declare const enum Directions2 {
            >  Up,
            >  Down,
            >  Left,
            >  Right
            >}
            >let directions2 = [Directions2.Up, Directions2.Down, Directions2.Left, Directions2.Right]
            >
            >
            >// 被编译为.js（不会生成枚举的变量）
            >var directions2 = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
            >```
            ></details>
    3. 有静态方法的枚举

        `enum` + `namespace`

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >// .ts
        >enum Weekday {
        >  Monday,
        >  Tuesday,
        >  Wednesday,
        >  Thursday,
        >  Friday,
        >  Saturday,
        >  Sunday
        >}
        >
        >namespace Weekday {
        >  export function isBusinessDay(day: Weekday) {
        >    switch (day) {
        >      case Weekday.Saturday:
        >      case Weekday.Sunday:
        >        return false;
        >      default:
        >        return true;
        >    }
        >  }
        >}
        >
        >// const mon = Weekday.Monday;
        >// const sun = Weekday.Sunday;
        >
        >// console.log(Weekday.isBusinessDay(mon));
        >// console.log(Weekday.isBusinessDay(sun));
        >
        >
        >// 被编译为.js
        >"use strict";
        >var Weekday;
        >(function (Weekday) {
        >    Weekday[Weekday["Monday"] = 0] = "Monday";
        >    Weekday[Weekday["Tuesday"] = 1] = "Tuesday";
        >    Weekday[Weekday["Wednesday"] = 2] = "Wednesday";
        >    Weekday[Weekday["Thursday"] = 3] = "Thursday";
        >    Weekday[Weekday["Friday"] = 4] = "Friday";
        >    Weekday[Weekday["Saturday"] = 5] = "Saturday";
        >    Weekday[Weekday["Sunday"] = 6] = "Sunday";
        >})(Weekday || (Weekday = {}));
        >(function (Weekday) {
        >    function isBusinessDay(day) {
        >        switch (day) {
        >            case Weekday.Saturday:
        >            case Weekday.Sunday:
        >                return false;
        >            default:
        >                return true;
        >        }
        >    }
        >    Weekday.isBusinessDay = isBusinessDay;
        >})(Weekday || (Weekday = {}));
        >// const mon = Weekday.Monday;
        >// const sun = Weekday.Sunday;
        >// console.log(Weekday.isBusinessDay(mon));
        >// console.log(Weekday.isBusinessDay(sun));
        >```
        ></details>

    - 遍历枚举类型

        `in`

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >enum A {
        >  'top',
        >  'down',
        >}
        >
        >function func() {
        >  for (var key in A) {
        >    console.log(key);
        >  }
        >}
        >
        >func(); // => '0' => '1' => 'top' => 'down'
        >```
        ></details>
    - 赋值兼容

        1. 枚举与数字类型相互兼容

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >enum Status {
            > Ready,
            > Waiting
            >}
            >
            >let status1 = Status.Ready;
            >let num1 = 3
            >let num2 = 3 as const
            >
            >status1 = num1;
            >status1 = num2;
            >num1 = status1;
            >num2 = status1  // Error, Type 'Status' is not assignable to type '1'.
            >```
            ></details>
        2. 来自于不同枚举的枚举变量，被认为是不兼容

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >enum Status {
            > Ready,
            > Waiting
            >}
            >enum Color {
            > Red,
            > Blue
            >}
            >
            >let status1 = Status.Ready;
            >let color = Color.Red;
            >
            >status1 = color; // Error
            >```
            ></details>
7. 泛型（Generics）

    `名称<多个类型名>使用部分`。泛型是指在定义函数（`<多个类型名>(参数): 返回值`）、接口（`interface 接口名<多个类型名>`）或类（`class 类名<多个类型名>`）时，不预先指定具体的类型，而在使用时再指定类型的一种特性。

    - 定义 - 赋值

        1. 定义：类型变量/泛型变量（用任意的非保留关键字）

            >当使用简单的泛型时，泛型常用`T`、`U`、`V`表示。若在参数里，不止拥有一个泛型，则应该使用一个更语义化名称，如`TKey`、`TValue`（通常情况下，以`T`作为泛型的前缀，在其他语言如C++里，也被称为模板）。
        2. 赋值：传入类型，可以是自定义类型，可以是类型推论

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >function func<T, P>(a: T, b: P, c: Array<T | P>) {
    >  return `${a} ${b} ${c}`;
    >}
    >
    >func<string, number>("aaa", 222, ["a", "b", 3]);   // 显式定义（不是类型推论）
    >func<"aaa", 222>("aaa", 222, ["aaa", "aaa", 222]); // 显式定义（不是类型推论）
    >func("a", 2, ["aa", 22]);                          // 类型推论。会报错，等价于：func<"a", 2>("a", 2, ["aa", 22])
    >func("a" as string, 2 as number, ["aa", 22]);      // 类型推论
    >
    >
    >class A<T extends number | string> {
    >  constructor(private paras: T[]) {}
    >}
    >
    >new A<string>(["a1", "a2", "123"]);        // 显式定义（不是类型推论）
    >new A<number | string>(["a1", "a2", 123]); // 显式定义（不是类型推论）
    >new A(["a1", 123]);                        // 类型推论
    >```
    ></details>

    1. 泛型函数

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >function identity<T>(arg: T): T {
        >    return arg;
        >}
        >
        >let myIdentity1: <U>(arg: U) => U = identity;
        >let myIdentity2: {<T>(arg: T): T} = identity;
        >let myIdentity3 = identity<string>;
        >```
        ></details>
    2. 泛型接口、泛型类型别名

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >// 泛型接口1
        >interface GenericIdentityFn {
        >    <T>(arg: T): T;
        >}
        >function identity<T>(arg: T): T {
        >    return arg;
        >}
        >let myIdentity: GenericIdentityFn = identity;
        >
        >// 泛型接口2
        >interface GenericIdentityFn<T> {
        >    (arg: T): T;
        >}
        >function identity<T>(arg: T): T {
        >    return arg;
        >}
        >let myIdentity: GenericIdentityFn<number> = identity;
        >
        >
        >// 泛型类型别名
        >type LinkedList<T> = { name: T; next: LinkedList<T> };
        >
        >var people: LinkedList<string>;
        >var s = people.name;
        >var s = people.next.name;
        >var s = people.next.next.name;
        >var s = people.next.next.next.name;
        >```
        ></details>
    3. 泛型类

        >类的静态属性不能使用泛型类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >class GenericNumber<T> {
        >  zeroValue: T;
        >  add: (x: T, y: T) => T = function (x, y) {
        >    return x;
        >  };
        >
        >  constructor(zeroValue: T) {
        >    this.zeroValue = zeroValue;
        >  }
        >}
        >
        >let myGenericNumber = new GenericNumber<number>(0);
        >```
        ></details>

    4. 没有~~泛型枚举~~、~~泛型命名空间~~。

    - 泛型参数的默认类型：`<类型名 = 默认数据类型>`
    - 泛型约束：`<类型名 extends 已有数据类型>`

        类型名 需要包含 已有数据类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >function loggingIdentity<T extends { length: number }> (arg: T): T {
        >  console.log(arg.length);
        >
        >  return arg;
        >}
        >loggingIdentity(3);                     // 报错
        >loggingIdentity({length: 10, value: 3});
        >
        >
        >function getProperty<T, K extends keyof T> (obj: T, key: K) {
        >  return obj[key];
        >}
        >getProperty({ a: 1 }, "a");
        >getProperty({ a: 1 }, "m"); // 报错
        >```
        ></details>
8. 内置类型别名

    >来自：[lib.es5.d.ts](https://github.com/microsoft/TypeScript/blob/master/lib/lib.es5.d.ts#L1455)、[typescript: Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)。

    1. `Partial`

        将类型定义的所有属性都修改为可选（非~~必须~~）。

        >e.g. `Partial<数据类型>`
    2. `Required`

        将类型定义的所有属性都修改为必须（非~~可选~~）。

        >e.g. `Required<数据类型>`
    3. `Readonly`

        将类型定义的所有属性都修改为只读（readonly）。

        >e.g. `Readonly<数据类型>`
    4. `Record`

        将类型A的所有属性值都映射到类型B上并创造一个新的类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type A = 'dog' | 'cat' | 'fish';
        >interface B {
        >   name: string,
        >   age: number,
        >}
        >
        >type C = Record<A, B>;
        >
        >const c: C = {
        >   dog: {
        >       name: 'dogName',
        >       age: 2
        >   },
        >   cat: {
        >       name: 'catName',
        >       age: 3
        >   },
        >   fish: {
        >       name: 'fishName',
        >       age: 5
        >   }
        >}
        >```
        ></details>
    5. `Pick`

        从类型定义的属性中，选取指定一组属性，返回一个新的类型定义。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >interface A {
        >  title: string
        >  completed: boolean
        >  description: string
        >}
        >
        >type someA = Pick<A, 'title'|'completed'>
        >
        >const a: someA = {
        >  title: 'Clean room',
        >  completed: false
        >}
        >```
        ></details>
    6. `Omit`

        去除类型定义中的某些属性。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >interface A {
        >  title: string
        >  completed: boolean
        >  description: string
        >}
        >
        >type AB = Omit<A, "completed"|"description">
        >
        >const a: AB = {
        >  title: 'Clean room'
        >}
        >```
        ></details>
    7. `Extract`

        从联合类型A中提取类型B。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type T0 = Extract<'a' | 'b' | 'c', 'a' | 'b'>          // -> 'a' | 'b'
        >type T1 = Extract<string | boolean, boolean | number>  // -> boolean
        >type T2 = Extract<string | number , boolean>           // -> never
        >```
        ></details>
    8. `Exclude`

        去除联合类型中的一部分。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type a = number | string | boolean
        >type b = Exclude<a, number | boolean>  // -> string
        >```
        ></details>
    9. `NonNullable`

        去除联合类型中的`null`和`undefined`。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type T1 = NonNullable<string | null | undefined>;  // -> string
        >type T2 = NonNullable<null | undefined>;           // -> never
        >```
        ></details>
    10. `ReturnType`

        获得函数类型的返回类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type F1 = () => Date;
        >function F2 (): Date { return new Date() }
        >
        >type F1ReturnType = ReturnType<F1>;        // -> Date
        >type F2ReturnType = ReturnType<typeof F2>; // -> Date
        >
        >type F3 = ReturnType<typeof setTimeout>;   // -> number
        >```
        ></details>
    11. `Parameters`

        获取函数类型的全部参数类型，以`元组`返回。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type F0 = (a: string, b: number) => boolean;
        >type F1 = Parameters<F0>;                      // -> [a: string, b: number] 或 [string, number]
        >type F2 = F1[1];                               // -> number
        >
        >type F3 = () => boolean;
        >type F4 = Parameters<F2>;                      // -> []
        >```
        ></details>
    12. `InstanceType`

        获得构造函数类型的实例类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >class C {
        >  x = 0;
        >  y = 0;
        >}
        >
        >type T0 = InstanceType<typeof C>; // -> C
        >```
        ></details>
    13. `ConstructorParameters`

        获取构造函数的全部参数类型，以`元组`或数组返回。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type T0 = ConstructorParameters<ErrorConstructor>;     // -> [message?: string]
        >type T1 = ConstructorParameters<FunctionConstructor>;  // -> string[]
        >type T2 = ConstructorParameters<RegExpConstructor>;    // -> [pattern: string | RegExp, flags?: string]
        >type T3 = ConstructorParameters<any>;                  // -> unknown[]
        >type T4 = ConstructorParameters<Function>;             // -> never。报错
        >```
        ></details>
    14. `ThisParameterType`

        获取函数类型中`this`参数的数据类型，若没有则返回`unknown`。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >function toHex(this: Number) {
        >    return this.toString(16);
        >}
        >
        >function numberToString(n: ThisParameterType<typeof toHex>) {
        >    return toHex.apply(n);
        >}
        >```
        ></details>
    15. `OmitThisParameter`

        移除函数类型中的`this`参数的数据类型，返回移除后的函数类型。
    16. `ThisType`

        >若使用，则需要开启`--noImplicitThis`。
9. 操作固有字符串的类型（不是~~值~~）

    >这些类型内置于编译器之中，以便提高性能，它们不存在于~~TypeScript提供的`.d.ts`文件中~~。

    1. `Uppercase<StringType>`

        将字符串中的每个字符转换为大写字母。
    2. `Lowercase<StringType>`

        将字符串中的每个字符转换为小写字母。
    3. `Capitalize<StringType>`

        将字符串中的首字母转换为大写字母。
    4. `Uncapitalize<StringType>`

        将字符串中的首字母转换为小写字母。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >// Uppercase改成Lowercase、Capitalize、Uncapitalize，均可行
    >
    >type Greeting = 'Hello, world' | 'Hi';
    >type ShoutyGreeting = Uppercase<Greeting>;  // -> "HELLO, WORLD" | "HI"
    >
    >
    >type ASCIICacheKey<Str extends string> = `ID-${Uppercase<Str>}`;
    >type MainID = ASCIICacheKey<'my_app'>;  // -> "ID-MY_APP"
    >```
    ></details>

### 语法

#### 类型推论（Type Inference）
若没有明确的指定类型，则依照类型推论规则推断出一个类型。

1. 最佳通用类型（从右向左）

    1. 当需要从几个表达式中推断类型时，会使用这些表达式的类型来推断出一个最合适的通用类型。
    2. （数组的情况下，）若没有找到最佳通用类型，则使用联合（数组）类型。

    - 声明时

        1. 若声明时有赋值，则推断成此赋值的类型。
        2. 若声明时没赋值，则推断成`any`。

    >配置`noImplicitAny`：当无法推断一个变量（或只能推断为一个隐式的`any`类型）时发出一个错误（显式添加`any`不报错）。
2. 上下文归类（从左向右）

    若等号左侧已经确定了类型，则右侧的赋值也会吸收左侧的类型，并尝试约束自己的行为。通常包含：函数的参数，赋值表达式的右边，类型断言，对象成员，数组字面量，返回值语句。

#### 类型断言（Type Assertion）
`<数据类型>变量名` 或 `变量名 as 数据类型`

>若JSX中使用`<数据类型>变量名`断言语法时，则与JSX的语法存在歧义（如：`let foo = <string>bar;</string>`），因此在`.tsx`中必须用`变量名 as 数据类型`的断言语法。

- 可以绕过检查

    1. 变量的类型（或类型推论） 和 断言的类型 可以单向赋值才能够成功（A类型是B类型的子级，或反过来），否则报错。
    2. `双重断言` 可以断言成任何类型：先断言成`any`，再断言成某类型。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >interface A {
    >  aa?: number
    >}
    >interface B {
    >  bb: number
    >}
    >
    >let a: A = { aa: 2 };
    >let b: B = a as B;                  // 不报错
    >let c: B = a as any;                // 不报错
    >let d: B = {} as B;                 // 不报错
    >let e: B = { aa: 2 } as B;          // 报错
    >let f: B = ({ aa: 2 } as any) as B; // 不报错，双重断言
    >```
    ></details>

1. const断言（const assertions）

    `as const`或`<const>`，该表达式中：①字面量类型不会被扩展（如：不能从`"hello"`转换为`string`），②对象类型的属性成为只读字面量类型，③数组成为只读元组。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >const x1 = 'x1';        // -> 'x1'
    >let x2 = 'x2';          // -> string
    >let x3 = 'x3' as const; // -> 'x3'
    >
    >const obj1 = { key: 'value' }           // -> { key: string }
    >const obj2 = { key: 'value' } as const  // -> { readonly key: 'value' }
    >
    >const arr1 = [1,2,3]            // -> number[]
    >const arr2 = [1,2,3] as const   // -> readonly [1,2,3]
    >```
    ></details>

#### 类型保护/类型守卫（Type Guards）
一些表达式，它们会在运行时检查以确保在块级作用域中获得更为精确的变量类型，从而减少不必要的类型断言，同时改善代码的可读性。

>TS能够理解`if-else`、`switch-case`等的逻辑分支下的类型变化。

1. 类型判断

    `typeof 变量 !==或=== 值`

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >function test(input: string | number) {
    >  if (typeof input == 'string') {
    >    // 这里 input 的类型「收紧」为 string
    >  } else {
    >    // 这里 input 的类型「收紧」为 number
    >  }
    >  // 这里 input 仅能访问此联合类型的所有类型里共有的属性/方法
    >}
    >```
    ></details>
2. 实例判断

    `变量 instanceof 构造函数`

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >class Foo {}
    >class Bar {}
    >
    >function test(input: Foo | Bar) {
    >  if (input instanceof Foo) {
    >    // 这里 input 的类型「收紧」为 Foo
    >  } else {
    >    // 这里 input 的类型「收紧」为 Bar
    >  }
    >  // 这里 input 仅能访问此联合类型的所有类型里共有的属性/方法
    >}
    >```
    ></details>
3. 属性判断

    `字面量 in 变量`

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >interface Foo {
    >  foo: string;
    >}
    >
    >interface Bar {
    >  bar: string;
    >}
    >
    >function test(input: Foo | Bar) {
    >  if ('foo' in input) {
    >    // 这里 input 的类型「收紧」为 Foo
    >  } else {
    >    // 这里 input 的类型「收紧」为 Bar
    >  }
    >  // 这里 input 仅能访问此联合类型的所有类型里共有的属性/方法
    >}
    >```
    ></details>
4. 字面量相等判断

    `变量 !==或=== 字面量`

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >type Foo = 'foo' | 'bar' | 'unknown';
    >
    >function test(input: Foo) {
    >  if (input != 'unknown') {
    >    // 这里 input 的类型「收紧」为 'foo' | 'bar'
    >  } else {
    >    // 这里 input 的类型「收紧」为 'unknown'
    >  }
    >  // 这里 input 仅能访问此联合类型的所有类型里共有的属性/方法
    >}
    >```
    ></details>

><details>
><summary>若上述条件不是直接通过字面量书写，而是通过一个条件函数来替代时，则类型保护便会失效</summary>
>
>```typescript
>function isString (input: any) {
>  return typeof input === 'string';
>}
>
>function foo (input: string | number) {
>  if (isString(input)) {
>    // 这里 input 的类型没有「收紧」，仍为 string | number
>  } else {
>    // 这里也一样
>  }
>}
>```
>
>1. 这是因为TS只能推断出`isString`是一个返回布尔值的函数，而并不知道这个布尔值的具体含义。
>2. 并且JS并没有内置非常丰富的、运行时的自我检查机制。当你在使用普通的JS对象时，你甚至无法访问`instanceof`或`typeof`。
>
>需要使用：自定义类型保护。
></details>

5. 自定义类型保护

    定义一个函数，它的返回值是一个`类型谓词`：`参数名 is 类型`。通过这个函数，可以缩小参数的类型范围。

    >本质是一种类型断言。

    ```typescript
    // 传进来参数的类型是`Fish | Bird`。函数返回`true`参数类型是`Fish`；函数返回`false`参数类型是除去`Fish`
    function isFish(pet: Fish | Bird): pet is Fish {
        return (pet as Fish).swim !== undefined;
    }

    // Both calls to 'swim' and 'fly' are now okay.
    let pet = getSmallPet() as Fish | Bird;

    if (isFish(pet)) {
      pet.swim();
    } else {
      pet.fly();
    }
    ```

#### 联合类型（Union Types）
`|`

1. 若未赋值，则只能访问此联合类型的所有类型里共有的属性/方法（不确定联合类型的变量到底是哪个类型）。

    - 类型断言 或 js逻辑判断（类型保护） 联合类型的变量成为联合类型其中的某一种类型，就可以访问此类型的属性/方法。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >function getLength(something: string | number) {
        >  something.toString(); // 访问此联合类型的所有类型里共有的属性/方法
        >  (something as string).length; // 类型断言
        >  (<number>something).toFixed(); // 类型断言
        >  if (typeof something === 'string') {
        >    something.length;  // js逻辑判断（类型保护）
        >  }
        >
        >  something.length; // 报错，只能访问此联合类型的所有类型里共有的属性/方法
        >  (<boolean>something).toString(); // 报错，只能类型断言成一个联合类型中存在的类型
        >}
        >```
        ></details>
2. 若已赋值，则只能访问类型推论出的某一个类型的属性/方法。

- 可辨识联合（Discriminated Unions）

    可辨识（公共属性名） + 联合类型（`|`） + 类型保护。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >// 可辨识：vType
    >interface Motorcycle {
    >  vType: "motorcycle"; // discriminant
    >  make: number; // year
    >}
    >
    >interface Car {
    >  vType: "car"; // discriminant
    >  transmission: 200 | 300;
    >}
    >
    >interface Truck {
    >  vType: "truck"; // discriminant
    >  capacity: number; // in tons
    >}
    >
    >// 联合类型
    >type Vehicle = Motorcycle | Car | Truck;
    >
    >function evaluatePrice(vehicle: Vehicle) {
    >  // 类型保护
    >  switch (vehicle.vType) {
    >    case "car":
    >      return vehicle.transmission * Math.PI;
    >    case "truck":
    >      return vehicle.capacity * Math.PI;
    >    case "motorcycle":
    >      return vehicle.make * Math.PI;
    >    default:
    >      const invalidVehicle: never = vehicle;
    >      throw new Error(`Unknown vehicle: ${invalidVehicle}`);
    >  }
    >}
    >```
    ></details>

>第一个值前面也可以添加`|`（主要为了格式化美观）。e.g. `type a = | number | string;`

#### 交叉类型（Intersection Types）
`&`

将多个类型合并为一个类型。

- 用法

    1. e.g. `number & string    // -> never`
    2. `{ 属性: 数据类型, } &` +

        1. 合并起来成为一个显式类型

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface A {
            >  a: number;
            >}
            >interface B {
            >  b: string;
            >}
            >type C = {
            >  c: boolean;
            >};
            >
            >const aa: A & B & C & { d: number } = {
            >  a: 1,
            >  b: "",
            >  c: false,
            >  d: 1,
            >};
            >```
            ></details>
        2. 与起来成为一个显式类型

            >e.g. `type X = string & (1 | '2' | true) // -> '2'`
        3. `{ 属性: 数据类型, } & 其他类型  // -> 可能没法直接给变量（可用于类型断言）`

            >e.g. `{ 'x': {}, } & string`
        4. `{ 属性: 数据类型1 } & { [key: string]: 数据类型2 }    // -> 可能没法直接给变量，用于二次获取属性`

#### `表达式!`
表示从前面的表达式（值，不是~~类型~~）里移除 ~~`null`~~ 和 ~~`undefined`~~。

><details>
><summary>e.g.</summary>
>
>```typescript
>// 配置文件：compilerOptions.strictNullChecks: true
>let foo: string | undefined
>
>foo.length     // 报错， - 'foo' is possibly 'undefined'
>foo!.length
>
>
>function func (x: undefined | string): string{
>  return x!
>}
>```
></details>

#### `typeof 值`
>也保留js中的含义，但优先使用TS的语义。作为TS语法 比 作为JS语法，值支持的写法更少。

获取一个值（不是~~类型~~）的声明类型（或类型推论）。

><details>
><summary>e.g.</summary>
>
>```typescript
>function foo(x: number): Array<number> {
>  return [x];
>}
>type F = typeof foo; // -> (x: number) => number[]
>
>
>class A {
>  a: string;
>  constructor() {
>    console.log("I'm A");
>  }
>}
>
>const a: A = { a: "" };
>
>type A2 = A;        // -> A的实例类型
>type A3 = typeof a; // -> a的类型（ === A的实例类型）
>type A4 = typeof A; // -> A的类型
>
>let a1: A2 = { a: "" };
>
>let a2: A3 = { a: "" };
>
>let a3: A4 = A;
>
>let a4: A4 = class B extends A {
>  constructor() {
>    super();
>    console.log("I'm B");
>  }
>};
>
>new a3(); // => I'm A
>new a4(); // => I'm A I'm B
>```
>
>```typescript
>const foo1 = 'Hello World';
>let bar1: typeof foo1;
>// bar1 仅能被赋值 'Hello World'
>bar1 = 'Hello World';      // ok
>bar1 = 'anything else';    // Error
>
>
>let foo2 = 'Hello World';
>let bar2: typeof foo2;
>bar2 = 'anything else';    // ok
>
>
>let foo3 = 'Hello World' as const
>let bar3: typeof foo3;
>// bar3 仅能被赋值 'Hello World'
>bar3 = 'Hello World';      // ok
>bar3 = 'anything else';    // Error
>```
></details>

#### `keyof 数据类型`（输入索引类型查询）
获取某种**数据类型**的所有公共键（属性名），以联合类型（`|`）返回。

<details>
<summary>e.g.</summary>

```typescript
interface Person {
  name: string;
  age: number;
  location?: string;
}

type K1 = keyof Person;                        // -> "name" | "age" | "location"
type K2 = keyof Person[];                      // -> number | "length" | "push" | "pop" | "concat" | ...
type K3 = keyof { [任意名: string]: Person };   // -> string | number （隐式转换key为number）

const a = { 'b': 1, 'c': '2', 3: 3, '4': 4 };
type K4 = keyof typeof a;                      // -> 'b' | 'c' | 3 | '4'
```

- 获取 对象或类型 的所有属性值，以联合类型（`|`）返回：

    >类似`enum`的功能，若非特别必要，请用`enum`代替。

    ```typescript
    const obj1 = {
      key1: "value1",
      key2: "value2"
    } as const;                 // 关键，若不加`as const`，则 Obj1Values1和Obj1Values2 -> string

    interface Interface1 {
      key1: "value1";
      key2: "value2";
    }

    class Class1 {
      key1 = "value1" as const; // 关键，若不加`as const`，则 Class1Values -> string
      key2 = "value2" as const;
    }


    type ValueOf<T> = T[keyof T];
    type Obj1Values1 = ValueOf<typeof obj1>;                // -> "value1" | "value2"

    type Obj1Values2 = (typeof obj1)[keyof (typeof obj1)];  // -> "value1" | "value2"

    type Interface1Values = Interface1[keyof Interface1]    // -> "value1" | "value2"

    type Class1Values = Class1[keyof Class1]                // -> "value1" | "value2"

    // enum EnumValues {
    //   'key1' = 'value1',
    //   'key2' = 'value2'
    // }
    ```
</details>

#### `类型[键名]`（索引访问类型）
在语法上，它们看起来像属性或元素访问，但最终会被转换为类型。

>不支持：~~`类型.键名`~~。

><details>
><summary>e.g.</summary>
>
>```typescript
>interface Person {
>  name: string;
>  age: number;
>  location: string;
>}
>
>type P1 = Person["name"];          // -> string
>type P2 = Person["name" | "age"];  // -> string | number
>type P3 = string["charAt"];        // -> (pos: number) => string
>type P4 = string[]["push"];        // -> (...items: string[]) => number
>type P5 = string[][0];             // -> string
>```
></details>

#### `in`
类型的属性、枚举的项名 通过`in`遍历获得。

><details>
><summary>e.g.</summary>
>
>```typescript
>type Keys = "a" | "b"
>type Obj = {
>  [p in Keys]: any
>} // -> { a: any, b: any }
>
>
>enum Keys2 {
>  'top',
>  'down'
>}
>type Obj2 = {
>  [p in Keys2]: any
>} // -> { 0: any, 1: any }
>```
></details>

#### 装饰器（Decorators）
`@装饰器表达式-最终求值后是一个函数`，可以被附加到`类声明`、`方法`、 `访问符(getter/setter)`、`属性`、`参数`上。不能用在声明文件(`.d.ts`)、（方法的重载、）任何外部上下文（如：`declare`的类）中。

1. `@expression`的expression求值后为一个函数，它在运行时被调用，被装饰的声明信息会被做为参数传入。
2. 当多个装饰器应用在一个声明上时：

    ```typescript
    // 书写在同一行上
    @f @g x


    // 书写在多行上
    @f
    @g
    x
    ```

    1. 由上至下依次对装饰器表达式求值。
    2. 求值的结果会被当作函数，由下至上依次调用。

#### `readonly`
属性标记为只读。

1. 方法的形参
2. 类、interface、type、内联类型注解 的属性

    >与访问修饰符同时使用时要放在其后面：`访问修饰符 readonly 属性名`。

- 自动推断

    在一些情况下，编译器能把一些特定的属性推断为readonly。

    >e.g. 在一个class中，如果你有一个只含有getter但是没有setter的属性，它能被推断为只读。

>相关内置：`Readonly`类型别名、`ReadonlyArray`泛型接口。

#### `this`
1. 返回类型`this`

    定义函数的返回值是`this`。
2. 参数`this`

    >`this`参数是个假的参数，它出现在参数列表的最前面。

    定义函数中`this`的类型。

#### `类型1 extends 类型2 ? 类型3 : 类型4`（条件类型）
若 类型1可以赋值给类型2（或 类型1是类型2的extends），则返回类型 类型3，否则返回 类型4。

><details>
><summary>e.g.</summary>
>
>```typescript
>type Type1 = number | boolean;
>
>type W<T> = T extends Type1 ? "yes" : string;
>
>type W1 = W<number>;                               // -> 'yes'
>type W2 = W<1>;                                    // -> 'yes'
>type W3 = W<W1>;                                   // -> string
>type W4 = W<number | boolean | string>;            // -> string
>
>
>class A {
>  a: number;
>}
>interface B extends A {
>  b: string;
>}
>interface C extends B {
>  c: boolean;
>}
>
>type Z<T> = T extends B ? "B+" : Type1;
>type Z1a = Z<A>;                                   // -> Type1
>type Z1c = Z<C>;                                   // -> 'B+'
>type Z2 = Z<{ a: 1; b: "" }>;                      // -> 'B+'
>type Z3 = Z<{ a: "1"; b: "" }>;                    // -> Type1
>
>
>type Type2 = { a: number; b: string };
>
>type X<T> = T extends Type2 ? true : false;
>
>type X1 = X<{ a: number }>;                        // -> false
>type X2 = X<{ a: number; b: string }>;             // -> true
>type X3 = X<{ a: number; b: string; c: number }>;  // -> true
>```
></details>

<details>
<summary><code>extends</code>关键字含义总结</summary>

1. 表示继承/拓展的含义

    1. `class` `extends` `class/abstract class`
    2. `interface` `extends` `interface/class/type`
2. 表示约束的含义

    泛型约束`<类型名 extends 数据类型>`
3. 表示分配的含义

    条件类型`类型1 extends 类型2 ? 类型3 : 类型4`（可以有`infer`）
</details>

#### `infer`
`infer`表示在`extends`条件类型语句中待推断的类型变量。

><details>
><summary>e.g.</summary>
>
>```typescript
>// 整句表示为：若`T`能赋值给 `(arg: infer P) => any`，则结果是`(arg: infer P) => any`类型中的参数`P`，否则返回为`T`
>type ParamType<T> = T extends (arg: infer P) => any ? P : T;
>
>
>interface User {
>  name: string;
>  age: number;
>}
>
>type Func = (user: User) => void;
>
>type Param = ParamType<Func>; // Param = User
>type AA = ParamType<string>; // string
>```
>
>```typescript
>// 获取数组的项值类型
>type ElementOfArray<ArrayType extends readonly unknown[]> = ArrayType extends readonly (infer ElementType)[] ? ElementType : never;
>```
></details>

#### `///`（三斜线指令）
包含单个XML标签的单行注释。注释的内容会做为编译器指令使用。

>1. 三斜线指令**仅**可放在包含它的文件的最顶端。
>2. 一个三斜线指令的前面只能出现单行或多行注释，这包括其它的三斜线指令。
>3. 如果它们出现在一个语句或声明之后，那么它们会被当做普通的单行注释，并且不具有特殊的涵义。

1. `/// <reference path="..." />`
2. `/// <reference types="..." />`
3. `/// <reference no-default-lib="true"/>`
4. `/// <amd-module />`
5. `/// <amd-dependency />`

#### `namespace`（命名空间）
生成的.js有一层命名空间包含内容（不容易污染全局变量），可嵌套。

><details>
><summary>e.g.</summary>
>
>```typescript
>// .ts
>namespace A1 {
>  class B1 {}
>  namespace A2 {
>    class B2 {}
>  }
>}
>
>
>// 被编译为.js
>var A1;
>(function (A1) {
>  var B1 = /** @class */ (function () {
>    function B1() {}
>    return B1;
>  })();
>
>  var A2;
>  (function (A2) {
>    var B2 = /** @class */ (function () {
>      function B2() {}
>      return B2;
>    })();
>  })(A2 || (A2 = {}));
>
>})(A1 || (A1 = {}));
>```
></details>

- 支持：合并

#### 模块化
- 文件作用域

    1. 全局模块

        若一个文件的根级位置没有`export`或`import`，则默认是全局命名空间（定义的变量/类型是全局作用域，会污染全局命名空间，也能直接使用其他全局作用域文件的变量/类型）。
    2. 文件模块/外部模块

        若一个文件的根级位置含有`export`或`import`，则该文件就是一个本地作用域的模块（全局作用域、本地作用域共同作用于该文件模块）。

>配置和书写建议：配置`module: commonjs`选项、使用[`ES6 Module`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#es6-module)语法（完全支持所有写法）导入、导出、编写模块。

1. 导出

    任何声明（如：变量、函数、类、类型别名、接口、namespace、枚举）都能够通过添加`export`关键字来导出。
2. 引入方式：

    1. 有类型声明

        1. 标准[`ES6 Module`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#es6-module)库
        2. 标准CommonJS库的TS特定写法：

            `import xx = require('xx')`
    2. 没有类型声明

        `const xx = require('xx')`（默认导入为`any`类型）

- 特殊：`export =`、`import 变量 = require(模块路径)`

    <details>
    <summary>e.g.</summary>

    ```typescript
    // ZipCodeValidator.ts
    let numberRegexp = /^[0-9]+$/;
    class ZipCodeValidator {
        isAcceptable(s: string) {
            return s.length === 5 && numberRegexp.test(s);
        }
    }
    export = ZipCodeValidator;


    // Test.ts
    import zip = require("./ZipCodeValidator");

    // Some samples to try
    let strings = ["Hello", "98052", "101"];

    // Validators to use
    let validator = new zip();

    // Show whether each string passed each validator
    strings.forEach(s => {
      console.log(`"${ s }" - ${ validator.isAcceptable(s) ? "matches" : "does not match" }`);
    });
    ```
    </details>

#### `名字.d.ts`（声明文件）
>只能定义数据类型，不能定义具体实现，否则报错。

`declare`声明各种类型（`interface`、`type`可以忽略`declare`关键字）。

1. 全局变量的声明文件

    `declare`并没有真的定义一个变量（只是定义了`全局变量/方法/类/枚举/接口/类型别名/命名空间/模块`的数据类型）：仅仅用于编译时的检查，在编译结果中会被删除。多种声明可以组合使用（对同一个名字进行多种不同的声明），是**或**的声明关系。

    1. 声明全局变量：

        `declare var/let/const 变量名: 数据类型`

        >`var/let`可赋值此全局变量；`const`不可赋值此全局变量。
    2. 声明全局方法：

        `declare function 方法名 (参数: 数据类型): 数据类型`

        >支持：重载。
    3. 声明全局类：

        ```typescript
        declare class 类名 {
          属性名: 数据类型                // 没有()是属性
          方法名1(参数: 数据类型): 数据类型  // 有()是方法
          方法名2()                     // 有()是方法
        }
        ```
    4. 声明全局枚举类型：

        ```typescript
        declare enum 变量名 {
          属性名
        }

        declare const enum 变量名 {
          属性名
        }
        ```
    5. 声明全局的接口、type

        >`declare`关键字是可选的。

        ```typescript
        // 可加可不加 declare
        interface 名字 {
            属性名: 数据类型
        }


        // 可加可不加 declare
        type 属性名 = 数据类型 或 字符串字面量类型
        ```
    6. 声明命名空间：

        >暴露在最外层的声明会作为全局类型作用于整个项目中，应该尽可能少定义全局类型，因此最好将它们方法`namespace`中。

        ```typescript
        declare namespace 变量名 {
            变量和数据类型
        }
        ```

        - 命名空间内可以包括所有类型的声明，也可以包含`namespace`（嵌套）
    7. 声明模块（提供给`import/require`）：

        ```typescript
        declare module 模块名 {
          export var bar: number;
        }
        ```

        - 利用webpack，TS也可以导入任何文件

            e.g. 在`某.d.ts`中书写：`declare module '*.css'`则允许导入.css文件，`declare module '*.jpg'`则允许导入.jpg文件。

    - 全局命名空间

        定义在 全局命名空间 的 变量、类型、命名空间 能在项目的所有TS代码里使用（全局模块、文件模块）。

        1. `.d.ts`中定义的内容

            >默认情况下，TS会解析项目内所有`.d.ts`文件。
        2. 在 全局模块 中定义的内容
        3. 在 文件模块 内的`declare global {}`中定义的内容

            >仅能在 文件模块 内使用`declare global {}`，在 全局模块 内使用会报错，在 `.d.ts`内使用无效果。

        ><details>
        ><summary>e.g.</summary>
        >
        >要定义全局的`window.a`
        >
        >```typescript
        >// 某.d.ts
        >interface Window {a: any;}
        >```
        >
        >```typescript
        >// 全局模块（没有import/export的文件）
        >interface Window {a: any;}
        >```
        >
        >```typescript
        >// 文件模块（有import/export的文件）
        >declare global {
        >  interface Window {a: any;}
        >}
        >```
        ></details>
2. 导出`export`

- 引入第三方库声明文件（不需任何配置，引入就可声明成功），可搜索：<https://www.typescriptlang.org/dt/search>

- [lib.d.ts](https://github.com/microsoft/TypeScript/tree/main/src/lib)

    当安装TS时，会顺带安装一个`lib.d.ts`声明文件。该文件包含JS运行时以及DOM中存在各种常见的环境声明，它自动包含在TS项目的编译上下文中。

    - 配置`noLib`从上下文中排除此文件。

    >若需要的话，则自建的`global.d.ts`是一种扩充`lib.d.ts`很好的方式。

#### 协变与逆变
>多态性：对一个简单类型Base和Child来说，若Child是Base的子类（Child ≼ Base），则Child类型的实例能赋值给Base类型的变量。
>
>1. 协变（Covariant）：只在同一个方向；
>2. 逆变（Contravariant）：只在相反的方向；
>3. 双向协变（Bivariant）：包括同一个方向和不同方向；
>4. 不变（Invariant）：若类型不完全相同，则它们是不兼容的。

1.  函数类型

    >在TS中，参数类型是双向协变的，而这并不安全。可以设置`strictFunctionTypes`来修复这个问题，变成参数类型是协变的。

    `返回值类型`是协变的、`参数类型`是逆变的：若`B ≼ A`，则`(x: T) => B` ≼ `(x: T) => A`、`(x: A) => T` ≼ `(x: B) => T`。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >class A {
    >  a() {}
    >}
    >class B extends A {
    >  b() {}
    >}
    >class C extends B {
    >  c() {}
    >}
    >
    >let a: (x: B) => B = (x) => x;
    >let b: (x: A) => C = (x) => { return x as C; };
    >let c: (x: A) => A = (x) => { return x as A; };
    >let d: (x: C) => C = (x) => { return x as C; };
    >let e: (x: C) => A = (x) => { return x as A; };
    >
    >a = b; // ok， 返回值类型是协变的、参数类型是逆变 没问题
    >a = c; // 错误
    >a = d; // 错误
    >a = e; // 错误
    >e = a; // ok， 返回值类型是协变的、参数类型是逆变 没问题
    >```
    ></details>
2. 数组类型

    允许不变的列表（immutable）在它的参数类型上是协变的；但对于可变的列表（mutable），其参数类型则必须是不变的（invariant），既不是协变也不是逆变（类型不会报错，但运行时可能出错-不安全）。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >class A {
    >  a() {}
    >}
    >class B extends A {
    >  b() {}
    >}
    >
    >let a: A[] = [];
    >let b: B[] = [];
    >
    >a = b;             // ok，协变 没问题
    >b = a;             // 错误，a不能赋值给b
    >```
    ></details>

### 其他
1. 配置

    [`tsconfig.json`](https://www.typescriptlang.org/zh/tsconfig)

    1. `tsc`（不带任何输入文件）会自动查找命令目录下的`tsconfig.json`；若带输入文件参数（`-p 「地址」`），则忽略 ~~`tsconfig.json`~~。
    2. `tsc --init`生成一个`tsconfig.json`文件。
2. 文件后缀

    `.ts`、`.tsx`（React、`JSX`）、`d.ts`

    >TypeScript错误`TS1128: Declaration or statement expected.`，可能导致的原因是：tsx文件名命名必须为全小写。
3. TS的声明

    TypeScript中的声明会创建以下三种实体之一：`命名空间`（Namespace），`类型`（Type）、`值`（Value）。

    1. 创建`命名空间`的声明：会新建一个命名空间，它包含了用`.`符号来访问时使用的名字。
    2. 创建`类型`的声明（类型声明空间）：包含可用来当做类型注解的内容。
    3. 创建`值`的声明（变量声明空间）：包含可用作变量的内容。

    | Declaration Type | Namespace | Type | Value（`declare`都不会生成Value） |
    | :--- | :---: | :---: | :---: |
    | Class |  | X | X |
    | Enum |  | X | X（除了~~常数枚举~~之外） |
    | Interface |  | X |  |
    | Type Alias |  | X |  |
    | Function |  |  | X |
    | Variable |  |  | X |
    | Namespace | X |  | X |
4. Tips

    1. 已经定义好的属性的数据类型，不能在之后赋值时再次定义新的数据类型（静态类型）。只能用其他变量来保存新的数据类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >let a: number = 1
        >a: string = String(a)      // 报错
        >let _a: string = String(a)
        >```
        ></details>
    2. 对于同名、后缀分别为`.js`和`.ts`的文件，引用时优先引用`.js`的文件
