#!/usr/bin/env python
# coding=utf-8

import os

"""重命令制定目录下的文件名
"""

path = u"F:/vode/activiti工作流-企业开发实例讲解/activiti第五天/"
for root, dirs, files in os.walk(path):
    for f in files:
        filepath = os.path.join(root, f)
        newfilepath = os.path.join(root, "05-" + f)
        os.rename(filepath, newfilepath)

