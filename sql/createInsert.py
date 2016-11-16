#! /usr/bin/python
# coding:utf-8

import sys

insert = "insert into tt_cnnick(nick, nick_x, nick_m, cnnick_qp, cnnick_jp,cnnick_m, counts) values"
sqlfile = open("/data/tt_nick.sql", "w", 1)

with open("/data/tt_nick") as ff:
    while 1:
        lines = ff.readlines(1000)
        if not lines:
            break;
        line = insert + ','.join(lines) + ";"
        sqlfile.write(line.replace('\n', '') + "\n")