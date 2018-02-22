# -*- encoding:utf-8-*-

class P(object):
    name = "parents"
    age = 100
    def __init__(self, name):
        self.name = name

class C(P):

    def __init__(self, name):
        self.name = name
    





def main():
    in_1 = input("please accept a number: ")
    print type(in_1)
    in_2 = raw_input("please accept a number: ")
    print type(in_2)



if __name__ == '__main__':
    main()
