#!/usr/bin/python
# coding:utf-8

import pymysql


"""统计nick

  CREATE TABLE fuzz.tbl_nick (
  nick VARCHAR(20) NOT NULL, --昵称
  cnnick varchar(20) null, --中文昵称
  nick_qp VARCHAR(20) NULL, --昵称的全拼
  nick_jp VARCHAR(20) NULL, --昵称的简拼
  english varchar(20) null, --出现的英文字母
  digit   varchar(10) null, --出现的数字
  counts  INT NULL,--出现的次数
  PRIMARY KEY (nick));
"""

create_sql = \
    "CREATE TABLE dict.%s (nick VARCHAR(20) NOT NULL,cn_nick VARCHAR(20) NULL," \
    "nick_qp VARCHAR(20) NULL,nick_jp VARCHAR(30) NULL," \
    "english varchar(20),digit varchar(20),counts INT NULL" \
    ")" \
    " ENGINE=MyISAM DEFAULT CHARSET=utf8;"

if __name__ == "__main__":
    myconn = pymysql.connect(host="127.0.0.1", user="root",
                             password="123456",
                             database="dict",
                             charset="utf8")


    # #假设有1Y数据那么按照一个表200w的方式创建
    tt = 1
    for i in range(1, 401, 1):
        table_name = "tbl_nick_" + str(tt)
        tt += 1
        create_table = create_sql % (table_name)
        print(create_table)
        mycur = myconn.cursor()
        mycur.execute(create_table)
        myconn.commit()
