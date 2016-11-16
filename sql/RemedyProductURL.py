#!/usr/bin/python
# coding:utf-8

"""
通过查询数据生成一些测试连接
"""
import cx_Oracle

db_url = 'hollycpm/hollycpm_v8hollycrm@135.255.9.201/qhunicom'
conn = cx_Oracle.connect(db_url)  #连接数据库
c = conn.cursor()  #获取cursor
x = c.execute('select sysdate from dual')  #使用cursor进行各种操作
x.fetchone()
c.close()  #关闭cursor
conn.close() 