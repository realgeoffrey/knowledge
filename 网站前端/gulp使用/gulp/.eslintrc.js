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
  ],
  plugins: [
    'html'
  ],
  globals: {
    //    '$': false
  },
  rules: {
    'arrow-parens': 0,
    'generator-star-spacing': 0,
    'space-before-function-paren': 0,
    'no-multi-spaces': [2, { ignoreEOLComments: true }],
    'no-trailing-spaces': [2, { skipBlankLines: true }],
    'no-console': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,

    // 'indent': [2, 4],
    'semi': [2, 'always'],
    'max-len': [1, { 'code': 150 }]
  }
};
