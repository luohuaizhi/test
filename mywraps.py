import time


def count_time(func):
    def wraps():
        stime = time.time()
        func()
        etime = time.time()
        ctime = etime - stime
        print ctime
    return wraps

def count_time1(func):
    def wraps(*args):
        stime = time.time()
        func(*args)
        etime = time.time()
        ctime = etime - stime
        print ctime
    return wraps

def count_time2(func):
    def wraps(*args, **kwargs):
        stime = time.time()
        func(*args, **kwargs)
        etime = time.time()
        ctime = etime - stime
        print ctime
    return wraps

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@count_time
def main():
    time.sleep(2)
    print "Hello World !"

@count_time1
def main1(strs):
    time.sleep(2)
    print "Hello %s !" % strs

@count_time2
def main2(a, u=""):
    time.sleep(2)
    print a+" %s !" % u

def mylog(fn):
    def log():
        print "when: <"+ t2s(time.localtime()) +"> run in "+ __file__ +" --__> "+fn.func_name
        fn()
        print "when: <"+ t2s(time.localtime()) +"> run out "+ __file__ +" --__> "+fn.func_name
    return log

def t2s(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", t)

class Wrapp(object):

    cnt = 0

    def __init__(self, fn):
        # print fn.__name__
        self.cnt += 1
        self.fn = fn

    def __call__(self,  *args, **kwargs):
        # print self # <Wrapp object> not <Obj object>,  don't user class decorator in class method, can't differentiate self

        # self.cnt += 1
        print "pre call"
        self.fn(obj, *args, **kwargs)
        print "call end"

    @classmethod
    def getCnt(cls):
        print cls.cnt

class Obj(object):

    def __init__(self, name):
        self.name = name

    @Wrapp
    def test(self):
        print "i'm %s , i'm running!" % self.name

# @mylog
@Wrapp
def test(name):
    time.sleep(2)
    print "i'm %s , i'm running!" % name
    return 0


if __name__ == '__main__':
    # main()
    # main1("World")
    # main2("Hello", u="World")
    # print Wrapp.getCnt()
    # test("joke")
    # print Wrapp.getCnt()
    # test("bob")
    # print Wrapp.getCnt()
    print Wrapp.getCnt()
    Obj("joke").test()
    print Wrapp.getCnt()
    Obj("bob").test()
    print Wrapp.getCnt()
