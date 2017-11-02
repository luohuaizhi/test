#-*-coding:UTF-8-*-
from datetime import datetime


def main():
    t=datetime.now()
    ts = t.strftime(u"%Y年%m月%d日".encode("gbk"))
    # ts = t.strftime("%Y年%m月%d日".decode("utf-8").encode("gbk"))
    print(ts)
   


if __name__ == '__main__':
    main()