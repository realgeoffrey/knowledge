WAP和PC是两套独立示例，按页面选用。

```css
/* WAP端媒体查询（320px~640px），单行最大width:32rem */
html {font-size: 10px;}
@media (min-width: 352px) {
  html {font-size: 11px;}
}
@media (min-width: 384px) {
  html {font-size: 12px;}
}
@media (min-width: 416px) {
  html {font-size: 13px;}
}
@media (min-width: 448px) {
  html {font-size: 14px;}
}
@media (min-width: 480px) {
  html {font-size: 15px;}
}
@media (min-width: 512px) {
  html {font-size: 16px;}
}
@media (min-width: 544px) {
  html {font-size: 17px;}
}
@media (min-width: 576px) {
  html {font-size: 18px;}
}
@media (min-width: 608px) {
  html {font-size: 19px;}
}
@media (min-width: 640px) {
  html {font-size: 20px;}
}
/* /WAP端媒体查询 */
```

```css
/* PC端媒体查询（960px~2560px），单行最大width:32rem */
html {font-size: 30px;}
@media (min-width: 992px) {
  html {font-size: 31px;}
}
@media (min-width: 1024px) {
  html {font-size: 32px;}
}
@media (min-width: 1056px) {
  html {font-size: 33px;}
}
@media (min-width: 1088px) {
  html {font-size: 34px;}
}
@media (min-width: 1120px) {
  html {font-size: 35px;}
}
@media (min-width: 1152px) {
  html {font-size: 36px;}
}
@media (min-width: 1184px) {
  html {font-size: 37px;}
}
@media (min-width: 1216px) {
  html {font-size: 38px;}
}
@media (min-width: 1248px) {
  html {font-size: 39px;}
}
@media (min-width: 1280px) {
  html {font-size: 40px;}
}
@media (min-width: 1312px) {
  html {font-size: 41px;}
}
@media (min-width: 1344px) {
  html {font-size: 42px;}
}
@media (min-width: 1376px) {
  html {font-size: 43px;}
}
@media (min-width: 1408px) {
  html {font-size: 44px;}
}
@media (min-width: 1440px) {
  html {font-size: 45px;}
}
@media (min-width: 1472px) {
  html {font-size: 46px;}
}
@media (min-width: 1504px) {
  html {font-size: 47px;}
}
@media (min-width: 1536px) {
  html {font-size: 48px;}
}
@media (min-width: 1568px) {
  html {font-size: 49px;}
}
@media (min-width: 1600px) {
  html {font-size: 50px;}
}
@media (min-width: 1632px) {
  html {font-size: 51px;}
}
@media (min-width: 1664px) {
  html {font-size: 52px;}
}
@media (min-width: 1696px) {
  html {font-size: 53px;}
}
@media (min-width: 1728px) {
  html {font-size: 54px;}
}
@media (min-width: 1760px) {
  html {font-size: 55px;}
}
@media (min-width: 1792px) {
  html {font-size: 56px;}
}
@media (min-width: 1824px) {
  html {font-size: 57px;}
}
@media (min-width: 1856px) {
  html {font-size: 58px;}
}
@media (min-width: 1888px) {
  html {font-size: 59px;}
}
@media (min-width: 1920px) {
  html {font-size: 60px;}
}
@media (min-width: 1952px) {
  html {font-size: 61px;}
}
@media (min-width: 1984px) {
  html {font-size: 62px;}
}
@media (min-width: 2016px) {
  html {font-size: 63px;}
}
@media (min-width: 2048px) {
  html {font-size: 64px;}
}
@media (min-width: 2080px) {
  html {font-size: 65px;}
}
@media (min-width: 2112px) {
  html {font-size: 66px;}
}
@media (min-width: 2144px) {
  html {font-size: 67px;}
}
@media (min-width: 2176px) {
  html {font-size: 68px;}
}
@media (min-width: 2208px) {
  html {font-size: 69px;}
}
@media (min-width: 2240px) {
  html {font-size: 70px;}
}
@media (min-width: 2272px) {
  html {font-size: 71px;}
}
@media (min-width: 2304px) {
  html {font-size: 72px;}
}
@media (min-width: 2336px) {
  html {font-size: 73px;}
}
@media (min-width: 2368px) {
  html {font-size: 74px;}
}
@media (min-width: 2400px) {
  html {font-size: 75px;}
}
@media (min-width: 2432px) {
  html {font-size: 76px;}
}
@media (min-width: 2464px) {
  html {font-size: 77px;}
}
@media (min-width: 2496px) {
  html {font-size: 78px;}
}
@media (min-width: 2528px) {
  html {font-size: 79px;}
}
@media (min-width: 2560px) {
  html {font-size: 80px;}
}
/* /PC端媒体查询 */
```

>每档从标出的宽度起生效。例如WAP端在351.5px时仍用10px，从352px起用11px。需要随视口宽度连续缩放时可用`vw`。
