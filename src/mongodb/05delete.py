# coding:UTF-8
# python3.x

import pymongo 

# 查看mongodb数据的基本信息
conn = pymongo.MongoClient("mongodb://localhost:27017/")

table = conn.local.table1


# update_one() 方法修改文档中的记录。
# 该方法第一个参数为查询的条件，第二个参数为要修改的字段
# 该方法方法只能修匹配到的第一条记录
# query = {"name":"test1"}
# table.delete_one(query)
 
# # 删除后输出
# for x in table.find():
#   print(x)