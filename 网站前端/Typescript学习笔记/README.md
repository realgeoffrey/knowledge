# [TypeScript](https://github.com/microsoft/TypeScript) 学习笔记

TypeScript 在 JavaScript 的基础上增加静态类型检查。接口、类型别名和类型断言会在编译时擦除。接口响应是否缺字段、DOM 元素是否存在，仍要在运行时判断。[官方手册：基础](https://www.typescriptlang.org/docs/handbook/2/basic-types.html)

本文按 **TypeScript 7.0、`strict: true`** 说明。除标明文件名的配套示例外，每个代码块均可独立阅读，标有“报错”或 `@ts-expect-error` 的行用于观察编译器诊断。文末附浏览器项目的配置和检查命令。[项目配置与类型检查](#项目配置与类型检查) · [TypeScript 7.0 发布说明](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

## 目录

- [类型](#类型)
    - [数据类型](#数据类型)
    - [类](#类)
    - [接口（Interfaces）](#接口interfaces)
    - [类型别名（Type Alias）](#类型别名type-alias)
    - [字面量类型](#字面量类型)
    - [枚举（Enum）](#枚举enum)
    - [泛型（Generics）](#泛型generics)
    - [内置工具类型（Utility Types）](#内置工具类型utility-types)
    - [内置字符串操作类型](#内置字符串操作类型)
- [语法](#语法)
    - [类型推论（Type Inference）](#类型推论type-inference)
    - [类型断言（Type Assertion）](#类型断言type-assertion)
    - [`satisfies`（类型校验）](#satisfies类型校验)
    - [类型保护/类型守卫（Type Guards）](#类型保护类型守卫type-guards)
    - [联合类型（Union Types）](#联合类型union-types)
    - [交叉类型（Intersection Types）](#交叉类型intersection-types)
    - [`表达式!`](#表达式)
    - [`typeof 值`](#typeof-值)
    - [`keyof 数据类型`（索引类型查询）](#keyof-数据类型索引类型查询)
    - [`类型[键名]`（索引访问类型）](#类型键名索引访问类型)
    - [`in`](#in)
    - [装饰器（Decorators）](#装饰器decorators)
    - [`readonly`](#readonly)
    - [映射修饰符（mapping modifiers）`+`、`-`](#映射修饰符mapping-modifiers-)
    - [`this`](#this)
    - [`类型1 extends 类型2 ? 类型3 : 类型4`（条件类型）](#类型1-extends-类型2--类型3--类型4条件类型)
    - [`infer`](#infer)
    - [`...`展开类型](#展开类型)
    - [`///`（三斜线指令，triple-slash directives）](#三斜线指令triple-slash-directives)
    - [`namespace`（命名空间）](#namespace命名空间)
        - [命名空间和模块的区别](#命名空间和模块的区别)
    - [模块化](#模块化)
    - [`名字.d.ts`（声明文件）](#名字dts声明文件)
    - [协变与逆变](#协变与逆变)
    - [注释指令](#注释指令)
- [工程实践](#工程实践)
    - [项目配置与类型检查](#项目配置与类型检查)
    - [前端示例：校验接口响应](#前端示例校验接口响应)
    - [声明的类型空间和值空间](#声明的类型空间和值空间)
    - [采用 TypeScript 的收益与成本](#采用-typescript-的收益与成本)

---

## 类型

### 数据类型

写类型注解时，原始值用小写的 `number`、`string`、`boolean`、`symbol`、`bigint`。大写的 `Number`、`String` 等还会接受包装对象。对于类实例则写类名，如 `const today: Date = new Date()`。函数用具体的调用签名描述参数和返回值。[官方手册：日常类型](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

1. 基本数据类型

    1. `number`，包含整数、浮点数、`NaN` 和正负无穷。
    2. `string`
    3. `boolean`
    4. `symbol`
    5. `bigint`。整数字面量写成 `1n`，算术运算时不能与 `number` 混用。
    6. `undefined`
    7. `null`

    开启 `strictNullChecks` 后，`null` 和 `undefined` 是不同的类型。例如 `string | null` 接受 `null`，要接受 `undefined` 需再写入联合类型。`undefined` 还可以赋给 `void`。关闭这项检查时，编译器允许把空值赋给 `string` 等类型，运行时访问空值仍会报错。

    参数 `a?: number` 可省略，也可显式传 `undefined`。参数 `a: number | undefined` 仍占一个必传位置。对于对象，`{ a?: number }` 接受 `{}`，而 `{ a: number | undefined }` 要求存在 `a`。打开 `exactOptionalPropertyTypes` 后，前一种写法只允许在提供 `a` 时写入数字。要显式写入 `undefined`，写成 `{ a?: number | undefined }`。读取可选属性时仍须考虑其缺失的情况。[配置说明](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html)

2. `void`

    显式声明返回 `void` 的函数可以执行到末尾、写 `return` 或 `return undefined`。开启 `strictNullChecks` 时，`return null` 会报错。当调用方把**回调类型**写成 `() => void`，表示调用方忽略结果，传入的函数可以返回值。[官方手册：返回类型 void](https://www.typescriptlang.org/docs/handbook/2/functions.html#return-type-void)

    ```ts
    const collected: number[] = []
    const collect: (n: number) => void = n => collected.push(n)
    const result = collect(1) // result 的静态类型是 void，push 在运行时返回新长度
    ```

    `Promise<void>` 适合等待异步操作完成而无需使用其兑现值。`Promise<undefined>` 则表示兑现值是 `undefined`。TS 5.1 起，显式标注返回 `undefined` 的函数也可以省略 `return`。[TS 5.1 发布说明](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-1.html#easier-implicit-returns-for-undefined-returning-functions)

    ```ts
    function a(): Promise<void> {
      return new Promise<void>(resolve => resolve())
    }

    function b(): Promise<undefined> {
      return Promise.resolve(undefined)
    }
    ```

3. `never`

    1. 表示永不存在的值的类型

        >e.g. 总是抛出异常或一直循环的函数可以标注为 `never`。遍历联合类型的全部分支后，剩余分支中的变量也会被收窄为 `never`。
    2. 没有共同取值的交叉类型或筛选后没有任何成员的联合类型会得到 `never`。

        >e.g. `number & string`、`Extract<string | number, boolean>`。

    `never`可以赋值给所有类型的变量（包括`undefined`和`null`），`never`是所有类型的子类型。`never`类型的变量仅能被`never`类型的值赋值。

    ><details>
    ><summary>抛错函数与 never 的赋值规则</summary>
    >
    >```ts
    >// 抛错或一直循环，调用方都得不到正常返回值
    >function error (message: string): never {
    >  throw new Error(message)
    >}
    >
    >// 推断的返回值类型为never
    >function fail () {
    >  return error('Something failed')
    >}
    >
    >// 抛错或一直循环，调用方都得不到正常返回值
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

    `any` 让该值的属性访问、调用、赋值等跳过多数类型检查。它也会传播到后续表达式。它能赋给几乎所有类型，`never` 是例外。开启 `noImplicitAny` 可以发现无法推断类型的未注解参数，显式写出的 `any` 仍然有效。
5. `unknown`

    任何值都可以赋给 `unknown`。可以直接做 `typeof`、相等性比较等检查。要调用它或读取业务属性，需要先缩小范围。`?.` 只能处理空值。它无法证实某个属性存在。

    ```ts
    function readMessage(input: unknown): string | undefined {
      if (typeof input === 'object' && input !== null && 'message' in input) {
        return typeof input.message === 'string' ? input.message : undefined
      }
    }
    ```

    `useUnknownInCatchVariables`（随 `strict` 开启）把 `catch (err)` 中的 `err` 设为 `unknown`。例如，可以先检查 `err instanceof Error`，再读取 `err.message`。
6. `Object`、`{}`、`object` 区别（以下开启 `strictNullChecks`）

    1. `Object` 描述 `toString` 等公共成员。字符串、数字等原始值也能赋给它。对象若自己声明了不兼容的同名成员，赋值仍可能失败。
    2. `{}` 表示没有要求任何特定成员。任何非空值都可以赋给它，包括 `0`、空字符串和有属性的对象。
    3. `object` 接受非原始值，例如对象、数组、函数。有了这个类型，编译器仍然不知道对象有哪些业务属性。[官方手册：object](https://www.typescriptlang.org/docs/handbook/2/functions.html#object)

        ><details>
        ><summary>用 object 注解后可以访问哪些成员</summary>
        >
        >```ts
        >let obj1: object
        >
        >obj1 = []
        >
        >obj1.toString()  // 允许访问Object.prototype上的属性
        >obj1.a()         // 报错，只允许使用Object.prototype上的属性
        >obj1.length      // 报错，只允许使用Object.prototype上的属性
        >
        >
        >let obj2: { a(): void }
        >
        >obj2 = { a: () => {} }
        >
        >obj2.toString()  // 允许访问Object.prototype上的属性
        >obj2.a()         // 允许访问定义的属性a
        >obj2.length      // 报错，声明的类型中没有 length
        >```
        ></details>
7. 对象类型

    1. 用`接口`定义。

        1. 必需属性（`属性名: 数据类型`）必须存在且类型兼容。已有变量可以有额外的属性，直接赋值或传参的对象字面量还会接受额外属性检查。
        2. 可选属性（`属性名?: 数据类型`）。
        3. 只读属性（`readonly 属性名: 数据类型`）限制通过这个类型重新赋值。可选性另外用 `?` 表示。若值是对象，内部可写的属性仍可修改。

            >`const` 限制变量重新绑定，`readonly` 限制属性写入。
        4. 索引签名（如 `[key: string]: T`）描述一组键对应的值。被该签名覆盖的已知属性也要与值类型兼容。用 `[key: number]` 可以只描述数字索引，或用模板字符串键描述某一类属性，如 ``[key: `data-${string}`]``。

            >不能用`in`替代`:`。

            1. 当对象同时有固定属性和动态键时，宽泛的字符串索引可能让拼写错误通过检查。例如，把子选择器放到单独的属性后，编译器就能发现拼错的 CSS 属性。

                <details>
                <summary>给嵌套 CSS 的选择器单独设一个属性</summary>

                ```ts
                // 错误示范：
                interface NestedCSS1 {
                  color?: string;
                  [selector: string]: string | undefined | NestedCSS1;
                }
                const example1: NestedCSS1 = {
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
                const example2: NestedCSS2 = {
                  color: 'red',

                  nest: {
                    '.subclass': {
                      color: 'blue',
                      colorxxx: 'red'   // 报错，未知属性 colorxxx
                    }
                  }
                }
                ```
                </details>
            2. 如果已存在的 JavaScript 对象把表单元数据和动态字段放在同一层，可用交叉类型描述它。下面的 `isValid` 同时受到布尔属性和字符串索引签名约束，含有布尔值 `isValid` 的对象字面量无法满足这两个约束。设计新类型时可以把字段放进 `fields: Record<string, FieldState>`。

                <details>
                <summary>用交叉类型描述已有表单对象</summary>

                ```ts
                type FieldState = {
                  value: string;
                };

                type FormState = { isValid: boolean } & { [fieldName: string]: FieldState };

                // 将它用于从某些地方获取的 JavaScript 对象
                declare const foo: FormState;

                const isValidBool = foo.isValid;
                const somethingFieldState = foo['something'];

                const bar: FormState = { isValid: true }; // 报错，布尔值不符合 FieldState
                ```
                </details>

        ><details>
        ><summary>给接口添加可选、只读和动态属性</summary>
        >
        >```ts
        >interface Person {
        >  name: string
        >
        >  func(): string
        >
        >  score?: number   // 可省略，读取时为 number | undefined
        >
        >  readonly id: number
        >
        >  // 索引签名：描述对象的属性
        >  [任意名: string]: string | (() => string) | number | undefined | boolean // 覆盖 name、func、score、id
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
        >tom.xxx = 1n // 报错，bigint 不在索引签名的值类型内
        >```
        ></details>
    2. `: 类型别名`、`: { 属性: 数据类型, }`（内联类型注解）

        `{ [key: string]: T }` 和 `Record<string, T>` 都可以描述字符串键到 `T` 的映射。值类型未知时可以写 `unknown`。开启 `noUncheckedIndexedAccess` 后，读取未显式声明的键会带上 `undefined`，例如 `Record<string, number>` 的任意键可能读到 `number | undefined`。[配置说明](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html)

        ><details>
        ><summary>字符串、数字和枚举键的映射</summary>
        >
        >```ts
        >type 数据类型 = string
        >enum 状态 { 草稿, 已发布 }
        >
        >type A ={
        >  [key: string]: 数据类型;
        >}
        >type A2 ={
        >  [key in string]: 数据类型;
        >}
        >
        >type B ={
        >  [key in 0|1]: 数据类型;       // 不能用`:`替代`in`
        >}
        >type C ={
        >  [key in 状态]: 数据类型;  // 不能用`:`替代`in`
        >}
        >```
        ></details>
    3. `: 类名`

        类名用在类型位置时描述**实例**的成员。要表示构造函数及静态成员，用 `typeof 类名`。

        ><details>
        ><summary>比较类的实例类型和对象字面量</summary>
        >
        >```ts
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

    - 额外属性检查（Excess Property Checks）

        把对象字面量直接赋给带有目标类型的变量或传给函数时，编译器会检查是否显式写入未知属性。传入已有变量时通常按结构检查，只要有要求的成员即可。缺少必需属性在两种写法中都会报错。[官方手册：额外属性检查](https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks)

        ><details>
        ><summary>传入对象变量与直接传入字面量</summary>
        >
        >```ts
        >function logName(something: { name: string }) {
        >  console.log(something.name);
        >}
        >
        >const person = { name: 'matt' };
        >const animal = { name: 'cow', diet: 'vegan, but has milk of own specie' };
        >const noName = { note: `I don't have a name property` };
        >
        >logName(person); // ok
        >logName(animal); // ok
        >logName(noName); // Error: 没有 `name` 属性
        >
        >logName({ name: 'matt' });                          // ok
        >logName({ name: 'matt', job: 'being awesome' });    // Error: 对象字面量只能指定已知属性，`job` 属性在这里并不存在。
        >logName({});                                        // 报错，缺少必需属性 name
        >```
        ></details>
8. 数组类型

    1. `数据类型[]`

        ><details>
        ><summary>对象数组和联合类型数组</summary>
        >
        >```ts
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
    2. 泛型 `Array<T>`，与 `T[]` 等价

        >e.g. `let arr: Array<number | string> = [1, '1']`

        - `ReadonlyArray<数据类型>`

            也可写作 `readonly T[]`。通过这个只读引用访问数组时，类型检查会阻止写入元素和调用 `push` 等方法。同一数组仍可通过可写引用修改。

            ><details>
            ><summary>通过只读引用访问同一个数组</summary>
            >
            >```ts
            >let a: number[] = [1, 2, 3, 4]
            >let ro: ReadonlyArray<number> = a  // 允许，普通数据类型 赋值给 ReadonlyArray
            >
            >ro[0] = 12      // 报错
            >ro.push(5)      // 报错
            >ro.length = 100 // 报错
            >
            >let b: number[] = ro               // 报错，ReadonlyArray赋值给一个普通数组也是不可以的
            >let c: number[] = [...ro]          // 复制得到新数组，可以写入且不影响原数组
            >```
            ></details>
    3. 用`接口`定义

        用数字索引签名描述按下标访问的元素。这种接口也接受对应的类数组对象。若要使用 `length`、`map` 等成员，应使用数组类型或显式声明这些成员。

        ```ts
        interface NumberArray {
          [任意名: number]: number | string
        }

        let arr: NumberArray = [1, '1']
        ```
    4. 元组（Tuple）

        1. 规定`数组`每一项的数据类型：

            1. 没有可选元素或剩余元素时，初始化需要给出约定数量的元素。可选元素如 `[string, number?]`，带剩余元素如 `[string, ...number[]]`。
            2. 固定长度元组的越界字面量下标会报错。非只读元组可以调用 `push`，即使运行时长度增加，静态类型也不会随之扩展。只读元组（如 `readonly [string, number]`）还能阻止这类改动。
        2. 用字面量下标取指定位置的类型，例如 `[string, number][0]` 得到 `string`。用 `[number]` 则得到所有元素类型的联合。

        ><details>
        ><summary>元组的长度、下标与 push</summary>
        >
        >```ts
        >let arr1: [string, number] = ['string', 1]
        >arr1.push(2)
        >arr1[2]                                          // 报错，固定元组没有下标 2
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
        ><summary>让数字索引只读</summary>
        >
        >```ts
        >interface ReadonlyStringArray {
        >  readonly [任意名: number]: string;
        >}
        >
        >let myArray: ReadonlyStringArray = ["Alice", "Bob"];
        >myArray[2] = "Mallory"; // error。readonly
        >```
        ></details>

    >元组编译后是普通 JavaScript 数组。[官方手册：元组](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)
9. 函数类型（方法类型）

    1. 函数声明可直接在参数和返回值上标注类型。返回值通常可以从函数体推断。回调参数还可能由上下文推断，例如 `[1, 2].map(n => n * 2)` 中的 `n` 是 `number`。
    2. 函数表达式的类型可以写成 `(x: number) => string`，也可以用带调用签名的接口、类型别名或内联对象类型表示。全局 `Function` 允许任意参数并返回 `any`，会丢失调用检查。
    3. 支持可选参数、默认参数、剩余参数。带默认值的参数不再写 `?`，传 `undefined` 会触发默认值。若它后面还有必需参数，需要保留它的位置，例如 `f(undefined, required)`。
    4. 调用时必须满足签名要求的参数个数。剩余参数可以用数组类型接收任意数量的同类参数，或用元组限制位置和数量。
    5. 回调的类型应按调用方**实际传入的参数**声明。例如 `(value: string, index: number) => void` 的实现可以只声明 `value`。`index?: number` 则表示调用方可能省略索引，要求使用索引的回调也要处理 `undefined`。
    6. 构造签名描述能用 `new` 调用的值。对象类型中写成 `new (参数): 实例类型`，类型表达式可以写成 `new (参数) => 实例类型`。

        ><details>
        ><summary>用构造签名描述 Point</summary>
        >
        >```ts
        >class Point {
        >  constructor(public x: number) {}
        >}
        >interface PointConstructor {
        >  new (x: number): Point
        >}
        >type PointFactory = new (x: number) => Point
        >
        >const makePoint: PointConstructor = Point
        >const AnotherPoint: PointFactory = makePoint
        >const point = new AnotherPoint(1) // Point
        >```
        ></details>
    7. 函数类型的[协变与逆变](#协变与逆变)

    ><details>
    ><summary>用声明、表达式和接口描述函数</summary>
    >
    >```ts
    >// 函数声明
    >
    >// 可选参数
    >function sum1 (x: number, y?: number): string {
    >  return String(x + (y ?? 0)) // 未传 y 时加 0，也保留 y = 0 的情况
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
    >let mySum1 = function (x: number, y: number) { // 推断返回类型为 string
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
    >  // 还可以继续定义属性，成为 方法-对象 混合类型： a: string; b(): void
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

    >重载签名、对象类型中的方法、`declare class` 的方法以及抽象方法都只写签名。普通函数的实现则要写函数体。

    - 支持：重载

        1. 优先从最前面的函数定义开始匹配，因此若多个函数定义有包含关系，则需优先把精确的定义写在前面。
        2. 调用者只能看到列出的重载签名。紧接在最后一个重载后面的**实现签名**负责检查函数体，不能用来匹配调用。
        3. 实现签名需要兼容每个重载。如果参数个数和返回类型都相同，只是输入有几种类型，通常可直接用联合类型。这样也能接收类型已经是联合的变量。

        ><details>
        ><summary>为字符串和数字提供重载签名</summary>
        >
        >```ts
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

        >编译后只保留一个函数体。若要对不同输入采取不同操作，由实现中的 JavaScript 条件分支负责。[官方手册：重载](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads)
10. 内置对象类型

    1. 浏览器环境

        `lib` 决定编译器认识哪些内置 API。`ES2022` 等 ECMAScript 库提供 `Date`、`Promise` 等声明，浏览器的 `document`、`HTMLElement`、`Window` 等来自 `DOM`。如果手动指定 `lib`，浏览器项目可写 `"lib": ["ES2022", "DOM", "DOM.Iterable"]`。这些声明不会给旧浏览器安装运行时 API。[配置说明](https://www.typescriptlang.org/tsconfig/lib.html)

        ```ts
        const email = document.querySelector('input[name="email"]')
        // 带属性的选择器只推断为 Element | null。检查后才能安全读取输入框的值。
        if (email instanceof HTMLInputElement) {
          console.log(email.value)
        }
        ```

    2. Node.js 环境

        `process`、`Buffer` 等 Node.js 专属 API 的声明由 `@types/node` 提供。安装与运行时对应的主版本（例如 Node.js 22 用 `npm install -D @types/node@22`），并在需要这些全局声明的项目配置中设置 `"types": ["node"]`。TS 6.0 起，`types` 默认是空数组。[TS 6.0 发布说明](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html#types-now-defaults-to-)

- 返回Promise类型

    `Promise<T>` 的 `T` 表示兑现值的类型。标准库把 `.catch()` 回调的拒绝原因声明为 `any`。若要在使用前检查类型，可写 `.catch((reason: unknown) => …)`。

    ><details>
    ><summary>Promise 的兑现值和拒绝原因</summary>
    >
    >```ts
    >function a(): Promise<number | string> {  // 兑现值可以是数字或字符串
    >  return new Promise((resolve, reject) => {
    >    const random = Math.random();
    >    if (random < 0.3) {
    >      resolve(1);               // number
    >    } else if (random < 0.6) {
    >      resolve("1");             // string
    >    } else {
    >      reject(false);            // 拒绝原因不受兑现值类型约束
    >    }
    >  });
    >}
    >
    >function b(): Promise<string> {
    >  return Promise.resolve(123);  // 报错，要求 string
    >}
    >
    >function c(): Promise<string> {
    >  return Promise.reject(123);   // 拒绝路径不会产生 string 兑现值
    >}
    >```
    ></details>

### 类

类声明同时引入实例类型和运行时的构造函数。例如，`const a: Animal = new Animal(...)` 中，冒号后描述实例，`new` 后使用构造函数。

1. 访问修饰符（Access Modifiers）

    规定类的属性或方法在类型检查中的访问权限。如果需要 JavaScript 运行时也强制私有性，可使用 `#age` 这样的私有字段。[官方手册：成员可见性](https://www.typescriptlang.org/docs/handbook/2/classes.html#member-visibility)

    1. `public`（默认）成员可以在类内外访问。
    2. `private` 成员可以在声明它的类中访问，包括通过该类的其他实例读取。类外和子类中直接用点语法访问会报错。

        >`private constructor` 允许类内部创建实例（例如静态工厂方法），禁止外部直接 `new` 或继承。
    3. `protected` 成员可在声明类及其子类内访问，例如子类方法中的 `this.sex`。类外通过实例直接访问会报错。

        ><details>
        ><summary><code>protected constructor</code> 允许类内部构造实例，也允许子类调用 <code>super()</code>。外部不能直接 <code>new</code> 基类。</summary>
        >
        >e.g.
        >
        >```ts
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
        >let john = new Person()     // 报错，Person 的构造函数是 protected，外部不能直接调用
        >let howard = new Employee()
        >```
        ></details>

    ><details>
    ><summary>从类内、类外及子类访问成员</summary>
    >
    >```ts
    >class Animal {
    >  public constructor (name: string, age: number, sex: boolean) {
    >    this.name = name
    >    this.age = age // 类的只读属性在构造函数里初始化
    >    this.sex = sex
    >  }
    >
    >  public name: string
    >  // 开启 strictPropertyInitialization 后，非可选且类型不含 undefined 的普通字段需要初始化。
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
    >  constructor (name: string, age: number, sex: boolean) {
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

        在构造函数参数前加 `public`、`protected`、`private` 或 `readonly`，会同时声明并初始化同名实例属性。

        ><details>
        ><summary>用参数属性初始化实例</summary>
        >
        >```ts
        >// 两种写法都将构造参数保存为实例属性
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

    - 子类重写成员（override）

        1. 公有成员重写后仍须为 `public`。
        2. 基类的 `private` 成员只能在声明类内访问。子类不能重新声明同名成员。
        3. 受保护成员可保持 `protected` 或扩大为 `public`。使用 `override` 可让编译器核对基类中是否存在该成员。开启 `noImplicitOverride` 可要求显式标记对具体成员的重写。
2. `typeof 类名`

    取类构造函数的类型，包含静态成员、`prototype` 以及构造信息。对于有公开构造函数的具体类，这个类型可以直接作为 `new` 的目标。

    ><details>
    ><summary>区分 Greeter 实例与构造函数</summary>
    >
    >```ts
    >class Greeter {
    >  static staticGreeting = 'Hello, there'
    >  greeting: string = 'welcome'
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

    1. TS 禁止直接 `new` 一个抽象类，可用它作为基类或类型注解。
    2. 抽象类可以同时包含抽象成员和有实现的方法。

        抽象方法仅允许出现在抽象类中。
    3. 具体子类必须实现所有尚未实现的抽象成员。抽象子类可以留给后续的具体子类实现。

    >下面的 `Animal` 负责保存名字，并通过抽象方法 `sayHi` 让每种动物提供自己的问候语。

    ><details>
    ><summary>由具体子类实现抽象方法</summary>
    >
    >```ts
    >abstract class Animal {    // 抽象类
    >  public name: string
    >
    >  public constructor (name: string) {
    >    this.name = name
    >  }
    >
    >  public abstract sayHi (): void // 抽象方法
    >  public func () {}        // 抽象类中允许存在非抽象方法
    >}
    >
    >class Cat extends Animal {  // 具体子类，实现抽象方法
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

    `class C implements I` 检查类的实例是否符合接口。它不会给方法参数推断类型，也不会为类补充接口上的可选属性。普通接口描述的是公开成员。要检查构造函数或静态方法，可另外定义带 `new` 或静态成员的接口，再把**类本身**赋给该接口类型的变量，例如函数类型一节的 `PointConstructor`。[官方手册：implements](https://www.typescriptlang.org/docs/handbook/2/classes.html#implements-clauses)

    ><details>
    ><summary>用 implements 检查类的实例成员</summary>
    >
    >```ts
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
    >  }
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
    >  public override lightOn(str: string) {
    >    console.log("Car2 light on", str, this.xx1, this.xx2);
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

    1. 比较实例类型时按实例成员的结构匹配。比较构造函数或静态成员，要使用 `typeof 类名`。
    2. 如果目标实例类型包含 `private` 或 `protected` 成员，源类型必须具有源自同一份类声明的相应成员。子类继承来的成员符合这一条件。[官方手册：类的兼容性](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#classes)

### 接口（Interfaces）

`interface` 描述对象应提供的成员。TypeScript 按结构检查兼容性，调用方可以传入具有更多成员的对象。直接传入或赋值的对象字面量还会做多余属性检查，能及早发现配置项拼写错误。[对象类型与多余属性检查](https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks)

```ts
interface Alarm {
  alert(): void;
}

function testAlarm(alarm: Alarm) {
  alarm.alert();
}

const device = { alert() {}, lightOn() {} };
testAlarm(device);
// @ts-expect-error 直接传入的字面量中多了 Alarm 未声明的 lightOn
testAlarm({ alert() {}, lightOn() {} });
```

接口可以同时描述属性、调用签名和索引签名。`[index: number]: string` 只规定用数字索引时的元素类型。需要数组的 `length`、`map` 等成员时，通常直接用 `string[]` 或 `readonly string[]`。

<details>
<summary>例：一个可以调用、也有属性和方法的计数器</summary>

```ts
interface Counter {
  (start: number): string;
  interval: number;
  reset(): void;
}

function getCounter(): Counter {
  let count = 0;
  function counter(start: number) {
    count += start;
    return String(count);
  }
  counter.interval = 123;
  counter.reset = () => { count = 0; };
  return counter;
}

const c = getCounter();
c(10);          // "10"
c.reset();
c.interval = 5;
```

</details>

- **继承与实现。** `interface B extends A` 要求 `B` 的值可赋给 `A`。接口可继承多个接口、类的实例类型，或成员静态可知的对象类型别名。类可用 `implements` 检查实例是否符合接口或这类对象别名。继承已有属性时，新属性的类型须可赋给原类型。
- **声明合并。** 同一作用域中的同名接口会合并。重复的普通属性要用相同类型和修饰符。同名方法签名可形成重载。接口也可与同名的类合并，给实例类型补充成员。合并只影响类型，新增的方法需要有对应的运行时实现。[声明合并](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#merging-interfaces)

```ts
type Named = { name: string };
interface Alarm { alert(): void }
interface LightableAlarm extends Alarm, Named { lightOn(): void }
interface LightableAlarm { lightOff(): void } // 给同一个接口补充成员

const deskAlarm: LightableAlarm = {
  name: "desk", alert() {}, lightOn() {}, lightOff() {},
};
```

<details>
<summary>例：接口继承带有私有成员的类</summary>

类的 `private`、`protected` 成员在兼容性检查中要求有相同的声明来源。下面的 `Button` 从 `Control` 继承了 `state`，另一个类自己声明的同名字段无法满足接口。

```ts
class Control {
  private state = 0;
  isActive() { return this.state > 0; }
}
interface SelectableControl extends Control {
  select(): void;
}
class Button extends Control implements SelectableControl {
  select() {}
}

// @ts-expect-error 两个 state 来自不同的私有声明
class ImageControl implements SelectableControl {
  private state = 0;
  isActive() { return this.state > 0; }
  select() {}
}
```

</details>

### 类型别名（Type Alias）

`type` 给已有类型取名字，可表示原始类型、对象、函数、元组、联合类型等。同一作用域内不能重复声明同名类型别名。给 `string` 起名为 `Name` 后，两者仍然可以互相赋值。[类型别名与接口](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

```ts
type Name = string;
type NameResolver = () => string;
type NameOrResolver = Name | NameResolver;

function getName(value: NameOrResolver): Name {
  return typeof value === "string" ? value : value();
}
```

别名可以在属性中递归引用自身。表示有限树或链表时，需要允许叶子或末尾节点结束。

```ts
type Tree<T> = { value: T; left?: Tree<T>; right?: Tree<T> };
type LinkedList<T> = { value: T; next: LinkedList<T> | null };

const names: LinkedList<string> = { value: "Lin", next: null };
```

`&` 组合类型，结果须同时满足两边的要求。它也可组合接口。两个类型出现同名属性时，冲突可以进入交叉类型，影响后续赋值。接口的 `extends` 则会在继承处检查兼容性。[接口继承与交叉类型](https://www.typescriptlang.org/docs/handbook/2/objects.html#interface-extension-vs-intersection)

```ts
interface Named { name: string }
type User = Named & { age: number };
type Bad = { id: string } & { id: number };
type BadId = Bad["id"]; // never，值须同时是 string 和 number
```

### 字面量类型

字符串、数字、布尔值和 bigint 的字面量可以直接用作类型。用 `|` 列出允许的取值，也可以让对象的某个字段标识不同分支。

```ts
type Easing = "ease-in" | "ease-out" | "ease-in-out";
type FontSize = 12 | 16 | 24;
type Result = { ok: true; value: string } | { ok: false; error: Error };

function getMessage(result: Result) {
  return result.ok ? result.value : result.error.message;
}
```

模板字面量类型可将前缀、后缀与已有联合类型组合。在多个位置插入联合类型时，结果包含每个位置取值的所有组合。[模板字面量类型](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html)

```ts
type Locale = "en" | "zh";
type Message = "welcome" | "footer";
type MessageID = `${Locale}_${Message}`;
// "en_welcome" | "en_footer" | "zh_welcome" | "zh_footer"
```

### 枚举（Enum）

普通 `enum` 同时声明一个类型和一个运行时对象。数字成员默认从 `0` 开始，后续未初始化的成员接着前一个数值常量递增。成员也可显式指定数值或字符串。字符串成员和运行时计算出的成员之后，下一项要显式初始化。[枚举](https://www.typescriptlang.org/docs/handbook/enums.html)

```ts
enum Level { Low, Normal = 3, High }
enum Direction { Up = "UP", Down = "DOWN" }

console.log(Level.Low, Level.Normal, Level.High); // 0 3 4
console.log(Level[4]);                           // "High"
console.log(Direction.Up);                      // "UP"
type LevelName = keyof typeof Level;            // "Low" | "Normal" | "High"
```

- **运行时映射。** 数字成员有正向和反向映射。两个成员共用一个数值时，反向查到的是最后写入的成员名。`Object.keys(Level)` 会同时枚举名字和数字键（字符串形式）。字符串成员只有从名字到值的映射。
- **常量与计算成员。** `Read = 1 << 1` 可以在编译时求值，`Random = Math.random()` 需要运行时求值。从 TS 5.0 起，含计算成员的枚举也可按成员类型收窄。[TS 5.0 枚举变更](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#all-enums-are-union-enums)
- **数值兼容。** 数字枚举可赋给 `number`。以数值常量定义的枚举能在编译期拒绝未声明的数字字面量，但一个宽泛的 `number` 仍可赋给它。例如从接口读到数字状态码时，应先验证该值属于业务允许的范围。

```ts
enum Status { Ready, Waiting }
const ready: Status = Status.Ready;
// @ts-expect-error 这个数字枚举的成员值只有 0、1
const missing: Status = 3;

function isStatus(value: number): value is Status {
  return value === Status.Ready || value === Status.Waiting;
}
```

<details>
<summary>常数枚举、外部枚举、通过命名空间增加方法</summary>

- `const enum` 只允许编译期可计算的成员。`tsc` 在常规整项目编译下会内联成员访问，默认移除枚举声明。`preserveConstEnums` 可保留本地枚举对象。
- `declare enum` 描述外部已有的枚举对象。声明本身没有 JavaScript 产物，程序读取成员时需要有真实对象。
- `declare const enum` 可让消费者内联外部成员。启用 `isolatedModules` 时不能访问外部常数枚举成员。库公开这种声明还可能使编译时内联值与运行时依赖版本不一致。[常数枚举的跨项目限制](https://www.typescriptlang.org/docs/handbook/enums.html#const-enum-pitfalls)
- 在普通枚举之后声明同名 `namespace`，可向枚举对象增加方法。

```ts
enum Weekday { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday }
namespace Weekday {
  export function isBusinessDay(day: Weekday) {
    return day !== Weekday.Saturday && day !== Weekday.Sunday;
  }
}
Weekday.isBusinessDay(Weekday.Monday); // true
```

</details>

前端项目也常用 `as const` 对象存放一组协议值。对象能直接在运行时遍历，用索引访问类型即可得到值的联合。

```ts
const Direction = { Up: "UP", Down: "DOWN" } as const;
type DirectionValue = (typeof Direction)[keyof typeof Direction]; // "UP" | "DOWN"
const initial: DirectionValue = "UP";
```

### 泛型（Generics）

泛型用类型参数表达多个位置之间的关系。比如函数 `identity<T>(arg: T): T` 保留输入的具体类型。调用者可以显式给出 `T`，也可以让编译器根据实参推断。[泛型](https://www.typescriptlang.org/docs/handbook/2/generics.html)

```ts
function identity<T>(arg: T): T { return arg; }

const title = identity("首页");             // "首页"
const count = identity<number>(1);         // number
const stringIdentity = identity<string>;   // (arg: string) => string
```

- **泛型函数与泛型接口。** 类型参数写在调用签名上时，每次调用都可以选择不同类型。写在接口名上时，使用接口的地方先确定类型，随后各次调用共用它。类型别名也可以带参数，例如上面的 `LinkedList<T>`。

```ts
interface GenericCall { <T>(arg: T): T }
interface FixedCall<T> { (arg: T): T }

const anyIdentity: GenericCall = value => value;
const numberIdentity: FixedCall<number> = value => value;
anyIdentity("a");
anyIdentity(2);
numberIdentity(2);
```

<details>
<summary>例：同一类型参数出现多次时，显式选择要允许的元素类型</summary>

```ts
function combine<T, U>(first: T, second: U, rest: Array<T | U>): Array<T | U> {
  return [first, second, ...rest];
}
combine<string, number>("a", 2, ["aa", 22]);
combine<"a", 2>("a", 2, ["a", 2]);
// @ts-expect-error 推断到的元素类型是 "a" | 2，无法放入 "aa" 或 22
combine("a", 2, ["aa", 22]);
```

</details>

- **约束与默认值。** `extends` 指定实参类型必须满足的约束，如 `T extends { length: number }`。默认类型写在 `=` 后，例如 `Page<T = string>`。约束也可引用其他类型参数，下面让返回值随传入的属性名变化。

```ts
type Page<T = string> = { items: T[]; total: number };
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const settings = { theme: "dark", fontSize: 16 };
const size = getProperty(settings, "fontSize"); // number
// @ts-expect-error settings 没有 zoom 属性
getProperty(settings, "zoom");
```

- **泛型类。** 类的类型参数对实例成员生效。不同 `T` 的实例共享同一个类的静态成员，所以静态成员无法引用类上的 `T`。静态方法可以声明自己的类型参数。

```ts
class Box<T> {
  constructor(readonly value: T) {}
  static of<U>(value: U) { return new Box(value); }
}
const countBox = Box.of(42); // Box<number>
```

- **保留字面量。** TS 5.0 的 `const` 类型参数可以保留直接传入的对象或数组字面量的具体形状，适合从选项列表推导允许值。已经扩宽的变量仍保留原类型。[const 类型参数](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#const-type-parameters)

```ts
function options<const T extends readonly string[]>(values: T): T {
  return values;
}
const tabs = options(["home", "settings"]); // readonly ["home", "settings"]
type Tab = (typeof tabs)[number];           // "home" | "settings"
```

### 内置工具类型（Utility Types）

工具类型从已有类型推导出新类型，常用于给表单、请求参数、回调等建模。它们在编译后被擦除。[内置工具类型](https://www.typescriptlang.org/docs/handbook/utility-types.html)

**调整对象属性**

| 写法 | 用途 |
| --- | --- |
| `Partial<T>` | 将顶层属性改为可选，常用于表示局部更新。 |
| `Required<T>` | 去掉顶层属性的可选标记。 |
| `Readonly<T>` | 将顶层属性改为只读，不会冻结运行时对象。 |
| `Record<K, V>` | 把键 `K` 映射到值类型 `V`。有限键联合会逐个检查键是否齐全。 |
| `Pick<T, K>` | 选取 `T` 的指定属性，`K` 必须是 `T` 的键。 |
| `Omit<T, K>` | 移除指定键的类型信息，运行时对象仍保有原字段。 |

```ts
interface Todo { title: string; completed: boolean; description?: string }
type TodoPatch = Partial<Todo>;
type FullTodo = Required<Todo>;
type TodoPreview = Pick<Todo, "title" | "completed">;
type NewTodo = Omit<Todo, "completed">;

const patch: TodoPatch = { completed: true };
const labels: Record<"open" | "done", string> = { open: "进行中", done: "已完成" };
```

`Partial` 等工具只处理一层。比如 `Partial<{ theme: { color: string } }>` 允许整个 `theme` 缺省，一旦提供 `theme`，其中的 `color` 仍然必填。可以用映射类型写出这一过程。

```ts
type MyPartial<T> = { [K in keyof T]?: T[K] };
type MyRequired<T> = { [K in keyof T]-?: T[K] };
type MyReadonly<T> = { readonly [K in keyof T]: T[K] };
```

**筛选联合成员**

`Extract<T, U>` 保留 `T` 中可赋给 `U` 的成员。`Exclude<T, U>` 移除这些成员。`NonNullable<T>` 去掉 `null` 和 `undefined`。筛选按成员的可赋值关系判断，例如 `Exclude<string, "done">` 仍是 `string`。

```ts
type Result = { ok: true; data: string } | { ok: false; error: Error };
type Failure = Extract<Result, { ok: false }>; // { ok: false; error: Error }
type Pending = Exclude<"idle" | "busy" | "done", "done">; // "idle" | "busy"
type Present = NonNullable<string | null | undefined>;   // string
```

**从函数与构造函数提取类型**

`Parameters<F>` 提取参数元组，`ReturnType<F>` 提取返回值。函数值用 `typeof` 取得其类型。普通的 `Function` 没有足够具体的调用签名。针对带重载的函数，这两个工具按最后一个对外可见的签名提取。浏览器的 `window.setTimeout` 返回 `number`，跨环境保存计时器句柄时可用 `ReturnType<typeof setTimeout>` 跟随当前项目的声明。

```ts
function format(value: number, digits: number) { return value.toFixed(digits); }
type FormatArgs = Parameters<typeof format>; // [value: number, digits: number]
type Formatted = ReturnType<typeof format>;  // string
// @ts-expect-error Function 没有提取返回类型所需的调用签名
type Invalid = ReturnType<Function>;

class Point { constructor(public x: number, public y: number) {} }
type Coordinates = ConstructorParameters<typeof Point>; // [x: number, y: number]
type PointInstance = InstanceType<typeof Point>;        // Point
```

**异步结果与 this**

- `Awaited<T>` 模拟 `await` 对值的处理，递归解开 `Promise` 和具有相应 `then` 签名的对象，并对联合类型的成员分别处理。`Promise<T>` 描述标准 Promise 实例，`PromiseLike<T>` 则只要求兼容的泛型 `then` 方法。[Awaited](https://www.typescriptlang.org/docs/handbook/utility-types.html#awaitedtype)

```ts
type Loaded = Awaited<boolean | Promise<Promise<string>>>; // boolean | string
async function loadItems() { return [{ id: 1, title: "首页" }]; }
type Items = Awaited<ReturnType<typeof loadItems>>; // { id: number; title: string }[]
```

- `ThisParameterType<F>` 提取显式声明的 `this` 参数类型，未声明时得到 `unknown`。`OmitThisParameter<F>` 给出移除该参数后的调用签名。运行时要固定接收者，可用 `bind`。
- `ThisType<T>` 用在对象字面量的上下文类型中，使方法内部的 `this` 按 `T` 检查。需要开启 `noImplicitThis`（包含在 `strict` 中）。对象在运行时如何绑定 `this`，仍由实际调用方式决定。

```ts
function toHex(this: number) { return this.toString(16); }
type Receiver = ThisParameterType<typeof toHex>; // number
const toHex15: OmitThisParameter<typeof toHex> = toHex.bind(15);
toHex15(); // "f"

type Methods = { increment(): void } & ThisType<{ count: number }>;
const methods: Methods = {
  increment() { this.count += 1; },
};
const counter = { count: 0, ...methods };
counter.increment();
```

**指定泛型的推断来源**

`NoInfer<T>`（TS 5.4）让某个参数按 `T` 检查，同时阻止编译器从该位置推断 `T`。下面只从选项列表推断 `T`，避免无效默认值被推断进允许值的联合。[NoInfer](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)

```ts
function selectDefault<T extends string>(options: readonly T[], value: NoInfer<T>): T {
  if (!options.includes(value)) throw new Error("无效选项");
  return value;
}
selectDefault(["light", "dark"], "dark");
// @ts-expect-error "auto" 不在第一个参数给出的允许值中
selectDefault(["light", "dark"], "auto");
```

### 内置字符串操作类型

`Uppercase<S>`、`Lowercase<S>` 转换整段字符串的大小写。`Capitalize<S>`、`Uncapitalize<S>` 只处理开头字符。标准库用 `intrinsic` 声明这些类型，具体转换由编译器实现，不随区域设置变化。JavaScript 字符串值需要通过运行时方法转换。[内置字符串操作类型](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html#intrinsic-string-manipulation-types)

```ts
type Greeting = "Hello, world" | "Hi";
type ShoutyGreeting = Uppercase<Greeting>;            // "HELLO, WORLD" | "HI"
type CacheKey<S extends string> = `ID-${Uppercase<S>}`;
type MainID = CacheKey<"my_app">;                     // "ID-MY_APP"
type EventName = `on${Capitalize<"click" | "focus">}`; // "onClick" | "onFocus"
```

---

## 语法

### 类型推论（Type Inference）

类型注解省略时，TS 可以根据初始值、候选元素和表达式所在的位置推断类型。[官方手册：类型推论](https://www.typescriptlang.org/docs/handbook/type-inference.html)

1. 从值推断。`let title = '首页'` 可重新赋值，推断为 `string`。`const title = '首页'` 保留字面量类型 `'首页'`。对象的可写属性和普通数组的元素通常会拓宽。
2. 最佳通用类型。从多个候选类型中寻找能容纳所有元素的类型。例如 `const ids = [1, 2, 'guest']` 推断为 `(number | string)[]`。
3. 上下文类型。表达式所在的位置可以提供预期类型，例如事件回调的参数来自 `addEventListener` 的签名。

    ```ts
    document.addEventListener('keydown', event => {
      console.log(event.key); // event 推断为 KeyboardEvent
    });
    ```

开启 `noImplicitAny` 后，普通函数参数若既无注解又无上下文，会因隐式 `any` 报错。未初始化的局部变量还可以根据后续赋值确定使用处的类型。例如 `let value; value = 'ok'; value.toUpperCase();` 可以通过检查。[官方说明：后续赋值对类型推断的影响](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#improved-any-inference)

### 类型断言（Type Assertion）

`值 as 类型` 告诉编译器按指定类型检查这个表达式。`.ts` 也支持 `<类型>值`，`.tsx` 中使用 `as` 以避免与 JSX 标签混淆。断言会在编译时擦除，运行时的值和属性都保持原样。[官方手册：类型断言](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)

- 直接断言通常要求源类型和目标类型有足够重叠。对不相关的类型，编译器会提示错误。`as unknown as T` 可以绕过这项检查，所以缺少运行时证据时，即使能编译也可能出错。

    ```ts
    const numericId = 42;
    // @ts-expect-error number 和 string 没有足够重叠
    const wrong = numericId as string;
    const forced = numericId as unknown as string; // 静态类型是 string，实际值仍是 42
    ```

- `const` 断言（const assertions）

    对字面量使用 `as const`，可以保留字面量类型，把对象字面量的属性推断为只读，把数组字面量推断为只读元组。这些限制作用于类型检查。若属性引用外部已创建的可变数组，该数组的内容仍可修改。[官方说明：const 断言](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions)

    ><details>
    ><summary>观察 as const 对对象和数组的推断</summary>
    >
    >```ts
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

### `satisfies`（类型校验）

TS 4.9+ 可以用 `表达式 satisfies 目标类型` 检查配置是否满足约束，同时保留表达式各成员推断出的具体类型。适合在书写配置时发现缺项、拼错的键或错误值。[官方说明：satisfies](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator)

```ts
type Page = 'home' | 'help';
const routes = {
  home: '/',
  help: '/help',
} as const satisfies Record<Page, string>;

type HomePath = typeof routes.home; // -> '/'
```

### 类型保护/类型守卫（Type Guards）

TS 会沿控制流分析条件、赋值和提前返回等语句，缩小某一位置上变量可能的类型。类型守卫是 TS 能理解的运行时检查。[官方手册：类型收窄](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)

1. 类型判断

    `typeof 变量 === 'string'` 等。`typeof null` 也等于 `'object'`，访问可能为 `null` 的对象前要单独排除 `null`。

    ><details>
    ><summary>用 typeof 区分字符串和数字</summary>
    >
    >```ts
    >function test(input: string | number) {
    >  if (typeof input === 'string') {
    >    // 这里 input 的类型「收紧」为 string
    >  } else {
    >    // 这里 input 的类型「收紧」为 number
    >  }
    >  // 这里 input 仅能访问此联合类型的所有类型里共有的属性/方法
    >}
    >```
    ></details>
2. 实例判断

    `变量 instanceof 构造函数` 检查原型链。右侧需要运行时存在的值，`interface` 会在编译时擦除。

    ><details>
    ><summary>用 instanceof 区分两个类的实例</summary>
    >
    >```ts
    >class Foo { foo = 1; }
    >class Bar { bar = 2; }
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

    `属性名 in 对象` 检查对象及其原型链。某个成员若将该属性声明为可选，它可能同时出现在两个分支。

    ><details>
    ><summary>用 in 检查成员是否存在</summary>
    >
    >```ts
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

    `变量 === 字面量` 或 `变量 !== 字面量`。

    ><details>
    ><summary>用字面量比较排除一个成员</summary>
    >
    >```ts
    >type Foo = 'foo' | 'bar' | 'unknown';
    >
    >function test(input: Foo) {
    >  if (input !== 'unknown') {
    >    // 这里 input 的类型「收紧」为 'foo' | 'bar'
    >  } else {
    >    // 这里 input 的类型「收紧」为 'unknown'
    >  }
    >  // 这里 input 仅能访问此联合类型的所有类型里共有的属性/方法
    >}
    >```
    ></details>

5. 自定义类型保护

    返回类型写作 `参数名 is 类型`。返回 `true` 表示参数属于该类型，返回 `false` 时，调用方可以排除该类型。编译器信任显式谓词，函数实现需要保证两个方向都正确。

    ```ts
    interface Fish { swim(): void }
    interface Bird { fly(): void }

    function isFish(pet: Fish | Bird): pet is Fish {
      return 'swim' in pet && typeof pet.swim === 'function';
    }

    function move(pet: Fish | Bird) {
      if (isFish(pet)) {
        pet.swim();
      } else {
        pet.fly();
      }
    }
    ```

    从 TS 5.5 起，简单的守卫函数也能推断出类型谓词。函数需省略返回类型、只有一个返回点且没有隐式返回、不修改参数，并返回能够区分参数类型的布尔条件。[官方说明：推断类型谓词](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html#inferred-type-predicates)

    ```ts
    const isString = (input: unknown) => typeof input === 'string';
    const names = ['Ada', null, 'Lin'].filter(isString); // -> string[]
    const scores = [0, undefined, 8].filter(n => n !== undefined); // -> number[]，保留 0
    ```

    对校验失败就抛错的函数，可以写 `asserts 参数名 is 类型`。调用正常返回后，后面的语句就能使用收窄后的类型。

    ```ts
    function assertInput(el: Element | null): asserts el is HTMLInputElement {
      if (!(el instanceof HTMLInputElement)) throw new Error('找不到输入框');
    }

    const el = document.querySelector('#search');
    assertInput(el);
    console.log(el.value); // HTMLInputElement
    ```

### 联合类型（Union Types）

`A | B` 接受属于 `A` 或 `B` 的值，也允许同时满足两者。读取联合类型的值时，只能直接使用对当前所有候选类型都有效的操作。类型守卫和赋值都可能使变量在当前位置收窄。

```ts
function getLength(value: string | number) {
  return typeof value === 'string' ? value.length : String(value).length;
}

let id: string | number = 42;
id.toFixed();           // 这里是 number
id = 'guest';
id.toUpperCase();       // 这里是 string，声明类型仍允许以后赋 number
```

- 可辨识联合（Discriminated Unions）

    各成员用同名属性的不同字面量值标识自己。用 `switch` 按该属性分支，剩余情况赋给 `never` 可以检查是否穷尽所有成员。以后若新增车型却漏掉对应分支，赋给 `never` 的那一行就会报错。

    ><details>
    ><summary>按车型分支并检查是否遗漏</summary>
    >
    >```ts
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

> 多行书写联合类型时，第一个成员前也可以添加 `|`，例如 `type Id = | number | string;`。

### 交叉类型（Intersection Types）

`A & B` 表示一个值必须同时满足 `A` 和 `B` 的要求。

1. 没有值能同时满足 `number` 和 `string`，因此 `number & string` 为 `never`。
2. 交叉多个对象类型，得到同时具有它们全部属性的类型。

    ><details>
    ><summary>交叉类型对对象成员的要求</summary>
    >
    >```ts
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

3. 对联合类型取交叉，可以留下两者共有的成员。例如 `type X = string & (1 | '2' | true)` 得到 `'2'`。
4. 同名属性也要同时满足两个约束。例如 `({ id: number } & { id: string })['id']` 得到 `never`。交叉类型不会像 JS 对象展开那样用后面的值覆盖前面的值。

### `表达式!`

开启 `strictNullChecks` 时，后缀 `!` 告诉编译器在这个表达式的类型中排除 `null` 和 `undefined`。生成的 JS 不包含空值检查。例如 `document.querySelector('#save')!.classList` 在找不到元素时会抛出异常。需要处理元素缺失时，用条件判断或可选链。

```ts
const button = document.querySelector('#save');
button?.classList.add('ready'); // 找不到按钮就跳过
if (button) {
  button.addEventListener('click', () => console.log('保存'));
}
```

### `typeof 值`

在表达式中，JS 的 `typeof value` 返回字符串，例如 `'string'`。在类型位置，TS 的 `typeof` 查询变量或其属性的类型，适合从已有值派生类型。要表示函数调用的返回类型，可以写 `ReturnType<typeof fn>`。[官方手册：typeof 类型运算符](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html)

><details>
><summary>查询函数、类和字面量的类型</summary>
>
>```ts
>function foo(x: number): Array<number> {
>  return [x];
>}
>type F = typeof foo; // -> (x: number) => number[]
>
>
>class A {
>  a = '';
>  constructor() {
>    console.log("I'm A");
>  }
>}
>
>const a: A = { a: "" };
>
>type A2 = A;        // -> A的实例类型
>type A3 = typeof a; // -> a的类型（ === A的实例类型）
>type A4 = typeof A; // -> 类 A 的构造函数及静态成员的类型
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
>```ts
>const foo1 = 'Hello World';
>let bar1: typeof foo1;
>// bar1 仅能被赋值 'Hello World'
>bar1 = 'Hello World';      // ok
>// @ts-expect-error 只接受特定字面量
>bar1 = 'anything else';
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
>// @ts-expect-error 只接受特定字面量
>bar3 = 'anything else';
>```
></details>

### `keyof 数据类型`（索引类型查询）

`keyof T` 得到可以用于访问 `T` 的键类型，键可以是 `string`、`number` 或 `symbol`。对于联合类型，`keyof (A | B)` 只包含各成员都支持的键。[官方手册：keyof](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html)

<details>
<summary>查询对象、数组与索引签名的键</summary>

```ts
interface Person {
  name: string;
  age: number;
  location?: string;
}

type K1 = keyof Person;                        // -> "name" | "age" | "location"
type K2 = keyof Person[];                      // -> number | "length" | "push" | "pop" | "concat" | ...
type K3 = keyof { [任意名: string]: Person };   // -> string | number （JS 会将数字属性键转为字符串，obj[0] 与 obj["0"] 等价）

const a = { 'b': 1, 'c': '2', 3: 3, '4': 4 };
type K4 = keyof typeof a;                      // -> 'b' | 'c' | 3 | '4'
```

- 用 `T[keyof T]` 获取对象各属性值类型的联合。对于 `as const` 声明的配置对象，可以直接派生值的字面量联合。

    ```ts
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

    ```
</details>

### `类型[键名]`（索引访问类型）

在类型位置，用 `T[K]` 查询键 `K` 对应的属性值类型。键也可以是联合类型，查询结果是各属性类型的联合。[官方手册：索引访问类型](https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html)

1. `Person["name"]` 取出属性 `name` 的值类型。
2. `数组类型[number]` 取出元素类型，对元组可得到各位置元素类型的联合。
3. `{ [key: string]: V }[string]` 得到字符串索引签名的值类型 `V`。

><details>
><summary>从属性、方法和数组中提取类型</summary>
>
>```ts
>interface Person {
>  name: string;
>  age: number;
>  location: string;
>}
>type P1 = Person["name"];          // -> string
>type P2 = Person["name" | "age"];  // -> string | number
>
>type P3 = string["charAt"];        // -> (pos: number) => string
>type P4 = string[]["push"];        // -> (...items: string[]) => number
>type P5 = string[][0];             // -> string
>
>type A = [...{a: string; b: number;}[], boolean]
>type B = A[number]                 // -> boolean | {a: string; b: number;}
>```
></details>

<details>
<summary>从已有响应类型挑选页面所需的部分属性</summary>

```ts
interface TaskResponse {
  stTask: {
    uId: number;
    uType: number;
    uState: number;
    strRewardId: string;
    stNormal: { stRewardProgress: { vctNode: number[]; total: number } };
  };
}

type Task = TaskResponse['stTask'];
type Progress = Task['stNormal']['stRewardProgress'];
type TaskView = Pick<Task, 'uId' | 'uType' | 'uState' | 'strRewardId'> & {
  stNormal: { stRewardProgress: Pick<Progress, 'vctNode'> };
};

const data: { stTask: TaskView } = {
  stTask: {
    uId: 0, uType: 0, uState: 0, strRewardId: '',
    stNormal: { stRewardProgress: { vctNode: [] } },
  },
};
```
</details>

### `in`

在映射类型中，`[P in K]` 为键类型 `K` 的每个成员生成一个属性。`[P in keyof T]` 遍历 `T` 的键。这里的 `in` 出现在类型位置，运行时的 `'key' in obj` 则检查属性是否存在。

```ts
type Keys = 'a' | 'b';
type Flags = { [P in Keys]: boolean }; // -> { a: boolean; b: boolean }

enum Direction { Up, Down }
type ByValue = { [P in Direction]: boolean };              // 键为 0 和 1
type ByName = { [P in keyof typeof Direction]: boolean };  // 键为 'Up' 和 'Down'
```

TS 4.1+ 可用 `as` 重命名映射后的键。把键映射为 `never`，该键就会从结果中移除。[官方手册：映射类型](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html#key-remapping-via-as)

```ts
type PublicFields<T> = {
  [P in keyof T as P extends `_${string}` ? never : P]: T[P];
};
type Card = PublicFields<{ title: string; _cache: number }>; // -> { title: string }
```

### 装饰器（Decorators）

`@expression` 中的表达式会求值为装饰器函数。TS 支持两套调用约定，阅读库文档时先看项目的 `experimentalDecorators` 设置。[TS 5.0 装饰器说明](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#decorators) · [旧版实验性装饰器手册](https://www.typescriptlang.org/docs/handbook/decorators.html)

| | TS 5.0+ 的标准提案语义 | 旧版实验性语义 |
| --- | --- | --- |
| 配置 | `experimentalDecorators` 关闭或省略 | `experimentalDecorators: true` |
| 适用位置 | 类、方法、字段、getter/setter、`accessor` | 类、方法、属性、访问器以及构造函数或方法的参数 |
| 方法装饰器收到的参数 | 原方法和 `context`，例如 `context.name` | `target`、属性键和属性描述符 |
| 元数据选项 | 不支持 `emitDecoratorMetadata` | 可配合 `emitDecoratorMetadata` 发出类型元数据 |

下面是标准提案语义的方法装饰器。装饰器在定义类时执行，返回的新函数在调用方法时执行。

```ts
function trimResult<This>(
  method: (this: This) => string,
  _context: ClassMethodDecoratorContext<This, (this: This) => string>,
) {
  return function (this: This) {
    return method.call(this).trim();
  };
}

class Page {
  @trimResult
  title() { return ' 首页 '; }
}

new Page().title(); // -> '首页'
```

同一声明叠加多个装饰器时，表达式从上到下求值，所得装饰器函数从下到上调用。例如叠写 `@f()`、`@g()`，先求值 `f()`，再求值 `g()`，然后依次应用 `g` 和 `f` 返回的装饰器。

### `readonly`

`readonly` 可以标记对象或类的属性，也可以声明只读数组和元组。类中只有 getter 的属性自动是只读的。构造函数的参数属性可以写作 `public readonly id: string`。对于普通函数参数，可以在其**类型**上表达只读要求。

```ts
interface Config {
  readonly options: { pageSize: number };
}

function total(scores: readonly number[]) {
  // scores.push(0); // 报错，readonly number[] 没有 push 方法
  return scores.reduce((sum, score) => sum + score, 0);
}

const config: Config = { options: { pageSize: 20 } };
config.options.pageSize = 50; // 属性 options 的引用只读，内部 pageSize 仍可写
```

相关内置类型有 `Readonly<T>` 和 `ReadonlyArray<T>`。它们提供静态检查。需要在运行时冻结对象时可使用 `Object.freeze`，其冻结效果也是浅层的。

### 映射修饰符（mapping modifiers）`+`、`-`

增加（不写默认`+`）或去除：`readonly`或`?`

```ts
// Removes 'readonly' attributes from a type's properties
type CreateMutable<Type> = {
  -readonly [Property in keyof Type]: Type[Property];
};

// Removes 'optional' attributes from a type's properties
type Concrete<Type> = {
  [Property in keyof Type]-?: Type[Property];
};
```

### `this`

1. 返回类型 `this` 表示调用者的具体实例类型，子类也能保留自己的类型，常用于链式调用。
2. 函数参数列表开头可以写 `this: 类型`，显式约束函数的调用接收者。这个参数在生成 JS 时会被擦除。箭头函数捕获外层 `this`。

```ts
class Counter {
  value = 0;
  increment(): this {
    this.value += 1;
    return this;
  }
}
class Resettable extends Counter {
  reset() { this.value = 0; }
}
new Resettable().increment().reset();

function readValue(this: HTMLInputElement) {
  return this.value;
}
const input = document.createElement('input');
readValue.call(input);
```

### `类型1 extends 类型2 ? 类型3 : 类型4`（条件类型）

若 `类型1` 可赋值给 `类型2`，结果为 `类型3`，否则为 `类型4`。当 `extends` 左侧是单独的泛型类型参数 `T` 时，传入联合类型会分别判断每个成员，再把结果合并。写成 `[T] extends [U]` 可以整体判断。[官方手册：条件类型](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#distributive-conditional-types)

><details>
><summary>比较联合类型逐项判断与整体判断</summary>
>
>```ts
>type Type1 = number | boolean;
>
>type W<T> = T extends Type1 ? "yes" : string;
>
>type W1 = W<number>;                               // -> 'yes'
>type W2 = W<1>;                                    // -> 'yes'
>type W3 = W<W1>;                                   // -> string
>type W4 = W<number | boolean | string>;            // -> 'yes' | string，简化为 string
>
>type OnlyNumbers<T> = T extends number ? T : never;
>type Part = OnlyNumbers<1 | 'x'>;                  // -> 1
>type AllNumbers<T> = [T] extends [number] ? true : false;
>type Whole = AllNumbers<1 | 'x'>;                  // -> false
>
>
>class A {
>  a = 0;
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
    2. `interface` 可扩展具有静态已知成员的对象类型，例如其他接口、类的实例类型或对象类型别名
2. 表示约束的含义

    泛型约束`<类型名 extends 数据类型>`
3. 在条件类型中判断可赋值性

    条件类型`类型1 extends 类型2 ? 类型3 : 类型4`（可以有`infer`）
</details>

### `infer`

`infer` 在条件类型的 `extends` 匹配模式中声明待推断的类型变量。匹配成功时，可在 `?` 分支引用它。

><details>
><summary>推断函数参数和数组元素的类型</summary>
>
>```ts
>// 整句表示为：若`T`能赋值给 `(arg: infer P) => unknown`，则结果是`(arg: infer P) => unknown`类型中的参数`P`，否则返回为`T`
>type ParamType<T> = T extends (arg: infer P) => unknown ? P : T;
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
>```ts
>// 获取数组的项值类型
>type ElementOfArray<ArrayType extends readonly unknown[]> = ArrayType extends readonly (infer ElementType)[] ? ElementType : never;
>```
></details>

### `...`展开类型

在元组类型中，`...` 可以展开数组或元组类型，也可以和 `infer` 配合匹配元组的开头或末尾。

1. 元组

    ```ts
    type A = [number, ...string[]]  // 元组第一项是number，后面项是string（后面可为空）

    const a: A = [1, 's']
    const b: A = [1]
    ```
2. 元组 + 类型变量/泛型变量

    ```ts
    type MyConcat<T extends readonly unknown[], U extends readonly unknown[]> = [...T, ...U]

    type result = MyConcat<[1, 2], [3, 4]>  // -> [1, 2, 3, 4]
    ```
3. 元组 + 类型变量/泛型变量 + `infer`

    ```ts
    // 匹配已知非空的元组，支持 as const 推断的只读元组
    type FirstOfArray<T extends readonly unknown[]> = T extends readonly [infer L, ...unknown[]] ? L : never
    type result1 = FirstOfArray<[1, 2, 3]>   // -> 1


    // 匹配元组尾项。普通数组可能为空，无法保证有尾项
    type LastOfArray<T extends readonly unknown[]> = T extends readonly [...unknown[], infer R] ? R : never
    type result2 = LastOfArray<[1, 2, 3]>   // -> 3
    ```

### `///`（三斜线指令，triple-slash directives）

三斜线指令写在文件顶部，前面可以有注释或其他三斜线指令。出现在语句或声明之后时，它只是普通注释。

| 指令 | 用途 |
| --- | --- |
| `/// <reference path="./globals.d.ts" />` | 按路径纳入另一个文件，常见于旧式全局声明 |
| `/// <reference types="node" />` | 引用已安装的类型包，例如 `@types/node` |
| `/// <reference lib="es2018.promise" />` | 引入指定的内置库声明，例如 `Promise.prototype.finally` |

普通源码之间的依赖用 `import` 表达。阅读旧代码时还可能遇到 `amd-module`、`amd-dependency` 和 `no-default-lib`。TypeScript 7.0 已移除 AMD 模块输出；项目需要选择环境声明时，可在 `tsconfig.json` 中设置 `lib`。[三斜线指令](https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html) · [TypeScript 7.0 发布说明](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

### `namespace`（命名空间）

命名空间可以嵌套，同一作用域内同名的命名空间可以合并。只有导出的成员才能用 `命名空间.成员` 访问。下面的 `format` 会使 `Labels` 生成运行时对象，`type Id` 和函数参数上的注解会被擦除。

```ts
namespace Labels {
  export type Id = number;
  const prefix = "item";
  export function format(id: Id) {
    return `${prefix}-${id}`;
  }
}

Labels.format(3); // "item-3"
// Labels.prefix; // 类型错误，prefix 仅在命名空间内部可见
```

#### 命名空间和模块的区别

脚本里的顶层命名空间可以成为全局名字。模块里的命名空间只在本模块中可见，其他文件需要通过导出、导入访问它。维护全局脚本或为已有全局库写声明时会遇到 `namespace`；前端应用通常用 ES 模块组织文件和依赖，需要按需加载时使用动态 `import()`。[命名空间与模块](https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html)

### 模块化

包含顶层 `import` 或 `export` 的文件具有模块作用域，`export {}` 也可以显式标记模块。其余文件的判定还取决于 `moduleDetection`、模块模式和文件后缀等因素。例如，`"moduleDetection": "force"` 会把所有非声明源文件视为模块。脚本文件的顶层声明可能与项目中的其他全局声明重名。[模块](https://www.typescriptlang.org/docs/handbook/2/modules.html) · [moduleDetection](https://www.typescriptlang.org/tsconfig/moduleDetection.html)

* **区分值导入和类型导入。** `import type` 和 `export type` 只服务于类型检查，整个语句都会被擦除。`class` 同时声明了类型和值：仅用作类型时可写 `import type`，执行 `new` 或 `instanceof` 时需要导入运行时的类。

```ts
// user.ts
export interface User { id: number }
export const guest: User = { id: 0 };
```

```ts
// main.ts，与 user.ts 同目录
import { guest, type User } from "./user.js";

const current: User = guest; // 生成的 JS 保留 guest 导入
console.log(current.id);
```

* **按实际加载代码的工具选择配置。** 浏览器应用由打包器处理导入时，可用 `module: "ESNext"` 与 `moduleResolution: "Bundler"`。直接由 Node.js 加载 `tsc` 输出时，可让 `module` 和 `moduleResolution` 都使用 `"NodeNext"`，并用 `package.json` 的 `"type": "module"` 或 `.mts` 标识 ESM。原生 Node ESM 的相对导入需要扩展名：上例的 `./user.js` 是输出路径，TypeScript 做类型检查时可解析到 `user.ts`。实际运行时由宿主解析导入，`paths` 也不会自动改写输出路径。[模块解析与扩展名替换](https://www.typescriptlang.org/docs/handbook/modules/reference.html#file-extension-substitution) · [按宿主选择编译选项](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html)

* **维护 CommonJS 时对照库的实际导出。** 现有库可能通过 `module.exports = value` 导出整个值，声明文件可用 `export = value` 描述这种形状。TypeScript 的对应导入写法是 `import value = require("包名")`。给未声明的库补上准确的声明，可以保留参数检查和编辑器提示。[CommonJS 与 ES 模块互操作](https://www.typescriptlang.org/docs/handbook/modules/appendices/esm-cjs-interop.html)

### `名字.d.ts`（声明文件）

声明文件描述运行环境或 JavaScript 库**已经提供**的 API。它可以描述类型，也可以声明可用的变量、函数、类或枚举；加载这份声明不会创建任何运行时对象。[声明文件入门](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)

| 需要描述的内容 | 写法 |
| --- | --- |
| 全局值 | `declare const BUILD_ID: string`；可重新赋值的绑定可用 `declare let` |
| 全局函数 | `declare function render(id: string): void`；有多个调用签名时可写重载 |
| 类与枚举 | `declare class Player { play(): void }`、`declare enum Mode { Read, Write }` |
| 接口与别名 | `interface Options { debug?: boolean }`、`type Id = string` |
| 带成员的全局对象 | `declare namespace SDK { function init(): void }` |
| 自己的模块 | 在声明文件顶层用 `export` 描述实际导出的类型和值 |

**给已有的浏览器全局对象补类型。** 假设页面上的另一个脚本可能会设置 `window.buildId`，模块形式的 `.d.ts` 中可以使用 `declare global` 扩展现有的 `Window` 接口。可选属性提醒调用方处理脚本未设置值的情况。

```ts
// globals.d.ts
export {};

declare global {
  interface Window {
    buildId?: string;
  }
}
```

若 `.d.ts` 本身是全局脚本，也可以直接在顶层写 `interface Window { buildId?: string }`。两种写法都要求声明文件已被当前项目纳入，例如放在 `include` 包含的 `src/` 下。[全局扩充](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#global-augmentation)

**描述模块或静态资源。** 下面假设打包器将 JPG 的默认导出处理成 URL 字符串。在一个按脚本处理、没有顶层导入导出的 `.d.ts` 中，可以这样描述这一约定：

```ts
// assets.d.ts
declare module "*.jpg" {
  const url: string;
  export default url;
}
```

给已有模块补成员时，在模块文件里写 `declare module "包名" { … }` 表示**模块扩充**。两种写法的含义受所在文件作用域影响。声明只负责类型，静态资源仍需打包器支持相应的加载方式。[环境模块与模块扩充](https://www.typescriptlang.org/docs/handbook/modules/reference.html#ambient-modules)

**查找第三方库及环境的类型。** 先看库是否自带声明，例如包在 `package.json` 中声明 `types` 或经 `exports` 暴露类型。没有自带声明时，可查找匹配的 `@types/包名`。从 TS 6.0 起，`compilerOptions.types` 默认为 `[]`；如果 Node 子项目需要 `process` 等全局声明，应安装 `@types/node` 并将 `"node"` 列入该项目的 `types`。普通模块导入仍按模块解析规则查找对应声明。[发布声明文件](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html) · [TS 6.0 的 types 默认值](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#types-now-defaults-to)

### 协变与逆变

设 `B` 可赋给 `A`，例如 `HTMLButtonElement` 可赋给 `HTMLElement`。比较 `F<B>` 和 `F<A>` 时，保持这个赋值方向称为**协变**，反向称为**逆变**，两个方向均接受称为**双变**，两个方向都不由这个子类型关系保证称为**不变**。

**函数类型。** 在 `strictFunctionTypes` 下，普通函数类型的参数按逆变检查，返回值通常按协变检查。能处理任意元素的函数当然能处理按钮；只会处理按钮的函数，无法承担处理任意元素的职责。方法和构造器声明的参数保留了双变的兼容规则。[严格函数类型](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-6.html#strict-function-types)

```ts
type Handler<T> = (element: T) => void;
const showId: Handler<HTMLElement> = element => console.log(element.id);
const disable: Handler<HTMLButtonElement> = button => { button.disabled = true; };

const onButton: Handler<HTMLButtonElement> = showId;
// @ts-expect-error 普通元素可能没有 disabled 属性
const onElement: Handler<HTMLElement> = disable;

const createElement: () => HTMLElement = () => document.createElement("button");
```

**数组类型。** 即使开启 `strict`，可变的 `B[]` 仍可赋给 `A[]`。两个变量指向同一数组，通过 `A[]` 写入的元素可能缺少 `B` 的成员。只读取元素的函数可以把形参声明为 `readonly A[]`（等同于 `ReadonlyArray<A>`），同时接收可变和只读数组。[只读数组](https://www.typescriptlang.org/docs/handbook/2/objects.html#the-readonlyarray-type)

```ts
class A { a() {} }
class B extends A { b() {} }

const children: B[] = [new B()];
const readOnly: readonly A[] = children;
// readOnly.push(new A()); // 类型错误，readonly A[] 没有 push
const base: A[] = children;
base.push(new A()); // 类型检查通过，写入的是同一个数组
for (const child of children) {
  child.b(); // 第二次迭代会在运行时抛出 TypeError
}
```

### 注释指令

| 指令 | 作用 |
| --- | --- |
| `// @ts-expect-error` | 下一行预期有类型错误。若错误消失，指令自身会报错，适合验证 API 拒绝某种输入 |
| `// @ts-ignore` | 抑制下一行的 TypeScript 诊断，错误消失后也不会提示 |
| `// @ts-check` | 写在 JS 文件顶部，单独启用该文件的类型检查 |
| `// @ts-nocheck` | 写在 JS 或 TS 文件顶部，跳过当前文件的语义检查 |

例如给输入框更新函数写一条负例，以免重构后意外允许传入数字。[TS 3.9 的预期错误指令](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html#-ts-expect-error-comments)

```ts
function setQuery(text: string) { return text.trim(); }
// @ts-expect-error 查询条件只接受字符串
setQuery(42);
```

## 工程实践

### 项目配置与类型检查

下例适用于**由打包器生成 JavaScript 的浏览器应用**。把配置放在项目根目录，将源码放在 `src/`。已有项目先看自己的 `tsconfig.json` 和 TypeScript 版本。

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "verbatimModuleSyntax": true,
    "strict": true,
    "noEmit": true
  },
  "include": ["src"]
}
```

在安装了 TypeScript 的项目中运行以下命令：

```sh
npx tsc --version
npx tsc -p tsconfig.json --noEmit
npx tsc -p tsconfig.json --showConfig
```

* 不指定文件运行 `tsc` 会从当前目录向上查找 `tsconfig.json`。`-p` 接受配置文件或项目目录，不能再与源文件参数混用。TS 6.0 起，在含 `tsconfig.json` 的目录执行 `tsc src/main.ts` 会报 TS5112。确实需要忽略项目配置、单独检查文件时，可用 `tsc --ignoreConfig --strict --noEmit src/main.ts`。[TS 6.0 命令行变更](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#specifying-command-line-files-when-tsconfigjson-exists-is-now-an-error)
* `target` 设置 `tsc` 输出的 JavaScript 语法目标，也会影响默认库的选择。`lib` 显式决定哪些 API 的声明可见：例如 `ES2018.Promise` 声明 `Promise.prototype.finally`，`DOM` 声明 `document`。这些选项都不会为浏览器安装 polyfill。使用打包器输出时，还要在打包器中设置兼容目标。[target](https://www.typescriptlang.org/tsconfig/target.html) · [lib](https://www.typescriptlang.org/tsconfig/lib.html)
* `strict` 开启一组严格检查。可进一步启用 `noUncheckedIndexedAccess`，让不保证存在的下标读取带上 `undefined`；启用 `exactOptionalPropertyTypes` 后，给可选属性显式写入 `undefined` 需要该类型本身允许它。这两项需单独开启。[索引访问检查](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html) · [精确可选属性](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html)
* `noEmit: true` 让 `tsc` 只检查类型，适合已由打包器负责输出的项目。如果让 `tsc` 生成 JavaScript，在普通项目编译中即使出现类型错误也可能生成文件。需要在报错时阻止输出，可设置 `noEmitOnError: true`。[noEmitOnError](https://www.typescriptlang.org/tsconfig/noEmitOnError.html)
* `extends` 复用配置。`references` 声明项目之间的依赖，使 `tsc --build` 能按顺序构建。浏览器项目和 Node 服务可各自选择 `lib`、`types`、模块模式和 `include`。`rootDir` 影响输出目录结构，源文件范围由 `files`、`include` 及依赖关系等决定。[项目引用](https://www.typescriptlang.org/docs/handbook/project-references.html)

```text
my-project/
├── src/                  # 浏览器端代码
├── server/               # 由 Node.js 加载的代码
├── tsconfig.base.json    # 公共选项
├── tsconfig.client.json  # 浏览器项目，include 指向 src/
├── tsconfig.server.json  # 服务端项目，include 指向 server/
└── tsconfig.json         # 只作构建入口时，设置 files: [] 并列出 references
```

在这个多项目结构中，从根目录运行 `npx tsc -b` 才会依次构建引用的项目。只想检查浏览器子项目时可以运行 `npx tsc -p tsconfig.client.json --noEmit`。对仅含 `files: []` 和 `references` 的根配置运行 `tsc -p tsconfig.json` 会漏掉子项目里的错误。

**文件后缀。** `.ts` 用于普通源码，`.tsx` 支持 JSX（同时配置 `jsx`），`.d.ts` 用于声明。`.mts`、`.cts` 可以分别显式标记 ESM、CommonJS，对应声明后缀为 `.d.mts`、`.d.cts`。组件文件可以叫 `UserCard.tsx`。遇到 TS1128（预期声明或语句）时，先检查报错处及前面的括号、JSX 标签和语法；导入路径的大小写应与文件名一致。[JSX](https://www.typescriptlang.org/docs/handbook/jsx.html) · [模块文件格式](https://www.typescriptlang.org/docs/handbook/modules/reference.html#module-format-detection)

### 前端示例：校验接口响应

假设用户头像组件要显示接口返回的昵称。`fetch()` 收到 404 时通常也会返回 `Response`。先用 `response.ok` 检查状态码是否为 200–299，再把 JSON 当作 `unknown`，检查 `name` 后交给组件。这个函数可以接收 `await fetch("/api/me")` 的返回值。[Fetch 标准](https://fetch.spec.whatwg.org/#ok-status) · [类型收窄](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)

```ts
type Profile = { name: string };

async function readProfile(response: Response): Promise<Profile> {
  if (!response.ok) throw new Error(`读取用户资料失败：HTTP ${response.status}`);
  const data: unknown = await response.json();
  if (typeof data !== "object" || data === null ||
      !("name" in data) || typeof data.name !== "string") {
    throw new Error("用户资料缺少字符串字段 name");
  }
  return { name: data.name };
}
```

### 声明的类型空间和值空间

同一条声明可以占据多个空间。比如 `class Player` 在类型位置表示实例，在值位置表示构造函数。`declare class Player` 也允许在值位置引用构造函数，但运行时的构造函数必须由外部实现提供。[声明合并](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#basic-concepts)

| 声明 | 命名空间 | 类型 | 值 |
| --- | :---: | :---: | :---: |
| `class`、`enum` | | ✓ | ✓ |
| `interface`、`type` | | ✓ | |
| `function`、变量 | | | ✓ |
| `namespace` | ✓ | | 含运行时声明或语句时可作值 |

普通枚举会生成运行时对象；`const enum` 的成员在常见的 `tsc` 配置下会内联。判断名字在哪个空间可用，与判断它是否生成 JavaScript，应分开看。

### 采用 TypeScript 的收益与成本

* **收益。** 参数、返回值和联合类型能表达组件或 API 的使用约定；编辑器据此补全、跳转和重构。把类型检查接入 CI，可以在部署前发现遗漏的分支、传错的参数和拼错的属性。
* **成本和边界。** 项目需要维护类型声明及编译配置，复杂类型也会增加阅读和检查成本。来自网络、表单或存储的值仍要在运行时检查，尤其是把 JSON 转为业务对象时。
* **渐进迁移。** 可以用 `allowJs` 将 JS 纳入项目，用 `checkJs` 或单文件的 `// @ts-check` 逐步开展检查。迁到 `.ts` 后，对暂时不确定的输入可先标记为 `unknown`，在实际使用处逐步收窄。[从 JavaScript 迁移](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html)

**延伸阅读**　[TypeScript 入门教程](https://github.com/xcatliu/typescript-tutorial) · [TypeScript 使用手册中文翻译](https://github.com/zhongsp/TypeScript) · [TypeScript Deep Dive 中文版](https://github.com/jkchao/typescript-book-chinese)
