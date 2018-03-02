# -*- encoding:utf-8 -*-

def decorator_a(func):#这里是把f作为参数传入
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)  #这里调用的是f 最终执行的函数

    return inner_a


def decorator_b(func): #这里是把inner_a 作为参数传入
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)   #这里调用的是inner_a

    return inner_b  #此时f=inner_b

#多重装饰器 相当于函数连锁赋值   注意区别函数和函数调用的区别
@decorator_b
@decorator_a
def f(x):
    print('Get in f')
    return x * 2


print(f(1))