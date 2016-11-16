#!/usr/bin/python
# coding:utf-8

import fileinput
import os


SQL = "update TBL_SHEET_PROBLEM_IMMED t set t.timelimit ='%s'," \
      " t.accepttimelimit='%s',t.dealtimelimit='%s',t.explain_koujing='%s' where t.problem_id='%s';"

for line in fileinput.input(os.getcwd() + "/yxjscn.txt"):
    tt = line.split()
    ss = tt[1].split(",")
    # print ss[0]+":"+ss[1]+":"+ss[2]
    #print tt[0]+":"+ tt[1]+":"+tt[2]+":"+tt[3]+":"+tt[4]
    print SQL % (ss[0], ss[1], ss[2], tt[4], tt[0])
