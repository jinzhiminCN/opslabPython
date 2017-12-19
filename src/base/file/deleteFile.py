#!/usr/bin/python
# coding:utf-8

import fileinput
import os
import shutil

path = "E:/update"
for line in fileinput.input("file.txt"):
    f = path + "/" + line.split()[8]
    if os.path.exists(f):
        print("delete dir " + f + " ...")
        shutil.rmtree(f)
