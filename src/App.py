#! /usr/bin/python
# coding=UTF-8
# version:python3.x


import os
import re
import logging

"""常用设置和共用方法"""

# 设置编码
ENCODING = "UTF-8"
# 数据库密码
MYSQL_LOCAL_USER = "root"
MYSQL_LOCAL_PASSWRD = "123456"

# 获取工程路径
BASE_PATH = os.getcwd().replace("\\", "/").split("src/")[0]


def trim_path(file_name):
    """返回标准的路径"""
    return os.path.normpath(file_name).replace("\\","/")


def base_path_file(file_name):
    """获取完整的文件路径"""
    return trim_path(BASE_PATH + file_name)


# 获取工程资源路径
BASE_RESOURCE_PATH = BASE_PATH + "resource/"


def resource_file(file_name):
    """返回完整的资源文件路径"""
    return trim_path(BASE_RESOURCE_PATH + file_name)


# 获取临时路径
BASE_TEMP_PATH = BASE_PATH + "resource/temp/"


def temp_file(file_name):
    """返回完整的临时文件路径"""
    return trim_path(BASE_TEMP_PATH + file_name)


def logger(modeule_name):
    """Initialize logging module."""
    logger = logging.getLogger(modeule_name)
    formatter = logging.Formatter('%(asctime)s-(%(name)s)-[%(levelname)s] %(message)s')
    logger.setLevel(logging.DEBUG)

    # Create a file handler to store error messages
    log_file = temp_file("run.log")
    fhdr = logging.FileHandler(log_file, mode='w')
    fhdr.setLevel(logging.ERROR)
    fhdr.setFormatter(formatter)

    # Create a stream handler to print all messages to console
    chdr = logging.StreamHandler()
    chdr.setFormatter(formatter)

    logger.addHandler(fhdr)
    logger.addHandler(chdr)

    return logger


if __name__ == '__main__':
    print(BASE_PATH)
    print(BASE_RESOURCE_PATH)
    print(BASE_TEMP_PATH)
    print(trim_path("c:\\files\\\\file2//files"))
    print(resource_file("opencv/green-spiral.jpg"))
    print(temp_file("green-spiral.jpg"))
    print(os.path.normpath("c:\\files\\\\file2//files"))