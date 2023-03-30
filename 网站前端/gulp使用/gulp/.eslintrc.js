module.exports = {
  'root': true,
  'parserOptions': {
    'parser': 'babel-eslint'
  },
  'env': {
    'browser': true,
    'node': true,
    'es6': true
  },
  'globals': {
    // 'xla': false
  },
  'extends': [
    'standard',
    'plugin:vue/recommended'
  ],
  'plugins': [
    'html',  // eslint-plugin-html
    'vue'   // eslint-plugin-vue
  ],
  'rules': {  // 0 === 'off'; 1 === 'warn'; 2 === 'error'
    /* 重载ESLint */
    'prefer-const': [2, { 'destructuring': 'all' }],  // 在解构中，所有变量都应该是const，该规则将发出警告。否则，忽略它们
    'prefer-promise-reject-errors': 1,  // 忽略要求使用 Error 对象作为 Promise 拒绝的原因
    'no-console': 0,  // 允许console
    'max-len': [0, { 'code': 150 }],  // 设置最大长度

    /* 重载ESLint（standard） */
    'eqeqeq': 1,  // 强制使用`===/!==`替代`==/!=`
    'no-new': 0,  // 允许单独使用`new 构造函数()`，而不赋值
    'no-multi-spaces': [2, { ignoreEOLComments: true }],  // 忽略行尾注释前的多个空格
    'no-trailing-spaces': [2, { skipBlankLines: true }],  // 允许在空行使用空白符
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0, // 是否禁止debugger

    /* 重载vue */
    'vue/order-in-components': 1,  // Vue实例属性顺序
    'vue/attributes-order': 0,  // 标签的属性顺序
    'vue/no-v-html': 0, // 允许v-html
    'vue/max-attributes-per-line': 0, // 标签每行容纳属性数量
    'vue/singleline-html-element-content-newline': 0, // 允许单行标签
    'vue/component-name-in-template-casing': [1, 'PascalCase', {  // template内组件名使用方式（PascalCase/kebab-case）
      'ignores': [
        // Vue
        'component',
        'transition',
        'transition-group',
        'keep-alive',
        'slot',

        // router
        'router-link',
        'router-view',

        // nuxt
        'nuxt',
        'nuxt-child',
        'nuxt-link',
        'no-ssr'
      ]
    }]

    /* 团队选择 */
    // 'semi': [2, 'always'], // 分号
    // 'indent': [2, 4],  // 缩进长度
    // 'vue/html-indent': [2, 4]  // 模板缩进长度
  }
}
