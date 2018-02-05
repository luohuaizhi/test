# -*-encoding:utf-8-*-
import sys

end = 0 # 终点
cnt = 0 # 统计组合方式

def jump(start):
    global cnt
    for i in [1,2]:
        cur = str(start)+"+"+str(i)
        if eval(cur) >= end:
            print cur
            cnt += 1
            continue
        jump(cur)


def main(n):
    """
    一只青蛙一次可以跳1阶或者2阶，n阶，有多少种到达终点的方式。(递归)
    """
    global end
    end = n
    jump(0)
    print "count: "+str(cnt)
    


if __name__ == "__main__":
    main(int(sys.argv[1]))