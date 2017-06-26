# Git心得

>除了基本GIT操作外的操作。

### 如何在一台电脑中使用2（多个）个Github账号的SSH keys

>在github网站中：不同账户无法使用相同的**SSH key**。

1. 生产多对的**SSH keys**，并放入 **.ssh文件夹**：

    ```bash
    ssh-keygen -f '地址/名字'
    ```
2. 为不同账户地址设置对应的SSH key路径：

    **~/.ssh/config**文件添加
    ```bash
    Host 账户1.github.com
    	HostName github.com
    	User git
    	IdentityFile ~/.ssh/键1

    Host 账户2.github.com
    	HostName github.com
    	User git
    	IdentityFile ~/.ssh/键2
    ```
3. 克隆仓库时修改**仓库地址**：

    `git@github.com:账户/仓库.git` -> `git@账户.github.com:账户/仓库.git`
    ```bash
    #进入文件夹1
    git clone git@账户1.github.com:账户1/仓库.git

    #进入文件夹2
    git clone git@账户2.github.com:账户2/仓库.git
    ```
    >如果已经克隆过的仓库，仅需要修改`.git/config`文件夹内的`url`仓库地址即可。

### 设置gitconfig
1. 用户名和邮箱

    1. 全局设置

        ```bash
        git config --global user.email 邮箱
        git config --global user.name 用户名
        ```
    2. 为具体项目设置

        ```bash
        cd 进入某个git仓库
        git config user.email 邮箱
        git config user.name 用户名
        ```
2. 全局忽略文件

    1. 添加忽略文件

        ```bash
        git config --global core.excludesfile ~/.gitignoreglobal
        ```
    2. 打开添加的文件.gitignoreglobal，填写要全局忽略的文件（夹）

        e.g.
        ```bash
        .idea
        ```

### 减少Git项目下载大小
1. 处理版本中已push的commits

    >慎重，无法恢复。

    1. 取消**至**第一个commit之后的任意commit：

        ```bash
        git reset --hard HEAD~数字      # 取消当前版本之前的N次提交
        git push origin HEAD --force    # 强制提交到远程版本库，从而删除之前的N次提交数据
        ```
        >最多能取消至第二条commit；要删除第一条commit，不如先删除仓库再创建仓库。
    2. 操作第一个commit之后的任意commit：

        ```bash
        git rebase -i --root master     # 选择commit处理状态，用s或f向上合并
        # git rebase --abort    # 取消所有rebase操作
        # git rebase --continue    # 出现冲突时候能够合并继续处理
        # git rebase --skip    # （当无法使用--continue）出现冲突时丢弃commit，会造成内容丢失（慎重使用）
        # 编辑commit信息
        git push origin HEAD --force    # 强制提交到远程版本库

        # 其他用户需要 git remote 然后 git pull origin master
        ```
        >当处理太多commits时候容易造成冲突。

    >1. [GitLab](https://about.gitlab.com/)默认设置**master**分支是**protected**状态，无法`git push --force`。
    >
    >    可以在Gitlab设置里面通过：*project* > *Settings* > *Protected branches* > *Developers can push*或*UNPROTECT*，打开权限（强烈不建议长期开启）。
    >2. Github默认允许`git push --force`。
2. 仅在Git项目中选择下载某些文件夹或文件

    >Git1.7.0以后加入了**Sparse Checkout模式**，允许Check Out指定文件或文件夹。但是只能选择一次（？），如果要更改选择的文件夹或文件，必须全部重新操作。

    1. 在空白文件夹内，创建空的本地仓库，然后将远程仓库地址加入到项目的**.git/config**文件中：

        ```bash
        git init
        git remote add -f origin 仓库地址
        ```
    2. 设置git允许使用**Sparse Checkout模式**：

        ```bash
        git config core.sparsecheckout true
        ```
    3. 选择需要单独克隆的文件或文件夹，写入 **.git/info/sparse-checkout**文件：

        ```bash
        echo 'images' >> .git/info/sparse-checkout # 所有包括有 images 的文件夹或文件（如/xxx/xxx/images/*、/images/*、images）
        echo 'js/release' >> .git/info/sparse-checkout
        ```
    4. 仅对设置过的内容进行所有git操作：

        ```bash
        git pull origin master
        ```
3. 减少克隆深度

    `git clone 仓库地址 --depth 数字`

### 恢复内容
1. 未提交的内容清空、恢复

    ```bash
    git reset --hard HEAD
    ```