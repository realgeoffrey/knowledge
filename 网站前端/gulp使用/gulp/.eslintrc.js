module.exports = {
  root: true,
  parserOptions: {
    'parser': 'babel-eslint'
  },
  env: {
    browser: true,
    node: true
  },
  extends: [
    'standard'
    // 'plugin:vue/recommended' // .vue
  ],
  plugins: [  // 二选一
    'html'  // eslint-plugin-html
    // 'vue'   // eslint-plugin-vue
  ],
  globals: {
    // '$': false
  },
  rules: {  // 0 === 'off'; 1 === 'warn'; 2 === 'error'
    'no-multi-spaces': [2, { ignoreEOLComments: true }],
    'no-trailing-spaces': [2, { skipBlankLines: true }],
    'no-console': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    'max-len': [1, { 'code': 150 }],
    // 'indent': [2, 4],
    // 'semi': [2, 'always'],

    'vue/attributes-order': 0,
    'vue/order-in-components': 0
  }
}
