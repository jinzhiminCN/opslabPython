#!/usr/bin/python
# coding:utf-8

select_sql = "select  nick,count(*) counts from " \
             "tt_data_%d  group by nick  union"

for i in range(1, 750, 1):
    print select_sql % i