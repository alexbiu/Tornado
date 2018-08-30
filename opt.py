import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config

tornado.options.define('port',default=8000,type=int,help='run server...')
tornado.options.define('itcast',default=[],type=str,multiple=True,help='incast subject...')

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http请求方式"""
        self.write('hello Itcast')

if __name__ == '__main__':
    # tornado.options.parse_command_line()
    tornado.options.parse_config_file('./config')
    print(tornado.options.options.itcast)
    print(tornado.options.options.port)
    app = tornado.web.Application([(r'/',IndexHandler),])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
