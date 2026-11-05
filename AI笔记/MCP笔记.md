# MCP笔记

### 定义

模型上下文协议（Model Context Protocol，MCP）是开源的标准化通信协议，用于在 LLM 应用与外部数据源、工具、服务之间做安全、双向集成。对话型模型演进到能执行任务的 Agent 后，需要动态拉取上下文并对环境产生副作用；MCP 统一了「多源上下文 + 工具集」的交互方式。

协议以 JSON-RPC 2.0 为消息格式，强调 **有状态连接** 与 **能力协商**。它不规定宿主（Host）如何调模型，而规范传输层、生命周期与核心原语的交互方式；与具体大模型厂商解耦，同一套服务端逻辑可接入 Claude Desktop、Cursor 等兼容宿主的客户端。

协议与版本对齐的类型与消息结构见 **[schema](https://modelcontextprotocol.io/specification/2025-11-25/schema)**（[schema.ts](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.ts)），便于强类型解析与兼容演进。

### 相关产物

1. **[SDK](https://modelcontextprotocol.io/docs/sdk)**：各语言分仓实现，封装传输、生命周期与原语。
2. **[Inspector](https://github.com/modelcontextprotocol/inspector)**：可视化调试 MCP 服务器与消息流。
3. **[servers](https://github.com/modelcontextprotocol/servers)**：官方参考服务器集合。
- **[registry](https://github.com/modelcontextprotocol/registry)**：社区驱动的服务器注册与发现。
- **[llms.txt](https://modelcontextprotocol.io/llms.txt)**：文档索引，便于工具/模型按需拉取规范页面。

### 生命周期

三阶段： **初始化**（能力协商与协议版本）、**运行**、**关闭**。

1. **初始化**：首次交互须为 `initialize`；服务端返回能力与 `serverInfo` 后，客户端 **必须** 再发 `notifications/initialized`，此后进入正常运行。收到 `initialize` 的响应前，客户端 **不应** 发送除 ping 以外的请求；收到 `initialized` 前，服务端 **不应** 发送除 ping 与 logging 以外的请求。
2. **运行与版本**：客户端在 `initialize` 中携带其支持的 `protocolVersion`；服务端支持则原样返回，否则回退到自己支持的版本；客户端不接受则应断开。HTTP 传输下，协商完成后客户端 **必须** 在后续请求中带 `MCP-Protocol-Version`（协商结果）；若服务端收不到该头且无法从别处得知版本，**应** 假定 `2025-03-26`；版本非法或不支持则 **必须** 响应 `400`。
3. **关闭**：**stdio** — 客户端宜先关闭子进程 stdin，等待进程退出或响应 `SIGTERM`，必要时 `SIGKILL`；服务端也可关闭 stdout 并退出。**HTTP** — 关闭对应连接即可。

### 分层

1. **数据层**：生命周期与能力协商；

    数据层承载 MCP 的核心语义：交互由生命周期状态机驱动，起点是初始化。

    传输连通后，客户端须先发送 `initialize`，与对方协商协议版本与能力（Capabilities）。在客户端发出 `notifications/initialized` 之前，通道处于受限态：除 ping 与面向客户端的日志通知外，不得发送其他业务请求。若服务端无法支持客户端声明的协议版本，应断开连接，避免后续解析失败。
2. **传输层**：

    承载 JSON-RPC。

    1. 标准输入输出 (stdio) 机制
    2. 可流式 HTTP (Streamable HTTP) 机制

    | 评估维度        | stdio 传输机制                               | Streamable HTTP 传输机制                                 |
    |----------------|--------------------------------------------|---------------------------------------------------------|
    | 应用场景        | 本地工具集成、CLI 脚本、同物理机或容器内通信       | 远程 API 代理、云端微服务、多用户并发访问的数据源               |
    | 进程与生命周期   | 由客户端作为子进程启动，生命周期与客户端进程强绑定   | 独立运行的 Web 服务或守护进程，具备独立的生命周期               |
    | 并发与多路复用   | 单一连接，独占式 1:1 通信，无原生并发处理         | 支持多客户端并发连接，通过多线程或异步 I/O 处理请求              |
    | 会话状态追踪机制 | 隐式关联（完全依赖于子进程实例的内存状态与管道连接）  | 显式关联（强制依赖 MCP-Session-Id 头部维持状态机）            |
    | 容错与重连能力   | 脆弱（管道断裂或进程崩溃即视为连接永久终止）        | 健壮（支持基于 Last-Event-ID 的断点续传与消息重放）            |
    | 安全模型与授权   | 进程级隔离，天然继承宿主操作系统的用户权限边界      | 需配置远程服务器侧鉴权（如 OAuth 2.0）、CORS 与 Origin 校验     |

### 角色

1. **宿主（Host）**：发起连接的 LLM 应用（如 AI IDE、智能体平台、对话界面）。既是模型运行环境，也是安全与用户权限的最终执行者：管理人机交互、决定向模型注入哪些工具，并承担 Human-in-the-loop 等确认职责。
2. **客户端（Client）**：嵌在宿主内的协议栈；每个接入的 Server 对应一个 Client，维持独立有状态连接。负责状态机与报文解析，把宿主意图转成符合 MCP 的 JSON-RPC 请求，并处理服务端异步通知。
3. **服务端（Server）**：对外部提供上下文（如文件、数据库）与执行能力（如 API、编译）的实例，可本地或远程部署。响应客户端请求；在授权前提下可反向请求采样、用户输入等，**不**绑定任一 LLM 厂商的 API Key。

### 原语

| 原语方向归属           | 核心能力类别            | JSON-RPC 典型方法调用                                   | 功能定位与系统职责描述                                           |
|----------------------|----------------------|-------------------------------------------------------|--------------------------------------------------------------|
| Server 提供给 Client  | Tools (工具)          | tools/list, tools/call                                | 暴露可产生副作用的执行动作，供模型发现与调用。 |
|                      | Resources (资源)      | resources/list, resources/read                        | 暴露只读或可订阅的状态与配置，供拉取长上下文或 RAG。 |
|                      | Prompts (提示词)      | prompts/list, prompts/get                              | 暴露可复用模板与工作流预设，统一交互口径。 |
| Client 提供给 Server  | Sampling (采样)       | sampling/createMessage                                 | Server 经宿主调用模型，无需自持厂商 API 密钥。 |
|                      | Elicitation (信息诱导) | elicitation/create, notifications/elicitation/complete | Server 向用户索取结构化输入或 OAuth 等确认。 |
|                      | Roots (根路径)        | roots/list, notifications/roots/list_changed           | Server 获知客户端允许访问的路径边界，便于沙盒。 |
| 基础实用工具 (双向)     | 日志 (Logging)        | logging/setLevel, notifications/message                | Client 设日志级别，Server 向宿主推送运行信息。 |
|                      | 长任务 (Tasks)        | tasks/result, tasks/cancel                              | 实验能力：封装长耗时或异步操作，减轻单次 RPC 阻塞。 |

**通知**：无 `id` 的 JSON-RPC 消息；收到 `notifications/*/list_changed` 后应再调用对应 `*/list` 刷新列表。

### JSON-RPC 示例

`initialize` 请求 / 响应：

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
      "name": "example-server", // 服务器名不影响 MCP 是否被调用
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

`notifications/tools/list_changed`（收到后客户端通常会再发 `tools/list`）：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

### 模型何时调用 MCP 工具

是否调用某一 MCP 工具由模型与宿主策略共同决定：MCP 只声明能力。实际选用受 Host 规则、用户意图，以及模型对 **`name`、`description`（及 `title` 等）** 的解读影响。配置里 **mcpServers 的键名**、服务端身份的`serverInfo.name`（`new McpServer({ name: "xxx" })`） 等 **不会** 与「选哪个工具」一一对应；应把 **工具级** `name` / `description` 写清楚，并在用户指令中明确动作与对象，以提高命中率。
