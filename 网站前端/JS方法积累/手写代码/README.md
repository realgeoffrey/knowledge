# JS手写代码

>题目可参考：<https://bigfrontend.dev/zh>。

## 目录
1. 原生代码实现

    1. [手写`Object.create`](#手写objectcreate)
    1. [手写`instanceof`或`Object.prototype.isPrototypeOf`](#手写instanceof或objectprototypeisprototypeof)
    1. [手写`new`](#手写new)
    1. [手写`Promise`、`Promise.prototype.then/catch/finally`](#手写promisepromiseprototypethencatchfinally)
    1. [手写`Promise.resolve/reject/all/any/race/allSettled`](#手写promiseresolverejectallanyraceallsettled)
    1. [手写`Function.prototype.call/apply`](#手写functionprototypecallapply)
    1. [手写`Function.prototype.bind`](#手写functionprototypebind)
    1. [手写`Array.prototype.reduce`](#手写arrayprototypereduce)
    1. [手写`JSON.stringify`](#手写jsonstringify)
1. 功能

    1. [深复制（深拷贝）](#深复制深拷贝)
    1. [柯里化](#柯里化)
    1. [防抖函数、节流函数](#防抖函数节流函数)
    1. [小数加法](#小数加法)
    1. [大数加法](#大数加法)
    1. [`loadScript`（类似webpack实现`import()`的JSONP+缓存）](#loadscript类似webpack实现import的jsonp缓存)
    1. [`loadScript`支持超时重试](#loadscript支持超时重试)
    1. [函数组合compose、pipe](#函数组合composepipe)
1. 模拟实现

    1. [实现Koa的洋葱模型compose](#实现koa的洋葱模型compose)
    1. [实现`memo`](#实现memo)
    1. [实现`EventEmitter`（不返回取消方法）](#实现eventemitter不返回取消方法)
    1. [实现`EventEmitter`（返回取消方法）](#实现eventemitter返回取消方法)
    1. [调度器任务并发（单任务插入）](#调度器任务并发单任务插入)
    1. [调度器任务并发（多任务插入）](#调度器任务并发多任务插入)
    1. [多任务同时执行且按顺序输出结果](#多任务同时执行且按顺序输出结果)
    1. [任务队列链式调用和取消](#任务队列链式调用和取消)
1. 代码题

    1. [解压字符串](#解压字符串)
    1. [HEX转换为RGBA](#hex转换为rgba)
    1. [n从1开始，每个操作可以对n加1或加倍，如果要使n是任意数，最少需要几个操作](#n从1开始每个操作可以对n加1或加倍如果要使n是任意数最少需要几个操作)
    1. [实现`_.get(object, path, [defaultValue])`](#实现_getobject-path-defaultvalue)
    1. [洗牌算法shuffle](#洗牌算法shuffle)
    1. [对角线打印二维数组](#对角线打印二维数组)
    1. [添加千位分隔符](#添加千位分隔符)
    1. [下划线转驼峰](#下划线转驼峰)
    1. [判断同花顺](#判断同花顺)
    1. [模版字符串替换](#模版字符串替换)
    1. [将二维数组两两拼接](#将二维数组两两拼接)
    1. [拆分一维数组](#拆分一维数组)
1. DOM相关

    1. [遍历所有元素](#遍历所有元素)
    1. [DOM转JSON](#dom转json)
1. react自定义Hook

    1. [`useDebounce`（值）](#usedebounce值)
    1. [`useTimeout`](#usetimeout)
    1. [`useScroll`](#usescroll)
    1. [`useClickOutside`](#useclickoutside)
    1. [`useHover`（`useFocus`一样）](#usehoverusefocus一样)
    1. [`useIsFirstRender`](#useisfirstrender)
    1. [`usePrevious`](#useprevious)
    1. [`useUpdateEffect`](#useupdateeffect)
    1. [`useToggle`](#usetoggle)
    1. [`useArray`](#usearray)
    1. [`usePersistCallback`](#usepersistcallback)
    1. [`useCountdown`](#usecountdown)

---
### 手写`Object.create`
```js
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
```js
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
```js
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

```js
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

```js
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

    ```js
    Promise.myResolve = function (value) {
      if (value instanceof Promise) {
        return value;
      }
      return new Promise((resolve) => {
        resolve(value);
      });
    };
    ```
2. `Promise.reject`

    ```js
    Promise.myReject = function (reason) {
      return new Promise((resolve, reject) => {
        reject(reason);
      });
    };
    ```
3. `Promise.all`

    ```js
    Promise.myAll = function (iterable) {
      return new Promise((resolve, reject) => {
        // if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
        //   return reject(new Error("不是可迭代对象"));
        // }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组
        const results = Array.from({length: promises.length}); // 存储所有 Promise 对象的完成信息
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

    ```js
    Promise.myAny = function (iterable) {
      return new Promise((resolve, reject) => {
        // if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
        //   return reject(new Error("不是可迭代对象"));
        // }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组
        const errors = Array.from({length: promises.length}); // 存储所有 Promise 对象的失败信息
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

    ```js
    Promise.myRace = function (iterable) {
      return new Promise((resolve, reject) => {
        // if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
        //   return reject(new Error("不是可迭代对象"));
        // }

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

    ```js
    Promise.myAllSettled = function (iterable) {
      return new Promise((resolve, reject) => {
        // if (iterable === undefined || iterable === null || typeof iterable[Symbol.iterator] !== "function") {
        //   return reject(new Error("不是可迭代对象"));
        // }

        const promises = Array.from(iterable); // 将可迭代对象转换为数组
        const results = Array.from({length:promises.length}); // 存储所有 Promise 对象的完成信息或失败信息
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

    ```js
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

    ```js
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
```js
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

  // 优化：设置原型链，确保通过 new BoundFunction() 创建的实例可以访问原函数的原型上的方法
  // BoundFunction.prototype = Object.create(func.prototype);          // fixme: bind原逻辑是`新函数.prototype === undefined`，这里为了解决new构造函数逻辑，没法设为undefined
  // BoundFunction.prototype.constructor = BoundFunction;

  return BoundFunction;
};
```

### 手写`Array.prototype.reduce`
```javascript
Array.prototype.myReduce = function (callback, current) {
  if (typeof callback !== "function") { throw TypeError("undefined is not a function");}
  if (this.length === 0 && arguments.length === 1) { throw TypeError("Reduce of empty array with no initial value");}

  const arr = this;

  // 第二个参数可选（有第二个参数则多一次执行回调）
  if (current === undefined) {
    current = arr[0];
  } else {
    current = callback(current, arr[0], 0, arr);
  }

  for (let i = 1; i < arr.length; i++) {
    current = callback(current, arr[i], i, arr);
  }

  return current;
};
```

### 手写`JSON.stringify`
```js
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

```js
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

---
### 深复制（深拷贝）
```js
function cloneDeep(obj, weakmap = new WeakMap()) {
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
          newObj[key] = cloneDeep(obj[key], weakmap);   // 递归
        }
      }

      // 处理自有Symbol类型属性名
      const symbolKeys = Object.getOwnPropertySymbols(obj);
      symbolKeys.forEach((key) => {
        newObj[key] = cloneDeep(obj[key], weakmap); // 递归
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

```js
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
console.log(cloneDeep(obj));
// console.log(structuredClone(obj))
```
</details>

### 柯里化
1. 柯里化

    ```js
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

    ```js
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

    ```js
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

### 防抖函数、节流函数
1. 防抖函数

    ```js
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

    ><details>
    ><summary>实现：一段时间内方法1只执行1遍，若再执行则执行方法2</summary>
    >
    >```js
    >function execute2(fn1, fn2, timeout) {
    >  let flag = false;
    >
    >  return function (...args) {
    >    if (!flag) {
    >      fn1.apply(this, args); // 第一次执行的函数
    >      flag = true;
    >      setTimeout(() => {
    >        flag = false;
    >      }, timeout);
    >    } else {
    >      fn2.apply(this, args); // 后续执行的函数
    >    }
    >  };
    >}
    >```
    ></details>
2. 节流函数

    1. 解法一

        ```js
        function throttle(func, wait) {
          let waiting = false;
          let lastArgs = null;

          return function (...args) {
            if (!waiting) {
              func.apply(this, args);
              waiting = true;

              let timeout = () => {
                setTimeout(() => {
                  waiting = false;

                  if (lastArgs) {
                    func.apply(this, lastArgs);
                    waiting = true;

                    lastArgs = null;
                    timeout();
                  }
                }, wait);
              };

              timeout();
            } else {
              lastArgs = args;
            }
          };
        }
        ```
    2. 解法二

        简化：第一次执行，之后需要在跨度时间结束后执行才有效，不记录失效期间的执行。

        ```js
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

### 小数加法
支持符号。微调可实现：减法、乘法。

```js
function decimalSum(...nums) {
  // 获取最大精度
  const precision = Math.max(
    ...nums.map((num) => {
      return getPrecision(num);
    })
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

### 大数加法
><https://bigfrontend.dev/zh/problem/add-BigInt-string>

不支持符号。

```js
function bigIntSum(...nums) {
  const result = [];

  // [12,34,567] -> [['1','2'], ['3','4'], ['5','6','7']]
  const numsArr = nums.map((num) => {
    return String(num).split("");
  });

  let carry = 0; // 进位

  while (
    numsArr.some((numArr) => {    // 还有没有处理完毕的数字
      return numArr.length > 0;
    }) ||
    carry
  ) {
    const sum = numsArr.reduce((pre, numArr) => {
      return pre + Number(numArr.pop() || 0);
    }, carry);

    result.unshift(sum % 10);
    carry = Math.floor(sum / 10);
  }

  return result.join("");
}
```

### `loadScript`（类似webpack实现`import()`的JSONP+缓存）
```js
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
<summary><del><code>loadScript</code>（JSONP+缓存+错误重试、超时重试）</del></summary>

>不能终止 JSONP动态加载的脚本 执行。

```js
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

### `loadScript`支持超时重试
```js
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

### 函数组合compose、pipe
>compose：<https://leetcode.cn/problems/function-composition/description/>；pipe：<https://bigfrontend.dev/zh/problem/what-is-composition-create-a-pipe>。

>compose由后往前执行，pipe由前往后执行，实现逻辑颠倒一下数组顺序即可。第一个函数可传多个参数，之后函数参数是前一个函数返回值。

1. 解法一

    ```js
    function compose(functions) {
      if (functions.length === 0) {
        return (arg) => arg;
      }
      return function (...arg) {
        const firstValue = functions.pop()(...arg);

        return functions.reduceRight((preValue, curFunc) => {
          return curFunc(preValue); // 返回值
        }, firstValue);
      };
    }
    ```
2. 解法二

    ```js
    function compose(functions) {
      if (functions.length === 0) {
        return (arg) => arg;
      }
      return functions.reduceRight((preFunc, curFunc) => {
        return (...arg) => curFunc(preFunc(...arg));    // 返回方法
      });
    }
    ```

---
### 实现Koa的洋葱模型compose
```js
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
    // ②创建指针（用于：保证一个中间件只能调用一次next）
    let index = -1;

    function dispatch(i) {
      // ②处理一个中间件调用多次next（避免破坏洋葱模型）
      if (i <= index) { return Promise.reject(new Error("next() called multiple times"));}
      index = i;

      // ①
      let fn = middlewares[i];

      if (i === middlewares.length) {
        // ③每一次调用compose 且 这个compose最后一个中间件调用next
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

```js
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

### 实现`memo`
><https://bigfrontend.dev/zh/problem/implement-general-memoization-function>

```js
function memo(func, resolver) {
  const cache = new Map();

  return function (...props) {
    const cacheKey = resolver ? resolver(...props) : props.join(",");

    if (cache.has(cacheKey)) {
      return cache.get(cacheKey);
    }
    const value = func.apply(this, props);
    cache.set(cacheKey, value);
    return value;
  };
}
```

### 实现`EventEmitter`（不返回取消方法）
```js
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

    const onceCallback = (...data) => {
      callback(...data);
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
  emit(eventName, ...data) {
    if (!this.events[eventName]) {
      return;
    }

    this.events[eventName].forEach((callback) => callback(...data));
  }
}
```

### 实现`EventEmitter`（返回取消方法）
><https://bigfrontend.dev/zh/problem/create-an-Event-Emitter>

```js
class EventEmitter {
  events = {};

  subscribe(eventName, callback) {
    if (!this.events[eventName]) {
      this.events[eventName] = new Map();
    }

    const key = Symbol();
    this.events[eventName].set(key, callback);

    return {
      release: () => {
        this.events[eventName].delete(key);
      },
    };
  }

  emit(eventName, ...args) {
    if (!this.events[eventName]) {
      return;
    }
    for (const callback of this.events[eventName].values()) {
      callback(...args);
    }
  }
}
```

### 调度器任务并发（单任务插入）
```js
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

1. 解法

    ```js
    class Schedular {
      tasks = []; // 待执行任务队列
      runningCount = 0; // 当前正在运行的任务数

      constructor(maxCount = 2) {
        this.maxCount = maxCount; // 最大并行任务数
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
        while (this.runningCount < this.maxCount && this.tasks.length > 0) {
          this.runningCount++;

          this.tasks.shift()(); // 取出队列中的任务、执行
        }
      }
    }
    ```

### 调度器任务并发（多任务插入）
实现传入`(多个urls, 并行数量max)`，返回Promise实例，值包含每个urls按顺序请求后结果（请求方式无所谓，可以用`fetch`模拟）。

```js
batchFetch([n个url], 10).then((data)=>{ 按顺序n个url的结果 })
```

1. 解法

    ```js
    function batchFetch(urls, max) {
      return new Promise((resolve) => {
        // 正在运行的任务数量
        let runningCount = 0;
        // 任务
        const tasks = [];
        // 结果
        const result = [];

        urls.forEach((url) => {
          tasks.push(async () => {
            // 真正执行任务
            const res = task(1000 * Math.random(), url)

            await res.catch(() => {})

            runningCount--;

            // 执行当前任务后继续尝试执行剩下任务
            run();

            return res
          })
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

    ```js
    const task = (duration, order) => {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          if (Math.random() < 0.5) {
            resolve(order);
            console.log("执行成功", order);
          } else {
            reject(order);
            console.log("执行失败", order);
          }
        }, duration);
      });
    };

    batchFetch(Array.from({ length: 10 }).map((item, index) => index), 2)
      .then((data) => {
        console.log(data, '完成了');
      });
    ```
    </details>

### 多任务同时执行且按顺序输出结果
多任务尽快并行执行，但输出要按照原本调用顺序（意味着后面的任务要等待前面的任务完成后才能输出）。

```js
async function batchTasks(...tasks) {
  const promiseResult = [];

  for (const task of tasks) {
    promiseResult.push(task());
  }

  for (const result of promiseResult) {
    await result
      .then((data) => {
        console.log("完成输出->", data);
      })
      .catch((err) => {
        console.log("失败输出->", err);
      });
  }
}
```

<details>
<summary>使用测试</summary>

```js
// 注意：执行2次才返回Promise
const task = (duration, order) => {
  return function () {
    return new Promise((resolve, reject) => {
      console.log("开始执行：", order);
      setTimeout(() => {
        Math.random() > 0.5 ? resolve(order) : reject(order);
        console.log("执行完成 >", order, "。等待输出");
      }, duration);
    });
  };
};

batchTasks(task(10, 1), task(1000, 2), task(10, 3), task(5000, 4));
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

1. 解法

    ```js
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

    ```js
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

---
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

    ```js
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

    ```js
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

    ```js
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

    ```js
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

    ```js
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

    ```js
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

### 实现`_.get(object, path, [defaultValue])`
><https://bigfrontend.dev/zh/problem/implement-lodash-get>

```js
function get(source, path, defaultValue = undefined) {
  const props = Array.isArray(path)
    ? path
    : path.replaceAll("[", ".").replaceAll("]", "").split(".");

  let result = source;
  for (const key of props) {
    if (Object.hasOwn(result, key)) {
      result = result[key];
    } else {
      return defaultValue;
    }
  }

  return result;
}
```

### 洗牌算法shuffle
```js
function shuffle(arr) {
  for (let i = 0, len = arr.length; i < len; i++) {
    // i位置的数和[i, len-1]位置的数调换，保证每个数在任一位置的概率相同
    const swapIndex = Math.floor(Math.random() * (len - i) + i);

    // 元素交换
    [arr[swapIndex], arr[i]] = [arr[i], arr[swapIndex]];
  }
}
```

### 对角线打印二维数组
><https://blog.csdn.net/qiyei2009/article/details/80295930>

```js
// 从右向左
function rtl(arr) {
  const result = [];

  const row = arr[0].length; // 行长度
  const column = arr.length; // 列长度

  // i、_i：行下标；j：列下标
  for (let i = row - 1; i >= 0; i--) {
    for (let j = 0, _i = i; j <= column - 1 && _i <= row - 1; j++, _i++) {
      result.push(arr[j][_i]);
    }
  }

  // i：行下标；j、_j：列下标
  for (let j = 1; j <= column - 1; j++) {
    for (let i = 0, _j = j; i <= row - 1 && _j <= column - 1; i++, _j++) {
      result.push(arr[_j][i]);
    }
  }

  return result;
}
```

```js
// 从左向右
function ltr(arr) {
  const result = [];

  const row = arr[0].length; // 行长度
  const column = arr.length; // 列长度

  // i、_i：行下标；j：列下标
  for (let i = 0; i <= row - 1; i++) {
    for (let j = 0, _i = i; j <= column - 1 && _i >= 0; j++, _i--) {
      result.push(arr[j][_i]);
    }
  }

  // i：行下标；j、_j：列下标
  for (let j = 1; j <= column - 1; j++) {
    for (let i = row - 1, _j = j; i >= 0 && _j <= column - 1; i--, _j++) {
      result.push(arr[_j][i]);
    }
  }

  return result;
}
```

<details>
<summary>使用测试</summary>

```js
const arr = [
  [1, 2, 3, 4, 5 ],
  [6, 7, 8, 9, 10],
  [11,12,13,14,15]
];

console.log(rtl(arr), [5, 4, 10, 3, 9, 15, 2, 8, 14, 1, 7, 13, 6, 12, 11]);
console.log(ltr(arr), [1, 2, 6, 3, 7, 11, 4, 8, 12, 5, 9, 13, 10, 14, 15]);
```
</details>

>来回变化顺序遍历：[对角线遍历](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#对角线遍历)。

### 添加千位分隔符
><https://bigfrontend.dev/zh/problem/add-comma-to-number>

1. 解法一

    正则匹配替换。

    ```js
    function addComma(num) {
      let str = num.toString();

      // 开头(符号 n个数字)(3个数字)
      const reg = /^(-?\+?\d+)(\d{3})/;

      // 多次匹配
      while (reg.test(str)) {
        str = str.replace(reg, "$1,$2");
      }

      return str;
    }
    ```
2. 解法二

    字符串分割：符号、整数部分、小数部分。

    ```js
    function addComma(num) {
      let numStr = num.toString();

      // 符号
      let symbol = "";
      if (numStr[0] === "-" || numStr[0] === "+") {
        symbol = numStr[0];
        numStr = numStr.slice(1);
      }

      // 小数点后
      let fraction = numStr.split(".")[1] ?? "";
      numStr = numStr.split(".")[0];

      // 整数处理
      let integer = "";
      while (numStr.length > 3) {
        integer = "," + numStr.slice(-3) + integer;
        numStr = numStr.slice(0, numStr.length - 3);
      }
      if (numStr) {
        integer = numStr + integer;
      }

      return symbol + integer + (fraction ? `.${fraction}` : "");
    }
    ```

### 下划线转驼峰
><https://bigfrontend.dev/zh/problem/convert-snake_case-to-camelCase>

连续的下划线`__`，打头的下划线`_a`和结尾的下划线`a_`需要被保留。

1. 解法一

    正则。

    ```js
    function snakeToCamel(str) {
      return str.replaceAll(/([^_])_([^_])/g, (_, before, after) => {
        return before + after.toUpperCase();
      });
    }
    ```
2. 解法二

    ```js
    function snakeToCamel(str) {
      // 第一个字一定不会被处理
      let result = str[0];

      for (let i = 1; i < str.length; i++) {
        if (
          // 不是连续的下划线
          str[i] === "_" &&
          str[i - 1] !== "_" &&
          str[i + 1] !== "_" &&
          // 不是结尾
          i < str.length - 1
        ) {
          result += str[i + 1].toUpperCase();
          i++;
        } else {
          result += str[i];
        }
      }
      return result;
    }
    ```

### 判断同花顺
```js
function isStraightFlush(arr) {
  // 每种花色定义：1~13 14~26 27~39 40~52

  // 判断同花
  for (let i = 1; i < arr.length; i++) {
    if (color(arr[i - 1]) !== color(arr[i])) {
      return false;
    }
  }

  // 判断顺子
  arr.sort((a, b) => a - b);
  const length = arr.length;
  let i = 0;
  if (
    (arr[0] === 1 || arr[0] === 14 || arr[0] === 27 || arr[0] === 40) &&
    (arr[length - 1] === 13 ||
      arr[length - 1] === 26 ||
      arr[length - 1] === 39 ||
      arr[length - 1] === 52)
  ) {
    i = 1; // 跳过第一个，因为已和最后一个位置形成连张
  }
  for (i = i + 1; i < length; i++) {
    if (arr[i - 1] + 1 !== arr[i]) {
      return false;
    }
  }

  return true;
}

function color(num) {
  if (num <= 13) {
    return "color 1";
  } else if (num <= 26) {
    return "color 2";
  } else if (num <= 39) {
    return "color 3";
  } else if (num <= 52) {
    return "color 4";
  }
}
```

### 模版字符串替换
templateReplace("${name} is ${year} year old", { name: "aa", year: 12 }) => aa is 12 year old

```js
function templateReplace(str, obj) {
  return str.replace(/\$\{(.*?)}/g, (_, $1) => {  // *?非贪婪模式
    return obj[$1.trim()] ?? "";    // 若题目要模拟语法，则：eval($1)
  });
}
```

### 将二维数组两两拼接
输入一个二维数组，将其两两拼接，输出一个二维数组

```
例如输入
[[1,2],[3,4],[5,6]]
输出
[[1,3,5],[1,4,5],[1,3,6],[1,4,6],[2,3,5],[2,4,5],[2,3,6],[2,4,6]]
```

1. 解法

    看不懂。

    ```js
    function concatenateArrays(arrays) {
      // 辅助函数，用于对两个数组进行拼接
      function concat(a, b) {
        const result = [];
        for (const x of a) {
          for (const y of b) {
            result.push([x, ...(y instanceof Array ? y : [y])]);
          }
        }
        return result;
      }

      // 递归函数，将数组进行两两拼接
      function helper(start) {
        if (start === arrays.length - 1) {
          return arrays[start];
        }

        return concat(arrays[start], helper(start + 1));
      }

      return helper(0);
    }
    ```

### 拆分一维数组
1. 解法一

    ```js
    /**
     * 分割数组，并以嵌套数组形式返回
     * @param {Array} arr - 数组
     * @param {Number} n - 分割除数
     * @returns {Array} result - 如：[[0, 1, 2], [3, 4, 5], [6]]
     */
    function divideArr(arr, n) {
      let temp = [];
      const result = arr.reduce((pre, current) => {
        temp.push(current);

        if (temp.length >= n) {
          pre.push(temp);
          temp = [];
        }

        return pre;
      }, []);

      if (temp.length !== 0) {
        result.push(temp);
      }

      return result;
    }
    ```
2. 解法二

    ```js
    function divideArr(arr, n) {
      const result = [];
      let temp = [];

      for (let i = 0; i < arr.length; i++) {
        temp.push(arr[i]);

        if (temp.length >= n) {
          result.push(temp);
          temp = [];
        }
      }

      if (temp.length !== 0) {
        result.push(temp);
      }

      return result;
    }
    ```

---
### 遍历所有元素
1. 解法一

    dom.children遍历，队列实现层序遍历

    ><https://bigfrontend.dev/zh/problem/Traverse-DOM-level-by-level>

    ```js
    function flatten(root) {
      if (root === null) { return []; }

      const result = [];

      const queue = [root];
      while (queue.length > 0) {
        const head = queue.shift();
        result.push(head);
        queue.push(...head.children);
      }

      return result;
    }
    ```
2. 解法二

    [`document.createNodeIterator(root[, whatToShow[, filter]])`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createNodeIterator)

    ```js
    function getNode(root) {
      const result = [];

      const it = document.createNodeIterator(root);
      let node = it.nextNode();
      while (node) {
        if (node.tagName) {
          result.push(node);
        }
        node = it.nextNode();
      }
      return result;
    }
    ```

### DOM转JSON
```js
function dom2Json(node) {
  if (!node.tagName) { return; }

  const obj = {};
  obj.tagName = node.tagName.toLowerCase(); // 其他要加什么属性，直接：obj.xx = node.xx
  obj.children = [];
  node.childNodes.forEach((child) => {
    const obj2 = dom2Json(child);
    obj2 && obj.children.push(obj2);
  });
  return obj;
}
```

---
### `useDebounce`（值）
><https://bigfrontend.dev/zh/react/useDebounce>

```ts
import { useEffect, useState } from "react";

export function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(timeoutId);
    };
  }, [value, delay]);

  return debouncedValue;
}
```

### `useTimeout`
><https://bigfrontend.dev/zh/react/usetimeout>

1. reset the timer if delay changes
2. DO NOT reset the timer if only callback changes

```ts
import { useEffect, useRef } from "react";

export function useTimeout(callback: (...props: any[]) => any, delay: number) {
  const callbackRef = useRef(callback);
  callbackRef.current = callback;

  useEffect(() => {
    const id = setTimeout(() => callbackRef.current(), delay);
    return () => clearTimeout(id);
  }, [delay]);
}
```

### `useScroll`
滚动后更新x、y。

```js
import { useEffect, useState } from "react";

export function useScroll(scrollRef) {
  const [pos, setPos] = useState([0, 0]);

  useEffect(() => {
    const dom = scrollRef.current;

    function handleScroll() {
      setPos([dom.scrollLeft, dom.scrollTop]);
    }

    dom?.addEventListener("scroll", handleScroll, false);
    return () => {
      dom?.removeEventListener("scroll", handleScroll, false);
    };
  }, [scrollRef, scrollRef.current]);

  return pos;
}
```

### `useClickOutside`
><https://bigfrontend.dev/zh/react/useclickoutside>

```js
import { useEffect, useRef } from "react";

export function useClickOutside(callback) {
  const ref = useRef(null);

  useEffect(() => {
    const click = ({ target }) => {
      if (target && ref.current && !ref.current.contains(target)) {
        callback();
      }
    };

    document.addEventListener("mousedown", click);

    return () => {
      document.removeEventListener("mousedown", click);
    };
  }, [callback]);   // fixme:依赖项是否改为`[]`

  return ref;
}
```

### `useHover`（`useFocus`一样）
><https://bigfrontend.dev/zh/react/useHover>

```ts
import { Ref, useCallback, useRef, useState } from "react";

export function useHover<T extends HTMLElement>(): [Ref<T>, boolean] {
  const [isHovered, setIsHovered] = useState(false);
  const handleMouseEnter = useCallback(() => setIsHovered(true), []);
  const handleMouseLeave = useCallback(() => setIsHovered(false), []);

  const ref = useRef<T>();
  const callbackRef = useCallback(
    (node: T) => {
      if (ref.current) {
        ref.current.removeEventListener("mouseenter", handleMouseEnter);
        ref.current.removeEventListener("mouseleave", handleMouseLeave);
      }

      ref.current = node;

      if (ref.current) {
        ref.current.addEventListener("mouseenter", handleMouseEnter);
        ref.current.addEventListener("mouseleave", handleMouseLeave);
      }
    },
    [handleMouseEnter, handleMouseLeave]
  );

  return [callbackRef, isHovered];
}
```

<details>
<summary>其他解法</summary>

```ts
import { Ref, useEffect, useRef, useState } from "react";

export function useHover<T extends HTMLElement>(): [ Ref<T | undefined>, boolean] {
  const ref = useRef<T>();
  const [isHovering, setHovering] = useState(false);

  useEffect(() => {
    const element = ref.current;

    const setTrue = () => {
      setHovering(true)
    };
    const setFalse = () => {
      setHovering(false)
    };

    element?.addEventListener("mouseenter", setTrue);
    element?.addEventListener("mouseleave", setFalse);

    return () => {
      // setHovering(false);
      element?.removeEventListener("mouseenter", setTrue);
      element?.removeEventListener("mouseleave", setFalse);
    };
  }, [ref.current]); // 会执行2次：一次初始化ref.current===''、一次引用赋值ref.current===dom，但函数体执行时ref.current大概率都等于dom，因此会有些问题
  return [ref, isHovering];
}
```
</details>

### `useIsFirstRender`
><https://bigfrontend.dev/zh/react/useIsFirstRender>

```ts
import { useEffect, useRef } from "react";

export function useIsFirstRender(): boolean {
  const isFirst = useRef(true);

  useEffect(() => {
    isFirst.current = false;
  }, []);

  return isFirst.current;
}
```

<details>
<summary>其他解法</summary>

```ts
import { useRef } from "react";

export function useIsFirstRender(): boolean {
  const isFirstRender = useRef(true);

  if (isFirstRender.current) {
    isFirstRender.current = false;
    return true;
  }

  return false;
}
```
</details>

### `usePrevious`
><https://bigfrontend.dev/zh/react/usePrevious>

输出浏览器渲染前的值。

```ts
import { useEffect, useRef } from "react";

export function usePrevious<T>(state: T): T | undefined {
  const ref = useRef<T>();

  useEffect(() => {
    ref.current = state;
  });

  return ref.current;
}
```

### `useUpdateEffect`
><https://bigfrontend.dev/zh/react/useUpdateEffect>

实现：与`useEffect`类似，但跳过第一次渲染。

```ts
import { DependencyList, EffectCallback, useEffect, useRef } from "react";

export function useUpdateEffect(effect: EffectCallback, deps?: DependencyList) {
  const isFirstRender = useRef(true);

  const cb = useRef(effect);
  cb.current = effect;

  useEffect(() => {
    let cleanUpCallback: ReturnType<typeof effect>;

    if (!isFirstRender.current) {
      cleanUpCallback = cb.current();
    } else {
      isFirstRender.current = false;
    }

    return () => {
      cleanUpCallback && cleanUpCallback();
    };
  }, deps);
}
```

### `useToggle`
><https://bigfrontend.dev/zh/react/useToggle>

```ts
import { useReducer } from "react";

export function useToggle(isOn?: boolean): [boolean, () => void] {
  const [onState, toggle] = useReducer((state) => !state, !!isOn);

  return [onState, toggle];
}
```

### `useArray`
><https://bigfrontend.dev/zh/react/useArray>

```ts
import { useCallback, useMemo, useState } from "react";

type UseArrayActions<T> = {
  value: T[];
  push: (item: T) => T;
  removeByIndex: (index: number) => void;
};

export function useArray<T>(initialValue: T[]): UseArrayActions<T> {
  const [value, setValue] = useState<T[]>(initialValue);

  const push = useCallback((item: T): T => {
    setValue((prev) => [...prev, item]);
    return item;
  }, []);
  const removeByIndex = useCallback((index: number) => {
    setValue((prev) => {
      const copy = prev.slice();
      copy.splice(index, 1);
      return copy;
    });
  }, []);

  return useMemo(
    () => ({ value, push, removeByIndex }),
    [value, push, removeByIndex]
  );
}
```

### `usePersistCallback`
```ts
import { useCallback, useRef } from "react";

// ①返回一个固定不变化的函数，②调用usePersistCallback传入的回调函数内部的所有变量都是实时的（③不需要依赖项），④回调函数可以引用自己
export function usePersistCallback<T extends (...args: any[]) => any>(rawFunc: T) {
  const func = useRef(rawFunc);
  func.current = rawFunc;

  return useCallback((...args: Parameters<T>):ReturnType<T> => {
    return func.current(...args);
  }, []);
}
```

<details>
<summary>使用测试</summary>

```ts
const func1 = usePersistCallback((a: string, b: number) => {    // func1是固定不变化的变量
  // 可以使用任何变量，每次都会用最新值（不需要依赖项）
  // （最重要的：）这里内部引用`func1()`，每一次调用的变量都用最新值
}); // 方便针对：依赖变量a触发执行的内容，包含除了a之外的变量也必须是当前最新值

func1('', 1)    // 任意位置调用
```
</details>

### `useCountdown`
hook倒计时组件，支持执行倒计时结束的回调，展示成”00:00:00”的格式。

```ts
import { useEffect, useRef, useState } from "react";

export const useCountdown = (
  deadlineTime: number,
  props?: { onComplete?: Function },
) => {
  const { onComplete } = props || {};
  const refOnComplete = useRef(onComplete);
  refOnComplete.current = onComplete;

  const [leftTime, setLeftTime] = useState(deadlineTime - Date.now());

  useEffect(() => {
    let timeoutId = 0;

    function countdown() {
      const leftTime = deadlineTime - Date.now();

      setLeftTime(leftTime < 0 ? 0 : leftTime);

      if (leftTime > 0) {
        timeoutId = window.setTimeout(countdown, 1000);
      } else {
        refOnComplete.current && refOnComplete.current();
      }
    }

    countdown();

    return () => {
      clearInterval(timeoutId);
    };
  }, [deadlineTime]);

  return formatTime(leftTime); // 建议放到渲染层去format
};

function formatTime(ms: number) {
  const hours = Math.floor(ms / (1000 * 60 * 60));
  const minute = Math.floor((ms / (1000 * 60)) % 60);
  const second = Math.round((ms / 1000) % 60);
  return `${hours < 10 ? `0${hours}` : hours}:${minute < 10 ? `0${minute}` : minute}:${second < 10 ? `0${second}` : second}`;
}
```
