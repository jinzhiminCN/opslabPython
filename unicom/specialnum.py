#!/usr/bin/python
# coding:utf-8

import sys
import fileinput

strs = "insert into tbl_special_phone(phonenum,username,phonetype,usermem) values('%s','%s','%s','%s');"

for line in fileinput.input("C:/Users/Administrator/Desktop/test.txt"):
    tt = line.split()
    insert = strs % (tt[0], tt[1], tt[2], '02')
    print insert
