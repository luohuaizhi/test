from pony.orm import *

db = Database('mysql', host='rm-bp1d20s6587m22hano.mysql.rds.aliyuncs.com', passwd='IdentityFile6', user='tk_yufa', db='tk_lhz')


class Interest(db.Entity):
    product_type = Required(str, 32)
    repay_count = Required(float)
    month_interest_rate = Required(float)
    month_service_fee = Required(float)
    month_management_fee = Required(float)
    total_interest_rate = Required(float)

db.generate_mapping(create_tables = True)
