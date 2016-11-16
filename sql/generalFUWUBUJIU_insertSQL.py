#!/usr/bin/python
# coding:utf-8
import uuid

from QDataHandle.resource import kehuduanwenti


"""
生成服务补救插入的SQL
"""

insert_sql1 = """INSERT INTO CPM_AUTHORIZE_CONFIG
  (CREATE_USER_CODE,
   REMARK,
   AUTHORIZE_TYPE_ID,
   END_TIME,
   ROLE_ID,
   ID,
   START_TIME,
   SHEET_TYPE_NAME,
   SHEET_TYPE_ID,
   AUTHORIZE_TYPE_NAME,
   AMOUNT_LIMIT,
   ROLE_NAME)
VALUES
  ('4004','%s','%s','2016-04-19 15:30:12','%s',
   '%s','2037-04-19 15:30:54','%s','%s','%s','%s','%s');
""".strip('\n').replace("\n", '')
insert_sql2 = """
INSERT INTO CPM_AUTHORIZE_PRODUCT_REF
  (ID, PRODUCT_ID, AUTHORIZE_ID, PRODUCT_NAME)
VALUES('%s','%s','%s','%s');
""".strip('\n').replace("\n", '')

"""授权类型
1>无限额授权
2>有限额授权
3>产品授权
4>临时授权
"""
AUTHORIZE_TYPE_ID = '3'

AUTHORIZE_TYPE_NAME = '产品授权'

"""授权岗位
TREE20160305112836933	地市部门经理级
TREE20160305112750726	地市店长级
TREE20160305112803736	地市副总经理级
TREE20160305112738798	地市营业员级
TREE20160305112848242	地市员工级
TREE20160305112826374	地市总经理级
TREE20160305112912614	二线处理人
TREE20160305112926311	省部门主任级
TREE20160305112615171	省副总经理级
TREE20160305112815269	省员工级
TREE20160305112701433	省总经理级
TREE20160305112728048	投诉处理运营主管
TREE20160305112715901	投诉处理组长
TREE20160305112858845	一线话务员

"""
ROLE_ID = 'TREE20160305112858845'
ROLE_NAME = '一线话务员'

AMOUNT_LIMIT = '20'

product_id = 'f04aa67328ca42e59c07734bd99654a0'
product_name = '省员工级'
for lst in kehuduanwenti.code:
    key = str(uuid.uuid1()).replace("-", "").upper()
    print  insert_sql1 % (str(lst[1]), AUTHORIZE_TYPE_ID, ROLE_ID, key,
                          str(lst[1]), str(lst[0]), AUTHORIZE_TYPE_NAME,
                          AMOUNT_LIMIT, ROLE_NAME)

    print  insert_sql2 % (str(uuid.uuid1()).replace("-", "").upper(),
                          product_id, key, product_name)
