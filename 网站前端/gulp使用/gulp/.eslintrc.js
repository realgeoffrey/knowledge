module.exports = {
  'root': true,
  'parserOptions': {
    'parser': 'babel-eslint'
  },
  'env': {
    'browser': true,
    'node': true,
    'es6': true,
    'jquery': true
  },
  'globals': {
    // 'xla': false
  },
  'extends': [
    'standard'
    // 'plugin:vue/recommended' // .vue
  ],
  'plugins': [  // 二选一
    'html'  // eslint-plugin-html
    // 'vue'   // eslint-plugin-vue
  ],
  'rules': {  // 0 === 'off'; 1 === 'warn'; 2 === 'error'
    /* 重载standard */
    'eqeqeq': 1,  // 强制使用`===/!==`代替`==/!=`
    'no-new': 0,  // 允许单独使用`new 构造函数()`，而不赋值
    'no-multi-spaces': [2, { ignoreEOLComments: true }],  // 忽略行尾注释前的多个空格
    'no-trailing-spaces': [2, { skipBlankLines: true }],  // 允许在空行使用空白符
    'no-console': 0,  // 允许console
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0, // 是否禁止debugger
    'max-len': [1, { 'code': 150 }],  // 设置最大长度

    /* 重载vue */
    'vue/max-attributes-per-line': 0, // 标签每行最多的属性
    'vue/attributes-order': 0,  // 标签的属性顺序
    'vue/order-in-components': 0  // Vue实例属性顺序

    /* 不在vue预设内 */
    // （eslint-plugin-vue v5.0.0+）强制template内组件使用的命名方式（默认：都可以；'PascalCase'；'kebab-case'）
    // 'vue/component-name-in-template-casing': [1, 'PascalCase']

    /* 团队选择 */
    // 'semi': [2, 'always'], // 分号
    // 'indent': [2, 4],  // 缩进长度
    // 'vue/html-indent': [2, 4]  // 模板缩进长度
  }
}
