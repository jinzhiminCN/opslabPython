#!/usr/bin/python
# coding:gbk

import os


filelist_map = {}

for root, dirs, files in os.walk("C:/Users/Administrator/Desktop/upload"):
    for name in files:
        filelist_map[name] = os.path.join(root, name)

print len(filelist_map)
print filelist_map