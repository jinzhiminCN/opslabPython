#!/usr/bin/python
# coding:utf-8

import fileinput

from src import App

"""
    首先利用SQL导出表的注释信息：
    select * from user_col_comments
"""
if __name__ == "__main__":
    comment = "comment on column %s.%s is '%s';"
    for line in fileinput.input(App.BASE_DATA+"db/columncomment.txt"):
        if line:
            tt = line.split()
            if len(tt) == 3:
                print(comment % (tt[0], tt[1], tt[2]))
