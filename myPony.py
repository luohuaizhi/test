# encoding=utf-8
from pony.orm import *

db = Database()
db.bind("mysql", host="rm-bp1d20s6587m22hano.mysql.rds.aliyuncs.com", user="tk_yufa", passwd="IdentityFile6", db="tk_yufa")



class Global_Settings(db.Entity):
    key = PrimaryKey(str)
    value = Required(str)


class Zhimas(db.Entity):
    uid = Required(str,16)
    name = Required(str, 64)
    date = Required(str, 64)
    id_no = Required(str,20)
    url = Required(str, 255)
    zm_score = Required(int)
    zm_ivs = Required(int)


@db_session
def main():
    sql_debug(True)
    db.generate_mapping(create_tables=False)
    conf = select(c for c in Global_Settings if c.key == "choose:sign_server").get()
    print conf.value
    # zhima = select(r for r in Zhimas)
    # print zhima[0]

if __name__ == '__main__':
    main()
    