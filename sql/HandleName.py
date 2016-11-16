#!/usr/bin/python
# coding:utf-8


"""将nick中一些火星文已经一些标点符号等全部过滤"""

import pymysql
import re

pchinese = re.compile(ur"[\u4e00-\u9fa5]+?|[\w]+?")


def handle_name(nick):
    m = pchinese.findall(nick)
    if m:
        return ''.join(m)
    else:
        return '-'


myconn = pymysql.connect(host="127.0.0.1", user="root",
                         password="wyb2212852", database="0psdb",
                         charset="utf8")

filehand = open("/data/qdata.txt", "w", 1)

for top in range(4004, 1422998997, 1000):
    select_sql = "select qid,nick,count(*) from tt_data t where " \
                 " t.qid >=" + str(top) + " and t.qid < " \
                 + str(top + 1000) + " group by qid,nick"
    print "Handle ->" + str(top) + " - " + str(top + 1000)
    mscur = myconn.cursor()
    mscur.execute(select_sql)
    lst = mscur.fetchall()
    lst_result = []
    for data in lst:
        nick = handle_name(data[1])
        if nick != '-':
            dd = "(%d,'%s',%d)" % (data[0], nick, data[2])
            lst_result.append(dd)

    if lst_result:
        strs = ','.join(lst_result) + ';\n'
        filehand.write(strs.encode("utf-8"))

