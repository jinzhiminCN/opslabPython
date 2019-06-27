#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import hashlib
import json

import redis



jedis = redis.Redis(host='localhost',port=6379)

keys = jedis.keys("WEIBO#*")
for key in keys:

    value = json.loads(jedis.get(key))
    key = str(key, "UTF-8").replace("WEIBO#","")
    print(key,value)