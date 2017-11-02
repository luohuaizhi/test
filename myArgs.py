def main(a1, *args):
    print len(args)
    print a1
    print args


if __name__ == '__main__':
    try:
        main("aaaaaa111", 1,2,3,4)
    except Exception as e:
        print e.message
    else:
        pass
    finally:
        pass