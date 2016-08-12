#如何在[GitLab](https://about.gitlab.com/)项目中下载单个文件夹（s）或文件（s）

>Git1.7.0以后加入了**Sparse Checkout**模式，允许Check Out指定文件或者文件夹。

具体实现如下：

1. 新建空白文件夹，在文件夹内打开**终端**。

2. 在终端中执行命令：

    ```bash
    git init
    git remote add -f origin 项目仓库地址
    ```

    上面的代码会帮助你创建一个空的本地仓库，然后将远程**Git Server URL**加入到**/.git/config**文件中。

3. 在Config中允许使用**Sparse Checkout模式**：

    ```bash
    git config core.sparsecheckout true
    ```

4. 告诉Git哪些文件或者文件夹是你真正想Check Out的，你可以将它们作为一个列表保存在**.git/info/sparse-checkout**文件中。

    例如：
    ```bash
    echo "youxiba" >> .git/info/sparse-checkout
    echo "youpai/app" >> .git/info/sparse-checkout
    ```

5. 以正常方式从分支中将项目拉下来就可以实现对指定文件或文件夹的操作（git的各种操作）：

    ```bash
    git pull origin master
    ```

>具体可参考[Git的Sparse checkout文档](http://schacon.github.io/git/git-read-tree.html#_sparse_checkout)