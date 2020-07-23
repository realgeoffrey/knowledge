# 服务端相关

## 目录
1. [前端与服务端配合细节](#前端与服务端配合细节)
1. [中间件/拦截器的流程](#中间件拦截器的流程)
1. [服务器日志查看](#服务器日志查看)
1. [接口错误排查](#接口错误排查)
1. [其他](#其他)

    1. [ICE's brother](#ices-brother)

---
### 前端与服务端配合细节
1. 开发方式

    1. 并行（优先）：

        1. 先与服务端对接预期API，服务端产出API文档；
        2. 前端根据文档通过Mock方式开发（或服务端先提供Mock数据的API）；
        3. 当服务端API开发完毕后再用真实API加入前端页面（仅关闭Mock即可）。
    2. 串行：

        服务端比前端提前一个版本，交付的内容包括API+文档。
2. 分页加载、滚动加载

    1. 分页加载，前端用`第几页`+`每页几项`发起请求，服务端（提前）返回`总量`给前端做判断一共有几页。
    2. 滚动加载，用`游标`作为判断下一批请求内容的依据：

        - 分页的游标管理

            1. 普通情况，游标由前端（或客户端）管理

                前端用`游标id`发起请求，服务端返回`新的游标id`给前端作为下一次请求。
            2. 若快速变动的数据（如：推荐信息）、或要根据用户操作而快速改变的数据（如已推送给某用户的不再推送给ta、用户标记不喜欢的相关类型不再推送给ta），则游标由服务端管理。

                服务端用Redis等内存管理方式记录用户的ID，前端只需要每次请求相同的无参数接口就可从服务端返回分页数据。
    >- 若用分页加载的服务端接口实现滚动加载
    >
    >    1. 则可能出现请求到重复数据或略过数据的情况。（游标的，若没有管理好数据流，则也会出现重复数据或略过数据情况）。
    >    2. 前端（或客户端）也可以模拟游标管理方式：暴露一个加载更多的无参数接口，在接口内部实现类似服务端的游标管理。
    >
    >        <details>
    >        <summary>e.g.</summary>
    >
    >        ```javascript
    >        let arr = []    // 数据
    >        const size = 10 // 每页数量
    >        const total = 111 // 总量
    >
    >        function loadMore () {
    >          if (arr.length < total) {
    >            console.log('页数：', Math.ceil(arr.length / size) + 1)
    >            // 页码：Math.ceil(arr.length / size) + 1；每页数量：size
    >            // 用发起异步请求获取数据，数据插入arr
    >            arr = arr.concat(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    >          } else {
    >            // 已经加载所有内容
    >          }
    >          return arr
    >        }
    >
    >        loadMore()  // 加载更多直接调用，不用管理状态
    >        ```
    >        </details>
3. 服务端文档要求

    API文档确定的字段，就算为空，也必须按照文档要求返回` `或`[]`或`{}`，不允许返回内容丢失字段。
4. 扁平化的需要

    不同接口、但类别相同的数据，都按照相同的结构约定数据格式（如：[normalizr](https://github.com/paularmstrong/normalizr)）。

    ><details>
    ><summary>前端可以进行数据扁平化，把不同接口返回的数据都根据类别按照hash的方式存放在各自类别的store，并再保存一份数组记录展示顺序（把数据库的hash保存的方式移植到前端也用hash保存）</summary>
    >
    >e.g. 一个接口返回的数据包括articles、users数据，进行扁平化
    >
    >```javascript
    >// articles的store（内聚）
    >const articles = {}  // articles的store
    >articles.all = {}  // 存放articles的元数据（元数据：完整的单项数据，用唯一的id进行hash索引）
    >articles.hot = {  // 存放articles的hot的展示顺序
    >  sequence: [], // 元数据的id顺序
    >  hasMore: true // 是否继续请求
    >}
    >articles.new = {  // 存放articles的new的展示顺序
    >  sequence: [], // 元数据的id顺序
    >  hasMore: true // 是否继续请求
    >}
    >articles.flattenData = (data) => { // 扁平化数据：把单项数据全部保存在同一个地方
    >  articles.all[data.id] = Object.assign({}, articles.all[data.id], data)
    >}
    >articles.changeSequence = (data) => { // 写入某业务的展示顺序
    >  const list = articles[data.category]
    >
    >  if (data.refresh) {
    >    list.sequence = data.sequence
    >  } else {
    >    list.sequence = list.sequence.concat(data.sequence)
    >  }
    >}
    >
    >
    >// 相同省略：users的store
    >
    >
    >// 请求articles.hot的数据。返回的数据包含多种类别数据（articles、users）
    >function handleData (arr, category) {  // 处理数据
    >  articles.changeSequence({  // 写入hot的展示顺序
    >    category: category,
    >    refresh: false,
    >    sequence: arr.map((data) => {
    >      articles.flattenData(data.articles)   // 把元数据合并至articles
    >      // users.flattenData(data.users)   // 把元数据合并至users
    >
    >      return data.articles.id  // 返回articles的id用于保存顺序
    >    })
    >  })
    >
    >  console.log(category, JSON.parse(JSON.stringify(articles)))  // 打印
    >}
    >
    >// 针对articles.hot的第一次请求
    >const data1 = [
    >  { articles: { id: '1', data: 'articles第一个数据' }, users: { id: 'a', data: 'users第I个数据' } },
    >  { articles: { id: '20', data: 'articles第二个数据' }, users: { id: 'b', data: 'users第II个数据' } },
    >  { articles: { id: '300', data: 'articles第三个数据' }, users: { id: 'c', data: 'users第III个数据' } },
    >  { articles: { id: '4000', data: 'articles第四个数据' }, users: { id: 'd', data: 'users第IV个数据' } }
    >]
    >handleData(data1, 'hot')
    >
    >// 针对articles.hot的第二次请求
    >const data2 = [
    >  { articles: { id: '5000', data: 'articles第五个数据' }, users: { id: 'E', data: 'users第V个数据' } },
    >  { articles: { id: '600', data: 'articles第六个数据' }, users: { id: 'F', data: 'users第VI个数据' } },
    >  { articles: { id: '70', data: 'articles第七个数据' }, users: { id: 'G', data: 'users第VII个数据' } },
    >  { articles: { id: '8', data: 'articles第八个数据' }, users: { id: 'H', data: 'users第VIII个数据' } },
    >  { articles: { id: '1', data: 'articles第一的覆盖内容' }, users: { id: 'a', data: 'users第I个的覆盖内容' } }
    >]
    >handleData(data2, 'hot')
    >
    >// 针对articles.new的第一次请求
    >const data3 = [
    >  { articles: { id: '5000', data: 'articles第五的覆盖内容' }, users: { id: 'E', data: 'users第V的覆盖内容' } },
    >  { articles: { id: '8', data: 'articles第八的覆盖内容' }, users: { id: 'H', data: 'users第VIII的覆盖内容' } },
    >  { articles: { id: '300', data: 'articles第三的覆盖内容' }, users: { id: 'c', data: 'users第III的覆盖内容' } },
    >  { articles: { id: '20', data: 'articles第二的覆盖内容' }, users: { id: 'b', data: 'users第II的覆盖内容' } }
    >]
    >handleData(data3, 'new')
    >
    >console.log('接口获得的数据都进行扁平化处理；在对应类别的store按照id存取数据，再保存一份存放顺序的数组')
    >```
    ></details>
5. 接口请求失败，不能帮用户静默再次请求

    1. 提示用户（针对必要展示的信息）

        让用户认知网络错误（或其他错误）并且给用户操作重新加载的功能（如：跳转到网络出错或404页面）。

        >需要请求数据的应用都需要设计404和网络错误等容错页面。
    2. 静默失败（针对增量加载的信息，如：滚动加载）

        不提示用户失败，当用户再次触发时再次请求（减少用户挫败感）。
6. 不能把服务端返回的（错误）信息直接发送给用户看见，需要转换成用户能看得懂的语言。

    ><details>
    ><summary>也不能把前端错误信息发送给用户。若必须发送给用户错误信息，也需要转换成用户能看得懂的语言。</summary>
    >
    >e.g.
    >
    >```javascript
    >try {
    >  asd
    >} catch (e) {
    >  alert(e)  // 不可以把不经过翻译的错误信息发送给用户
    >}
    >```
    ></details>

### 中间件/拦截器的流程
从上到下，执行中间件，直到抵达路由匹配到的中间件为止，不再继续向下执行（若所有都不匹配，则执行兜底中间件）。

```javascript
// 一个请求路由进入到服务器，通过①②③的流程


// 处理API的 之前+之后 逻辑
app.use(async (ctx, next) => {
  // ① 处理之前逻辑

  await next()  // 执行下一个中间件

  // ③ 处理之后逻辑
})


// 匹配路由则执行，否则跳过
app.use((ctx) => {
  // ②执行业务，不再向后执行其他中间件
})


// 未匹配路由的兜底
app.use((ctx) => {
  // ②返回404之类
})
```

### 服务器日志查看
>可能在物理机、vps、容器（如：Docker、Kubernetes）中查看日志。

1. HTTP Server日志

    1. nginx

        1. `nginx -t`获得配置路径；
        2. 根据配置文件查找日志存放地点（`access_log`、`error_log`）；
        3. 查看日志文件。
2. 服务端应用程序日志

    1. Node.js

        1. pm2

            1. `pm2 list`获得进程列表；
            2. `pm2 info 「进程id或name」`获取进程信息；
            3. `pm2 log 「进程id或name」`查看进程日志。
        2. Docker

            1. `docker ps`获取容器信息；
            2. `docker logs -f --tail 「数字」 「容器ID」`查看Docker日志。
        3. Kubernetes

            1. `kubectl get namespace`查看所有命名空间；
            2. `kubectl get pod -n 「namespace名字」 | grep 「筛选关键字」`查看所有某命名空间的pod；
            3. `kubectl logs 「pod名字」 -n 「namespace名字」 -c 「container名字」 -f --tail 「数字」`查看pod日志。

### 接口错误排查
顺着请求链路排查：域名 -（DNS -> 服务器地址） -> HTTP Server（如：nginx、Apache Tomcat） -> 服务端应用程序（逻辑、IO）。

- 出错维度、链路：

    1. 判断是否发送到指定服务器地址

        如：域名解析、网络问题、本机的hosts/DNS（缓存）。
    2. 已发送到指定服务器地址，查看出错位置的**日志**

        1. HTTP server错误

            如：nginx日志。
        2. 服务端应用程序错误

            如：Node.js、Golang跑的服务端程序日志。
        3. 运维相关问题

            如：磁盘满了、硬盘坏了、数据库出问题、其他各种问题的信息。

1. 前端查错

    1. 跨域或其他浏览器策略问题会显示在控制台报错。
    2. 根据HTTP Response查询

        1. Headers
        2. Body

            1. 根据错误信息去匹配API文档给出的类型错误。
            2. 注意那些nginx标记的错误，说明在nginx层被阻止。

                ><details>
                ><summary>e.g.</summary>
                >
                >```html
                ><html>
                ><head><title>413 Request Entity Too Large</title></head>
                ><body>
                ><center><h1>413 Request Entity Too Large</h1></center>
                ><hr><center>nginx/1.19.0</center>
                ></body>
                ></html>
                >```
                ></details>
2. 服务端查错

    >若有错误信息，则方便直接定位出错点；若没有错误信息，则需要顺着链路查询。

    1. [查看服务器日志](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/服务端相关/README.md#服务器日志查看)
    2. 进入服务器或容器内：

        1. 宿主机`curl`容器监听端口，确认是否能从宿主机进入容器。
        2. 进入容器内，`curl`依赖的API，确认是否宿主机内能正常访问API。
        3. 在宿主机或容器内通用查询：

            1. [查看端口占用、网络链接，查看进程](https://github.com/realgeoffrey/knowledge/blob/master/工具使用/命令行备忘/README.md#查看端口占用网络链接查看进程)
            2. [查看磁盘空间占用](https://github.com/realgeoffrey/knowledge/blob/master/工具使用/命令行备忘/README.md#查看磁盘空间占用)

    - （一些log监控器提示的错误可能会缺失细节信息，）可以去服务器手动执行相同命令现场复现原始错误信息。

        1. gitlab-ci问题可以考虑按钮`Clear Runner Caches`清除缓存。

---
## 其他

### ICE's brother
>闭源。

一种二进制、支持字段动态增加，代码自动生成、跨平台的应用层协议。

1. .jce文件阅读

    1. `module`模块名（命名空间）

        命名空间不能嵌套，可以引用其他命名空间`模块名::struct名`。

        1. `struct`封装数据

            `字段id require/optional 类型 变量名[ = 默认值]`

            - 类型：

                1. 基本类型：

                    `void`、`bool`、`string`、`byte`、`short`、`int`、`double`、`float`、`long`、`unsigned byte`、`unsigned short`、`unsigned int`
                2. 复杂类型：

                    `Enum`枚举、`map<类型, 类型>`字典、`vector<类型>`序列（`vector<byte>`二进制码）、`常量`、`key[struct名, 多个变量名]`
            >任何`struct`、`map`、`vector`都可嵌套。
        2. `interface`暴露接口
