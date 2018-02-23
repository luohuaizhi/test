# -*- encoding:utf-8-*-

class Obj(object):

    def __call__(self, name):
        print "__call__ of %s" % name

    def __new__(cls, name):
        print "__new__"
        return super(Obj, cls).__new__(cls)

    # def __new__(cls, name, bases, attrs):
    #     print "__new__"
    #     return super(Obj, cls).__new__(cls, name, bases, attrs)

    def __init__(self, name):
        self.name = name
        print "__init__"

    def __del__(self):
        print "I'm del"

    def mydefault(self, *args):
        print "default"        

    def __getattr__(self, name):
        print "call fn: ", name
        return self.mydefault



def main():
    obj = Obj("test")
    print obj.name
    obj("james")
    obj.tt()


if __name__ == '__main__':
    main()
