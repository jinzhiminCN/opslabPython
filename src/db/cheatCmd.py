#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon


import os
import pymysql


path = "C:/Users/Administrator/Desktop/cheat-master/cheat/cheatsheets"

conn = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                       database="opslab_blog", charset="utf8")

insert_sql = 'insert into  t_search_cmd(id,type,cmd,createtime,updatetime,result,link)' \
             ' values(%d,"linux","%s",now(),now(),"%s","")'
index = 50000
for dirpath,dirname,filenames in os.walk(path):
    for filepath in filenames:
        if filepath == '__init__.py':
            continue

        index += 1
        f_n = os.path.join(dirpath,filepath)
        f_content= str(open(f_n,'r',encoding='utf-8').read()).replace('\"','\\"')
        mycur = conn.cursor()
        mycur.execute(insert_sql %(index,filepath,f_content))
        conn.commit()