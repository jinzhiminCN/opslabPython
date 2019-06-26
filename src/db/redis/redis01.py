#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import redis

r = redis.Redis(host='10.232.14.216',password="xwsptyapp", port=6379)
#True
print(r.set('foo', 'bar'))
#bar
print(r.get('foo'))


# set(name, value, ex=None, px=None, nx=False, xx=False)
#     ex：过期时间（秒），时间到了后redis会自动删除
#     px：过期时间（毫秒），时间到了后redis会自动删除。ex、px二选一即可
#     nx：如果设置为True，则只有name不存在时，当前set操作才执行
#     xx：如果设置为True，则只有name存在时，当前set操作才执行
r.set('name_2', 'Zarten_2')

# 有了redis连接后能通过连接执行响应的redis命令
