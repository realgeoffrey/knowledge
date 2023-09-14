# JS手写代码

## 目录
1. [手写`Object.create`](#手写objectcreate)
1. [手写`instanceof`或`Object.prototype.isPrototypeOf`](#手写instanceof或objectprototypeisprototypeof)
1. [手写`new`](#手写new)
1. [手写`Promise`、`Promise.prototype.then/catch/finally`](#手写promisepromiseprototypethencatchfinally)
1. [手写`Promise.resolve/reject/all/any/race/allSettled`](#手写promiseresolverejectallanyraceallsettled)
1. [手写防抖函数、节流函数](#手写防抖函数节流函数)
1. [手写`Function.prototype.call/apply`](#手写functionprototypecallapply)
1. [手写`Function.prototype.bind`](#手写functionprototypebind)
1. [手写柯里化](#手写柯里化)
1. [手写深复制（深拷贝）](#手写深复制深拷贝)
1. [手写`JSON.stringify`](#手写jsonstringify)
1. [手写小数加法](#手写小数加法)
1. [手写`loadScript`（类似webpack实现`import()`的JSONP+缓存）](#手写loadscript类似webpack实现import的jsonp缓存)
1. [实用方法：任务执行](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#任务执行)

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
  if (typeof obj !== "object" || obj === null) return false;

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
  const obj = Object.create(constructor.prototype);

  // 调用构造函数，并且this绑定到obj上
  const value = constructor.apply(obj, args);

  // 如果构造函数有返回值，并且返回的是对象，就返回value ;否则返回obj
  return value instanceof Object ? value : obj;
  // (typeof value === "object" && value !== null) || typeof value === "function" 等价于 value instanceof Object
}
```

### 手写`Promise`、`Promise.prototype.then/catch/finally`
>todo: 未处理包含then属性的对象

```javascript
class MyPromise {
  // 状态值
  static PENDING = "pending";
  static FULFILLED = "fulfilled";
  static REJECTED = "rejected";

  // 状态
  status = MyPromise.PENDING;
  // 用于存储 Promise 的结果值
  value = null;
  // 用于存储 错误信息
  error = null;
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
        this.error = err;

        // 处理pending时推入的回调
        this.errorCallbacks.forEach((fn) => fn(this.error));
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

        switch (this.status) {
          case MyPromise.FULFILLED: {
            try {
              if (typeof onFulfilled === "function") {
                const res = onFulfilled(this.value);
                fun(res);
              } else {
                resolve(this.value);
              }
            } catch (e) {
              reject(e);
            }
            break;
          }
          case MyPromise.REJECTED: {
            try {
              if (typeof onRejected === "function") {
                const res = onRejected(this.error);
                fun(res);
              } else {
                reject(this.error);
              }
            } catch (e) {
              reject(e);
            }
            break;
          }
          case MyPromise.PENDING: {
            this.successCallbacks.push(() => {
              try {
                if (typeof onFulfilled === "function") {
                  const res = onFulfilled(this.value);
                  fun(res);
                } else {
                  resolve(this.value);
                }
              } catch (e) {
                reject(e);
              }
            });
            this.errorCallbacks.push(() => {
              try {
                if (typeof onRejected === "function") {
                  const res = onRejected(this.error);
                  fun(res);
                } else {
                  reject(this.error);
                }
              } catch (e) {
                reject(e);
              }
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
      const result = context[uniqueKey](...Array.from(args)); // todo: 未处理args参数不是类数组对象的报错
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
  BoundFunction.prototype = Object.create(func.prototype);
  BoundFunction.prototype.constructor = BoundFunction;
  // todo: bind原逻辑是`新函数.prototype === undefined`，这里为了解决new构造函数逻辑，没法设为undefined

  return BoundFunction;
};
```

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
                .map((arg) => arg === placeholder ? remainingArgs.shift() ?? arg : arg)
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
    if (obj instanceof Date) {
      return new Date(obj);
    }

    // 正则
    if (obj instanceof RegExp) {
      return new RegExp(obj.source, obj.flags);
    }

    // 函数
    if (typeof obj === "function") {
      try {
        // 或`return new Function("return " + obj.toString())();`
        return eval(`(${obj.toString()})`); // 不支持：`a={b(){}};`中`a.b`方法（以及后面catch还报错的）
      } catch {
        try {
          // 或`return new Function("return function " + obj.toString())();`
          return eval(`(function ${obj.toString()})`); // 不支持：任何native code方法（包括.bind新创建的函数）
        } catch {
          return obj; // 暂不处理、直接返回：任何native code方法（包括.bind新创建的函数）
        }
      }
    }

    // todo: Set、Map复制（也要考虑键、值都是引用类型的循环引用问题）

    // 处理普通对象或数组
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
  if (typeof data === "string") {
    return `"${data}"`;
  }

  // Number
  if (data !== data) {  // NaN
    return "null";
  }
  if (data === Infinity || data === -Infinity) {
    return "null";
  }
  if (typeof data === "number") {
    return `${data}`;
  }

  // Boolean
  if (typeof data === "boolean") {
    return `${data}`;
  }

  // null
  if (data === null) {
    return "null";
  }

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

### 手写``
```javascript

```
