#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import hashlib
import json

import redis

jedis = redis.Redis(host='localhost',port=6379,db=1)

def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()

userino = {'userInfo': '//weibo.com/n/%E5%95%8A%E5%96%8F%E5%AD%A6%E5%BC%9F?from=feed&loc=at', 'userName': '啊喏学弟', 'uid': '/u/6510800440'}
rediskey = md5str(userino["userName"])
jedis.set(rediskey,json.dumps(userino, ensure_ascii=False))

ss = jedis.get(rediskey+'1111')
if ss:
    print("===>")
else:
    print("...")
uu = json.loads()
print(uu)
