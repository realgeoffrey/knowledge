# JS手写代码

## 目录
1. [手写`Object.create`](#手写objectcreate)
1. [手写`instanceOf`或`Object.prototype.isPrototypeOf`](#手写instanceof或objectprototypeisprototypeof)
1. [手写`new`](#手写new)
1. [手写`Promise`](#手写promise)
1. [手写``](#手写)
1. [手写``](#手写)
1. [手写``](#手写)


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

### 手写`instanceOf`或`Object.prototype.isPrototypeOf`
```javascript
function instanceOf(obj, constructor) {
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
  // (typeof value === 'object' && value !== null) || typeof value === 'function' 等价于 value instanceof Object
}
```

### 手写`Promise`
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

### 手写``
```javascript

```

### 手写``
```javascript

```

### 手写``
```javascript

```

### 手写``
```javascript

```

### 手写``
```javascript

```

### 手写``
```javascript

```

### 手写``
```javascript

```
