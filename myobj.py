class Parent(object):
    
    def __init__(self):
        print 3333333333


class Son(Parent):

    def __init__(self):
        Parent.__init__(self)
    
    def out(self):
        print 1234567890


if __name__ == '__main__':
    print "111111"
    s = Parent.Son()
    s.out()
    print "222222222"