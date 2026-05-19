# 分页加载mock

## 目录
1. []()

---

| 支持数 | 服务 | 搜索 | 分页 | 每页大小 | total | 结论 | 直接可用链接 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4/4 | DummyJSON User Search | ✅，`q=em` | ✅，`skip=0` | ✅，`limit=10` | ✅，body `total` | 四项都支持，适合作为搜索 + 分页 + 总量示例。 | <l>https://dummyjson.com/users/search?q=em&limit=10&skip=0</l> |
| 4/4 | GitHub Search | ✅，`q=stars:%3E100000` | ✅，`page=1` | ✅，`per_page=5` | ✅，body `total_count` | 四项都支持，注意 GitHub Search 有接口限流。 | <l>https://api.github.com/search/repositories?q=stars:%3E100000&page=1&per_page=5</l> |
| 4/4 | JSONPlaceholder | ✅，`q=voluptas` | ✅，`_start=0` 或 `_page=1` | ✅，`_limit=10` | ✅，header `X-Total-Count` | 四项都支持，但 total 在响应头，不在 body。 | <l>https://jsonplaceholder.typicode.com/posts?q=voluptas&_start=0&_limit=10</l><br><l>https://jsonplaceholder.typicode.com/posts?q=voluptas&_page=1&_limit=10</l> |
| 4/4 | MockAPI.io 包装版示例 | ✅，`search=Analyst` | ✅，`page=1` | ✅，`limit=10` | ✅，body `total`（按配置） | 四项都支持；当前响应是 `data + total` 包装结构。 | <l>https://61273138c2e8920017bc0b3c.mockapi.io/api/users?page=1&limit=10&search=Analyst</l> |
| 3/4 | MockAPI.io 免费版 | ✅，`search=Analyst` | ✅，`page=1` | ✅，`limit=10` | ❌，body 为数组 | 请求参数齐全，但响应没有 total，不能直接渲染完整分页器。 | <l>https://660d2bd96ddfa2943b33731c.mockapi.io/api/users?page=1&limit=10&search=Analyst</l> |
| 3/4 | PokéAPI | ❌ | ✅，`offset=0` | ✅，`limit=10` | ✅，body `count` | 不支持列表搜索参数，但分页和总量完整。 | <l>https://pokeapi.co/api/v2/pokemon?offset=0&limit=10</l> |
| 2.5/4 | Platzi Fake Store | ❌。但支持指定字段过滤搜索，如`title=鸿蒙` | ✅，`offset=0` | ✅，`limit=10` | ❌，body 为数组 | 只适合作为 offset/limit 列表加载示例。 | <l>https://api.escuelajs.co/api/v1/products?offset=0&limit=10&title=鸿蒙</l> |
| 2/4 | Random User | ❌ | ✅，`page=1` | ✅，`results=10` | ❌ | 适合模拟分页加载，不适合需要总页数的分页器。 | <l>https://randomuser.me/api/?page=1&results=10&seed=abc</l> |
