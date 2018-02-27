import sys
import traceback


class MyError(Exception):
    def __init__(self, value="this is my test error"):
        Exception.__init__(self, value)
        # self.value = value


def main():
    try:
        print "this is my exception demo"
        raise MyError
    except MyError as e:
        print e
        print sys.exc_info()
        print traceback.format_exc()
    except Exception as e:
        print e
        print traceback.format_exc()
    else:
        print "everything is ok"
    finally:
        print "It`s always to there"

if __name__ == '__main__':
    main()
