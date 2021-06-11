### Chrome使用

## 目录
1. [移植Chrome扩展程序](#移植chrome扩展程序)
1. [Chrome全屏截图](#chrome全屏截图)

---
### 移植Chrome扩展程序
把一台电脑的Chrome扩展移植到另一台电脑的Chrome扩展

1. 获得扩展的ID： <chrome://extensions/>
2. 去扩展目录拷贝扩展程序的文件夹到另一台电脑的Chrome扩展目录中

    1. macOS：

        1. `/Users/「用户名」/Library/Application Support/Google/Chrome/Default/Extensions`
        2. `/Users/「用户名」/Library/Application Support/Google/Chrome/Profile 10/Extensions`
    2. Windows：`C:\Users\「用户名」\AppData\Local\Google\Chrome\User Data\Default\Extensions`
3. <chrome://extensions/> 中点击「加载已解压的扩展程序」选择新增的文件夹下的版本文件夹

### Chrome全屏截图
1. 打开控制台
2. ctrl/command + shift + p
3. `>capture`

    ![capture](./images/capture.png)
