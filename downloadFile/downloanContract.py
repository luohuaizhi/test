import os
import urllib2
import MySQLdb


# URL='''https://www.yunsign.com/mmecserver3.0/httpDownload.do?isPdf=pdf&orderId=201710230932481935288&isHandWrite=Y&isForceSeal=Y&signType=md5&userId=13009640604&isSeal=N&certType=1&validType=SMS&time=1505900427600&appId=j7GP6sb57R&sign=6cb183e1a857fbf4642355b2340b0225'''
URL='''https://www.yunsign.com/mmecserver3.0/httpDownload.do?isPdf=pdf&orderId=%s&isHandWrite=Y&isForceSeal=Y&signType=md5&userId=13009640604&isSeal=N&certType=1&validType=SMS&time=1505900427600&appId=j7GP6sb57R&sign=6cb183e1a857fbf4642355b2340b0225'''
HOST="rr-bp1lvuaxx414eav97o.mysql.rds.aliyuncs.com"
DATABASE="tk_online"
USER="ol_read"
PWD="eETq0kKYXzBM97"
SQL='''SELECT contract_id, name, order_number, sign_time FROM `contract` LEFT JOIN `user` on `contract`.owner_id=`user`.id  where sign_type="YUNSIGN"  ORDER BY sign_time '''


def query(query_sql):
    mysql_conn = MySQLdb.Connect(host=HOST, user=USER, passwd=PWD, db=DATABASE, charset='utf8')
    cursor = mysql_conn.cursor()
    print query_sql
    cursor.execute(query_sql)
    data = cursor.fetchall()
    # print data
    cursor.close()
    mysql_conn.close()
    return data


def main():
    print "--------strart query-----------"
    data = query(SQL)
    print "--------query end   -----------"
    num = len(data)
    print num
    i = 0 
    print "--------start download-----------"
    return
    for record in data:
        i += 1
        print "--------- lave : %d --------"%(num-i)
        contract_id, user, order_id, sign_time = record
        date_folder = str(sign_time)[0:7]
        if not os.path.exists(date_folder):
            os.mkdir(date_folder)
        file_name = "%s-%s.pdf" % (order_id, user)
        file_path = os.path.join(date_folder, file_name)
        if os.path.exists(file_path):
            continue
        down_url = URL % contract_id
        # print down_url
        res = urllib2.urlopen(down_url)
        # print contact_file.headers
        content = res.read()
        with open(file_path, "wb") as f:
            f.write(content)

    print "-------- download end -----------"


if __name__ == '__main__':
    os.chdir('contract')
    main()
