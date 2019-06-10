#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

"""
删除文档中的内容
"""
import  os
import re

path =u"C:\\workspace\\mancmdline\\windows-commands"

titel_partter = re.compile("---\n(.|\n)*---\n+",re.M)

for dirpath,dirname,filenames in os.walk(path):
    for filepath in filenames:
        fn = os.path.join(dirpath,filepath)
        try:
            ff = open(fn,'r+',encoding="UTF-8")
            f_content = re.sub(titel_partter,'',ff.read())
            ff.seek(0)
            ff.truncate()
            ff.write(f_content)
        except Exception as e:
            print(fn,e)

