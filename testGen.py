LIST = [1,2,3]

def gen():
    index = 0
    while True:
        if index < len(LIST):
            yield LIST[index]
            index += 1
            continue
        else:
            break
    # return None

def main():
    g = gen()
    print g.next()
    print g.next()
    print g.next()
    LIST.append(22)
    print g.next()
    LIST.append(33)
    print g.next()
    print dir(g)

if __name__ == '__main__':
    main()