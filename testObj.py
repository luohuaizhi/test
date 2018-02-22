# -*- encoding:utf-8-*-

class Obj(object):

    def __call__(self, name):
        print "__call__ of %s" % name

    # def __new__(cls, name, bases, attrs):
    #     print "__new__"
    #     return super(Obj, cls).__new__(cls, name, bases, attrs)

    def __init__(self, name):
        self.name = name
        print "__init__"

    def __del__(self):
        print "I'm del"



def main():
    obj = Obj("test")
    print obj.name
    obj("james")


if __name__ == '__main__':
    main()
