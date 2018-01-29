

def test(a, b, c, d):
    print a, b, c, d
    return "->".join([str(a), str(b), str(c), str(d)])

def test1(a, b, c, d):
    print a, b, c, d
    return "->".join([str(a), str(b), str(c), str(d)])


def test2(*args, **kwargs):
    print "args: " + str(args)
    print "kwargs: " + str(kwargs)

def main():
    param = [1,2,3,4]
    param1 = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
    }
    
    print test(*param)
    print test1(**param1)
    print test2(*param, **param1)

if __name__ == '__main__':
    main()