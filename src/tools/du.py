#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

"""模拟linux的du命令"""

import os
import getopt
import sys


def dir_size(dir_path):
    """获取目录的大小"""
    size = 0
    for root, dirs, files in os.walk(dir_path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])

    return str(round(size / 1024 / 1024, 2)) + "M"


def trim_path(file_name):
    """返回标准的路径"""
    return os.path.normpath(file_name).replace("\\", "/")


def dir_info(dir_path, path_level):
    """返回指定路面下的path_level内的文件和文件夹"""
    re_list = []
    if path_level == 0:
        return re_list
    for file_name in os.listdir(dir_path):
        path_name = os.path.join(dir_path, file_name)
        if os.path.isfile(path_name):
            re_list.append(trim_path(path_name))
        if os.path.isdir(path_name):
            re_list.append(trim_path(path_name))
            re_list += dir_info(path_name, path_level - 1)
    return re_list


def usage():
    print("""
        -p(--path)              指定目录 默认值为当前目录
        -l(--path_level)        遍历深度默认为1
    """)


if __name__ == '__main__':
    # print(dir_size("c:/Temp"))
    # print(dir_info("C:/", 1))
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:l:", ["path=", "path_level="])
        if not opts:
            usage()
            exit()

        path = os.getcwd()
        path_level = 1
        for opt, value in opts:
            if opt in ('-h', '--help'):
                usage()
                exit()
            if opt in ('-p', '--path'):
                path = value
            if opt in ('-l', '--path_level'):
                path_level = value
        if not os.path.exists(path):
            print("系统找不到指定的路径: ", path)
            exit(-1)

        lst = dir_info(path, int(path_level))
        for ls in lst:
            print(ls, "=>", dir_size(ls))
    except getopt.GetoptError:
        usage()
        exit()
