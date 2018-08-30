import os
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler


define("port", default=8000, type=int, help="run server on the given port.")
class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html") # 渲染主页模板，并返回给客户端。


if __name__ == "__main__":
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application(
        [
            (r'^/$', IndexHandler),
            # (r'^/view/(.*)$', StaticFileHandler, {"path":os.path.join(current_path, "statics/html")}),
        ],
        static_path=os.path.join(current_path, "statics"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()