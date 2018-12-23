# coding:UTF-8
# python3.x

import pymongo 


# 查看mongodb数据的基本信息
conn = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = conn.list_database_names()
for name in dblist:
    print(name)
    for collection in conn[name].list_collection_names():
        print(name,"->",collection)
