#! /usr/bin/python
# coding:utf-8

#----------------------------------------------------------------------------------------------
# @Digest 使用Pymssql连接Mssql数据库
#
#----------------------------------------------------------------------------------------------
import sys
import fileinput
import pymssql

reload(sys)
sys.setdefaultencoding('utf-8')

#需要用到使用pymssql组件可以使用pip install pymssql进行安装
conn = pymssql.connect(host="127.0.0.1", user="sa", password="wyb2212852", database="GroupData1", charset='utf8')

#需要用到端口号时
# conn = pymssql.connect(host="127.0.0.1",port="端口号",user="sa",password="123",database="Northwind")

#获取游标
cur = conn.cursor()

#查询SQL
select_sql = "SELECT TOP 1000 [ID],[QQNum]\
      ,[Nick]\
      ,[Age]\
      ,[Gender]\
      ,[Auth]\
      ,[QunNum] FROM [GroupData1].[dbo].[Group10]"

#执行查询
cur.execute(select_sql)

list = cur.fetchall()
with open("C:\workspace\Python\MssqlToMysql\com_1.txt", "a+") as f:
    for data in list:
        print data[2].encode("latin1")
        f.write(data[2].encode("latin1"))


# ##播入一条sql语句
# sql="INSERT INTO [GroupData1].[dbo].[Group10]\
#            ([RegionID]\
#            ,[RegionDescription])\
#      VALUES\
#            ("+1+"\
#            ,'test')"
# # #执行插入
# #cur.execute(sql)
# # #提交事务,不执行提交,数据插入不会生效
# #conn.commit()


