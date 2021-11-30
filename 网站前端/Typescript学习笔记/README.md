# Typescript学习笔记

## 目录
1. [Typescript](#typescript)

    1. [类型](#类型)
    1. [语法](#语法)
    1. [其他](#其他)

---
### [Typescript](https://github.com/microsoft/TypeScript)
>参考：[TypeScript 入门教程](https://github.com/xcatliu/typescript-tutorial)、[TypeScript使用手册](https://github.com/zhongsp/TypeScript)。

TypeScript是JS的一个超集，主要提供了类型系统和对ES6的支持。

#### 类型
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

            >可以赋值给可选参数、可选属性(`?:`)。
        7. `null`

        >1. `undefined`和`null`可以赋值给所有类型的变量（除了`never`类型），`undefined`和`null`是所有类型的子类型（除了`never`类型）。
        >2. 若配置`strictNullChecks`，则：`undefined`只能赋值给类型`any`、`undefined`、`void`，`null`只能赋值给类型`any`、`null`。
    2. `void`

        1. 仅允许被`null`（只在--strictNullChecks未指定时）或`undefined`赋值。
        2. 表示`return null`（只在--strictNullChecks未指定时）、`return undefined`、`return`、没有任何返回值 的函数。

            ><details>
            ><summary>Promise的默认返回可以用<code>void</code>（不能用<del><code>undefined</code></del>）</summary>
            >
            >e.g.
            >
            >```typescript
            >function a (): Promise<void> {  // 只能用void
            >  return new Promise((resolve, reject) => {
            >    resolve();
            >  }).then(() => {
            >
            >  });
            >}
            >
            >
            >function b (): Promise<void> {  // 或 Promise<undefined>
            >  return new Promise((resolve, reject) => {
            >    resolve();
            >  }).then(() => {
            >    return undefined
            >  });
            >}
            >```
            ></details>
    3. `never`

        表示永不存在的值的类型（如：总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型；变量也可能是never类型，当它们被永不为真的类型保护所约束时）。当类型不存在时通常返回`never`（如：`number & string`、`Extract<string | number , boolean>`）。

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

        1. 任何值都可以赋给`unknown`。
        2. 当没有类型断言或基于控制流的类型细化时`unknown`不可以赋值给其它类型，除了它自己和`any`外。
        3. 在`unknown`没有被类型断言或js代码细化到一个确切类型之前，不允许在其上进行任何操作。
        4. `try-catch`抓到的是`unknown`，需要`if (err instanceof Error) {){}`之后使用。
        5. 用`?.`无效。
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
            >  // 描述对象的属性
            >  [x: string]: string | number | boolean // 必须包含：所有其他属性的类型的联合类型（|）
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
            >tom.id = 2   // 报错，readonly
            >tom.x = 'x'
            >tom.xx = 'xx'
            >tom.xxx = 1n // 报错，1n不是string | number | boolean
            >```
            ></details>
        2. `: { 属性: 数据类型, }`

            >`: { [x:string]: any }`等价于`: Record<string, any>`，表示对象类型，比 ~~`: object`~~、~~`: {}`~~ 更严格定义对象类型。
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

                与`Array<数据类型>`相似，只是把所有可变方法去掉了，因此可以确保数组创建后再也不能被修改。

                ><details>
                ><summary>e.g.</summary>
                >
                >```typescript
                >let a: number[] = [1, 2, 3, 4]
                >let ro: ReadonlyArray<number> = a
                >
                >ro[0] = 12      // 报错
                >ro.push(5)      // 报错
                >ro.length = 100 // 报错
                >
                >let b: number[] = ro    // 报错，ReadonlyArray赋值给一个普通数组也是不可以的
                >let c: number[] = ro as number[]  // 允许，类型断言重写
                >let d: ReadonlyArray<number> = ro as number[]  // 允许，类型断言重写
                >```
                ></details>
        3. 用`接口`定义

            用`任意属性`来定义索引和项。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface NumberArray {
            >  [index: number]: number | string // 描述数组
            >}
            >
            >let arr: NumberArray = [1, '1']
            >```
            ></details>
        4. 元组（Tuple）

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

        - 将索引签名设置为只读

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface ReadonlyStringArray {
            >  readonly [index: number]: string;
            >}
            >
            >let myArray: ReadonlyStringArray = ["Alice", "Bob"];
            >myArray[2] = "Mallory"; // error。readonly
            >```
            ></details>

        >枚举被编译为.js是数组。
    9. 函数类型

        1. 输入的参数、输出的结果都需要设置类型。
        2. 支持：函数声明、函数表达式。
        3. 支持：可选参数、默认参数、剩余参数。

            可选参数 和 默认参数 不能同时设置。e.g. 不允许：~~`y?: number = 1`~~。
        4. 引用函数传入的参数不允许多于或少于约定的参数数量（若有可选参数`?`、或默认参数`=`、或剩余参数`...`，则允许少传入参数）。
        5. 函数表达式可用`接口` 或 `对象`定义。
        6. 函数的参数和返回值可以根据`接口`进行类型推论。

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
        >// 接口
        >interface mySum {
        >  // 描述方法
        >  (xx: number, yy: number): string   // 定义的参数名和实现的函数参数名不用一致
        >}
        >let mySum3: mySum  // 显式定义（不是类型推论）
        >mySum3 = function (x, y) { // 类型推论
        >// 或：mySum3 = function (x: number, y: number): string {    // 显式定义（不是类型推论）
        >  return x + y + ''
        >}
        >
        >// 对象
        >function identity<T>(arg: T): T {
        >    return arg;
        >}
        >let myIdentity: {<T>(arg: T): T} = identity;
        >```
        ></details>

        >仅定义、不实现的方法都只有`()`、没有`{}`：`interface 中的方法`、`declare class 中的 方法`、`abstract class 中的 abstract 方法`。

        - 支持重载、合并

            优先从最前面的函数定义开始匹配，因此若多个函数定义有包含关系，则需优先把精确的定义写在前面。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
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
            >```
            ></details>

        - 显示定义

            1. `: 参数类型 => 返回类型`
            2. `: Function`
    10. 内置对象类型

        1. 浏览器环境

            [TypeScript核心库的定义文件](https://github.com/Microsoft/TypeScript/tree/master/src/lib)定义了所有浏览器环境需要用到的类型（预置在TypeScript中）。

            1. [ECMAScript标准提供的内置对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects)
            2. 文档对象模型（DOM）、浏览器对象模型（BOM）的内置对象
        - ~~Node.js~~

            Node.js不是内置对象的一部分，需引入第三方声明文件：`npm install @types/node --save-dev`。
2. 类

    1. 访问修饰符（Access Modifiers）

        规定类的属性/方法的访问权限。

        1. `public`（默认）：公有的，在任何地方都可以被访问。
        2. `private`：私有的，只能在声明的类中访问。（继承和实例化对象不能访问）

            >若 ~~类的构造函数设置为`private`~~，则这个类不能实例化、也不能够被继承。
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

            1. `public`仅可用`public`重载
            2. `private`不可以重载
            3. `protected`仅可用`public`或`protected`重载
    2. `typeof 类名`

        取**类**的类型，而不是~~实例~~的类型，包含类的所有`静态属性/方法`和`构造函数`。

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
        >let greeterMaker: typeof Greeter  // 类（静态属性/方法、构造函数）
        >greeterMaker = Greeter
        >greeterMaker.staticGreeting = 'Hey there'
        >
        >let greeter2: Greeter
        >greeter2 = new greeterMaker()
        >console.log(greeter2.greet(), greeter2.greeting)
        >```
        ></details>
    3. `abstract`

        抽象类、抽象方法。

        1. 抽象类不能实例化
        2. 抽象方法**必须**被子类实现（抽象类自己不能定义自己的抽象方法的实现）

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
    4. `implements`

        类实现接口（仅对类的实例属性/方法进行类型检查、不检查类的静态属性/方法）

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >interface Alarm {
        >  alert(num: number): void;
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
        >    console.log("Car1 light on", str);
        >    return true;
        >  }
        >
        >  x() {}
        >}
        >
        >class Car2 extends Car1 implements Alarm, Light {
        >  alert(num: number) {
        >    console.log("Car2 alert", num);
        >  }
        >
        >  public lightOn(str: string) {    // 可以用 private 吗？
        >    console.log("Car2 light on", str);
        >    return true;
        >  }
        >
        >  lightOff() {
        >    console.log("Car2 light off");
        >  }
        >
        >  protected xx() {}
        >}
        >```
        ></details>

    - 支持重载、合并

        1. 类中的属性在合并时会简单的合并到一个类中

            >合并的相同属性的类型必须是相同的。
        2. 类中方法的合并，与函数的合并一样：支持重载、合并。
3. 接口（Interfaces）

    `interface`

    1. 定义`对象`、`数组`、`函数`的形状（Shape：数量和数据类型）

        - 还可以定义混合类型（一个对象同时作为函数和对象使用）。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >interface Counter {
            >  (start: number): string  // 描述方法
            >
            >  interval: number         // 描述对象的属性
            >
            >  reset (): void           // 描述对象的方法
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

        接口继承

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

    - 支持重载、合并

        同名的interface会自动合并。

        1. 接口中的属性在合并时会简单的合并到一个接口中

            >合并的相同属性的类型必须是相同的。
        2. 接口中方法的合并，与函数的合并一样：支持重载、合并。
        3. 对象可以重载覆盖，但是需要用更多属性的对象，不能用更少属性的对象

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
4. `type`

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
    2. 字面量类型

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
        >
        >```
        ></details>
5. 枚举（Enum）

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

    console.log(E.aa, E.bb, E.cc, E.dd, E.ee); // => 0 123 124 222 223
    console.log(E[E.aa], E[E.bb], E[E.cc], E[E.dd], E[E.ee]); // => "aa" "bb" "cc" "dd" "ee"
    ```
    </details>

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

        与普通枚举的区别是：在编译阶段被删除、不能包含计算所得项、若手动赋值则枚举值必须是数字。

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

    - 遍历枚举类型

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
6. 泛型（Generics）

    `名称<类型名>其他内容`

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

    - 定义 - 赋值

        1. 定义：类型变量/泛型变量（用任意的非保留关键字）
        2. 赋值：传入类型，可以是自定义类型，可以是类型推论
    2. 泛型接口、泛型类型别名（`type`）

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >// 泛型接口
        >interface GenericIdentityFn {
        >    <T>(arg: T): T;
        >}
        >function identity<T>(arg: T): T {
        >    return arg;
        >}
        >let myIdentity: GenericIdentityFn = identity;
        >
        >
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
        >    zeroValue: T;
        >    add: (x: T, y: T) => T;
        >}
        >
        >let myGenericNumber = new GenericNumber<number>();
        >```
        ></details>
    4. 泛型函数

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
        >```
        ></details>

    >没有~~泛型枚举~~和~~泛型命名空间~~。

    5. 泛型参数的默认类型，`<类型名 = 数据类型>`
    6. 泛型约束，`<类型名 extends 数据类型>`

        类型名 需要包含 数据类型。

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
        >loggingIdentity({length: 10, value:3});
        >
        >
        >function getProperty<T, K extends keyof T> (obj: T, key: K) {
        >  return obj[key];
        >}
        >getProperty({ a: 1 }, "a");
        >getProperty({ a: 1 }, "m"); // 报错
        >```
        ></details>
7. 内置类型别名

    >来自：[lib.es5.d.ts](https://github.com/microsoft/TypeScript/blob/master/lib/lib.es5.d.ts#L1455)、[typescript: Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)。

    1. `Partial`

        将类型定义的所有属性都修改为可选（非~~必须~~）。

        >e.g. `Partial<数据类型>`
    2. `Required`

        将类型定义的所有属性都修改为必须（非~~可选~~）。

        >e.g. `Required<数据类型>`
    3. `Readonly`

        将类型定义的所有属性都修改为只读。

        >e.g. `Readonly<数据类型>`
    4. `Record`

        将类型A的所有属性值都映射到类型B上并创造一个新的类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type A = 'dog' | 'cat' | 'fish';
        >interface B {
        >   name:string,
        >   age:number,
        >}
        >
        >type C = Record<A, B>;
        >
        >const c:C = {
        >   dog:{
        >       name:'dogName',
        >       age:2
        >   },
        >   cat:{
        >       name:'catName',
        >       age:3
        >   },
        >   fish:{
        >       name:'fishName',
        >       age:5
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

        去除类型中的某些属性。

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
    7. `Exclude`

        去除联合类型中的一部分。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type a = number | string | boolean
        >type b = Exclude<a, number | boolean>  // string
        >```
        ></details>
    8. `Extract`

        从联合类型A中提取类型B。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type T0 = Extract<'a' | 'b' | 'c', 'a' | 'b'>          // 'a' | 'b'
        >type T1 = Extract<string | boolean, boolean | number>  // boolean
        >type T2 = Extract<string | number , boolean>           // never
        >```
        ></details>
    9. `NonNullable`

        去除联合类型中的`null`和`undefined`。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type T1 = NonNullable<string | null | undefined>;  // string
        >type T2 = NonNullable<null | undefined>;           // never
        >```
        ></details>
    10. `ReturnType`

        获得函数类型的返回类型。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type F1 = () => Date;
        >function F2 ():Date { return new Date() }
        >
        >type F1ReturnType = ReturnType<F1>;        // Date
        >type F2ReturnType = ReturnType<typeof F2>; // Date
        >```
        ></details>
    11. `Parameters`

        获取函数的全部参数类型，以`元组`返回。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type F0 = (a: string, b: number) => boolean;
        >type F1 = Parameters<F0>;                      // [a: string, b: number] 或 [string, number]
        >
        >type F2 = () => boolean;
        >type F3 = Parameters<F2>;                      // []
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
        >type T0 = InstanceType<typeof C>; // C
        >type T1 = C // T0等于T1
        >```
        ></details>
    13. `ConstructorParameters`

        获取构造函数的全部参数类型，以`元组`或数组返回。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >type T0 = ConstructorParameters<ErrorConstructor>;     // [message?: string]
        >type T1 = ConstructorParameters<FunctionConstructor>;  // string[]
        >type T2 = ConstructorParameters<RegExpConstructor>;    // [pattern: string | RegExp, flags?: string]
        >type T3 = ConstructorParameters<any>;                  // unknown[]
        >type T4 = ConstructorParameters<Function>;             // never。报错
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

#### 语法
- 类型推论（Type Inference）

    若没有明确的指定类型，则依照类型推论规则推断出一个类型：

    1. 若声明时有赋值，则推断成此赋值的类型。
    2. 若声明时没赋值，则推断成`any`。

- 类型断言（Type Assertion）：

    `<数据类型>变量名` 或 `变量名 as 数据类型`

    >若JSX中使用`<数据类型>变量名`断言语法时，则与JSX的语法存在歧义（如：`let foo = <string>bar;</string>`），因此在`.tsx`中必须用`变量名 as 数据类型`的断言语法。

    - 可以绕过检查

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
        >let a:A = {};
        >let b:B = a as B;  // 不报错
        >```
        ></details>

    1. const断言（const assertions）

        `as const`或`<const>`：该表达式中的字面类型不应被扩展（如：不能从`"hello"`转换为string），对象字面量获取只读属性，数组文字成为只读元组。

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >const x1 = 'x1';        // -> 'x1'
        >let x2 = 'x2';          // -> string
        >let x3 = 'x3' as const; // -> 'x3'
        >
        >const obj1 = { key: 'value' }           // -> { type: string }
        >const obj2 = { key: 'value' } as const  // -> { readonly key: 'value' }
        >
        >const arr1 = [1,2,3]            // -> number[]
        >const arr2 = [1,2,3] as const   // -> readonly [1,2,3]
        >```
        ></details>

- 联合类型（Union Types）

    `|`

    1. 若未赋值，则只能访问此联合类型的所有类型里共有的属性/方法（不确定联合类型的变量到底是哪个类型）。

        - 类型断言 或 js逻辑判断 联合类型的变量成为联合类型其中的某一种类型，就可以访问此类型的属性/方法。

            ><details>
            ><summary>e.g.</summary>
            >
            >```typescript
            >function getLength(something: string | number) {
            >  something.toString(); // 访问此联合类型的所有类型里共有的属性/方法
            >  (something as string).length; // 类型断言
            >  (<number>something).toFixed(); // 类型断言
            >  if (typeof something === 'string') {
            >    something.length;  // js逻辑判断
            >  }
            >
            >  something.length; // 报错，只能访问此联合类型的所有类型里共有的属性/方法
            >  (<boolean>something).length; // 报错，只能类型断言成一个联合类型中存在的类型
            >}
            >```
            ></details>
    2. 若已赋值，则只能访问类型推论出的某一个类型的属性/方法。

    - 可辨识联合（Discriminated Unions）

    >第一个值前面也可以添加`|`（主要为了格式化美观）。e.g. `type a = | number | string;`

- 交叉类型（Intersection Types）

    `&`

    将多个类型合并为一个类型。

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

- `!`

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
    >
    >
    >function func (x:undefined | string) :string{
    >  return x!
    >}
    >```
    ></details>

- `typeof`

    >也保留js中的含义，但优先使用ts的语义。

    获取一个变量的声明类型（若不存在，则获取该类型的推论类型）。

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
    >type A3 = typeof a; // -> a的类型（也就是A的实例类型）
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
    ></details>

- `keyof`（输入索引类型查询）

    获取某种**类型**的所有公共键（属性名），以联合类型（`|`）返回。

    ><details>
    ><summary>e.g.</summary>
    >
    >```typescript
    >interface Person {
    >  name: string;
    >  age: number;
    >  location?: string;
    >}
    >
    >type K1 = keyof Person;                  // -> "name" | "age" | "location"
    >type K2 = keyof Person[];                // -> number | "length" | "push" | "pop" | "concat" | ...
    >type K3 = keyof { [x: string]: Person }; // -> string | number （隐式转换key为number）
    >```
    ></details>

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

- 索引访问类型`[键名]`

    在语法上，它们看起来像属性或元素访问，但最终会被转换为类型。

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

- `in`

    类型的属性通过`in`遍历获得。

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

- 装饰器（Decorators）

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

- `readonly`

    属性标记为只读。

    1. 方法的形参
    2. 对象（`: { 属性: 数据类型, }`）、类、interface、type 的属性

        >与访问修饰符同时使用时要放在其后面。

- `new`

    构造函数相关。

- `this`

    1. 返回类型`this`

        定义函数的返回值是`this`。
    2. 参数`this`

        >`this`参数是个假的参数，它出现在参数列表的最前面。

        定义函数中`this`的类型。

- `类型1 extends 类型2 ? 类型3 : 类型4`

    >`extends`可用于：interface去继承另一个interface或类，泛型约束。

    有条件类型：若 类型1可以赋值给类型2 （或？ 类型1是类型2的扩展），则返回类型 类型3，否则返回 类型4。

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

- `infer`

    在条件类型语句中, 可以用 infer 声明一个类型变量并且对它进行使用，我们可以用它获取函数的返回类型。

- 类型守卫（Type Guards）

    一些表达式，它们会在运行时检查以确保在某个作用域里的类型。

    1. 类型谓词

        定义一个函数，它的返回值是一个`类型谓词`：`参数名 is 类型`。

        ```typescript
        function isFish(pet: Fish | Bird): pet is Fish {
            return (pet as Fish).swim !== undefined;
        }
        ```
    2. `字符串字面量或字符串字面量类型 in 联合类型`

        ><details>
        ><summary>e.g.</summary>
        >
        >```typescript
        >function move(pet: Fish | Bird) {
        >    if ("swim" in pet) {
        >        return pet.swim();
        >    }
        >    return pet.fly();
        >}
        >```
        ></details>
    3. `typeof 变量 !==或=== "number或string或boolean或symbol或bigint"`

        >e.g. `if (typeof x === 'number') {}`
    4. `变量 instanceof 构造函数`

        >e.g. `if(x instanceof Func) {}`

- 声明合并

    编译器将针对同一个名字的多个独立声明合并为单一声明。合并后的声明同时拥有原先多个声明的特性。

- `///`

    三斜线指令：包含单个XML标签的单行注释。注释的内容会做为编译器指令使用。

    >1. 三斜线指令**仅**可放在包含它的文件的最顶端。
    >2. 一个三斜线指令的前面只能出现单行或多行注释，这包括其它的三斜线指令。
    >3. 如果它们出现在一个语句或声明之后，那么它们会被当做普通的单行注释，并且不具有特殊的涵义。

    1. `/// <reference path="..." />`
    2. `/// <reference types="..." />`
    3. `/// <reference no-default-lib="true"/>`
    4. `/// <amd-module />`
    5. `/// <amd-dependency />`

- `namespace`

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
    >  var A2;
    >  (function (A2) {
    >    var B2 = /** @class */ (function () {
    >      function B2() {}
    >      return B2;
    >    })();
    >  })(A2 || (A2 = {}));
    >})(A1 || (A1 = {}));
    >```
    ></details>

- 声明文件

    `名字.d.ts`

    >只能定义数据类型，不能定义具体实现，否则报错。

    1. 全局变量的声明文件

        `declare`并没有真的定义一个变量（只是定义了`全局变量/方法/类/枚举/命名空间`的数据类型）、`interface`和`type`也并没有真的定义一个变量：仅仅用于编译时的检查，在编译结果中会被删除。

        1. 声明全局变量：

            `declare var/let/const 变量名: 数据类型`

            >`var/let`可赋值此全局变量；`const`不可赋值此全局变量。
        2. 声明全局方法：

            `declare function 方法名 (参数: 数据类型): 数据类型`

            >支持重载、合并。
        3. 声明全局类：

            ```typescript
            declare class 类名 {
              属性名: 数据类型                // 没有()是属性
              方法名1(参数: 数据类型): 数据类型  // 有()是方法
              方法名2()                     // 有()是方法
            }
            ```
            >仅定义、不实现的方法都只有`()`、没有`{}`：`interface 中的方法`、`declare class 中的 方法`、`abstract class 中的 abstract 方法`。
        4. 声明全局枚举类型：

            ```typescript
            declare enum 变量名 {
              属性名
            }
            ```
        5. 声明全局的接口、type

            >不需要`declare`关键字

            ```typescript
            interface 名字 {
                属性名: 数据类型
            }


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

    - 引入第三方库声明文件（不需任何配置，引入就可声明成功），可搜索：<https://www.typescriptlang.org/dt/search>

- 模块化

    1. 导出

        任何声明（如：变量、函数、类、类型别名、接口）都能够通过添加`export`关键字来导出。
    2. 引入方式：

        1. 有类型声明

            1. 标准ES6 Module库：

                `import * as xx from 'xx'` 或 `import xx from 'xx'`
            2. 标准CommonJS库：

                `import xx = require('xx')`
        3. 没有类型声明

            `const xx = require('xx')`（默认导入为`any`类型）

    - 特殊：`export =`、`import = require(模块路径)`

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

#### 其他
1. 配置

    [`tsconfig.json`](https://www.staging-typescript.org/tsconfig)

    1. `tsc`（不带任何输入文件）会自动查找命令目录下的`tsconfig.json`；若带输入文件参数，则忽略 ~~`tsconfig.json`~~。
    2. `tsc --init`生成一个`tsconfig.json`文件。
2. 文件后缀

    `.ts`、`.tsx`（React、`JSX`）

    >TypeScript错误`TS1128: Declaration or statement expected.`，可能导致的原因是：tsx文件名命名必须为全小写。
3. ts的声明

    TypeScript中的声明会创建以下三种实体之一：`命名空间`（Namespace），`类型`（Type）、`值`（Value）。

    1. 创建`命名空间`的声明：会新建一个命名空间，它包含了用`.`符号来访问时使用的名字。
    2. 创建`类型`的声明：用声明的模型创建一个类型并绑定到给定的名字上。
    3. 创建`值`的声明：创建在JavaScript输出中看到的值。

    | Declaration Type | Namespace | Type | Value |
    | :--- | :---: | :---: | :---: |
    | Namespace | X |  | X |
    | Class |  | X | X |
    | Enum |  | X | X |
    | Interface |  | X |  |
    | Type Alias |  | X |  |
    | Function |  |  | X |
    | Variable |  |  | X |
4. Tips

    1. 已经定义好的属性的数据类型，除非有重载机制，否则不能在之后赋值时再次定义新的数据类型。只能用其他临时变量来保存。

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
