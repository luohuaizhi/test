# coding=utf-8


class Test(object):
    """docstring for Test"""
    def __init__(self):
        super(Test, self).__init__()
        
    def fn(self, a, b):
        print a+b

    def fn1(self, *a, **b):
        return self.fn(*a, **b)


if __name__ == '__main__':
    Test().fn1(1, 2)