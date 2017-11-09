import os
import time


def main():
    time.sleep(18000)
    while True:
        p = os.popen('tasklist|findstr python')
        res = p.readlines()
        if res:
            print "not end, waiting %s..." % str(len(res))
            time.sleep(300)
        else:
            print "start robocopy"
            os.system(r'robocopy "E:\contract\contract" "G:\yunsign" /MIR')
            break


if __name__ == '__main__':
    main()
