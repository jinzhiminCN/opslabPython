#!/usr/bin/python
# coding:utf-8

import fileinput
from src.conf import  App
"""
根据文本文件生成INSERT的SQL语句
"""

insert_sql = """
  insert into tbl_general_codes
  (row_id,area_code,code_type,code_value,code_name,code_order,is_valid,is_system,create_time,enabled_time,disenabled_time,
    last_modify_time,remark,domain_id,id,sub_system_id,is_by_developer)
  values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"""


for line in fileinput.input(App.BASE_DATA+"db/generalCode.txt"):
    lists = line.strip('\n').split('|')
    l = insert_sql % (lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8]
                      , lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16],
                      lists[17])
    print(l.strip('\n'))