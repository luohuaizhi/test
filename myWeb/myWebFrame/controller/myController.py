# -*- encoding:utf-8-*-


def index(request):
    return "welcome!"


def ico(request):
    with open(r"D:\myGit\test\myWeb\img\fav.png", "rb") as f:
        img = f.read()
    return img

@myresponse
def login(request):
    page = tempalte("login.html")
    return page.decode("gbk")

@myresponse
def signin(request):
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='admin':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
