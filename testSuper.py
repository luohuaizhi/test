# -*- encoding:utf-8-*-

class P(object):
    name = "parents"
    age = 100
    def __init__(self, name):
        self.name = name

    def show(self):
        print("P show")


class C(P):

    def __init__(self, name):
        self.name = name

    def show(self):
        print "C show"





def main():
    c = C("c")
    print dir(c)
    print c.age
    print c.name
    super(C, c).__init__("im c")
    print c.name
    c.__init__("im really c")
    print c.name
    c.name = "no C0"
    print c.name
    print C.name
    c.__class__.name = "parents have child c"
    print C.name
    # 调动父类已被重写的方法
    c.show()
    c.__class__ = P
    c.show()


if __name__ == '__main__':
    main()
