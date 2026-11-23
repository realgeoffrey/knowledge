# Lark飞书生态开发

## 目录
1. [Lark开发平台](#lark开发平台)
1. [飞书开发平台](#飞书开发平台)

---
### [Lark开发平台](https://open.larksuite.com)
调用 Lark 服务端 API 时使用 `open.larksuite.com`。官方 Node.js SDK 需要显式选择 `Domain.Lark`。

### [飞书开发平台](https://open.feishu.cn)
飞书服务端 API 使用 `open.feishu.cn`，也是官方 Node.js SDK 的默认域名。应用的 App Secret 应保存在服务端，用于换取访问凭证。[SDK 调用说明](https://open.feishu.cn/document/server-side-sdk/nodejs-sdk/invoke-server-api)
