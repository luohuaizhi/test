
class A():
    cnt = 1

    def fn1(self, x):
        print "fn1", self.cnt, x

    @classmethod
    def fn2(cls, x):
        print "fn2", cls.cnt, x

    @staticmethod
    def fn3(x):
        print "fn3", x

def main():
    a=A()
    a.fn1(5)
    a.fn2(5)
    a.fn3(5)
    A.fn3(5)
    A.fn2(5)
    A.fn1(5)

if __name__ == '__main__':
    main()
