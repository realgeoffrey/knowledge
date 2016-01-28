var imagemin = require('gulp-imagemin'), /* imagemin*/
    svgo = require('imagemin-svgo'), /* svg压缩*/
    gifsicle = require('imagemin-gifsicle'), /* gif压缩*/
    jpegtran = require('imagemin-jpegtran'), /* jpg压缩*/
    pngquant = require('imagemin-pngquant'), /* png压缩*/
    optipng = require('imagemin-optipng'), /* png压缩*/
    sourcemaps = require('gulp-sourcemaps'), /* source map*/
    concat = require('gulp-concat'), /* 合并文件*/
    nano = require('gulp-cssnano'), /* css压缩*/
    postcss = require('gulp-postcss'), /* css工具*/
    autoprefixer = require('autoprefixer'), /* 添加css厂家前缀*/
    rename = require('gulp-rename'), /* 重命名*/
    makeUrlVer = require('gulp-make-css-url-version'), /* css添加时间戳*/
    sass = require('gulp-sass'), /* 编译sass*/
    uglify = require('gulp-uglify'), /* js压缩*/
    spritesmith = require('gulp.spritesmith'), /* 生成雪碧图&样式表*/
    fontmin = require('gulp-fontmin'), /* 字体子集化*/
    browserSync = require('browser-sync').create(), /* 浏览器同步测试工具*/
    gulp = require('gulp');

/* 图片压缩*/
gulp.task('doImage', function () {
    gulp.src(['../images/dev/**'])
        .pipe(
            imagemin([
                svgo(),
                gifsicle({optimizationLevel: 3}),
                jpegtran({progressive: true}),
                pngquant({speed: 1}),
                optipng({optimizationLevel: 7})
            ]))
        .pipe(gulp.dest('../images/release/'));
});

/* css：[合并]、压缩、添加厂商前缀、重命名、添加timestamp、source map*/
gulp.task('doCss', function () {
    gulp.src(['../css/dev/**/*.css'])
        .pipe(sourcemaps.init())
        //.pipe(concat('all.css'))
        .pipe(nano({
            discardUnused: false,
            zindex: false,
            reduceIdents: false,
            mergeIdents: false
        }))
        .pipe(postcss([autoprefixer()]))
        .pipe(rename({suffix: '.min'}))
        .pipe(makeUrlVer({useDate: true}))  //不被gulp-sourcemaps支持
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('../css/release/'));
});

/* scss：转译压缩css、添加厂商前缀、添加timestamp、source map*/
gulp.task('doScss', function () {
    gulp.src(['../scss/dev/**/*.scss'])
        .pipe(sourcemaps.init())
        .pipe(
            sass({outputStyle: 'compressed'}).on('error', sass.logError)
        )
        .pipe(postcss([autoprefixer()]))
        .pipe(makeUrlVer({useDate: true}))  //不被gulp-sourcemaps支持
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('../scss/release/'));
});

/* js：[合并]、压缩、重命名、source map*/
gulp.task('doJs', function () {
    gulp.src(['../js/dev/**/*.js'])
        .pipe(sourcemaps.init())
        //.pipe(concat('all.js'))
        .pipe(uglify({
            mangle: true, /* 默认：true 是否混淆变量名*/
            compress: true  /* 默认：true 是否完全压缩*/
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('../js/release/'));
});

/* 多图 -> 雪碧图 + 样式表*/
gulp.task('doSprites', function () {
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

/* ttf -> 多个兼容字体 + 样式表*/
gulp.task('doFont', function (cb) {
    var buffers = [];

    gulp.src(['../font/dev/*.html'])    /* 传入需要提取字体的页面，没有页面则所有字*/
        .on('data', function (file) {
            buffers.push(file.contents);
        })
        .on('end', function () {
            var text = Buffer.concat(buffers).toString('utf-8');
            gulp.src(['../font/dev/*.ttf']) /* 只能传入ttf类型*/
                .pipe(fontmin({text: text}))
                .pipe(gulp.dest('../font/release/'))
                .on('end', cb);
        });
});

/* default*/
gulp.task('default', ['doImage', 'doCss', 'doScss', 'doJs', 'doSprites', 'doFont']);

/* 监视文件，自动执行*/
gulp.task('watch', function () {
    gulp.watch(['../images/dev/**'], ['doImage']);
    gulp.watch(['../css/dev/**/*.css'], ['doCss']);
    gulp.watch(['../scss/dev/**/*.scss'], ['doScss']);
    gulp.watch(['../js/dev/**/*.js'], ['doJs']);
    gulp.watch(['../sprites/dev/**'], ['doSprites']);
    gulp.watch(['../font/dev/**'], ['doFont']);
});

/* 监听代理服务器*/
gulp.task('browserSync', function () {
    browserSync.init({
        proxy: 'localhost'  /* 服务器*/
        //server: '../../www/' /* 相对地址*/
    });
    gulp.watch([
        '../../www/**/*.html',
        '../../www/**/js/**/*.js',
        '../../www/**/css/**/*.css',
        '../../www/**/images/**'
    ]).on('change', browserSync.reload);    //刷新浏览器
});