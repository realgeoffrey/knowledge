# Typescript学习笔记

## 目录
1. [Typescript](#typescript)

---

### [Typescript](https://github.com/microsoft/TypeScript)
>参考：[TypeScript 入门教程](https://github.com/xcatliu/typescript-tutorial)、[TypeScript使用手册](https://github.com/zhongsp/TypeScript)。

TypeScript是JS的一个超集，主要提供了类型系统和对ES6的支持。

1. 配置

    `tsconfig.json`
2. 文件后缀

    `.ts`、`.tsx`（React、`JSX`）
3. 数据类型

    1. 基本数据类型

        1. `boolean`
        2. `number`
        3. `string`
        4. `symbol`
        5. `undefined`
        6. `null`
        >`undefined`和`null`可以赋值给所有类型的变量（除了`never`类型），`undefined`和`null`是所有类型的子类型（除了`never`类型）。
    2. `void`

        1. 仅允许赋值`undefined`或`null`。
        2. 表示没有任何返回值的函数。
    3. `never`

        表示永不存在的值的类型（如：总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型；变量也可能是never类型，当它们被永不为真的类型保护所约束时）。

        >`never`可以赋值给所有类型的变量（包括`undefined`和`null`），`never`是所有类型的子类型。

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

        >未声明类型的被认为是`any`。
    5. `unknown`

        对照于`any`、`unknown`是类型安全的。任何值都可以赋给`unknown`，但是当没有类型断言或基于控制流的类型细化时`unknown`不可以赋值给其它类型，除了它自己和`any`外。 同样地，在`unknown`没有被断言或细化到一个确切类型之前，是不允许在其上进行任何操作的。
    6. `object`或`{}`

        表示非原始类型（除了`boolean`、`number`、`string`、`symbol`、`undefined`、`null`之外的类型）。允许给它赋任意值和访问`Object.prototype`上的属性，但不能调用任意其他方法，即便它真的有这些方法。

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

        1. 用接口定义。

            1. 确定属性（`属性名: 数据类型`），对象不允许多于或少于约定的属性数量（若有任意属性时，则允许多定义属性）。
            2. 可选属性（`属性名?: 数据类型`）。
            3. 只读类型（`readonly 属性名: 数据类型`），创建对象时必须给此属性赋值，并且之后不能修改此属性。

                >作为变量使用用`const`，作为属性使用用`readonly`。
            4. 任意属性（`[任意名: string]: 数据类型`），确定属性、可选属性、只读属性的类型都必须是任意属性的类型的子集。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface Person {
            >  name: string
            >
            >  score?: number
            >
            >  readonly id: number
            >
            >  [x: string]: string | number
            >}
            >
            >let tom: Person = {
            >  name: 'Tom',
            >
            >  id: 1,
            >
            >  xx: 22
            >}
            >
            >tom.id = 2     // 报错，readonly
            >tom.x = 'x'
            >tom.xx = 'xx'
            >tom.xxx = true // 报错，true不是string | number
            >```
            ></details>
        2. `:{ 属性: 数据类型 }`
    8. 数组类型

        1. `数据类型[]`

            >e.g. `let arr: (number | string)[] = [1, '1']`
        2. 泛型`Array<数据类型>`

            >e.g. `let arr: Array<number | string> = [1, '1']`
        3. 用接口定义

            用`任意属性`来定义索引和项。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface NumberArray {
            >  [index: number]: number | string
            >}
            >
            >let arr: NumberArray = [1, '1']
            >```
            ></details>
        4. 元组

            规定`数组`每一项的数据类型：

            1. 直接赋值不能少于或多于约定长度。
            2. 下标赋值或`push`等可以大于规定长度，但要用前面所有数据类型的联合类型。

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
            >```
            ></details>

        >枚举被编译为.js是数组。
    9. 函数类型

        1. 输入的参数、输出的结果都需要设置类型。
        2. 支持：函数声明、函数表达式。
        3. 支持：可选参数、默认参数、剩余参数。
        4. 引用函数传入的参数不允许多于或少于约定的参数数量（若有可选参数、或默认参数、或剩余参数时，则允许少传入参数）。
        5. 函数表达式可用接口定义。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >// 函数声明
        >
        >// 可选参数
        >function sum1 (x: number, y?: number): number {
        >  if (y) {
        >    return x
        >  } else {
        >    return x + y
        >  }
        >}
        >
        >// 默认参数
        >function sum2 (x: number, y: number = 1): number {
        >  return x + y
        >}
        >
        >// 剩余参数
        >function sum3 (x: number, ...items: number[]): number {
        >  return x + items.reduce((a, b) => a + b, 0)
        >}
        >
        >
        >// 函数表达式
        >
        >// 类型推论
        >let mySum1 = function (x: number, y: number): number {
        >  return x + y
        >}
        >
        >// 显式定义（不是类型推论）
        >let mySum2: (x: number, y: number) => number = function (x: number, y: number): number {
        >  return x + y
        >}
        >
        >// 接口
        >interface mySum {
        >  (x: number, y: number): number
        >}
        >let mySum3: mySum
        >mySum3 = function (x, y) {
        >  return x + y
        >}
        >```
        ></details>

        >仅定义、不实现的方法都只有`()`、没有`{}`：`interface 中的方法`、`declare class 中的 方法`、`abstract class 中的 abstract 方法`。
        6. 支持重载、合并

            优先从最前面的函数定义开始匹配，因此若多个函数定义有包含关系，则需优先把精确的定义写在前面。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >function reverse (x: number): number
            >function reverse (x: string): string
            >function reverse (x: number | string): number | string {
            >  if (typeof x === 'number') {
            >    return Number(x.toString().split('').reverse().join(''))
            >  } else if (typeof x === 'string') {
            >    return x.split('').reverse().join('')
            >  }
            >}
            >```
            ></details>
    10. 内置对象类型

        1. 浏览器环境

            [TypeScript核心库的定义文件](https://github.com/Microsoft/TypeScript/tree/master/src/lib)定义了所有浏览器环境需要用到的类型（预置在TypeScript中）。

            1. [ECMAScript标准提供的内置对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects)
            2. 文档对象模型（DOM）、浏览器对象模型（BOM）的内置对象
        - ~~Node.js~~

            Node.js不是内置对象的一部分，需引入第三方声明文件：`npm install @types/node --save-dev`。

    - 联合类型（Union Types）

        `|`

        1. 若未赋值，则只能访问此联合类型的所有类型里共有的属性/方法（不确定联合类型的变量到底是哪个类型）。

            - 类型断言（Type Assertion）：`<数据类型>值` 或 `值 as 数据类型`（在`.tsx`中必须用后一种）

                断言联合类型的变量成为联合类型其中的一种类型（就可以访问此类型的属性/方法）。

                ><details>
                ><summary>e.g.</summary>
                >
                >```typescript
                >function getLength (something: string | number) {
                >  something.toString();       // 访问此联合类型的所有类型里共有的属性/方法
                >  (<string>something).length  // 类型断言
                >  something.length;           // 报错，只能访问此联合类型的所有类型里共有的属性/方法
                >  (<boolean>something).length // 报错，只能断言成一个联合类型中存在的类型
                >}
                >```
                ></details>
        2. 若已赋值，则只能访问类型推论出的某一个类型的属性/方法。
    - 类型推论（Type Inference）

        若没有明确的指定类型，则依照类型推论规则推断出一个类型：

        1. 若声明时有赋值，则推断成此赋值的类型。
        2. 若声明时没赋值，则推断成`any`。
4. 类

    1. 访问修饰符（Access Modifiers）

        规定类的属性/方法的访问权限。

        1. `public`（默认）：公有的，在任何地方都可以被访问。
        2. `private`：私有的，只能在声明的类中访问。（继承和实例化对象不能访问）
        3. `protected`：受保护的，只能在声明的类中、声明的继承子类中访问。（实例化对象不能访问）

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >class Animal {
        >  public constructor (name, age, sex) {
        >    this.name = name
        >    this.age = age
        >    this.sex = sex
        >  }
        >
        >  public name: string
        >  private readonly age: number
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
    2. 抽象类、抽象方法

        `abstract`定义抽象类、抽象方法。

        1. 抽象类不能实例化
        2. 抽象方法**必须**被子类实现

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

        >仅定义、不实现的方法都只有`()`、没有`{}`：`interface 中的方法`、`declare class 中的 方法`、`abstract class 中的 abstract 方法`。
    3. 类实现接口

        `implements`

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >interface Alarm {
        >  alert (number)
        >}
        >
        >interface Light {
        >  lightOn (string): boolean
        >
        >  lightOff? ()
        >}
        >
        >class Car1 implements Light {
        >  lightOn (str) {
        >    console.log('Car1 light on', str)
        >    return true
        >  }
        >
        >  x () {}
        >}
        >
        >class Car2 extends Car1 implements Alarm, Light {
        >  alert (num) {
        >    console.log('Car2 alert', num)
        >  }
        >
        >  lightOn (str) {
        >    console.log('Car2 light on', str)
        >    return true
        >  }
        >
        >  lightOff () {
        >    console.log('Car2 light off')
        >  }
        >
        >  xx () {}
        >}
        >```
        ></details>
    - 支持重载、合并

        1. 类中的属性在合并时会简单的合并到一个类中

            >合并的相同属性的类型必须是相同的。
        2. 类中方法的合并，与函数的合并一样：支持重载、合并。
5. 接口（Interfaces）

    `interface`

    1. 定义`对象`、`数组`、`函数`的形状（Shape：数量和数据类型），还可以定义混合类型（一个对象同时作为函数和对象使用）。

        ><details>
        ><summary>e.g. 混合类型</summary>
        >
        >```typescript
        >interface Counter {
        >  (start: number): string
        >
        >  interval: number
        >
        >  reset (): void
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

    - 接口继承

        `extends`

        1. 接口继承接口

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
            >```
            ></details>
        2. 接口继承类

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >class Point {
            >  x: number
            >  y: number
            >}
            >
            >interface Point3d extends Point {
            >  z: number
            >}
            >
            >let point3d: Point3d = { x: 1, y: 2, z: 3 }
            >```
            ></details>
    - 支持重载、合并

        1. 接口中的属性在合并时会简单的合并到一个接口中

            >合并的相同属性的类型必须是相同的。
        2. 接口中方法的合并，与函数的合并一样：支持重载、合并。
6. `type`

    1. 类型别名

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
    2. 字符串字面量类型

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type EventNames = 'click' | 'scroll' | 'mousemove'
        >function handleEvent(ele: Element, event: EventNames) {
        >    // do something
        >}
        >
        >handleEvent(document.getElementById('hello'), 'scroll')
        >handleEvent(document.getElementById('world'), 'dbclick') // 报错，event 不能为 'dbclick'
        >```
        ></details>
7. 枚举

    用于取值被限定在一定范围内的场景。语义化、限制值的范围（只允许使用已定义的枚举名）。

    >使用枚举类型可以为一组数值赋予友好的名字。

    1. 枚举成员的类型

        枚举名映射到枚举值，枚举值也映射到枚举名。

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
            2. 枚举项可以手动赋值，未手动赋值的枚举项会接着上一个枚举项递增。

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

        与普通枚举的区别是：在编译阶段被删除、不能包含计算成员、若手动赋值则枚举值必须是数字。

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
            >// 被编译为.js
            >var directions = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
            >```
            ></details>
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
            >// 被编译为.js
            >var directions2 = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
            >```
            ></details>
8. 泛型（Generics）

    `<类型名>`

    1. 可以是自定义类型，用任意的非保留关键字
    2. 泛型约束，`<类型名a extends 类型名b>`
    3. 泛型接口
    4. 泛型类
    5. 泛型参数的默认类型，`<类型名 = 数据类型>`
9. 声明文件

    `名字.d.ts`

    >只能定义数据类型，不能定义具体实现，否则报错。

    1. 全局变量的声明文件

        `declare`并没有真的定义一个变量（只是定义了`全局变量/方法/类/枚举/命名空间`的数据类型）、`interface`和`type`也并没有真的定义一个变量：仅仅用于编译时的检查，在编译结果中会被删除。

        1. 声明全局变量：

            `declare var/let/const 变量名: 数据类型`

            >`var/let`可赋值此全局变量；`const`不可赋值此全局变量。
        2. 声明全局方法：

            `declare function 方法名(参数: 数据类型): 数据类型`

            >支持重载、合并。
        3. 声明全局类：

            ```typescript
            declare class 类名 {
              属性名: 数据类型                 // 没有()是属性
              方法名1(参数: 数据类型): 数据类型 // 有()是方法
              方法名2()                       // 有()是方法
            }
            ```
            >仅定义、不实现的方法都只有`()`、没有`{}`：`interface 中的方法`、`declare class 中的 方法`、`abstract class 中的 abstract 方法`。
        4. 声明全局枚举类型：

            ```typescript
            declare enum 变量名 {
              属性名
            }
            ```
        5. 声明全局的接口、类型

            ```typescript
            // 用接口定义（对象、数组、函数、类）
            interface 名字 {
                属性名: 数据类型
            }


            // 类型（类型别名、字符串字面量类型）
            type 属性名 = 数据类型 或 字符串字面量类型
            ```

        >暴露在最外层的`interface`、`type`会作为全局类型作用于整个项目中，应该尽可能少定义全局类型，因此最好将它们方法`namespace`中。

        6. 声明命名空间：

            ```typescript
            declare namespace 变量名 {
                变量和数据类型
            }
            ```

            - 命名空间内可以包括所有类型的声明，也可以包含`namespace`（嵌套）
        - 多种声明可以组合使用（对同一个名字进行多种不同的声明），是**或**的声明关系。
    2. 导出`export`

    - 引入第三方库声明文件（不需任何配置，引入就可声明成功），可搜索：<https://microsoft.github.io/TypeSearch/>
10. `!`

    表示从前面的表达式里移除 ~~`null`~~ 和 ~~`undefined`~~。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >// 配置文件：compilerOptions.strictNullChecks: true
    >let foo: string | undefined
    >
    >foo.length     // 报错， - 'foo' is possibly 'undefined'
    >foo!.length
    >```
    ></details>
11. 其他

    1. 已经定义好的属性的数据类型，除非有重载机制，否则不能在之后赋值的时候再次定义新的数据类型。只能用其他临时变量来定义保存。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >let a: number = 1
        >a: string = String(a)      // 报错
        >let _a: string = String(a)
        >```
        ></details>
