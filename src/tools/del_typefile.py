#! /usr/bin/python
# coding=UTF-8
# version:python3.x


import os
from sys import path

"""删除指定的文件"""


def del_typefile(dir, filetypes):
    for root, dirs, files in os.walk(dir):
        for file in files:
            suffix = os.path.splitext(file)[1]
            if suffix in filetypes:
                filepath = os.path.join(root, file)
                if os.path.isfile(filepath):
                    print('del ' + filepath)
                    os.remove(filepath)


if __name__ == '__main__':
    filetypes = [".png", ".jpg", ".gif", ".class"]
    del_typefile("c:/xwtech", filetypes)
