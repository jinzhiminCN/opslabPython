#!/usr/bin/python
# coding:gbk

import sys, os, shutil


def copyFile(srcfile, destFile):
    if not os.path.exists(srcfile):
        return
    print srcfile + "->" + destFile
    path = os.path.dirname(destFile)
    # print path
    if not os.path.exists(path):
        os.mkdir(path)
    shutil.copy(srcfile, destFile)


path = "C:/Users/Administrator/Desktop/"
out = open("C:/Users/Administrator/Desktop/exisit.sh", "w")

with open('./data/attachment1.txt') as f:
    for line in f:
        tt = line.strip('\n').split(":")
        f = tt[1]
        if f.endswith(".V3", 3):
            srfFile = path + "V3/" + f
            dstFile = path + "upload/" + tt[0] + "/" + tt[2]
            copyFile(srfFile, dstFile)
            # out.write("find ./20160504 -iname \""+f+"\"\n")
            # out.write("find ./20160505 -iname \""+f+"\"\n")
            # out.write("find ./20160506 -iname \""+f+"\"\n")
            # out.write("find ./20160507 -iname \""+f+"\"\n")
            # out.write("find ./20160508 -iname \""+f+"\"\n")

            # afile = "upload/"+tt[0]+"/"+tt[2]
            # out.write("if [ -f \""+afile+"\" ];then\n")
            # out.write(" echo \"ok\"\n")
            # out.write("else\n")
            # out.write(" echo \""+line.strip('\n')+"\" >> exisit.txt\n")
            # out.write("fi\n")
            # out.write("\n")
