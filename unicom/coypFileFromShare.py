#!/usr/bin/python
# coding:gbk

import shutil

dstPath = "C:\\Users\\Administrator\\Desktop\\V3\\"
with open('./data/coypFileFromShare.txt') as f:
    for line in f:
        tt = line.strip('\n').split("\\")
        ff = tt[8]
        shutil.copy(line.strip('\n'), dstPath + ff)

