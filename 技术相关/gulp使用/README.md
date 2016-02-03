#gulp使用

- node's package for gulp

>By using gulp for the first time, error always occurred because of the bad network when we installed the plug-ins. If shit happened, we should have to re-install the problem plug-ins.

```json
{
    "name": "gulp.me",
    "version": "1.1.0",
    "author": "feijie",
    "description": "my gulp tools",
    "dependencies": {
        "browser-sync": "^2.11.1",
        "gulp": "^3.9.0",
        "gulp-concat": "^2.6.0",
        "gulp-cssnano": "^2.1.0",
        "gulp-load-plugins": "^1.2.0",
        "gulp-make-css-url-version": "0.0.13",
        "gulp-rename": "^1.2.2",
        "gulp-uglify": "^1.5.1",
        "imagemin-gifsicle": "^4.2.0",
        "imagemin-jpegtran": "^4.3.2",
        "imagemin-pngquant": "^4.2.0",
        "imagemin-svgo": "^4.2.0"
    }
}
```

- gulp settings for tasks


```javascript
var rename = require('gulp-rename'), /* 重命名*/
    concat = require('gulp-concat'), /* 合并文件*/
    jpegtran = require('imagemin-jpegtran'), /* jpg压缩*/
    pngquant = require('imagemin-pngquant'), /* png压缩*/
    gifsicle = require('imagemin-gifsicle'), /* gif压缩*/
    svgo = require('imagemin-svgo'), /* svg压缩*/
    nano = require('gulp-cssnano'), /* css压缩*/
    makeUrlVer = require('gulp-make-css-url-version'), /* css中url添加版本号*/
    uglify = require('gulp-uglify'), /* js压缩*/
    browserSync = require('browser-sync').create(), /* 同步修改*/
    reload = browserSync.reload, /* 刷新*/
    gulp = require('gulp');


/* 图片任务*/
gulp.task('doImage', function () {
    gulp.src(['../images/dev/**'])
        .pipe(jpegtran({progressive: true})())  /* jpg*/
        .pipe(pngquant()()) /* png*/
        .pipe(gifsicle()()) /* gif*/
        .pipe(svgo()()) /* svg*/
        .pipe(gulp.dest('../images/release/'));
});

/* css任务*/
gulp.task('doCss', function () {
    gulp.src(['../css/dev/*'])
        //        .pipe(concat('all.css'))    /* 合并文件*/
        .pipe(makeUrlVer()) /*路径自动添加版本号*/
        .pipe(nano({
            /* 压缩css*/
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
        //        .pipe(concat('all.js'))    /* 合并文件*/
        .pipe(uglify({
            /* js压缩*/
            mangle: true, /* 默认：true 是否混淆变量名*/
            compress: true  /* 默认：true 是否完全压缩*/
        }))
        .pipe(rename({suffix: ".min"}))
        .pipe(gulp.dest('../js/release/'));
});

/* 监听代理服务器*/
gulp.task('browserSync', function () {
    browserSync.init({
        proxy: "192.168.57.60"
    });
    gulp.watch("../../**/*.html").on('change', reload);
    gulp.watch("../../**/js/**").on('change', reload);
    gulp.watch("../../**/css/**").on('change', reload);
    gulp.watch("../../**/images/**").on('change', reload);
});

/* 监视文件，自动执行*/
gulp.task('watch', function () {
    gulp.watch('../images/dev/**', ['doImage']);
    gulp.watch('../css/dev/*.css', ['doCss']);
    gulp.watch('../js/dev/*.js', ['doJs']);
});


/* default*/
gulp.task('default', ['doImage', 'doCss', 'doJs']);
```