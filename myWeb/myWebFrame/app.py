# -*- encoding:utf-8-*-
import traceback
from wsgiref.simple_server import make_server
from urls import routes
from settings import *
from controller import *


class Application(object):

    def __init__(self, port):
        self.route = routes
        self.port = port

    def application(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        res = self.handle(environ)
        return res

    def handle(self, request):
        try:
            req_uri = request['PATH_INFO']
            handle_func = self.get_handle(req_uri)
            return handle_func(request)
        except KeyError:
            return "<h3>404 Bad Request!!!</h3>"
        except Exception as e:
            print traceback.format_exc()
            return e.message

    def get_handle(self, req_uri):  
        handle_name = self.route[req_uri]
        handle_func = eval(handle_name)
        return handle_func

    def run(self):
        httpd = make_server('', self.port, self.application)
        print('Serving HTTP on port %d...' % self.port)
        # 开始监听HTTP请求:
        httpd.serve_forever()


if __name__ == '__main__':
    Application(port).run()