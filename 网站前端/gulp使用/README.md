# gulp使用

>stream building tools.

1. Node's package for gulp(local): [package.json](tools/package.json)

    >1. By using gulp for the first time, error always occurred because of the bad network when we installed plug-ins.
    >2. If shit happened, we should have to uninstall then install the problem plug-ins.
2. Gulp settings for tasks: [gulpfile.js](tools/gulpfile.js)
    
    >[BrowserSync](https://www.browsersync.io/) is working with ajax. Blocking ajax will stop browserSync, such as [Mock.js](https://github.com/nuysoft/Mock).
3. Do not `watch` too many files(such as *node_modules* folder), to avoid checking too many files so that the watch task will take huge time.
4. Handlebars settings for [spritesmith](https://github.com/twolfson/gulp.spritesmith)

    1. [pc.handlebars](tools/pc.handlebars)
    2. [wap.handlebars](tools/wap.handlebars)
5. [.eslintrc.js](tools/.eslintrc.js) is for ESLint.
