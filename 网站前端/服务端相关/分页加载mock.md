# 分页加载mock

## 目录
1. []()

---

| 类型                    | 服务                    | 直接可用链接                                                                  | 分页参数                                 | 返回列表字段     | 是否有 total                            | 适配成 `{ total, list }`                                             |
| --------------------- | --------------------- | ----------------------------------------------------------------------- | ------------------------------------ | ---------- | ------------------------------------ | ----------------------------------------------------------------- |
| **skip/limit**        | DummyJSON Users       | `https://dummyjson.com/users?limit=10&skip=0`                           | `limit` 每页数量；`skip` 跳过数量             | `users`    | **有**：`total`                        | `{ total: res.total, list: res.users }`                           |
| **skip/limit + 搜索**   | DummyJSON User Search | `https://dummyjson.com/users/search?q=em&limit=10&skip=0`               | `q` 搜索；`limit`；`skip`                | `users`    | **有**：`total`                        | `{ total: res.total, list: res.users }`                           |
| **offset/limit**      | PokéAPI               | `https://pokeapi.co/api/v2/pokemon?offset=0&limit=10`                   | `offset` 偏移量；`limit` 每页数量            | `results`  | **有**：`count`                        | `{ total: res.count, list: res.results }`                         |
| **page/per_page**     | ReqRes                | `https://reqres.in/api/users?page=1&per_page=6`                         | `page` 页码；`per_page` 每页数量            | `data`     | **有**：`total`                        | `{ total: res.total, list: res.data }`                            |
| **page/per_page**     | GitHub Search         | `https://api.github.com/search/repositories?q=stars:>100000&page=1&per_page=5` | `q` 搜索；`page` 页码；`per_page` 每页数量 | `items`    | **有**：`total_count`                  | `{ total: res.total_count, list: res.items }`                     |
| **page/results**      | Random User           | `https://randomuser.me/api/?page=1&results=10&seed=abc`                 | `page` 页码；`results` 每页数量；`seed` 固定结果 | `results`  | **无真实 total**，只有 `info.page/results` | `{ total: 999, list: res.results }` 需要写死                          |
| **page/limit**        | MockAPI.io AntD 示例    | `https://660d2bd96ddfa2943b33731c.mockapi.io/api/users?page=1&limit=10` | `page` 页码；`limit` 每页数量               | 返回数组本身     | **无**，AntD 示例里 total 写死 100          | `{ total: 100, list: res }`                                       |
| **page/limit + 包装分页** | MockAPI.io 包装版示例      | `https://61273138c2e8920017bc0b3c.mockapi.io/api/users?page=1&limit=10` | `page` 页码；`limit` 每页数量               | 通常是 `data` | **有可能有**：`pagination.totalRecords`   | `{ total: res.pagination.totalRecords, list: res.data }`          |
| **_page/_limit**      | JSONPlaceholder       | `https://jsonplaceholder.typicode.com/posts?_page=1&_limit=10`          | `_page` 页码；`_limit` 每页数量             | 返回数组本身     | body 无；Header 可能有 `X-Total-Count`    | `{ total: 100, list: res }` 或读 header                             |
| **_start/_limit**     | JSONPlaceholder       | `https://jsonplaceholder.typicode.com/posts?_start=0&_limit=10`         | `_start` 起始位置；`_limit` 每页数量          | 返回数组本身     | body 无；Header 可能有 `X-Total-Count`    | `{ total: 100, list: res }` 或读 header                             |
| **offset/limit**      | Platzi Fake Store     | `https://api.escuelajs.co/api/v1/products?offset=0&limit=10`            | `offset` 偏移量；`limit` 每页数量            | 返回数组本身     | **无**                                | `{ total: 999, list: res }` 或用 `hasMore = res.length >= pageSize` |
| **limit only**        | FakeStoreAPI          | `https://fakestoreapi.com/products?limit=10`                            | 只有 `limit`，不是真分页                     | 返回数组本身     | **无**                                | `{ total: 20, list: res }`，只适合简单 mock                             |
