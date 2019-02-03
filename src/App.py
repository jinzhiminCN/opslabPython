#! /usr/bin/python
# coding=UTF-8
# version:python3.x


import datetime
import logging
import os

"""常用设置和共用方法"""

# 设置编码
ENCODING = "UTF-8"

# 获取工程路径
BASE_PATH = os.getcwd().replace("\\", "/").split("src/")[0]


def trim_path(file_name):
    """返回标准的路径"""
    return os.path.normpath(file_name).replace("\\", "/")


def base_path_file(file_name):
    """获取完整的文件路径"""
    return trim_path(BASE_PATH + file_name)


def resource_file(file_name):
    """返回完整的资源文件路径"""
    return trim_path(BASE_PATH + "resource/" + file_name)


def temp_file(file_name):
    """返回完整的临时文件路径"""
    return trim_path(BASE_PATH + "resource/temp/" + file_name)


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


def date_time_str():
    """获取当前时间"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print(BASE_PATH)
    print(trim_path("c:\\files\\\\file2//files"))
    print(resource_file("opencv/green-spiral.jpg"))
    print(temp_file("green-spiral.jpg"))
    print(trim_path("c:\\files\\\\file2//files"))
    print(date_time_str())
