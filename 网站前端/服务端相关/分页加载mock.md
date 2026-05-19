# 分页加载mock

## 目录
1. []()

---

| 类型                    | 服务                    | 直接可用链接                                                                  | 分页参数                                 | 返回列表字段     | 是否有 total                            |
| --------------------- | --------------------- | ----------------------------------------------------------------------- | ------------------------------------ | ---------- | ------------------------------------ |
| **skip/limit**        | DummyJSON Users       | <l>https://dummyjson.com/users?limit=10&skip=0</l>                           | `limit` 每页数量；`skip` 跳过数量             | `users`    | **有**：`total`                        |
| **skip/limit + 搜索**   | DummyJSON User Search | <l>https://dummyjson.com/users/search?q=em&limit=10&skip=0</l>               | `q` 搜索；`limit`；`skip`                | `users`    | **有**：`total`                        |
| **offset/limit**      | PokéAPI               | <l>https://pokeapi.co/api/v2/pokemon?offset=0&limit=10</l>                   | `offset` 偏移量；`limit` 每页数量            | `results`  | **有**：`count`                        |
| **page/per_page**     | ReqRes                | <l>https://reqres.in/api/users?page=1&per_page=6</l>                         | `page` 页码；`per_page` 每页数量            | `data`     | **有**：`total`                        |
| **page/per_page**     | GitHub Search         | <l>https://api.github.com/search/repositories?q=stars:>100000&page=1&per_page=5</l> | `q` 搜索；`page` 页码；`per_page` 每页数量 | `items`    | **有**：`total_count`                  |
| **page/results**      | Random User           | <l>https://randomuser.me/api/?page=1&results=10&seed=abc</l>                 | `page` 页码；`results` 每页数量；`seed` 固定结果 | `results`  | **无真实 total**，只有 `info.page/results` |
| **page/limit**        | MockAPI.io AntD 示例    | <l>https://660d2bd96ddfa2943b33731c.mockapi.io/api/users?page=1&limit=10</l> | `page` 页码；`limit` 每页数量               | 返回数组本身     | **无**，AntD 示例里 total 写死 100          |
| **page/limit + 包装分页** | MockAPI.io 包装版示例      | <l>https://61273138c2e8920017bc0b3c.mockapi.io/api/users?page=1&limit=10</l> | `page` 页码；`limit` 每页数量               | 通常是 `data` | **有可能有**：`pagination.totalRecords`   |
| **_page/_limit**      | JSONPlaceholder       | <l>https://jsonplaceholder.typicode.com/posts?_page=1&_limit=10</l>          | `_page` 页码；`_limit` 每页数量             | 返回数组本身     | body 无；Header 可能有 `X-Total-Count`    |
| **_start/_limit**     | JSONPlaceholder       | <l>https://jsonplaceholder.typicode.com/posts?_start=0&_limit=10</l>         | `_start` 起始位置；`_limit` 每页数量          | 返回数组本身     | body 无；Header 可能有 `X-Total-Count`    |
| **offset/limit**      | Platzi Fake Store     | <l>https://api.escuelajs.co/api/v1/products?offset=0&limit=10</l>            | `offset` 偏移量；`limit` 每页数量            | 返回数组本身     | **无**                                |
| **limit only**        | FakeStoreAPI          | <l>https://fakestoreapi.com/products?limit=10</l>                            | 只有 `limit`，不是真分页                     | 返回数组本身     | **无**                                |
