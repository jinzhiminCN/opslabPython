# coding:UTF-8
# python3.x

import pymongo 

# 查看mongodb数据的基本信息
conn = pymongo.MongoClient("mongodb://localhost:27017/")

table = conn.local.table1
# 查询一条数据
line = table.find_one()
print(line)

# 查询集合中所有数据
for line in table.find():
    print(line)


# 查询指定字段的数据 及只显示name字段
for line in table.find({},{"name":1}):
    print(line)

# 根据指定条件查询
query = {"name":"test1"}
for line in table.find(query):
    print(line)

# limit
# 只查询前三条记录
query = {"name":"test1"}
for line in table.find(query).limit(3):
    print(line)