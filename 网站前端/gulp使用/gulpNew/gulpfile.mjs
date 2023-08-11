import gulp from "gulp";
import imagemin, { gifsicle, mozjpeg, optipng, svgo } from "gulp-imagemin";
import pngquant from "imagemin-pngquant"; // 若出问题，则考虑GitHub520
import webp from "imagemin-webp";

/* 图片压缩 */
gulp.task("runImage", () => {
  return gulp
    .src(["./images/dev/**"])
    .pipe(
      imagemin([
        gifsicle({ optimizationLevel: 3 }), // gif压缩（无损）
        mozjpeg({ progressive: true }), // jpg压缩（有损）
        optipng({ optimizationLevel: 7 }), // png压缩（无损）
        pngquant({ speed: 1, strip: true }), // png压缩（有损）
        svgo(), //  svg压缩（无损）
      ]),
    )
    .pipe(gulp.dest("./images/release/"));
});

/* default */
gulp.task("default", gulp.parallel("runImage"));

/* 监视文件，自动执行（只能针对已经存在的文件修改，在文件夹增加的内容不会触发） */
gulp.task("watch", () => {
  gulp.watch(["./images/dev/**"], gulp.parallel("runImage"));
});

/* 图片转成webp */
gulp.task("runImageWebp", () => {
  return gulp
    .src(["./images/dev/**"])
    .pipe(
      imagemin([
        webp({ method: 6 }), // webp转换
      ]),
    )
    .pipe(gulp.dest("./images/release/"));
});
