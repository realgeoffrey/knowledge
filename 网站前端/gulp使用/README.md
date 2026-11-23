### gulp使用

>gulp: stream building tools.

#### [仅图片压缩](./gulpNew)
进入 `gulpNew/`，运行 `npm install` 安装图片压缩工具。

1. `npm run gulp`图片压缩
2. `npm run gulpWatch`watch图片压缩
3. `npm run gulpWebp`图片转成webp

#### [完整使用](./gulp)
进入 `gulp/` 后，先确认 Node.js 版本和架构，再运行 `npm install`。这个旧示例的 `gulp-sass@4` 依赖原生扩展 `node-sass@4`。例如，`node-sass@4.14.1` 为 x64 的 Node.js 14 提供预编译文件。[gulp-sass 依赖](https://github.com/dlmanning/gulp-sass/blob/v4.1.1/package.json) · [node-sass 支持的环境](https://github.com/sass/node-sass/releases/tag/v4.14.1)

1. <details>

    <summary>Node.js' package for gulp(local): <a href="./gulp/package.json">package.json</a></summary>

    1. `npm run gulp`
    2. `npm run gulp -- browserSync`

        >本例用 `gulp.watch(...).on('change', browserSync.reload)` 监听文件变化，并通知已连接的浏览器刷新。
    3. `npm run gulp -- delRelease`
    4. `npm run gulp -- watch`

    >1. By using gulp first time, error always occurred because of the bad network when we installed plug-ins.
    >2. Some plug-ins depend on [fsevents](https://github.com/strongloop/fsevents) which is only for macOS will fail when installed by cnpm :cry:. Try [nrm](https://github.com/Pana/nrm) to change registry then use npm.
    >3. If shit happened, we should have to uninstall then install the problem plug-ins.
    </details>
2. Gulp settings for tasks: [gulpfile.js](gulp/gulpfile.js)

    >[BrowserSync](https://browsersync.io/docs/gulp) 的客户端脚本需要连接开发服务器，才能接收刷新通知。
3. Do not `watch` too many files(such as *node_modules* folder), to avoid checking too many files so that the watch task will take huge time.
4. [.eslintrc.js](gulp/.eslintrc.js) is for ESLint.
5. [.babelrc](gulp/.babelrc) is for Babel.
6. [.editorconfig](gulp/.editorconfig) is for IDEs' editor.
7. Handlebars settings for [spritesmith](https://github.com/twolfson/gulp.spritesmith)

    1. [pc.handlebars](gulp/pc.handlebars)
    2. [wap.handlebars](gulp/wap.handlebars)

>When install error occurs, please try cnpm or yarn.
