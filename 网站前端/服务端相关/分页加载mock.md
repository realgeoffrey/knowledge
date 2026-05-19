# 分页加载mock

## 目录
1. []()

---

| 类型 | 服务 | 直接可用链接 |
| --- | --- | --- |
| **skip/limit**<br>请求参数：`limit`（每页数量）、`skip`（跳过数量）<br>响应包含：total **有** `total` | DummyJSON Users | <l>https://dummyjson.com/users?limit=10&skip=0</l> |
| **skip/limit + 搜索**<br>请求参数：`q`（搜索）、`limit`、`skip`<br>响应包含：total **有** `total` | DummyJSON User Search | <l>https://dummyjson.com/users/search?q=em&limit=10&skip=0</l> |
| **offset/limit**<br>请求参数：`offset`（偏移量）、`limit`（每页数量）<br>响应包含：total **有** `count` | PokéAPI | <l>https://pokeapi.co/api/v2/pokemon?offset=0&limit=10</l> |
| **page/per_page**<br>请求参数：`page`（页码）、`per_page`（每页数量）<br>响应包含：total **有** `total` | ReqRes | <l>https://reqres.in/api/users?page=1&per_page=6</l> |
| **page/per_page**<br>请求参数：`q`（搜索）、`page`（页码）、`per_page`（每页数量）<br>响应包含：total **有** `total_count` | GitHub Search | <l>https://api.github.com/search/repositories?q=stars:>100000&page=1&per_page=5</l> |
| **page/results**<br>请求参数：`page`（页码）、`results`（每页数量）、`seed`（固定结果）<br>响应包含：total **无**（仅 `info.page` / `results`） | Random User | <l>https://randomuser.me/api/?page=1&results=10&seed=abc</l> |
| **page/limit**<br>请求参数：`page`（页码）、`limit`（每页数量）<br>响应包含：total **无**（AntD 示例里 total 写死 100） | MockAPI.io AntD 示例 | <l>https://660d2bd96ddfa2943b33731c.mockapi.io/api/users?page=1&limit=10</l> |
| **page/limit + 包装分页**<br>请求参数：`page`（页码）、`limit`（每页数量）<br>响应包含：total **可能有** `pagination.totalRecords` | MockAPI.io 包装版示例 | <l>https://61273138c2e8920017bc0b3c.mockapi.io/api/users?page=1&limit=10</l> |
| **_page/_limit**<br>请求参数：`_page`（页码）、`_limit`（每页数量）<br>响应包含：total body **无**；Header 可能有 `X-Total-Count` | JSONPlaceholder | <l>https://jsonplaceholder.typicode.com/posts?_page=1&_limit=10</l> |
| **_start/_limit**<br>请求参数：`_start`（起始位置）、`_limit`（每页数量）<br>响应包含：total body **无**；Header 可能有 `X-Total-Count` | JSONPlaceholder | <l>https://jsonplaceholder.typicode.com/posts?_start=0&_limit=10</l> |
| **offset/limit**<br>请求参数：`offset`（偏移量）、`limit`（每页数量）<br>响应包含：total **无** | Platzi Fake Store | <l>https://api.escuelajs.co/api/v1/products?offset=0&limit=10</l> |
| **limit only**<br>请求参数：仅 `limit`（非真分页）<br>响应包含：total **无** | FakeStoreAPI | <l>https://fakestoreapi.com/products?limit=10</l> |
