from functools import wraps

DEC = 0


class WrapException(Exception):

    def __repr__(self):
        return "wrapper error!"

def re_try1(maxtry):
    print locals()
    def wrapper(fn):
        print locals()
        def _wrapper(*args, **kwargs):
            print locals()
            while maxtry > 0:
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    print e.message
                maxtry -= 1
        return _wrapper
    return wrapper


def re_try(max_try):
    print locals()
    def wrapper(func):
        print locals()
        @wraps(func)
        def _wrapper(*args, **kw):
            print locals()
            for i in xrange(max_try):
                try:
                    res = func(*args, **kw)
                    if res is None:
                        continue
                    else:
                        return res 
                except Exception as e:
                    print e.message
        return _wrapper
    return wrapper

@re_try(4)
def test(a, b):
    # return a+b
    if DEC == 2:
        return a+b
    else:
        raise WrapException

def main():
    print test(3,5)

if __name__ == '__main__':
    main()

