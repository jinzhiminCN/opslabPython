
# coding:utf-8

import pymysql

create_sql = "create table dicts.tbl_cnnick_%d(" \
             "cn_nick VARCHAR(20)," \
             "nick_qp VARCHAR(20)," \
             "nick_jp VARCHAR(30)," \
             "counts int)ENGINE=MyISAM DEFAULT CHARSET=utf8;"

if __name__ == "__main__":
    myconn = pymysql.connect(host="127.0.0.1", user="root",
                             password="123456",
                             database="dicts",
                             charset="utf8")

    mycur = myconn.cursor()
    for i in range(1, 401, 1):
        print (create_sql % (i))
        mycur.execute(create_sql % (i))

    myconn.commit()