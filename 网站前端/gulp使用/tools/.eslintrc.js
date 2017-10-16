module.exports = {
  root: true,
  parser: 'babel-eslint',
  extends: 'standard',
  plugins: [
    'html'
  ],
  rules: {
    'arrow-parens': 0,
    'generator-star-spacing': 0,
    'space-before-function-paren': 0,
    'no-console': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,

    'max-len': [1, 120]
  }
}