# -*- encoding:utf-8-*-
import traceback
from wsgiref.simple_server import make_server


def myresponse(func):
    def encode_response(*args, **kwargs):
        body = func(*args, **kwargs)
        res = body.encode('utf-8')
        return res
    return encode_response

def init_route():
    route = {
        "/": "index",
        "/signin": "signin",
        "/login": "login",
        "/favicon.ico": "ico"
    }
    return route


class Application(object):

    def __init__(self, port):
        self.route = init_route()
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
        httpd = make_server('127.0.0.1', self.port, self.application)
        print('Serving HTTP on port %d...' % self.port)
        # 开始监听HTTP请求:
        httpd.serve_forever()


def index(request):
    return "welcome!"


def ico(request):
    with open(r"D:\myGit\test\myWeb\img\fav.png", "rb") as f:
        img = f.read()
    return img


@myresponse
def login(request):
    page = u'''<form action="/signin" method="post">
              <p>用户名：<input name="username"></p>
              <p>密  码：<input name="password" type="password"></p>
              <p><button type="submit">登录</button></p>
              </form>'''
    return page.decode("gbk")

@myresponse
def signin(request):
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='admin':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    Application(8808).run()