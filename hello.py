import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """主路由配置"""
    def get(self):
        """对应http的get请求"""
        self.write('Hello Itcast')

if __name__ == "__main__":
    app = tornado.web.Application([(r'/',IndexHandler),])
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServre(app)
    http_server.bind(8000)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()
