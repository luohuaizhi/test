# -*- encoding:utf-8 -*-
import random


def main():
    """
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'System
    Random', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType', '__all__'
    , '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_acos', '_c
    eil', '_cos', '_e', '_exp', '_hashlib', '_hexlify', '_inst', '_log', '_pi', '_ra
    ndom', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betava
    riate', 'choice', 'division', 'expovariate', 'gammavariate', 'gauss', 'getrandbi
    ts', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate', 'paretovariate'
    , 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'tr
    iangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
    """
    print random.random()  # 随机返回一个0~1浮点数
    print random.randint(0, 9)  # 随机返回0,9之间的整数
    print random.randrange(0, 9)  # 随机返回0,9之间的整数
    print random.uniform(1, 9)  # 随机返回1,9之间的浮点数
    l = [1, 2, 3, 4]
    print random.choice(l)  # 随机选择一个列表项
    print random.sample(l, 2)  # 随机从l中得到一个子列表长度为2


if __name__ == "__main__":
    main()