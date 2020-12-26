module.exports = {
  root: true,
  extends: ["standard", "plugin:prettier/recommended"],
  plugins: ["prettier"],
  rules: {
    "prettier/prettier": [
      "error",
      {
        // 传入prettier的配置
        trailingComma: "none"
      }
    ]
  }
};
