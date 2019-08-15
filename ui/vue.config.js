module.exports = {
  runtimeCompiler: true,
  filenameHashing: false,

  chainWebpack: config => {
    const fontRule = config.module.rule('fonts').use('url-loader')
    fontRule.options({
      limit: 400000
    })
  }
}
