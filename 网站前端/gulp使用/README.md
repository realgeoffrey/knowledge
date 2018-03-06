# gulp使用

>gulp: stream building tools.

1. <details>

    <summary>Node's package for gulp(local): <a href="gulp/package.json">package.json</a></summary>

    1. `npm run gulp`
    2. `npm run gulp -- browserSync`
    3. `npm run gulp -- delRelease`
    4. `npm run gulp -- watch`

    >1. By using gulp first time, error always occurred because of the bad network when we installed plug-ins.
    >2. Some plug-ins depend on [fsevents](https://github.com/strongloop/fsevents) which is only for macOS will fail when installed by cnpm :cry:. Try [nrm](https://github.com/Pana/nrm) to change registry then use npm.
    >3. If shit happened, we should have to uninstall then install the problem plug-ins.
    </summary>
2. Gulp settings for tasks: [gulpfile.js](gulp/gulpfile.js)
    
    >[BrowserSync](https://www.browsersync.io/) is working with ajax. Blocking ajax will stop browserSync, such as [Mock.js](https://github.com/nuysoft/Mock).
3. Do not `watch` too many files(such as *node_modules* folder), to avoid checking too many files so that the watch task will take huge time.
4. [.eslintrc.js](gulp/.eslintrc.js) is for ESLint.
5. [.babelrc](gulp/.babelrc) is for Babel.
6. [.editorconfig](gulp/.editorconfig) is for IDEs' editor.
7. Handlebars settings for [spritesmith](https://github.com/twolfson/gulp.spritesmith)

    1. [pc.handlebars](gulp/pc.handlebars)
    2. [wap.handlebars](gulp/wap.handlebars)
