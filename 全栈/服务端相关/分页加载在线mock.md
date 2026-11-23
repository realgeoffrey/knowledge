# 分页加载在线mock

| 服务 | 搜索 | 分页 | 每页大小 | total | 结论 | 示例链接 |
| --- | --- | --- | --- | --- | --- | --- |
| DummyJSON User Search | ✅，`q=em` | ✅，`skip=0` | ✅，`limit=10` | ✅，body `total` | 四项都支持，适合作为搜索 + 分页 + 总量示例。 | <https://dummyjson.com/users/search?q=em&limit=10&skip=0> |
| GitHub Search | ✅，`q=stars:%3E100000` | ✅，`page=1` | ✅，`per_page=5` | ✅，body `total_count` | 有接口限流；每次搜索最多可取前 1,000 条，`total_count` 可能更大。 | <https://api.github.com/search/repositories?q=stars:%3E100000&page=1&per_page=5> |
| JSONPlaceholder | ✅，`q=voluptas` | ✅，`_start=0` 或 `_page=1` | ✅，`_limit=10` | ✅，header `X-Total-Count` | 四项都支持，但 total 在响应头，不在 body。 | <https://jsonplaceholder.typicode.com/posts?q=voluptas&_start=0&_limit=10><br><https://jsonplaceholder.typicode.com/posts?q=voluptas&_page=1&_limit=10> |
| MockAPI.io 包装版 | ✅，`search=Analyst` | ✅，`page=1` | ✅，`limit=10` | ✅，body `total`（按配置） | 四项都支持；当前响应是 `data + total` 包装结构。 | <https://61273138c2e8920017bc0b3c.mockapi.io/api/users?page=1&limit=10&search=Analyst> |
| MockAPI.io 数组示例 | ✅，`search=admin` | ✅，`page=1` | ✅，`limit=10` | ❌ | 此项目直接返回数组，未提供总量；响应结构取决于项目配置。 | <https://660d2bd96ddfa2943b33731c.mockapi.io/api/users?page=1&limit=10&search=admin> |
| PokéAPI | ❌ | ✅，`offset=0` | ✅，`limit=10` | ✅，body `count` | 不支持列表搜索参数，但分页和总量完整。 | <https://pokeapi.co/api/v2/pokemon?offset=0&limit=10> |
| Platzi Fake Store | ✅，按标题过滤，如 `title=shirt` | ✅，`offset=0` | ✅，`limit=10` | ❌ | 按标题筛选的 offset/limit 示例，列表响应不含总量。 | <https://api.escuelajs.co/api/v1/products?offset=0&limit=10&title=shirt> |
| Random User | ❌ | ✅，`page=1` | ✅，`results=10` | ❌ | 适合模拟分页加载，不适合需要总页数的分页器。 | <https://randomuser.me/api/?page=1&results=10&seed=abc> |
