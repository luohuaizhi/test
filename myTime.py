#-*-coding:UTF-8-*-
from datetime import datetime, timedelta


def main():
    t=datetime.now()
    ts = t.strftime(u"%Y年%m月%d日".encode("gbk"))
    # ts = t.strftime("%Y年%m月%d日".decode("utf-8").encode("gbk"))
    print(ts)
    bt = t-timedelta(days=3)
    print bt
    nt = t+timedelta(days=1)
    print nt
   


if __name__ == '__main__':
    main()