#!/usr/bin/python
# coding:utf-8

import fileinput
from conf import db

"""
    半自动化
    分组统计
"""

if __name__ == "__main__":
    # 更新业务产品类别b
    lst_day = []
    lst_count = [0]
    index = 0
    t = 0
    for line in fileinput.input("data/TimeCount.txt"):
        tt = line.split()
        day = '2015-12-00'
        if len(tt) == 2:
            if t != index:
                index += 1
            lst_day.append(tt[0])
            lst_count[index] = lst_count[index] + int(tt[1])
            lst_count.append(0)
            t += 1

        else:
            lst_count[index] = lst_count[index] + int(tt[0])

    for i in xrange(0, 31):
        print '%s-%d' % (lst_day[i], lst_count[i])
