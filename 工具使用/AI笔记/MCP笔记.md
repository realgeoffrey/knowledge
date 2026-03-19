### MCP笔记

1. **定义**：

    开放协议，在 LLM 应用与外部数据源/工具之间交换上下文与能力。消息为 **JSON-RPC 2.0**；**有状态连接**；不规定 Host 如何调用模型。**[schema](https://modelcontextprotocol.io/specification/2025-11-25/schema)（或<https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.ts>）**：与协议版本对齐的类型与消息结构定义。

1. **相关产物**：

    **[SDK](https://modelcontextprotocol.io/docs/sdk)**：各语言分仓实现，封装传输、生命周期与原语。**[Inspector](https://github.com/modelcontextprotocol/inspector)**：可视化调试 MCP 服务器与消息流。**[servers](https://github.com/modelcontextprotocol/servers)**：官方维护的参考服务器集合。**[registry](https://github.com/modelcontextprotocol/registry)**：社区驱动的服务器注册与发现。

1. **分层**

    - **数据层**：生命周期与能力协商；Server 侧 Tools / Resources / Prompts；Client 侧 Sampling、Roots、Elicitation；以及 Logging、进度、取消、通知等。
    - **传输层**：承载 JSON-RPC。标准两种：**stdio**：客户端拉起服务器子进程，一行一条 JSON-RPC，只从 stdin 读、向 stdout 写 MCP 消息，stderr 仅日志。**Streamable HTTP**：独立 HTTP 服务，客户端以 POST 提交消息，可用 SSE 流式收消息，多客户端；可用响应头 `MCP-Session-Id` 关联会话，后续请求带 `MCP-Protocol-Version` 标明协议版本。可自定义传输，须满足数据层与生命周期。**Authorization**：远程服务器侧鉴权（如 OAuth），与 Streamable HTTP 搭配；具体扩展见 **ext-auth** 仓库。客户端 **应** 在可行时支持 stdio。

1. **角色**：

    **Host**（发起连接的 LLM 应用）为每个 Server 建一个 **Client** 维持专用连接；**Server** 提供上下文与能力，可本地可远程。

1. **原语（方法名以规范为准）**

    | 方向 | 能力 | 典型方法 |
    | :--- | :--- | :--- |
    | Server提供给Client | Tools | `tools/list`、`tools/call` |
    | | Resources | `resources/list`、`resources/read` |
    | | Prompts | `prompts/list`、`prompts/get` |
    | Client提供给Server（由 Server 发请求） | Sampling | `sampling/createMessage` |
    | | Elicitation | `elicitation/create`，完成 `notifications/elicitation/complete` |
    | | Roots | `roots/list`，变更 `notifications/roots/list_changed` |
    | 日志 | 由 Client 向 Server 设置级别 `logging/setLevel`；由 Server 向 Client 发通知 `notifications/message`（Server 须声明 `logging` 能力） |
    | 实验性 | Tasks | 规范「公用能力」中的长任务：包装耗时或异步操作，支持延后取结果与状态跟踪 |

    - **服务端提供给客户端**

      - **Tools**：把「可调用的动作」暴露给 Host/模型（查库、调 API、改文件等）；模型或编排层通过 `tools/call` 触发，适合需要**副作用**或**写操作**的集成。
      - **Resources**：暴露**只读或订阅式**的上下文片段（文件片段、记录、配置视图等），供拉进对话或 RAG，不必每次写成一次工具调用；适合**稳定数据源**、大段引用。
      - **Prompts**：暴露**可复用模板**（系统提示、多步工作流说明、少样本示例），由用户或 Host 选用，统一团队/产品与模型的交互口径。

    - **客户端提供给服务端**（由 Server 发起请求，经 Client 转到 Host/用户/模型）

      - **Sampling**：Server 在自身逻辑里需要**再调一次 LLM**（总结、分类、多步推理）时，向 Host 借模型，**不在 Server 里绑死厂商或 API Key**，权限与模型选择在用户侧。
      - **Elicitation**：Server 缺参数、需**确认危险操作**或**选枚举**时，向用户要结构化输入；适合 CLI/图形 Host 统一做人机确认。
      - **Roots**：Server 要知道**当前允许操作的路径边界**（工作区、多仓库根），避免越权访问；与文件类 Tools/Resources 配合。

    - **日志**：Server 把运行信息以 `notifications/message` 推给 Client，便于 Host 里**调试与可观测**；`logging/setLevel` 由 Client 控制详细程度。
    - **Tasks（实验性）**：把**长时间或异步**工作从单次 RPC 里拆出去，之后按任务 ID 取结果/状态，避免阻塞与超时。
    - **通知**：无 `id` 的 JSON-RPC 通知，用于列表变更等；客户端收到 `notifications/*/list_changed` 后应再 `*/list` 刷新。

1. **JSON-RPC 示例**（`protocolVersion` 与字段以协商与规范为准）

    `initialize` 请求 / 响应：

    ```json
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
        "serverInfo": { // 服务器身份
          "name": "example-server",
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

    ```json
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
            "name": "weather_current", // 服务器命名空间中工具的唯一标识符；工具执行主键，命名应明确
            "title": "Weather Information", // 用户可读的显示名称，客户端可向用户展示
            // 详细说明该工具的功能及何时使用该工具
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

    ```json
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
