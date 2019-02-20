#!/usr/bin/python
# coding:utf-8

import xlrd
import sys
from datetime import date, datetime, time
import pandas as pd




insert_sql = " insert into T_CRMPACKAGE_INFO(CRM_PACKAGEID,ECP_CODE,CRM_FEE,PACKAGNAME,PACKAGEDESC) values('{}','{}','{}','{}','');"
df = pd.read_excel('c:/副本资费套餐费.xlsx')
data = df.ix[:, ['产品编码', '产品标识', '产品费用', '产品名称', ]].values
i = 0
for dd in data:
    i += 1
    if len(dd) == 4:
        print(insert_sql.format(
            str(dd[0]).strip().replace('\n', ''),
            str(dd[1]).strip().replace('\n', ''),
            str(dd[2]).strip().replace('\n', ''),
            str(dd[3]).strip().replace('\n', ''))
        )
