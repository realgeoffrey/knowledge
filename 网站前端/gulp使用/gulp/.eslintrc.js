module.exports = {
  root: true,
  parser: 'babel-eslint',
  env: {
    browser: true,
    node: true,
    es6: true,
    jquery: true
  },
  globals: {
    // 'xla': false
  },
  extends: [
    'standard'
    // 'plugin:vue/recommended' // .vue
  ],
  plugins: [  // 二选一
    'html'  // eslint-plugin-html
    // 'vue'   // eslint-plugin-vue
  ],
  rules: {  // 0 === 'off'; 1 === 'warn'; 2 === 'error'
    'no-multi-spaces': [2, { ignoreEOLComments: true }],
    'no-trailing-spaces': [2, { skipBlankLines: true }],
    'no-console': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    'max-len': [1, { 'code': 150 }],

    'vue/attribute-hyphenation': 0,
    'vue/max-attributes-per-line': 0,
    'vue/attributes-order': 0,
    'vue/order-in-components': 0

    // 'semi': [2, 'always'],
    // 'indent': [2, 4],
    // 'vue/html-indent': [2, 4]
  }
}
