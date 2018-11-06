#!/usr/bin/python
# coding:utf-8

import fileinput

input = open("c:/mysql/result.sql", "a", 1)

sql = "insert into %s select * from %s;drop table %s;\n"

insert_table = "tt_nick_540"
count = 0
for line in fileinput.input('c:/mysql/insert.sql'):
    tt = line.split()

    input.write(sql % (insert_table, tt[0], tt[0]))
    count = count + int(tt[1])

print(count)
