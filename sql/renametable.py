#!/usr/bin/python
# coding:utf-8

import fileinput

input = open("c:/mysql/rename.sql", "a", 1)

sql = "alter  table %s rename to tbl_nick_%d;\n"

count = 1
for line in fileinput.input('c:/mysql/select.sql'):
    table = line.split()[0]
    input.write(sql % (table, count))
    count += 1
