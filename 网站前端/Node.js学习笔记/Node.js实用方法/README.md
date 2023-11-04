# Node.js实用方法

## 目录
1. [确保文件夹存在](#确保文件夹存在)

---
### 确保文件夹存在

```js
const fs = require("fs");
const path = require("path");

// 确保文件夹存在（不存在则创建，可判断多层文件夹）
function validateFolder(pathWay) {
  if (fs.existsSync(pathWay)) {
    return true;
  } else {
    if (validateFolder(path.dirname(pathWay))) {
      fs.mkdirSync(pathWay);
      console.log(`创建 ${pathWay}`);
      return true;
    }
  }
}
```
