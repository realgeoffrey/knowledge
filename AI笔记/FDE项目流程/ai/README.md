# AI 实现补充

业务定义见 [spec](../spec/README.md)，执行边界见 [AGENTS](../AGENTS.md)。这里只保留代码之外仍有用的实现决定、工程命令和当前技术限制；没有实际需要就不新增文件。

## 按真实工程填写

- 工程入口、运行环境与安装/启动/构建/测试命令：依据实际构建文件与锁文件核定，不从模板猜测。
- 采用的技术与组件映射：复用相邻实现；数据结构与接口优先引用已有定义，不复制业务字段或 OpenAPI。
- 技术限制与恢复方式：只写当前适用且不能直接从代码得知的内容，不记录会议、任务过程或逐次测试结果。

## 检查命令

在项目根按影响选择：

```sh
python3 ai/scripts/check_context.py
python3 ai/scripts/sync_design.py --check
python3 -m unittest discover -s ai/scripts -p 'test_*.py'
node --test ai/scripts/test_*.cjs
```

入口、链接、编号或目录变化运行结构检查。设计 tokens、规范标记或页面登记变化，先改 [design.md](../prototypes/design.md)，运行 `python3 ai/scripts/sync_design.py` 后再 `--check`。Python 工具变化跑对应单测；原型交互或共享脚本变化跑 Node 测试并实际操作受影响页面。

结构检查默认读取根入口及 `spec/`、`prototypes/`、`ai/` 的 Markdown。来源与人工待定文件仅核目标存在，不读正文；`--check-file <项目相对路径.md>` 可追加其他项目 Markdown，拒绝保护文件及符号链接绕过。

工具只检查简单单行内联链接、ATX 标题、显式锚点、REQ/AC 唯一定义及设计同步，不证明业务正确、确认通过、Mermaid 语法、布局或真实接口可用。图表变化须在本地实际渲染；临时工具和产物不入库。结果在当前对话说明。
