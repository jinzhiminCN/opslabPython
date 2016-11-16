#!/usr/bin/python
# coding:utf-8

import fileinput
from conf import db

"""
    半自动化
    利用Python生成一些SQL用户根据业务反映的EXCEL修改数据
"""

if __name__ == "__main__":
    # 更新业务产品类别
    lines = []
    lst = []
    for line in [l for l in fileinput.input("sheet.txt") if l.strip()]:
        tt = ''.join(line.split()).split(":")

        lines.append(tt[0])
        # code_id = db.problem_key(tt[1])
        # code_id = db.complain_key(tt[1])
        # code_id = db.product_key(tt[1])
        # 用户品牌 SUBTYPE sql_subtype
        # 工单性质 DETERMINE_STATUS
        # 业务类别 ANALYSIS_BUSINESS_TYPE
        # 问题责任归属 ANALYSIS_PROBLEM_CHANNEL
        # 管理范围 ANALYSIS_MANAGER_SCOPE
        # 业务组织方式 ANALYSIS_BUSINESS_ORGANIZATION
        # 管理范围 ANALYSIS_MANAGER_SCOPE
        # 分析纬度.信息化部支撑系统 ANALYSIS_INFO_SYSTEM
        # 客户类型 CUSTOMER_TYPE
        # 通信质量位置信息 TXWZXX
        code_id = db.code_key(tt[1], 'ANALYSIS_INFO_SYSTEM')
        # 投诉地
        # code_id = tt[1]
        # code_id = db.dept_id(tt[1])

        if code_id:
            lst.append(tt[0])
            # 客户端问题定位
            # print db.sql_problem_id %(code_id,tt[0])
            # print db.sql_determine_problem_id % (code_id, tt[0])

            # 业务产品列表
            # print db.sql_product_category % (code_id,tt[0])

            # 管理范围
            # print db.sql_anlymanagescope % (code_id, tt[0])

            # 用户品牌
            # print db.sql_subtype % (code_id,tt[0])

            # 客户类型
            # print db.sql_CUSTOMER_TYPE % (code_id,tt[0])

            # 投诉地
            # print db.sql_manufac_name % (code_id,tt[0])

            # 工单性质
            # print db.sql_determine_status % (code_id,tt[0])

            # 责任部门
            # print db.sql_determine_duty_dept % (code_id, tt[0])

            # 业务类型
            # print db.sql_business_type % (code_id, tt[0])

            # 业务产品类别
            # print db.sql_determine_product_category % (code_id, tt[0])

            # 问题责任归属
            # print db.sql_problem_channel % (code_id,tt[0])

            # 管理端问题定位
            # print db.sql_complain_target %(code_id,tt[0])

            # 信息化部支撑系统
            print db.sql_anly_info_system % (code_id, tt[0])

            # 业务组织方式
            # print db.sql_business_organization %(code_id,tt[0])

            # 通信质量位置信息
            # print db.sql_anlyproblemlocal %(code_id,tt[0])
    # 处理成功的
    print "==" * 10
    print "需要处理:%d" % len(lines)
    print "处理成功:%d" % len(lst)
    # 未处理成功的
    ret = list(set(lines) ^ set(lst))
    print '==' * 10
    print ret
