# JS手写代码

## 目录
1. 原生代码实现

    1. [手写`Object.create`](#手写objectcreate)
    1. [手写`instanceof`或`Object.prototype.isPrototypeOf`](#手写instanceof或objectprototypeisprototypeof)
    1. [手写`new`](#手写new)
    1. [手写`Promise`、`Promise.prototype.then/catch/finally`](#手写promisepromiseprototypethencatchfinally)
    1. [手写`Promise.resolve/reject/all/any/race/allSettled`](#手写promiseresolverejectallanyraceallsettled)
    1. [手写`Function.prototype.call/apply`](#手写functionprototypecallapply)
    1. [手写`Function.prototype.bind`](#手写functionprototypebind)
    1. [手写`JSON.stringify`](#手写jsonstringify)
1. 功能

    1. [手写深复制（深拷贝）](#手写深复制深拷贝)
    1. [手写柯里化](#手写柯里化)
    1. [手写防抖函数、节流函数](#手写防抖函数节流函数)
    1. [手写小数加法](#手写小数加法)
    1. [手写`loadScript`（类似webpack实现`import()`的JSONP+缓存）](#手写loadscript类似webpack实现import的jsonp缓存)
    1. [手写`loadScript`支持超时重试](#手写loadscript支持超时重试)
    1. [手写发布订阅模式](#手写发布订阅模式)
1. 模拟实现

    1. [实现一个Koa的洋葱模型](#实现一个koa的洋葱模型)
1. 代码题

    1. [解压字符串](#解压字符串)
    1. [调度器任务并发（单任务插入）](#调度器任务并发单任务插入)
    1. [调度器任务并发（多任务插入）](#调度器任务并发多任务插入)
    1. [任务队列链式调用和取消](#任务队列链式调用和取消)
    1. [HEX转换为RGBA](#hex转换为rgba)
    1. [n从1开始，每个操作可以对n加1或加倍，如果要使n是任意数，最少需要几个操作](#n从1开始每个操作可以对n加1或加倍如果要使n是任意数最少需要几个操作)

---
### 手写`Object.create`
```javascript
function create(proto, propertiesObject) { // 不支持null
  function F() {}

  F.prototype = proto;
  F.prototype.constructor = F;

  const obj = new F();
  propertiesObject && Object.defineProperties(obj, propertiesObject);

  return obj;
}
```

### 手写`instanceof`或`Object.prototype.isPrototypeOf`
```javascript
function myInstanceof(obj, constructor) {
  if (obj === null || (typeof obj !== "object" && typeof obj !== "function")) { return false; }

  // 获得对象原型链（非标准：obj.__proto__）
  let proto = Object.getPrototypeOf(obj);

  // 沿着原型链向上查找，直到找到构造函数的原型或到达原型链的顶部（null）
  while (proto) {
    if (proto === constructor.prototype) {
      return true;
    }
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
```

### 手写`new`
```javascript
function myNew(constructor, ...args) {
  // 创建：原型是传入构造函数的 空对象
  const obj = Object.create(constructor.prototype); // 或：const obj = {}; obj.__proto__ = constructor.prototype;

  // 调用构造函数（obj绑定到this上）
  const value = constructor.apply(obj, args);

  // 若构造函数返回是 对象，则返回；否则返回obj
  return value instanceof Object ? value : obj;
  // (typeof value === "object" && value !== null) || typeof value === "function" 等价于 value instanceof Object
}
```

### 手写`Promise`、`Promise.prototype.then/catch/finally`
>fixme: 未处理包含then属性的对象

```javascript
class MyPromise {
  // 状态值
  static PENDING = "pending";
  static FULFILLED = "fulfilled";
  static REJECTED = "rejected";

  // 状态
  status = MyPromise.PENDING;
  // 用于存储 Promise 的结果值（完成、失败）
  value = null;
  // 用于存储 成功回调函数的队列
  successCallbacks = [];
  // 用于存储 失败回调函数的队列
  errorCallbacks = [];

  constructor(executor) {
    const resolve = (res) => {
      if (this.status === MyPromise.PENDING) {
        this.status = MyPromise.FULFILLED;
        this.value = res;

        // 处理pending时推入的回调
        this.successCallbacks.forEach((fn) => fn(this.value));
      }
    };
    const reject = (err) => {
      if (this.status === MyPromise.PENDING) {
        this.status = MyPromise.REJECTED;
        this.value = err;

        // 处理pending时推入的回调
        this.errorCallbacks.forEach((fn) => fn(this.value));
      }
    };
    try {
      // 执行（传入 执行成功回调函数 和 执行失败回调函数 作为参数）
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  // then 方法，用于注册成功回调函数和失败回调函数
  then(onFulfilled, onRejected) {
    return new MyPromise((resolve, reject) => {
      // 模拟microtask
      setTimeout(() => {
        const fun = (res) => {
          if (res instanceof MyPromise) {
            res.then(resolve, reject);
          } else {
            resolve(res);
          }
        };

        const fulfilledCb = () => {
          try {
            if (typeof onFulfilled === "function") {
              fun(onFulfilled(this.value));
            } else {
              resolve(this.value);
            }
          } catch (e) {
            reject(e);
          }
        };
        const rejectedCb = () => {
          try {
            if (typeof onRejected === "function") {
              fun(onRejected(this.value));
            } else {
              reject(this.value);
            }
          } catch (e) {
            reject(e);
          }
        };

        switch (this.status) {
          case MyPromise.FULFILLED: {
            fulfilledCb();
            break;
          }
          case MyPromise.REJECTED: {
            rejectedCb();
            break;
          }
          case MyPromise.PENDING: {
            this.successCallbacks.push(() => {
              fulfilledCb();
            });
            this.errorCallbacks.push(() => {
              rejectedCb();
            });
            break;
          }
        }
      });
    });
  }

  // catch 方法，用于注册失败回调函数（参考then）
  catch(onRejected) {
    return this.then(null, onRejected);
  }
}
```

<details>
<summary>包含<code>Promise.prototype.finally</code></summary>

```javascript
class MyPromise {
  // 状态值
  static PENDING = "pending";
  static FULFILLED = "fulfilled";
  static REJECTED = "rejected";

  // 状态
  status = MyPromise.PENDING;
  // 用于存储 Promise 的结果值（完成、失败）
  value = null;
  // 用于存储 成功回调函数的队列
  successCallbacks = [];
  // 用于存储 失败回调函数的队列
  errorCallbacks = [];
  // 用于存储 结束回调函数的队列
  endCallbacks = [];

  constructor(executor) {
    const resolve = (res) => {
      if (this.status === MyPromise.PENDING) {
        this.status = MyPromise.FULFILLED;
        this.value = res;

        // 处理pending时推入的回调
        this.successCallbacks.forEach((fn) => fn(this.value));
        this.endCallbacks.forEach((fn) => fn());
      }
    };
    const reject = (err) => {
      if (this.status === MyPromise.PENDING) {
        this.status = MyPromise.REJECTED;
        this.value = err;

        // 处理pending时推入的回调
        this.errorCallbacks.forEach((fn) => fn(this.value));
        this.endCallbacks.forEach((fn) => fn());
      }
    };
    try {
      // 执行（传入 执行成功回调函数 和 执行失败回调函数 作为参数）
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  // then 方法，用于注册成功回调函数和失败回调函数
  then(onFulfilled, onRejected) {
    return new MyPromise((resolve, reject) => {
      // 模拟microtask
      setTimeout(() => {
        const fun = (res) => {
          if (res instanceof MyPromise) {
            res.then(resolve, reject);
          } else {
            resolve(res);
          }
        };

        const fulfilledCb = () => {
          try {
            if (typeof onFulfilled === "function") {
              fun(onFulfilled(this.value));
            } else {
              resolve(this.value);
            }
          } catch (e) {
            reject(e);
          }
        };
        const rejectedCb = () => {
          try {
            if (typeof onRejected === "function") {
              fun(onRejected(this.value));
            } else {
              reject(this.value);
            }
          } catch (e) {
            reject(e);
          }
        };

        switch (this.status) {
          case MyPromise.FULFILLED: {
            fulfilledCb();
            break;
          }
          case MyPromise.REJECTED: {
            rejectedCb();
            break;
          }
          case MyPromise.PENDING: {
            this.successCallbacks.push(() => {
              fulfilledCb();
            });
            this.errorCallbacks.push(() => {
              rejectedCb();
            });
            break;
          }
        }
      });
    });
  }

  // catch 方法，用于注册失败回调函数（参考then）
  catch(onRejected) {
    return this.then(null, onRejected);
  }

  // finally 方法，用于注册结束回调函数
  finally(onReached) {
    return new MyPromise((resolve, reject) => {
      // 模拟microtask
      setTimeout(() => {
        const finallyFun = () => {
          this.status === MyPromise.FULFILLED && resolve(this.value);
          this.status === MyPromise.REJECTED && reject(this.error);
        };

        const fun = (res) => {
          if (res instanceof MyPromise) {
            res.then(finallyFun, reject);
          } else {
            finallyFun();
          }
        };

        switch (this.status) {
          case MyPromise.PENDING: {
            this.endCallbacks.push(() => {
              try {
                if (typeof onReached === "function") {
                  const res = onReached();
                  fun(res);
                } else {
                  finallyFun();
                }
              } catch (e) {
                reject(e);
              }
            });
            break;
          }
          default: {
            try {
              if (typeof onReached === "function") {
                const res = onReached();
                fun(res);
              } else {
                finallyFun();
              }
            } catch (e) {
              reject(e);
            }
            break;
          }
        }
      });
    });
  }
}
```
</details>

### 手写`Promise.resolve/reject/all/any/race/allSettled`
1. `Promise.resolve`

    ```javascript
    Promise.resolve = function (value) {
      if (value instanceof Promise) {
        return value;
      }
      return new Promise((resolve) => {
        resolve(value);
      });
    };
    ```
2. `Promise.reject`

    ```javascript
    Promise.reject = function (reason) {
      return new Promise((resolve, reject) => {
        reject(reason);
      });
    };
    ```
3. `Promise.all`

    ```javascript
    Promise.all = function (iterable) {
      return new Promise((resolve, reject) => {
        if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
          return reject(new Error("不是可迭代对象"));
        }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组
        const results = new Array(promises.length); // 存储所有 Promise 对象的完成信息
        let fulfilledCount = 0;

        if (promises.length === 0) {
          resolve(results);
        }

        promises.forEach((promise, index) => {
          Promise.resolve(promise).then(
            (result) => {
              results[index] = result;
              fulfilledCount++;

              if (fulfilledCount === promises.length) {
                resolve(results); // 所有 Promise 对象都解析时，解析结果数组
              }
            },
            (error) => {
              reject(error); // 任何一个 Promise 对象被拒绝时，立即拒绝并返回原因
            },
          );
        });
      });
    };
    ```
4. `Promise.any`

    ```javascript
    Promise.any = function (iterable) {
      return new Promise((resolve, reject) => {
        if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
          return reject(new Error("不是可迭代对象"));
        }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组
        const errors = new Array(promises.length); // 存储所有 Promise 对象的失败信息
        let rejectedCount = 0;

        if (promises.length === 0) {
          reject(new AggregateError("All promises were rejected"));
        }

        promises.forEach((promise, index) => {
          Promise.resolve(promise).then(
            (result) => {
              resolve(result); // 只要有一个 Promise 解析，立即解析结果
            },
            (error) => {
              errors[index] = error;
              rejectedCount++;

              if (rejectedCount === promises.length) {
                reject(new AggregateError(errors)); // 所有 Promise 对象都被拒绝时，拒绝并返回一个 AggregateError 对象
              }
            },
          );
        });
      });
    };
    ```
5. `Promise.race`

    ```javascript
    Promise.race = function (iterable) {
      return new Promise((resolve, reject) => {
        if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
          return reject(new Error("不是可迭代对象"));
        }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组

        promises.forEach((promise) => {
          Promise.resolve(promise).then(
            (result) => {
              resolve(result); // 只要有一个 Promise 解析，立即解析结果
            },
            (error) => {
              reject(error); // 只要有一个 Promise 被拒绝，立即拒绝并返回原因
            },
          );
        });
      });
    };
    ```
6. `Promise.allSettled`

    ```javascript
    Promise.allSettled = function (iterable) {
      return new Promise((resolve, reject) => {
        if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
          return reject(new Error("不是可迭代对象"));
        }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组
        const results = new Array(promises.length); // 存储所有 Promise 对象的完成信息或失败信息
        let settledCount = 0;

        if (promises.length === 0) {
          resolve([]);
        }

        promises.forEach((promise, index) => {
          Promise.resolve(promise)
            .then(
              (result) => {
                results[index] = { status: "fulfilled", value: result }; // 存储解析的结果
              },
              (err) => {
                results[index] = { status: "rejected", reason: err }; // 存储拒绝的原因
              },
            )
            .finally(() => {
              settledCount++; // 增加已经解析或拒绝的 Promise 对象数量

              if (settledCount === promises.length) {
                resolve(results); // 所有 Promise 对象都解析或拒绝时，解析并返回结果数组
              }
            });
        });
      });
    };
    ```

### 手写`Function.prototype.call/apply`
1. `Function.prototype.call`

    ```javascript
    Function.prototype.myCall = function (context, ...args) {
      context = context || window; // 若传递undefined或null，则使用全局对象window（或globalThis）

      const uniqueKey = Symbol(); // 创建一个唯一的键，用于确保不会覆盖 context 上已有的属性
      context[uniqueKey] = this;
      const result = context[uniqueKey](...args);
      delete context[uniqueKey];

      return result;
    };
    ```
2. `Function.prototype.apply`

    ```javascript
    Function.prototype.myApply = function (context, args) {
      context = context || window; // 若传递undefined或null，则使用全局对象window（或globalThis）

      const uniqueKey = Symbol(); // 创建一个唯一的键，用于确保不会覆盖 context 上已有的属性
      context[uniqueKey] = this;
      const result = context[uniqueKey](...Array.from(args)); // fixme: 未处理args参数不是类数组对象的报错
      delete context[uniqueKey];

      return result;
    };
    ```

### 手写`Function.prototype.bind`
```javascript
Function.prototype.myBind = function (context, ...args) {
  const func = this; // 当前函数

  function BoundFunction(...innerArgs) {
    // new 构造函数的：BoundFunction.prototype在this（实例）的原型链上
    if (this instanceof BoundFunction) {
      // 当作为构造函数调用时，this不绑定，但参数变化效果还在，那么就new原函数+参数变化
      return new func(...args, ...innerArgs);
    } else {
      // 当作为普通函数调用时，绑定上下文并传递参数执行函数
      return func.apply(context, [...args, ...innerArgs]);
    }
  }

  // 设置原型链，确保通过 BoundFunction 创建的实例可以访问原函数的原型上的方法
  BoundFunction.prototype = Object.create(func.prototype);          // fixme: bind原逻辑是`新函数.prototype === undefined`，这里为了解决new构造函数逻辑，没法设为undefined
  BoundFunction.prototype.constructor = BoundFunction;

  return BoundFunction;
};
```

### 手写`JSON.stringify`
```javascript
function stringify(data, weakmap = new WeakMap()) {
  // 处理带toJSON属性
  if (typeof data === "object" && data && typeof data.toJSON === "function") {
    return stringify(data.toJSON(), weakmap);
  }
  if (typeof data === "bigint") {
    if (typeof BigInt.prototype.toJSON === "function") {
      return stringify(data.toJSON(), weakmap);
    }
    throw new Error("Do not know how to serialize a BigInt at JSON.stringify");
  }

  // String
  if (typeof data === "string") { return `"${data}"`; }

  // Number
  if (data !== data) { return "null"; }  // NaN
  if (data === Infinity || data === -Infinity) { return "null"; }
  if (typeof data === "number") { return `${data}`; }

  // Boolean
  if (typeof data === "boolean") { return `${data}`; }

  // null
  if (data === null) { return "null"; }

  // 处理普通对象或数组
  if (!weakmap.has(data)) {
    if (Array.isArray(data)) {
      const newData = [];
      weakmap.set(data, newData);

      for (const value of data) {
        // 若在数组中，则返回null
        if(value === undefined || typeof value === "symbol" || typeof value === "function"){
          newData.push('null');
        }else{
          newData.push(stringify(value, weakmap));
        }
      }

      return `[${newData.join(",")}]`;
    }
    if (typeof data === "object") {
      const newData = [];
      weakmap.set(data, newData);

      Object.entries(data).reduce((acc, [key, value]) => {
        // 若在对象中，则需要删除
        if (value === undefined || typeof value === "symbol" || typeof value === "function") {
          return acc;
        }

        acc.push(`"${key}":${stringify(value, weakmap)}`);
        return acc;
      }, newData);
      return `{${newData.join(",")}}`;
    }
  } else {
    throw new Error("Converting circular structure to JSON");
    // 或：
    // if(Array.isArray(data)){
    //   return `[${weakmap.get(data)}]`
    // }
    // return `{${weakmap.get(data)}}`
  }
}
```

<details>
<summary>使用测试</summary>

```javascript
/* 使用测试 */
/* 使用测试 */
function l2() {}
var l3 = function () {};
var l4 = () => {};
var obj = {
  a: null,
  b: undefined,
  c: false,
  d: 4,
  e: "e",
  f: Symbol("f"),
  g: 7n,
  h: {
    h1: 8,
    h2: Symbol("h2"),
    h3: undefined,
    h4: () => {},
  },
  i: ["i", 9, Symbol("i"), undefined, () => {}],
  j: new Date(),
  k: /^[abcdefghijk]*/gim,
  l: {
    l0: console.log,
    l1: l2.bind(),
    l2: l2,
    l3: l3,
    l4: l4,
    l5: function () {},
    l6() {},
    l7: () => {},
    l8: (_) => "l8",
    l9: (_) => ({}),
    l10: (a) => a,
    l11: (a) => ({ a }),
  },

  m: new Set(["m", 13, ["m", 13]]),
  n: new Map([
    [1, { n: 1 }],
    [{ n: 1 }, 14],
  ]),
};
BigInt.prototype.toJSON = function () {
  return Number(this);
};
// obj.h.h5 = obj;
// obj.i.push(obj)

console.log(JSON.stringify(obj));
console.log(stringify(obj));
```
</details>

### 手写深复制（深拷贝）
```javascript
function deepClone(obj, weakmap = new WeakMap()) {
  // 基本数据类型：`Undefined`、`Null`、`Boolean`、`Number`、`String`、`Symbol`、`BigInt`
  if (obj === null || (typeof obj !== "object" && typeof obj !== "function")) {
    return obj;
  }
  // 引用数据类型
  else {
    // 日期
    if (obj instanceof Date) { return new Date(obj); }

    // 正则
    if (obj instanceof RegExp) { return new RegExp(obj.source, obj.flags); }

    // 函数
    if (typeof obj === "function") {
      const funcStr = obj.toString();

      try {
        // 或：return new Function("return " + funcStr)();
        return eval("(" + funcStr + ")"); // 不支持：`a={b(){}};`中`a.b`方法（以及后面catch还报错的）
      } catch {
        try {
          // 或：return new Function("return function " + funcStr)();
          return eval("(function " + funcStr + ")"); // 不支持：任何native code方法（包括.bind新创建的函数）
        } catch {
          return obj; // 暂不处理、直接返回：任何native code方法（包括.bind新创建的函数）
        }
      }
    }

    // fixme: Set、Map复制（也要考虑键、值都是引用类型的循环引用问题）

    // 处理普通对象或数组（对象、数据可以统一处理）
    if (!weakmap.has(obj)) {
      // 数组、对象，递归拷贝每个项或属性
      const newObj = obj instanceof Array ? [] : {};
      weakmap.set(obj, newObj);

      // 处理自有属性
      for (const key in obj) {
        // 不处理原型链
        if (obj.hasOwnProperty(key)) {  // 或：Object.hasOwn(obj, key)
          newObj[key] = deepClone(obj[key], weakmap);   // 递归
        }
      }

      // 处理自有Symbol类型属性名
      const symbolKeys = Object.getOwnPropertySymbols(obj);
      symbolKeys.forEach((key) => {
        newObj[key] = deepClone(obj[key], weakmap); // 递归
      });

      return newObj;
    } else {  // 缓存避免自引用导致死循环
      return weakmap.get(obj);
    }
  }
}
```

<details>
<summary>使用测试</summary>

```javascript
/* 使用测试 */
function l2() {}
var l3 = function () {};
var l4 = () => {};
var obj = {
  a: null,
  b: undefined,
  c: false,
  d: 4,
  e: "e",
  f: Symbol("f"), // structuredClone不支持
  g: 7n,
  h: { h: 8 },
  i: ["i", 9],
  j: new Date(),
  k: /^[abcdefghijk]*/gim,
  l: {
    // structuredClone不支持
    l0: console.log,
    l1: l2.bind(),
    l2: l2,
    l3: l3,
    l4: l4,
    l5: function () {},
    l6() {},
    l7: () => {},
    l8: (_) => "l8",
    l9: _ => ({}),
    l10: (a) => a,
    l11: (a) => ({ a }),
  },

  m: new Set(["m", 13, ['m', 13]]),
  n: new Map([
    [1, { n: 1 }],
    [{ n: 1 }, 14],
  ]),
};
obj.h.h2 = obj;

console.log(obj);
console.log(deepClone(obj));
// console.log(structuredClone(obj))
```
</details>

### 手写柯里化
1. 柯里化

    ```javascript
    function curry(fn) {
      return function curried(...args) {
        // 实参个数达到原函数的形参个数，则直接执行原函数
        if (args.length >= fn.length) { // 注意：fn.length的形参计算规则（针对默认值的参数之前，不包含剩余参数，形参的解构仅算一个参数数量）
          return fn.apply(this, args);
        }
        // 否则返回一个新的函数，继续接收剩余的参数
        else {
          return function (...remainingArgs) {
            return curried.apply(this, [...args, ...remainingArgs]);
          };
        }
      };
    }
    ```
2. 支持占位符的柯里化

    ```javascript
    // 支持占位符
    function curry(fn, placeholder = curry.placeholder) {
      return function curried(...args) {
        // 实参个数达到原函数的形参个数 && 都不是占位符，则直接执行原函数
        if (args.length >= fn.length && args.slice(0, fn.length).every((arg) => arg !== placeholder)) {
          return fn.apply(this, args);
        }
        // 否则返回一个新的函数，继续接收剩余的参数
        else {
          return function (...remainingArgs) {
            return curried.apply(
              this,
              args
                .map((arg) => arg === placeholder ? remainingArgs.shift() ?? arg : arg) // 若之前参数有占位符，则从之后参数替换填上（不管之后参数是不是占位符，若之后参数还是占位符则再下一次调用会处理）
                .concat(remainingArgs)
            );
          };
        }
      };
    }

    curry.placeholder = Symbol("_"); // 定义占位符
    ```

    <details>
    <summary>使用测试</summary>

    ```javascript
    /* 使用测试 */
    const _ = curry.placeholder;

    const fn = curry(function (a, b, c, d, e) {
      return [a, b, c, d, e];
    });

    // 验证 输出全部都是 [1, 2, 3, 4, 5]
    console.log(fn(1, 2, 3, 4, 5, _, _));
    console.log(fn(1, 2, 3, 4, 5));
    console.log(fn(_, 2, 3, 4, 5)(1));
    console.log(fn(1, _, 3, 4, 5)(2));
    console.log(fn(1, 2, 3, 4, 5));
    console.log(fn(1, 2, 3, _, 5)(4));
    console.log(fn(1, _, 3)(_, 4)(2)(5));
    console.log(fn(_, 2)(_, _, 4)(1)(3)(5));
    console.log(fn(_, 2)(_, 3, _, _)(1)(4)(5));
    console.log(fn(1, 2, _, _)(3)(4)(5));
    console.log(fn(1, _, _)(_, 3)(2)(4)(5));
    console.log(fn(1, 2)(3, 4, 5));
    console.log(fn(_, _)(_, _, 3, 4, 5)(1, 2));
    console.log(fn(_, _)(_, _, 3, 4, 5, _, _, _)(1, 2));
    console.log(fn(_, 2, 3, 4, 5)()(1, _, _, _, 6, _, 7));
    ```
    </details>

### 手写防抖函数、节流函数
1. 防抖函数

    ```javascript
    function debounce(func, delay) {
      let timeoutId;

      return function (...args) {
        clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
          func.apply(this, args);
        }, delay);
      };
    }
    ```
2. 节流函数

    ```javascript
    function throttle(fn, delay) {
      let lastTime = 0;

      return function (...arg) {
        let nowTime = Date.now();
        if (nowTime - lastTime >= delay) {
          fn.apply(this, arg);
          lastTime = nowTime;
        }
      };
    }
    ```

### 手写小数加法
```javascript
function decimalSum(...nums) {
  // 获取最大精度
  const precision = Math.max(
    ...nums.map((num) => {
      return getPrecision(num);
    }),
  );

  return (
    nums.reduce((before, num) => {
      return before + num * Math.pow(10, precision);
    }, 0) / Math.pow(10, precision)
  );
}

// 获取小数的精度
function getPrecision(num) {
  const decimalPart = String(num).split(".")[1];
  return decimalPart ? decimalPart.length : 0;
}
```

### 手写`loadScript`（类似webpack实现`import()`的JSONP+缓存）
```javascript
// 缓存已加载的脚本（以[加载地址src, Promise实例]存储）
const loadedScripts = new Map();

function loadScript(src) {
  // 如果已经加载过，则直接返回缓存的Promise
  if (loadedScripts.has(src)) {
    return loadedScripts.get(src);
  }

  // 创建一个新的Promise
  const promise = new Promise((resolve, reject) => {
    // JSONP
    const script = document.createElement("script");
    script.src = src;

    // 当脚本加载成功时，解析Promise
    script.onload = () => {
      resolve(script);
    };

    // 当脚本加载失败时，拒绝Promise
    script.onerror = () => {
      reject(new Error(`加载脚本失败: ${src}`));
    };

    document.head.append(script);
  });

  // 将Promise存储到缓存中
  loadedScripts.set(src, promise);
  return promise;
}
```

<details>
<summary><del>手写<code>loadScript</code>（JSONP+缓存+错误重试、超时重试）</del></summary>

>不能终止 JSONP动态加载的脚本 执行。

```javascript
// 缓存已加载的脚本（以[加载地址src, Promise实例]存储）
const loadedScripts = new Map();

function loadScript(src, reTryTimes = 5, timeout = 1000) {
  // 如果已经加载过，则直接返回缓存的Promise
  if (loadedScripts.has(src)) {
    return loadedScripts.get(src);
  }

  // 创建一个新的Promise
  const promise = new Promise((resolve, reject) => {
    let jsonp = new Jsonp(reTryTimes, timeout);

    // 创建一个可取消的jsonp（参数：重试次数, 超时时间）
    function Jsonp(times, ms) {
      let timeoutId;
      // 超时重试（假设，超时之后脚本不会执行 或 执行多次无副作用，因为动态加载的<script>不能被外界终止）
      if (times > 0 && ms > 0) {
        timeoutId = setTimeout(() => {
          jsonp.cancel();
          jsonp = new Jsonp(times - 1, ms); // 或传超时间：0（仅支持超时一次）
        }, timeout);
      }

      const now = Date.now();

      // JSONP
      let script = document.createElement("script");
      script.src = src;

      // 当脚本加载成功时
      script.onload = () => {
        clearTimeout(timeoutId);
        resolve(script);
      };

      // 当脚本加载失败时
      script.onerror = () => {
        clearTimeout(timeoutId);
        // 错误重试：若 能重试 && 在超时时间内，则重试
        if (times > 0 && Date.now() - now < ms) {
          jsonp.cancel();
          jsonp = new Jsonp(times - 1, ms); // 或传剩余时间：Date.now() - now
        } else {
          reject(new Error(`加载脚本失败: ${src}`));
        }
      };

      document.head.append(script);

      return {
        cancel: () => {
          script.onload = script.onerror = null;
          document.head.removeChild(script); // 或：script.remove()
          script = null;
        },
      };
    }
  });

  // 将Promise存储到缓存中
  loadedScripts.set(src, promise);
  return promise;
}
```
</details>

### 手写`loadScript`支持超时重试
```javascript
const loadScript = async (modulePath, timeoutMs = 10000, retryTimes = 3) => {
  for (let i = 0; i < retryTimes; i++) {
    try {
      return await Promise.race([import(modulePath), timeoutReject(timeoutMs)]);
    } catch (error) {
      console.error(error);
    }
  }
  return Promise.reject("failed");
};

const timeoutReject = (ms) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject("timeout reject!");
    }, ms);
  });
};
```

### 手写发布订阅模式
```javascript
class EventEmitter {
  // 事件名: 回调列表
  events = { /* eventName1: [callback1, ...] */ };

  // 订阅事件
  on(eventName, callback) {
    if (!this.events[eventName]) {
      this.events[eventName] = [];
    }
    this.events[eventName].push(callback);
  }

  // 订阅单次事件
  one(eventName, callback) {
    if (!this.events[eventName]) {
      this.events[eventName] = [];
    }

    const onceCallback = (data) => {
      callback(data);
      this.off(eventName, onceCallback);
    };
    onceCallback.originCallback = callback; // 用于unsubscribe
    this.events[eventName].push(onceCallback);
  }

  // 取消订阅事件
  off(eventName, callback) {
    if (!this.events[eventName]) {
      return;
    }

    if (callback) {
      this.events[eventName] = this.events[eventName].filter((cb) => {
        return !(cb === callback || cb.originCallback === callback);    // .originCallback：one相关
      });
    } else {
      this.events[eventName] = [];
    }
  }

  // 发布事件
  emit(eventName, data) {
    if (!this.events[eventName]) {
      return;
    }

    this.events[eventName].forEach((callback) => callback(data));
  }
}
```

### 实现一个Koa的洋葱模型
```javascript
class Koa {
  middlewares = [];

  use(fn) {
    this.middlewares.push(fn); // 发布订阅，先收集中间件
    return this;
  }

  listen(...args) {
    console.log("启动");
    // require("node:http")
    //   .createServer(() => {
    const fn = compose(this.middlewares); // 组合中间件
    const ctx = {};
    fn(ctx, (ctx, next) => {
      console.log(ctx, "last", next);
      next();
    });
    // })
    // .listen(...args);
  }
}

// 官方实现比较简洁，且处理了所有情况（包括多次调用compose的嵌套情况），无法再优化：https://github.com/koajs/compose/blob/master/index.js
function compose(middlewares) { // 返回一个中间件（可以继续被当做普通中间件使用）
  // if (!Array.isArray(middlewares))
  //   throw new TypeError("Middleware stack must be an array!");
  // for (const fn of middlewares) {
  //   if (typeof fn !== "function")
  //     throw new TypeError("Middleware must be composed of functions!");
  // }

  return function (context, lastNext) {
    // 创建指针（用于：保证一个中间件只能调用一次next）
    let index = -1;

    function dispatch(i) {
      // ②处理一个中间件调用多次next（避免破坏洋葱模型）
      if (i <= index) { return Promise.reject(new Error("next() called multiple times"));}
      index = i;

      let fn = middlewares[i];

      // ③兼容（单次调用compose产生的）最后一个中间件继续调用next时
      if (i === middlewares.length) {
        fn = lastNext;
      }
      if (!fn) {
        // ④（所有中间件中）最后一个中间件回调不存在 或 最后一个中间件继续调用next后的函数执行，会导致fn为假
        return Promise.resolve();
      }
      try {
        // ①每个中间件调用next时，就是调用下一个中间件（把下一个中间件的方法体替换掉上一个中间件的next函数）
        return Promise.resolve(fn(context, dispatch.bind(null, i + 1)));
      } catch (err) {
        return Promise.reject(err);
      }
    }

    // 执行第一个中间件
    return dispatch(0);
  };
}
```

<details>
<summary>使用测试</summary>

```javascript
/* 使用测试 */
const app = new Koa();

function sleep(ms) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, ms);
  });
}

// 按照①②③④⑤⑥执行后输出

app.use(async (ctx, next) => {
  console.log("①", ctx);
  ctx.a1 = "a1";
  await next();
  console.log("⑥", ctx);
  ctx.a6 = "a6";
});

app.use(async (ctx, next) => {
  await sleep(1000);
  console.log("②", ctx);
  ctx.a2 = "a2";
  return next().then(async () => {
    await sleep(1000);
    console.log("⑤", ctx);
    ctx.a5 = "a5";
  });
});

app.use((ctx, next) => {
  console.log("③", ctx);
  ctx.a3 = "a3";
  return next();
});

app.use(async (ctx, next) => {
  await sleep(1000);
  console.log("④", ctx);
  ctx.a4 = "a4";
});

app.use(async (ctx, next) => {
  // 前一个中间件没有执行`next`，因此后面的中间件不再被执行
  console.log("无", ctx);
});

app.listen(3001);
```
</details>

### 解压字符串
><https://bigfrontend.dev/zh/problem/uncompress-string>

给定一个压缩过后的字符串，请恢复其原始状态。

```
uncompress('3(ab)') // 'ababab'
uncompress('3(ab2(c))') // 'abccabccabcc'
```

- 数字 `k` 之后如果有一对括号，意味着括号内的子字符串在原来的状态中重复了k次。`k`是正整数。
- 测试用例的输入均为有效字符串，原始字符串中不存在数字

1. 解法一

    栈保存嵌套的部分（有先进后出就用栈）。

    ```javascript
    function uncompress(str) {
      // 遇见 "(" 就入栈，遇见 ")" 就出栈，栈可以解决嵌套问题
      const stack = [];

      let currentStr = "";
      let repeatTimes = 0;

      for (let char of str) {
        // 解析数字
        if (char >= "0" && char <= "9") {
          repeatTimes = repeatTimes * 10 + Number(char);
        }
        // 将当前的字符串和数字分别入栈，并重置当前的数字和字符串
        else if (char === "(") {
          stack.push([currentStr, repeatTimes]);
          currentStr = "";
          repeatTimes = 0;
        }
        // 出栈，获取之前保存的数字和字符串
        else if (char === ")") {
          let [prevStr, prevRepeatTimes] = stack.pop();

          // 将重复的字符串追加到之前的字符串后面
          currentStr = prevStr + currentStr.repeat(prevRepeatTimes);
        }
        // 普通字符，追加到当前字符串后面
        else {
          currentStr += char;
        }
      }

      return currentStr;
    }
    ```
2. 解法二

    正则匹配，递归处理非嵌套的部分。

    ```javascript
    function uncompress(str) {
      // 仅解决非嵌套的
      const result = str.replace(
        /(\d+)\((\D*?)\)/gi, // 仅匹配所有："数字(字母)"。注意：需要`*?`惰性匹配，否则会匹配到后面非配对的内容
        (_, multiplier, subString) => {
          return subString.repeat(multiplier);
        },
      );

      // 解决了非嵌套的之后，产生新的非嵌套内容，递归再次尝试正则匹配
      return result.includes("(") ? uncompress(result) : result;
    }
    ```

### 调度器任务并发（单任务插入）
```javascript
// 请实现一个调度器，这个调度器保证任务的并发数为2
class Schedular {
  // add返回一个promise，add的promise根据task()的promise状态改变
  add (task) {}
}

const task = (duration, order) => {
  return function () {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(order);
      }, duration);
    });
  };
};

// 开始测试
const schedular = new Schedular();
schedular.add(task(100, 1)).then(res => console.log(res));
schedular.add(task(500, 2)).then(res => console.log(res));
schedular.add(task(300, 3)).then(res => console.log(res));
schedular.add(task(50, 4)).then(res => console.log(res));
// 结果应该为1, 3, 4, 2
```

1. 解法一

    ```javascript
    class Schedular {
      tasks = []; // 待执行任务队列
      runningCount = 0; // 当前正在运行的任务数

      constructor(maxRunningCount = 2) {
        this.maxRunningCount = maxRunningCount; // 最大并行任务数
      }

      add(task) {
        return new Promise((resolve) => {
          this.tasks.push(async () => {
            // 真正执行任务
            resolve(await task());
            this.runningCount--;

            // 执行当前任务后继续尝试执行剩下任务
            this.schedule();
          });

          // 启动执行
          this.schedule();
        });
      }

      schedule() {
        while (this.runningCount < this.maxRunningCount && this.tasks.length > 0) {
          this.runningCount++;

          this.tasks.shift()(); // 取出队列中的任务、执行
        }
      }
    }
    ```

### 调度器任务并发（多任务插入）
实现传入`(多个urls, 并行数量max)`，返回Promise实例，值包含每个urls按顺序请求后结果（请求方式无所谓，可以用`fetch`模拟）。

```javascript
batchFetch([n个url], 10).then((data)=>{ 按顺序n个url的结果 })
```

1. 解法一

    ```javascript
    function batchFetch(urls, max) {
      return new Promise((resolve) => {
        // 正在运行的任务数量
        let runningCount = 0;
        // 任务
        const tasks = [];
        // 结果
        const result = [];

        urls.forEach((url) => {
          tasks.push(() => {
            return new Promise(async (resolve) => {
              // 真正执行任务
              resolve(await task(1000 * Math.random(), url)());
              runningCount--;

              // 执行当前任务后继续尝试执行剩下任务
              run();
            });
          });
        });

        function run() {
          while (tasks.length > 0 && runningCount < max) {
            runningCount++;

            const promise = tasks.shift()(); // 取出队列中的任务、执行
            result.push(promise);
          }

          // 完成条件
          if (result.length === urls.length) {
            resolve(Promise.allSettled(result));
          }
        }

        // 启动执行
        run();
      });
    }
    ```

    <details>
    <summary>使用测试</summary>

    ```javascript
    /* 使用测试 */
    // 注意：执行2次才返回Promise
    const task = (duration, order) => {
      return function () {
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve(order);
            console.log("执行完毕", order);
          }, duration);
        });
      };
    };
    batchFetch(Array.from({ length: 100 }).map((item, index) => index), 10,)
      .then((data) => {
        console.log('完成了', data);
      });
    ```
    </details>

### 任务队列链式调用和取消
任务队列，可以链式调用、可以取消前一个任务。

```
// 实现一个 arrange 函数,可以进行时间和工作调度
// [ > ... ] 表示调用函数后的打印内容
// arrange('William').execute();
// > William is notified

// arrange('William').do('commit').execute();
// > William is notified
// > Start to commit

// arrange('William').wait(5).do('commit').execute();
// > William is notified
// 等待 5 秒
// > Start to commit

// arrange('William').waitFirst(5).do('push').execute();
// 等待 5 秒
// > William is notified
// > Start to push
```

1. 解法一：

    ```javascript
    class Task {
      taskQueue = []; // 存放执行队列
      timeoutId = 0; // 保证链式调用在最后一个调用后才真的执行（否则会一插入就执行，无法通过execute控制）

      // 执行所有队列（async-await）
      execute() {
        clearTimeout(this.timeoutId);
        this.timeoutId = setTimeout(async () => {
          while (this.taskQueue.length > 0) {
            await this.taskQueue.shift().func();
          }
        }, 0);

        return this;
      }

      // 下面所有行为，把插入执行队列push改为unshift，就可以插队

      // 普通行为（可被cancel）
      arrange(name = "a name") {
        this.taskQueue.push({
          type: "arrange",
          // msg: name,
          func: () => {
            console.log(`${name} is notified`);
          }
        });

        return this.execute();
      }

      // 普通行为（可被cancel）
      do(sth = "do sth") {
        this.taskQueue.push({
          type: "do",
          // msg: sth,
          func: () => {
            console.log(sth);
          }
        });

        return this.execute();
      }

      // 使后面的链式休眠后再执行（可被cancel）
      wait(ms = 1000) {
        this.taskQueue.push({
          type: "wait",
          // msg: ms,
          func: () => {
            return new Promise((resolve) => {
              console.log(`wait:${ms}ms`);
              setTimeout(() => resolve(), ms);
            });
          }
        });

        return this.execute();
      }

      // 取消之前任意类型任务
      cancel() {
        if (this.taskQueue.length > 0) {
          this.taskQueue.pop();
        }

        return this.execute();
      }
    }
    ```

    <details>
    <summary>使用测试</summary>

    ```javascript
    /* 使用测试 */
    var obj = new Task();
    arrange = obj.arrange.bind(obj);    // obj.arrange()可以直接用，但是为了题目就bind

    // arrange('William')//.execute();  // 已实现，加不加.execute()都一样执行
    // > William is notified

    // arrange('William').do('commit')//.execute();
    // > William is notified
    // > Start to commit

    // arrange('William').wait(1000).do('commit')//.execute();
    // > William is notified
    // 等待 5 秒
    // > Start to commit

    // arrange('William').waitFirst(1000).do('commit')//.execute();
    // 等待 5 秒
    // > William is notified
    // > Start to commit

    // arrange("will")
    //   .wait(500)
    //   .wait(1000)
    //   .cancel()
    //   .cancel()
    //   .do("1好")
    //   .do("2好")
    //   .cancel()
    //   .wait(1500)
    //   .wait(2000)
    //   .do("3好")
    //   .do("4好")
    //   // .execute()
    ```
    </details>

### HEX转换为RGBA
><https://bigfrontend.dev/zh/problem/convert-HEX-color-to-RGBA>

假如你在写一些CSS，需要决定[颜色码](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)。你可以选择16进制表示的#fff 或者 函数格式rgba(255,255,255,1)。

请完成一个函数，将16进制格式的颜色转换为函数格式。

```
hexToRgb('#fff')
// 'rgba(255,255,255,1)'
```

- Alpha 通道的小数部分请限制在最多2位，需要的话请round up。
- 别忘了做参数有效性检测

1. 解法一

    ```javascript
    function hexToRGB(hex) {
      // 三、四、六、八值语法
      if (!/^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{4}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$/.test(hex)) {
        throw new Error("无效的hex");
      }

      // 去除 #
      hex = hex.replace("#", "");

      let r, g, b, a;

      if (hex.length === 3 || hex.length === 4) {
        r = parseInt(hex[0] + hex[0], 16);
        g = parseInt(hex[1] + hex[1], 16);
        b = parseInt(hex[2] + hex[2], 16);
        a = hex[3] === undefined ? 1 : parseInt(hex[3] + hex[3], 16) / 255;
      } else {
        r = parseInt(hex.slice(0, 2), 16);
        g = parseInt(hex.slice(2, 4), 16);
        b = parseInt(hex.slice(4, 6), 16);
        a = hex[7] === undefined ? 1 : parseInt(hex.slice(6, 8), 16) / 255;
      }

      return `rgba(${r},${g},${b},${a})`;
    }
    ```
2. 解法二

    ```javascript
    function hexToRGB(hex) {
      // 三、四、六、八值语法
      if (!/^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{4}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$/.test(hex)) {
        throw new Error("无效的hex");
      }

      // 去除 #
      hex = hex.replace("#", "");

      const [r, g, b, a = 255] = hex
        // 三、四值语法翻倍
        .split("")
        .reduce((acc, current) => `${acc}${hex.length < 6 ? current.repeat(2) : current}`, "",)

        .match(/../g)
        .map((hex) => parseInt(hex, 16));

      return `rgba(${r},${g},${b},${a / 255})`;
    }
    ```

### n从1开始，每个操作可以对n加1或加倍，如果要使n是任意数，最少需要几个操作
><https://www.nowcoder.com/questionTerminal/56983ced1a9547948928c1813d6ba4f0>

1. 解法一

    转化为二进制，1个"0"需要1步，1个"1"需要2步。

    ```javascript
    function minimumStep(n = 1) {
      // 转化为二进制，那么从0b1到0b1xxx，左移1位是x2，+1是+1
      const binary = n.toString(2);
      let zeroCount = 0;
      let oneCount = 0;
      for (let str of binary.slice(1)) {
        if (str === "0") {
          // 多一个0需要1步：+1
          zeroCount++;
        } else {
          // 多一个1需要2步：+1 x2
          oneCount++;
        }
      }

      return zeroCount + oneCount * 2;  // 若题目改成从0开始，则这里额外：+1
    }
    ```
2. 解法二

    动态规划。

    ```javascript
    function minimumStep(n) {
      // dp[i]：到达数量i的最少步骤
      const dp = new Array(n + 1);
      dp[1] = 0;    // 若题目改成从0开始，则这里：dp[1]=1

      for (let i = 2; i <= n; i++) {
        if (i % 2 === 0) {
          dp[i] = Math.min(dp[i - 1] + 1, dp[i / 2] + 1);
        } else {
          dp[i] = dp[i - 1] + 1;
        }
      }

      return dp[n];
    }
    ```
