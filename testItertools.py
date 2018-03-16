# -*- encoding:utf-8 -*-
import itertools


def main():
    # chain
    print(list(itertools.chain([1,2,3], (3,4,5))))
    # count(start=0, step=1)
    for item in itertools.count(2, 2):
        print item
        if item == 10:
            break
    # ifilter(contintion,data)
    print(list(itertools.ifilter(lambda x : x%2, [1,2,3,4,5,6,7,8,9])))
    # filterfalse(contintion,data)
    print(list(itertools.ifilterfalse(None,[1,2,0,1,0,3])))
    print(list(itertools.ifilterfalse(lambda x : x%2, [1,2,3,4,5,6,7,8,9])))
    print(list(itertools.ifilterfalse(lambda x : x < 20, (20, 30, 22, 40, 19, 1))))
    # compress()
    print(list(itertools.compress([1,0,1], ["a","b","c"])))
    # starmap(func, [])
    print(list(itertools.starmap(max,[[1,2,3],[2,3,4],[3,6,9]])))
    # repeat(object[, times])
    print(list(itertools.repeat("repeat", 5)))
    # dropwhile(func, seq );当函数f执行返回假时, 开始迭代序列
    print(list(itertools.dropwhile(lambda x: x<3, [1,2,3,4,5,6])))
    # takewhile(func, seq );当函数f执行返回假时, 停止迭代序列
    print(list(itertools.takewhile(lambda x: x>4, [1,2,3,4,5,6])))
    # islice(seq[, start], stop[, step]);
    print(list(itertools.islice(itertools.count(10), 5)))
    print(list(itertools.islice("1234567890", 1, 8, 2)))
    # cycle(seq, times)
    print(list(itertools.islice(itertools.cycle("abc"), 8)))
    # 建一个迭代器，生成项imap(fn, [], [])
    print(list(itertools.imap(lambda x,y:"imap: "+str(x)+"+"+str(y), [2,2,2], [3,3,3,4])))
    # product(iter1,iter2, ... iterN, [repeat=1])
    # 创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数
    for i in itertools.product([1,2,3], [4,5,6], [7,8,9], repeat=1):
        print i
    for i in itertools.product([1,2,3], [4,5,6], repeat=2):
    # for i in itertools.product([1,2,3], [4,5,6], [1,2,3], [4,5,6], repeat=1):
        print i
    # permutations(p[,r]);返回p中任意取r个元素做排列的元组的迭代器
    for i in itertools.permutations([1, 2, 3], 3):
        print i
    # combinations(iterable,r);创建一个迭代器，返回iterable中所有长度为r的子序列, note:不带重复
    print(list(itertools.combinations([1,2,3], 2)))
    # combinations_with_replacement() 带重复
    print(list(itertools.combinations_with_replacement([1,2,3], 2)))
    # tee(iterable [, n])-> (<itertools.tee object at 0x0288CAA8>, <itertools.tee object at 0x0288CAD0>, ...)
    t1 = itertools.tee([1,2,3], 2)[1]
    for i in t1:
        print i


if __name__ == '__main__':
    main()
