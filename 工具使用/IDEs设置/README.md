### IDEs' Setting

1. There are **phpstorm** and **webstorm** settings. I exported `.jar` to make sure settings in my workplace and my PCs are the same.

    [phpstorm.jar](https://raw.githubusercontent.com/realgeoffrey/knowledge/master/工具使用/IDEs设置/phpstorm_04.25.jar)(webstorm can use too)
2. **Help -> Edit Custom VM Options** can change the memories for the IDE.

>Chinese Language Pack：please go to [PhpStorm-Chinese](https://github.com/ewen0930/PhpStorm-Chinese) or [WebStorm-Chinese](https://github.com/ewen0930/WebStorm-Chinese).

3. Terminal的vi乱码解决办法：

    在Git安装目录下的etc目录下的bash.bashrc文件（如：`C:\Program Files\Git\etc\bash.bashrc`），最后一行添加：

    ```text
    export LANG="zh_CN.UTF-8"
    export LC_ALL="zh_CN.UTF-8"
    ```
