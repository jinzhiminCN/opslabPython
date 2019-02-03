#!/usr/bin/python
# coding:utf-8

create = "create table fuzz.tt_nick_%d as select nick,count(*) counts from tencent.tt_data_%d group by nick;\n"

sqlfile = open("c:/create.sql", "w", 1)

for i in range(1, 751, 1):
    sqlfile.write(create % (i, i))
