# coding:UTF-8
# python3.x

import datetime
import pymongo 

# 查看mongodb数据的基本信息
conn = pymongo.MongoClient("mongodb://localhost:27017/")

table = conn.local.table1
with open("c:/test.txt", 'w') as ff:
    for i in range(10000000):
        createtime =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = {"name":"test3","age":13,"createtime":createtime}
        table.insert_one(user)
        ff.write(str(user))


