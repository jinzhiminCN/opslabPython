#!/usr/bin/python
# coding:utf-8

import fileinput

"""
    半自动化
    利用Python生成一些SQL用户根据业务反映的EXCEL修改数据
"""

if __name__ == "__main__":
    for line in fileinput.input("data/sheetflow.txt"):
        if line:
            print "'%s'," % line.strip()
