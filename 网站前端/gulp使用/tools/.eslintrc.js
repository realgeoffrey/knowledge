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
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    'max-len': [1, 120]
  },
};
// npm install eslint babel-eslint eslint-plugin-html eslint-plugin-standard eslint-plugin-promise eslint-plugin-node eslint-plugin-import eslint-config-standard -g