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

# MIDI (mid)，文件
FILE_PREFIX_MIDI = "4D546864"
# JPEG (jpg)，文件
FILE_PREFIX_JPEG = "FFD8FF"
# PNG文件
FILE_PREFIX_PNG = "89504E47"
# 4.  GIF (gif)，文件
FILE_PREFIX_GIF = "47494638"
# TIFF (tif)，文件
FILE_PREFIX_TIFF = "49492A00"
# Windows Bitmap (bmp)，文件
FILE_PREFIX_BMP = "424D"
# CAD (dwg)，文件
FILE_PREFIX_CAD = "41433130"
# Adobe Photoshop (psd)，文件
FILE_PREFIX_PSD = "38425053"
# Rich Text Format (rtf)，文件
FILE_PREFIX_RTF = "7B5C727466"
# XML (xml)，文件
FILE_PREFIX_XML = "3C3F786D6C"
# HTML (html)，文件
FILE_PREFIX_HTML = "68746D6C3E"
# Email [thorough only] (eml)，文件
FILE_PREFIX_EML = "44656C69766572792D646174653A"
# Outlook Express (dbx)，文件
FILE_PREFIX_DBX = "CFAD12FEC5FD746F"
# Outlook (pst)，文件
FILE_PREFIX_PST = "2142444E"
# MS Word/Excel (xls.or.doc)，文件
FILE_PREFIX_OFFICE = "D0CF11E0"
# MS Access (mdb)，文件
FILE_PREFIX_MDB = "5374616E64617264204A"
# WordPerfect (wpd)，文件
FILE_PREFIX_WPD = "FF575043"
# Postscript (eps.or.ps)，文件
FILE_PREFIX_EPS = "252150532D41646F6265"
# Adobe Acrobat (pdf)，文件
FILE_PREFIX_PDF = "255044462D312E"
# Quicken (qdf)，文件
FILE_PREFIX_QDF = "AC9EBD8F"
# Windows Password (pwl)，文件
FILE_PREFIX_PWL = "E3828596"
# ZIP Archive (zip)，文件
FILE_PREFIX_ZIP = "504B0304"
# RAR Archive (rar)，文件
FILE_PREFIX_RAR = "52617221"
# Wave (wav)，文件
FILE_PREFIX_WAV = "57415645"
# AVI (avi)，文件
FILE_PREFIX_AVI = "52494646"
# Real Audio (ram)，文件
FILE_PREFIX_RAM = "2E7261FD"
# Real Media (rm)，文件
FILE_PREFIX_RM = "2E524D46"
# Windows Media Audio（wma）（asf）,文件
FILE_PREFIX_WMA = "3026b2758e66cf"
# wrf, 文件
FILE_PREFIX_WRF = "574f5446000600"
# MPEG (mpg)，文件
FILE_PREFIX_MPG = "000001BA"
# MPEG (mpg)，文件
FILE_PREFIX_MPG = "000001B3"
# Quicktime (mov)，文件
FILE_PREFIX_MOV = "6D6F6F76"
# Windows Media (asf)，文件
FILE_PREFIX_ASF = "3026B2758E66CF11"




if __name__ == '__main__':
    print(BASE_PATH)
    print(trim_path("c:\\files\\\\file2//files"))
    print(resource_file("opencv/green-spiral.jpg"))
    print(temp_file("green-spiral.jpg"))
    print(trim_path("c:\\files\\\\file2//files"))
    print(date_time_str())
