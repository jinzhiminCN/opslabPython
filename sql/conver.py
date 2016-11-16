#! /usr/bin/python
# coding:utf-8

import pymssql
import pymysql

#需要用到使用pymssql组件可以使用pip install pymssql进行安装
msconn = pymssql.connect(host="127.0.0.1", user="sa", password="wyb2212852", database="GroupData1", charset='utf8')
myconn = pymysql.connect(host="127.0.0.1", user="root", password="wyb2212852", database="0psdb", charset="utf8")
#需要用到端口号时
# conn = pymssql.connect(host="127.0.0.1",port="端口号",user="sa",password="123",database="Northwind")

#获取游标
mscur = msconn.cursor()

#查询SQL
select_sql = "SELECT TOP 100 [ID],[QQNum]\
      ,[Nick]\
      ,[Age]\
      ,[Gender]\
      ,[Auth]\
      ,[QunNum] FROM [GroupData1].[dbo].[Group10]"
#InsertSQL
insert_sql = "INSERT INTO 0psdb.tt_data VALUES"
#执行查询
mscur.execute(select_sql)
list = mscur.fetchall()
for data in list:
    insert_sql += "(" + str(data[1]) + ",'" + unicode(data[2].encode("latin1"), "gbk").strip() + "'," + str(
        data[6]) + "),"

print insert_sql[:-1]
mycur = myconn.cursor()
mycur.execute(insert_sql[:-1])
myconn.commit()