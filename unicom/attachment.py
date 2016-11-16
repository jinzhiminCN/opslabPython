#!/usr/bin/python
# coding:gbk

import sys, os, shutil


def copyFile(srcfile, destFile):
    dstPath = "C:/Users/Administrator/Desktop/"
    print srcfile + "->" + destFile
    path = dstPath + os.path.dirname(destFile)
    # print path
    if not os.path.exists(path):
        os.mkdir(path)
    shutil.copy(srcfile, dstPath + destFile)


attment_file = {}
attment = []
filelist = []
with open('./data/attachment1.txt') as f:
    for line in f:
        tt = line.strip('\n').split(":")
        afile = "upload/" + tt[0] + "/" + tt[2]
        attment_file[tt[1]] = afile
        attment.append(tt[1])

filelist_map = {}
for root, dirs, files in os.walk("C:/Users/Administrator/Desktop/附件/"):
    for name in files:
        filelist_map[name] = os.path.join(root, name)
        filelist.append(name)

lst = list((set(attment).union(set(filelist))) ^ (set(attment) ^ set(filelist)))
print len(lst)

for x in lst:
    srcFile = filelist_map[x]
    dstFile = attment_file[x]
    copyFile(srcFile, dstFile)