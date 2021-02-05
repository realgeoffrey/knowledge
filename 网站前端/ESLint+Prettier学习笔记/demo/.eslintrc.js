module.exports = {
  root: true,
  parser: "@typescript-eslint/parser",
  extends: ["standard", "prettier/@typescript-eslint", "plugin:prettier/recommended"],
  plugins: ["prettier"],
  rules: {
    "prettier/prettier": [
      "warn",
      {
        // 传入prettier的配置
        trailingComma: "none",
        printWidth: 120
      }
    ]
  }
};
