#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon
import  os
path =u"C:\workspace\mancmdline\linux-commands"
for dirpath,dirname,filenames in os.walk(path):
    for filepath in filenames:
        fn = os.path.join(dirpath,filepath)
        os.rename(fn,fn+".md")