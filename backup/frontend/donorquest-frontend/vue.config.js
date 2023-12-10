module.exports = {
    publicPath: 'http://localhost:8080'
    outputDir: '.././backend/static/dist',
    indexPath: '.././backend/donation/templates/_base.html',
    configureWebpack: {
        devServer: {
            // headers: { "Access-Control-Allow-Origin": "*" }
            devMiddleware: {
                writeToDisk: true
            }
        }
    }
}  