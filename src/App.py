# coding=UTF-8
# version:python3.x
import os

"""app常用配置"""


# 获取工程路径
BASE_PATH = os.path.split(os.path.realpath(__file__))[0].replace("\\","/").replace("/src", "")

# 获取工程资源路径
BASE_RESOURCE = BASE_PATH + "/resource"

# 获取临时路径
BASE_TEMP = BASE_PATH + "/resource/temp/"

# 数据文件路基
BASE_DATA = BASE_PATH + "/resource/data/"

# 设置编码
ENCODING = "UTF-8"

# 数据库密码
MYSQL_LOCAL_USER = ""
MYSQL_LOCAL_PASSWRD = ""