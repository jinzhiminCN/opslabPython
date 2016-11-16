#! /usr/bin/python
# coding:UTF-8


'''
    @Digest:统计群信息表的记录总数
'''

import pymssql

msconn = pymssql.connect(host="127.0.0.1", user="sa", password="wyb2212852", database="QunInfo1", charset='utf8')

count = 0
x = 1
for i in range(1, 12):
    for y in range(1, 11):
        table = "[QunInfo" + str(i) + "].[dbo].[QunList" + str(x) + "]"
        x += 1

        count_sql = "select count(*) from " + table
        cur = msconn.cursor()
        count_sql = "select COUNT(*) FROM " + table
        cur.execute(count_sql)
        t_count = cur.fetchall()[0][0]
        print table + "->" + t_count
        count += t_count

msconn.close()

print "群信息共计:" + str(count)