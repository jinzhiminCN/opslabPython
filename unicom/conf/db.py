#!/usr/bin/python
# coding:utf-8

import db_code
import db_problem
import db_product
import db_complain
import db_departments

# 客户端投诉问题定位
sql_problem_id = "update tbl_main_sheet t set t.problem_type_id='%s' where t.main_sheet_flow_no='%s';"

# 归档时客户端投诉问题定位
sql_determine_problem_id = \
    "update tbl_main_sheet t set t.determine_problem_type_id='%s' where t.main_sheet_flow_no='%s';"

# 修改业务产品
sql_product_category = "update tbl_main_sheet t set t.product_category='%s'  where t.main_sheet_flow_no='%s';"

# 用户品牌SUBTYPE
sql_subtype = "update tbl_sheet_customer_info sci set sci.sub_type='%s' where sci.main_sheet_flow_no='%s';"

# 客户类型
sql_CUSTOMER_TYPE = "update tbl_sheet_customer_info sci set sci.customer_type='%s' where sci.main_sheet_flow_no='%s';"

# 用户投诉地(此处没有编码直接存入汉字即可)
sql_manufac_name = "update tbl_sheet_customer_info sci set sci.manufac_name= '%s' where sci.main_sheet_flow_no='%s';"

# 有理投诉DETERMINE_STATUS
sql_determine_status = "update tbl_main_sheet t set t.DETERMINE_STATUS='%s'  where t.main_sheet_flow_no='%s';"

# 问题责任归属
sql_problem_channel = \
    "update tbl_sheet_content_field t set t.problem_channel ='%s' where t.sheet_flow_no ='%s';"

# 管理端问题责任定位
sql_complain_target = \
    "update tbl_sheet_content_field t set t.complain_target ='%s' where t.sheet_flow_no ='%s';"

# 分析纬度.业务类别(ANALYSIS_BUSINESS_TYPE)
sql_business_type = \
    "update tbl_sheet_content_field t set t.business_type ='%s' where t.sheet_flow_no ='%s';"

# 分析纬度.产品类别
sql_determine_product_category = \
    "update tbl_sheet_content_field t set t.product_type ='%s' where t.sheet_flow_no ='%s';"

# 分析纬度.问题责任归属
sql_determine_duty_dept = "update tbl_main_sheet t set t.determine_duty_dept='%s'  where t.main_sheet_flow_no='%s';"

# 分析纬度.管理范围ANALYSIS_MANAGER_SCOPE
sql_anlymanagescope = \
    "update tbl_sheet_content_field t set t.anlymanagescope ='%s' where t.sheet_flow_no ='%s';"

# 分析纬度.业务组织方式
sql_business_organization = \
    "update tbl_sheet_content_field t set t.business_organization ='%s' where t.sheet_flow_no ='%s';"

# 分析纬度.信息化部支撑系统
sql_anly_info_system = \
    "update tbl_sheet_content_field t set t.anly_info_system ='%s' where t.sheet_flow_no ='%s';"

# 分析纬度.通信问题位置
sql_anlyproblemlocal = \
    "update tbl_sheet_content_field t set t.anlyproblemlocal ='%s' where t.sheet_flow_no ='%s';"


# 满意度


def problem_key(key):
    """通过客户端投诉问题得到编码"""
    lst = []
    key = ''.join(key.replace("\\", '/').split())
    if key[:1] != '/':
        key = '/' + key
    for problem in db_problem.problems:
        problem_name = ''.join(problem[1].replace("\\", "/").split())

        if problem_name == key:
            lst.append(problem[0])

    if lst:
        return max(lst)
    else:
        return ''


def product_key(key):
    """通过产品名称获取产品编码"""
    lst = []
    key = ''.join(key.replace('\\', '/').split())
    if key[:1] != '/':
        key = '/' + key
    for p in db_product.products:
        product_name = ''.join(p[1].replace('\\', '/').split())
        # print '%s-%s' % (key, product_name)
        if product_name == key:
            lst.append(p[0])

    if lst:
        return max(lst)
    else:
        return ''


def complain_key(key):
    """通过管理端问题获取投诉问题编码"""
    lst = []
    key = ''.join(key.replace('\\', '/').split())
    if key[:1] != '/':
        key = '/' + key

    for c in db_complain.complains:
        complain_name = ''.join(c[1].replace('\\', '/').split())

        if complain_name == key:
            lst.append(c[0])

    if lst:
        return max(lst)
    else:
        return ''


def code_key(name, code_type):
    """通过编码名称,编码类型获得编码ID"""
    lst = []
    for code in db_code.codes:
        if code_type == code[2] and name.strip() == code[1].strip():
            lst.append(code[0])

    if lst:
        return max(lst)
    else:
        return ''


def dept_id(dept_name):
    """根据部门名称获得部门ID"""
    if dept_name == '无':
        return ''

    lst = []
    for dept in db_departments.departments:
        if dept_name == dept[1].strip():
            lst.append(dept[0])

    if lst:
        return max(lst)
    else:
        return ''
