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
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print "pre call"
        self.fn(*args, **kwargs)
        print "call end"

# @mylog
@Wrapp
def test():
    time.sleep(2)
    print "im running!"
    return 0


if __name__ == '__main__':
    # main()
    # main1("World")
    # main2("Hello", u="World")
    test()
