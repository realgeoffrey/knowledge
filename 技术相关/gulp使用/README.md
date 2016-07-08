#gulp使用

1. node's package for gulp([package.json](tools/package.json))

    >By using gulp for the first time, error always occurred because of the bad network when we installed the plug-ins. If shit happened, we should have to re-install the problem plugins.

    ```json
    {
      "name": "gulp.me",
      "version": "1.3.0",
      "author": "feijie",
      "description": "my gulp tools",
      "dependencies": {
        "browser-sync": "^2.13.0",
        "gulp": "^3.9.0",
        "gulp-concat": "^2.6.0",
        "gulp-cssnano": "^2.1.2",
        "gulp-load-plugins": "^1.2.4",
        "gulp-make-css-url-version": "0.0.13",
        "gulp-rename": "^1.2.2",
        "gulp-uglify": "^1.5.4",
        "gulp.spritesmith": "^6.2.1",
        "imagemin-gifsicle": "^4.2.0",
        "imagemin-jpegtran": "^4.3.2",
        "imagemin-pngquant": "^4.2.2",
        "imagemin-svgo": "^4.2.0"
      }
    }
    ```

2. gulp settings for tasks([gulpfile.js](tools/gulpfile.js))

    ```javascript
    var jpegtran = require('imagemin-jpegtran'), /* jpg压缩*/
        pngquant = require('imagemin-pngquant'), /* png压缩*/
        gifsicle = require('imagemin-gifsicle'), /* gif压缩*/
        svgo = require('imagemin-svgo'), /* svg压缩*/
        concat = require('gulp-concat'), /* 合并文件*/
        makeUrlVer = require('gulp-make-css-url-version'), /* css中url添加版本号*/
        nano = require('gulp-cssnano'), /* css压缩*/
        rename = require('gulp-rename'), /* 重命名*/
        uglify = require('gulp-uglify'), /* js压缩*/
        browserSync = require('browser-sync').create(), /* 浏览器同步测试工具*/
        reload = browserSync.reload, /* 刷新浏览器*/
        spritesmith = require('gulp.spritesmith'), /* 生成雪碧图&样式表*/
        gulp = require('gulp');


    /* 图片任务*/
    gulp.task('doImage', function () {
        gulp.src(['../images/dev/**'])
            .pipe(jpegtran({progressive: true})())  /* jpg：压缩程度比较小*/
            .pipe(pngquant()()) /* png：能够把png8与png24压缩成png8（可透明）*/
            .pipe(gifsicle()()) /* gif*/
            .pipe(svgo()()) /* svg*/
            .pipe(gulp.dest('../images/release/'));
    });

    /* css任务*/
    gulp.task('doCss', function () {
        gulp.src(['../css/dev/*'])
            //.pipe(concat('all.css'))    /* 合并文件*/
            //.pipe(makeUrlVer()) /*路径自动添加版本号*/
            .pipe(nano({
                discardUnused: false,
                zindex: false,
                reduceIdents: false,
                mergeIdents: false
            }))
            .pipe(rename({suffix: ".min"})) /* 重命名*/
            .pipe(gulp.dest('../css/release/'));
    });

    /* js任务*/
    gulp.task('doJs', function () {
        gulp.src(['../js/dev/*'])
            //.pipe(concat('all.js'))    /* 合并文件*/
            .pipe(uglify({
                mangle: true, /* 默认：true 是否混淆变量名*/
                compress: true  /* 默认：true 是否完全压缩*/
            }))
            .pipe(rename({suffix: ".min"}))
            .pipe(gulp.dest('../js/release/'));
    });

    /* 监听代理服务器*/
    gulp.task('browserSync', function () {
        browserSync.init({
            proxy: "192.168.57.60"  /* 服务器*/
            //server: "../../" /* 相对地址*/
        });
        gulp.watch("../../**/*.html").on('change', reload);
        gulp.watch("../../**/js/**/*.js").on('change', reload);
        gulp.watch("../../**/css/**/*.css").on('change', reload);
        gulp.watch("../../**/images/**").on('change', reload);
    });

    /* 多图 -> 雪碧图 + 样式表*/
    gulp.task('sprites', function () {
        /* pc版*/
        gulp.src('../sprites/dev/*')
            .pipe(spritesmith({
                padding: 2, /* 合并图间距*/
                algorithm: 'top-down', /* 排列方式 ['binary-tree' | 'top-down' | 'left-right' | 'diagonal' | 'alt-diagonal']*/
                imgName: 'sprites.png', /* 输出合并后图片*/
                cssTemplate: 'pc.handlebars', /* 渲染输出css的模板文件*/
                cssName: 'sprites_pc.css' /* 输出合并后样式（后缀为[.css | .sass | .scss | .less | .styl/.stylus | .json]）*/
            }))
            .pipe(gulp.dest('../sprites/release/'));

        /* wap版（rem+%）*/
        gulp.src('../sprites/dev/*')
            .pipe(spritesmith({
                padding: 2,
                algorithm: 'top-down',
                imgName: 'sprites.png',
                cssTemplate: 'wap.handlebars',
                cssName: 'sprites_wap.scss'
            }))
            .pipe(gulp.dest('../sprites/release/'));
    });

    /* 监视文件，自动执行*/
    gulp.task('watch', function () {
        gulp.watch('../images/dev/**', ['doImage']);
        gulp.watch('../css/dev/**/*.css', ['doCss']);
        gulp.watch('../js/dev/**/*.js', ['doJs']);
        gulp.watch('../sprites/dev/**', ['sprites']);
    });


    /* default*/
    gulp.task('default', ['doImage', 'doCss', 'doJs', 'sprites']);
    ```
3. handlebars settings for spritesmith(gulp plugin)

    1. pc([pc.handlebars](tools/pc.handlebars)):

        ```handlebars
        {{#sprites}}
        .sprites_{{name}} {
            background: url({{{escaped_image}}}) {{px.offset_x}} {{px.offset_y}} no-repeat;
            width: {{px.width}};
            height: {{px.height}};
        }
        {{/sprites}}
        ```
    2. wap([wap.handlebars](tools/wap.handlebars)):

        ```handlebars
        @charset "utf-8";

        @function rem($px) {
            @return $px / 20 + rem;
        }

        {{#extend "scss"}}
            {{#content "sprites"}}

        // 图片类内@include
                {{#each sprites}}
        @mixin sprites_{{name}} {
            background-position: {{#if offset_x}}{{offset_x}}/({{width}}-{{total_width}})*100%{{else}}0{{/if}} {{#if offset_y}}{{offset_y}}/({{height}}-{{total_height}})*100%{{else}}0{{/if}};
            width: rem({{width}});
            height: rem({{height}});
            @extend %sprites_img;
        }
                {{/each}}
            {{/content}}

            {{#content "spritesheet"}}

        %sprites_img {
            background-image: url('{{{spritesheet.escaped_image}}}');
            background-size: rem({{spritesheet.width}}) rem({{spritesheet.height}});
            background-repeat: no-repeat;
        }
            {{/content}}
        {{/extend}}
        ```