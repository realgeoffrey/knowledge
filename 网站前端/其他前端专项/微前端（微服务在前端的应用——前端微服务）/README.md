# 微前端（微服务在前端的应用——前端微服务）

## 目录
1. [应用拆分与集成](#应用拆分与集成)

---
### 应用拆分与集成
按业务边界把前端拆成可独立交付的子应用，再在同一产品中组合。主应用管理路由、挂载位置和共享能力，子应用负责自己的业务和生命周期。

[single-spa](https://single-spa.js.org/docs/microfrontends-concept/) 和 [qiankun](https://github.com/umijs/qiankun) 可编排子应用的挂载、卸载。webpack 模块联邦（Module Federation）解决不同构建间的模块加载与共享，可作为集成手段。
