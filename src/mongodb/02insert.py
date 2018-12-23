# coding:UTF-8
# python3.x

import datetime
import uuid
from pymongo import MongoClient

def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = MongoClient("127.0.0.1",27017)

# 链接local数据库,没有则自动创建
db = conn.local

# 使用table1集合,没有则自动创建
# 插入数据
# insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入

# insert_one() 方法返回 InsertOneResult 对象，
# 该对象包含 inserted_id 属性，它是插入文档的 id 值
x = db.table1.insert_one({"name":"test1","age":13,"createtime":current_time()})
print(x.inserted_id)

# 插入多条数据
# insert_many() 方法返回 InsertManyResult 对象，
# 该对象包含 inserted_ids 属性，该属性保存着所有插入文档的 id 值。
users = [
        {"name":"test3","age":13,"createtime":current_time()},
        {"name":"test4","age":13,"createtime":current_time()}
    ]
x = db.table1.insert_many(users)
print(x.inserted_ids)

# 指定ID插入
users = [
        {"_id":uuid.uuid1(),"name":"test3","age":13,"createtime":current_time()},
        {"name":"test4","age":13,"createtime":current_time()}
    ]
x = db.table1.insert_many(users)
print(x.inserted_ids)


