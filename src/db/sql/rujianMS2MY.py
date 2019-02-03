
# coding:UTF-8


'''
    @Digest:统计群信息表的记录总数
'''

import pymssql

msconn = pymssql.connect(host="127.0.0.1", user="sa", password="123456", database="shifenzheng", charset='utf8')

table = "[shifenzheng].[dbo].[cdsgus]"
count_sql = "select count(*) from " + table
cur = msconn.cursor()
count_sql = "select COUNT(*) FROM " + table
cur.execute(count_sql)
t_count = cur.fetchall()[0][0]
print (table + "->" + str(t_count))

msconn.close()

print ("共计:" + str(t_count))