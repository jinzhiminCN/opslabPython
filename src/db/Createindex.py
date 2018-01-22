#!/usr/bin/python
# coding:utf-8

index_file = open("index.sql", "w", 1)
create_index = "create index IDX_TT_NICK on tt_data_%d(nick);"
for i in range(1, 750, 1):
    index_file.write(create_index % i + "\n")
