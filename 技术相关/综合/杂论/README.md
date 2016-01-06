#杂论

##CSS
- 限定布局宽度，让内容决定布局高度。

- z-index用于控制设置了absolute、relative或fixed定位的元素。
应该只给有堆叠关系的节点设置此属性，而不要试图通过设定个别元素的z-index来确保元素不重叠。

- 用css创造三角形
'''css
div {
    border: 12px solid;
    border-color: transparent #000 transparent transparent;
    height: 0;
    width: 0;
}
```