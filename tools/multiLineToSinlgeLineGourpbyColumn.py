#! /usr/bin/python
# coding:UTF-8
import fileinput
import os, uuid

"""
    @author: neptune
    @time: 2014-02-20
    @descript: 将如下数据转换为一行
    077f89f0407e14fa01449acedf2667c2	GWKDYWB101	18609770767	1
    077f89f0407e14fa01449acedf2667c2	GWKDYWB201	18509710001	2
    077f89f0407e14fa01449acedf2667c2	GWKDYWB301	15500779875	3
    077f89f044aedf360145010d05573fae	GWWY101	15609716600	1
    077f89f044aedf360145010d05573fae	GWWY201	18609790677	2
    077f89f044aedf360145010d05573fae	GWWY301	13007792360	3
    转换后的数据为
    077f89f0407e14fa01449acedf2667c2 GWKDYWB301 15500779875 GWKDYWB201 18509710001 GWKDYWB101 18609770767
    077f89f044aedf360145010d05573fae GWWY301 13007792360 GWWY201 18609790677 GWWY101 15609716600
"""
struts = "'%s:%s':{'user':'%s','phone':'%s'}"
path = os.getcwdu() + "\\multiLine.txt"
keys = []
str_dict = "{"
for line in fileinput.input(path):
    lists = line.strip('\n').split()
    keys.append(lists[0])
    str_dict += struts % (lists[0], lists[3], lists[1], lists[2]) + ","

dicts = eval(str_dict[:-1] + "}")
result = """
        insert into CPM_SHEET_UPGRADE_CONFIG  (row_id,dept_id, manage_user_id,
        manage_phone_no,deputy_manage_user_id,deputy_manage_phone_no,
        general_manage_user_id, general_manage_phone_no) values
        ('%s','%s','%s','%s','%s','%s','%s','%s');
        """

for key in list(set(keys)):
    value1 = dicts.get(key + ":1")
    value2 = dicts.get(key + ":2")
    value3 = dicts.get(key + ":3")
    if not value1:
        value1 = {'user': '', 'phone': ''}
    if not value2:
        value2 = {'user': '', 'phone': ''}
    if not value3:
        value3 = {'user': '', 'phone': ''}
    print result % (str(uuid.uuid1()).replace('-', ''), key,
                    value3['user'], value3['phone'],
                    value2['user'], value2['phone'],
                    value1['user'], value1['phone'])
