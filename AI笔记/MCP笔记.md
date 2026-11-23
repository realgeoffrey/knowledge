# MCP笔记

### 定义

模型上下文协议（Model Context Protocol，MCP）是开放的通信协议，用于连接 LLM 应用与外部数据源、工具、服务。对话型模型演进到能执行任务的 Agent 后，需要动态拉取上下文，也可能通过工具修改外部状态。MCP 统一了「多源上下文 + 工具集」的交互方式，访问权限仍由宿主和服务端执行。

协议以 JSON-RPC 2.0 为消息格式，规范传输、能力声明与核心原语。宿主（Host）决定如何调用模型，同一套服务端逻辑可接入 Claude Desktop、Cursor 等兼容宿主。

**版本约定**：`2026-07-28` 改为逐请求声明版本与能力。下面同时保留 `2025-11-25` 的握手、传输表和完整报文，便于对照已有实现。两版字段与方法各有差异。[新版变更](https://modelcontextprotocol.io/specification/2026-07-28/changelog) · [旧版 schema](https://modelcontextprotocol.io/specification/2025-11-25/schema) · [旧版 schema.ts](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.ts)

### 相关产物

1. **[SDK](https://modelcontextprotocol.io/docs/sdk)**：各语言分仓实现，封装传输、生命周期与原语。
2. **[Inspector](https://github.com/modelcontextprotocol/inspector)**：可视化调试 MCP 服务器与消息流。
3. **[servers](https://github.com/modelcontextprotocol/servers)**：官方参考服务器集合。
4. **[registry](https://github.com/modelcontextprotocol/registry)**：社区驱动的服务器注册与发现。
5. **[llms.txt](https://modelcontextprotocol.io/llms.txt)**：文档索引，便于工具/模型按需拉取规范页面。

### 生命周期

**2026-07-28**：已知服务端支持新版时，客户端可直接发业务请求。每个请求都在 `params._meta` 中携带协议版本和客户端能力。[新版版本协商](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)

兼容新旧两版的客户端通过 stdio 连接版本未知的服务端时，应先用 `server/discover` 探测。探测成功后选用双方支持的版本。若返回 `UnsupportedProtocolVersionError`，从错误列出的版本中选择兼容版本重试，无共同版本则报错。只有遇到无法识别为新版的错误或探测超时，才回退到旧版 `initialize` 握手。[stdio 兼容流程](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio#backward-compatibility)

**2025-11-25** 分为 **初始化**、**运行**、**关闭** 三阶段。[旧版生命周期](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle)

1. **初始化**：首次交互须为 `initialize`。服务端返回能力与 `serverInfo`、客户端接受协议版本后，客户端 **必须** 再发 `notifications/initialized`。客户端在收到初始化响应前应只发 ping 请求，服务端在收到就绪通知前应只发 ping 请求或日志通知。
2. **运行与版本**：客户端在 `initialize` 中携带其支持的 `protocolVersion`。服务端支持则原样返回，否则返回自己支持的另一版本。若客户端不支持返回的版本，则应断开。HTTP 传输下，协商完成后客户端 **必须** 在后续请求中带 `MCP-Protocol-Version`（应为协商结果）。若服务端收不到该头且无法从别处得知版本，**应** 假定 `2025-03-26`。版本非法或不支持则 **必须** 响应 `400`。
3. **关闭**：**stdio** — 客户端宜先关闭子进程 stdin，超时未退出再发 `SIGTERM`，必要时发 `SIGKILL`。服务端也可关闭 stdout 并退出。**HTTP** — 若服务端分配了会话 ID，客户端用完后应携该 ID 发送 HTTP DELETE。服务端可用 `405` 表示不支持主动结束会话。无论是否分配了 ID 或接受 DELETE，客户端退出时都应关闭仍打开的 HTTP 连接（包括 SSE 流）。

### 分层

1. **数据层**：生命周期、能力声明，以及工具、资源、提示词等方法的请求与响应。

    例如，客户端用 `tools/list` 发现工具，再用 `tools/call` 指定工具名和实参。两版都保留这两个方法，但报文字段有变化，见下文示例。

2. **传输层**：

    承载 JSON-RPC。stdio 每行一条 UTF-8 消息，服务端 stdout 专供协议报文，普通日志可写 stderr。Streamable HTTP 可返回 JSON 或 SSE 事件流。

    1. 标准输入输出 (stdio) 机制
    2. 可流式 HTTP (Streamable HTTP) 机制

    下表按 [2025-11-25 传输规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)。

    | 评估维度        | stdio 传输机制                               | Streamable HTTP 传输机制                                 |
    |----------------|--------------------------------------------|---------------------------------------------------------|
    | 应用场景        | 本地工具集成、CLI 脚本、同物理机或容器内通信       | 远程 API 代理、云端微服务、多用户并发访问的数据源               |
    | 进程与生命周期   | 由客户端作为子进程启动，生命周期与客户端进程强绑定   | 独立运行的 Web 服务或守护进程，具备独立的生命周期               |
    | 并发与多路复用   | 一个客户端连接一个子进程，可用请求 ID 匹配多个在途请求 | 独立服务可处理多个客户端，每条客户端消息用独立 POST 发送 |
    | 会话状态追踪机制 | 通过该子进程与管道关联 | 服务端可选发放 `MCP-Session-Id`，该会话的后续请求必须携带。带此 ID 的请求若收到 `404`，客户端必须丢弃旧 ID，发送不带会话 ID 的 `initialize` 重建会话 |
    | 容错与重连能力   | 管道断裂后需重启子进程并重新初始化 | 服务端可选择支持 SSE 续传，此时客户端可用 `Last-Event-ID` 恢复原流 |
    | 安全模型与授权   | 子进程以启动账号的权限运行，文件和网络访问取决于实际隔离配置 | 服务端须检查 `Origin`，存在且非法时返回 `403`。受保护服务还需身份验证与授权 |

    **2026-07-28 的 HTTP 差异**：移除了协议会话 ID 和 SSE 断点续传。跨调用状态可用服务端发放的句柄作为工具参数传递。订阅用 `subscriptions/listen` 建立长 POST 响应流。流中断后，若重发则使用新的 JSON-RPC 请求 ID。原调用可能已经完成；写工具应按业务操作 ID 查证结果，再按工具的幂等约定决定是否重试。[新版传输规范](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)

### 角色

1. **宿主（Host）**：使用 MCP 的 AI 应用（如 AI IDE、智能体平台、对话界面）。它管理客户端、模型调用与人机交互，决定向模型提供哪些工具、哪些操作需要用户确认。受保护资源的访问权限由服务端校验。
2. **客户端（Client）**：嵌在宿主内的协议栈，通常为每个接入的 Server 管理独立的通信。它负责解析报文，把宿主意图转成 JSON-RPC 请求，并处理响应与通知。
3. **服务端（Server）**：对外提供上下文（如文件、数据库）与执行能力（如 API、编译）的实例，可本地或远程部署。服务端响应客户端请求，需要用户补充信息时可使用双方支持的 elicitation 机制。

### 原语

下表按 **2025-11-25** 的能力提供方排列。方法列同时列出请求和通知，例如 `roots/list` 由 Server 请求，`notifications/roots/list_changed` 由 Client 通知。

| 能力提供方           | 核心能力类别            | JSON-RPC 典型方法与通知                                   | 功能定位与系统职责描述                                           |
|----------------------|----------------------|-------------------------------------------------------|--------------------------------------------------------------|
| Server 提供给 Client  | Tools (工具)          | tools/list, tools/call                                | 暴露可产生副作用的执行动作，供模型发现与调用。 |
|                      | Resources (资源)      | resources/list, resources/read                        | 暴露只读或可订阅的状态与配置，供拉取长上下文或 RAG。 |
|                      | Prompts (提示词)      | prompts/list, prompts/get                              | 暴露可复用模板与工作流预设，统一交互口径。 |
| Client 提供给 Server  | Sampling (采样)       | sampling/createMessage                                 | Server 经宿主调用模型，无需自持厂商 API 密钥。 |
|                      | Elicitation (请求用户输入) | elicitation/create, notifications/elicitation/complete | 表单可收集非敏感输入。密码、令牌等须经 URL 模式在站外处理，完成通知仅适用于 URL 模式。 |
|                      | Roots (根路径)        | roots/list, notifications/roots/list_changed           | Server 从 Client 获取工作范围（`file://` URI），实际文件访问边界由权限或沙盒执行。 |
| Server 提供给 Client  | 日志 (Logging)        | logging/setLevel, notifications/message                | Client 设日志级别，Server 向宿主推送运行信息。 |
| 基础实用工具 (双向)     | 长任务 (Tasks)        | tasks/get, tasks/result, tasks/cancel                  | 实验能力：双方按声明的支持范围查询状态、取回结果或取消任务。 |

**通知**是带 `method`、省略 `id` 的 JSON-RPC 消息，接收方不得发送 JSON-RPC 响应。使用 2025-11-25 的 Streamable HTTP 时，服务端接受通知 POST（如 `notifications/initialized`）后，必须返回 HTTP `202 Accepted`，响应体为空。收到列表变更通知后，可再次调用对应的 `*/list` 刷新列表。列表结果若含 `nextCursor`，用它作为下次请求的 `cursor` 继续翻页。

**2026-07-28** 的 `tools/call`、`resources/read`、`prompts/get` 可用多轮请求。服务端返回 `resultType: "input_required"` 时，至少携带 `inputRequests`、`requestState` 之一。客户端重试时用新的请求 ID，原样回传收到的 `requestState`，如有 `inputRequests` 则在 `inputResponses` 中逐项回应。该版也将 Roots、Sampling、Logging 标为弃用，Tasks 移至官方扩展。[多轮请求](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) · [新版原语变更](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

### JSON-RPC 示例

**2026-07-28** 可以直接列工具。下面是请求体，HTTP POST 还须设置 `Content-Type: application/json`、接受 JSON 与 SSE 的 `Accept`、`MCP-Protocol-Version: 2026-07-28` 和 `Mcp-Method: tools/list`。成功的列表响应含 `resultType: "complete"`、`tools`、`ttlMs` 与 `cacheScope`。[新版工具规范](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {},
      "io.modelcontextprotocol/clientInfo": { "name": "example-client", "version": "1.0.0" }
    }
  }
}
```

#### 2026-07-28 的 HTTP 调用怎样联调

调用 `tools/call` 时，使用与 `tools/list` 相同的 HTTP 端点和传输头。将 `Mcp-Method` 设为 `tools/call`，`Mcp-Name` 设为正文 `params.name` 中的工具名。按该工具在 `tools/list` 公布的输入 schema 构造参数。[Streamable HTTP 请求头](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)

如果工具声明了 `outputSchema`，成功结果中的 `structuredContent` 应符合该 schema。保留序列化为文本的副本有助于兼容只读文本的客户端。JSON-RPC 的 `id` 用来匹配请求和响应。[工具结果与结构化输出](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)

联调时分三层查。① 若新版服务端校验发现 `Mcp-Name` 与正文不一致，预期 HTTP 400 和协议错误 `HeaderMismatch`（`-32020`）；先修请求，看到 400 就切回旧握手会掩盖问题。② 协议报未知工具时，核对该服务端公布的工具名。③ 工具已运行但业务失败时，检查结果里的 `isError`；收到 `input_required` 则按多轮请求继续，页面要等到业务结果可确认后再展示完成。[传输与版本回退](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#backward-compatibility) · [工具错误处理](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#error-handling)

#### 2025-11-25 的完整交互

这版从 `initialize` 请求 / 响应开始。

```jsonc
// 请求
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25", // 协议版本协商
    "capabilities": { // 能力发现（客户端支持能力）
      "elicitation": {}
    },
    "clientInfo": { // 客户端身份
      "name": "example-client",
      "version": "1.0.0"
    }
  }
}

// 响应
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-11-25",
    "capabilities": { // 能力发现（服务端支持能力）
      "tools": {
        "listChanged": true
      },
      "resources": {}
    },
    "serverInfo": { // 服务器身份（代码里`new McpServer({ name: "example-server", version: "1.0.0" })`设置）
      "name": "example-server", // 服务端实现的名称，工具调用使用 tools/list 返回的工具名
      "version": "1.0.0"
    }
  }
}
```

`notifications/initialized`：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

`tools/list` 请求 / 响应：

```jsonc
// 请求
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}

// 响应
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "calculator_arithmetic",
        "title": "Calculator",
        "description": "Perform mathematical calculations",
        "inputSchema": {
          "type": "object",
          "properties": {
            "expression": {
              "type": "string",
              "description": "Mathematical expression to evaluate (e.g. '2 + 3 * 4', 'sin(30)', 'sqrt(16)')"
            }
          },
          "required": ["expression"]
        }
      },
      {
        "name": "weather_current", // （重要，影响该工具调用情况）服务器命名空间中工具的唯一标识符；工具执行主键，命名应明确
        "title": "Weather Information", // 用户可读的显示名称，客户端可向用户展示
            // （重要，影响该工具调用情况）详细说明该工具的功能及何时使用该工具
        "description": "Get current weather information for any location worldwide",
        "inputSchema": { // 定义预期输入参数的 JSON 模式：类型校验、必需/可选参数说明
          "type": "object",
          "properties": { // 参数名、类型、描述等（如默认值、枚举）
            "location": {
              "type": "string",
              "description": "City name, address, or coordinates (latitude,longitude)"
            },
            "units": {
              "type": "string",
              "enum": ["metric", "imperial", "kelvin"],
              "description": "Temperature units to use in response",
              "default": "metric"
            }
          },
          "required": ["location"] // 必填参数
        }
      }
    ]
  }
}
```

`tools/call` 请求 / 响应：

```jsonc
// 请求
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "weather_current", // 服务器命名空间中工具的唯一标识符
    "arguments": { // 与工具 inputSchema 对应的实参
      "location": "San Francisco",
      "units": "imperial"
    }
  }
}

// 响应
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [ // 工具返回内容对象数组
      {
        "type": "text", // 内容类型
        "text": "Current weather in San Francisco: 68°F, partly cloudy with light winds from the west at 8 mph. Humidity: 65%"
      }
    ]
  }
}
```

工具执行失败（如天气 API 返回错误）可用 `result.isError: true` 和 `content` 说明原因。调用未知工具、请求结构错误等协议问题则返回 JSON-RPC 顶层 `error`。[旧版工具错误处理](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#error-handling)

`notifications/tools/list_changed`（收到后客户端通常会再发 `tools/list`）：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

### 模型何时调用 MCP 工具

宿主决定哪些工具可用，可以按用户操作或程序逻辑直接调用，也可以让模型选择。让模型选择时，工具级 `name` 和 `description` 应写清动作、适用条件和参数含义。宿主配置里的 `mcpServers` 键名可能用作显示名或前缀，`serverInfo.name` 标识服务端实现。向该服务端发送 `tools/call` 时，`params.name` 应使用它在 `tools/list` 中公布的工具名。[工具规范](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
