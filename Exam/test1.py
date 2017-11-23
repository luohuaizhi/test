class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

A = zip(('a','b','c','d','e'),(1,2,3,4,5))
print A
A0 = dict(A)
print A0
A1 = range(10)
print A1
A2 = [i for i in A1 if i in A0]
print A2
A3 = [A0[s] for s in A0]
print A3
A4 = [i for i in A1 if i in A3]
print A4
A5 = {i:i*i for i in A1}
print A5
A6 = [[i,i*i] for i in A1]
print A6


# 1 1 1
# 1 2 1
# 3 2 3
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# []
# [1, 3, 2, 5, 4]
# [1, 2, 3, 4, 5]
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

