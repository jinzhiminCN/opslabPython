# coding:UTF-8
# python3.x

import pymongo 

# 查看mongodb数据的基本信息
conn = pymongo.MongoClient("mongodb://localhost:27017/")

table = conn.local.table1

## 类似于执行命令
## > db.table1.mapReduce(    
#       function() { emit(this.name,1); }, 
#       function(key, values) {return Array.sum(values)},
#         {                        out:"post_total"        } 
#       ).find()
map = "function() { emit(this.name,1); }"
reduce = """function(key, values) {return Array.sum(values)}"""
for doc in  table.map_reduce(map,reduce,"myresults").find():
    print(doc)