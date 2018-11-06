# coding:UTF-8
# python3.x


"""Imagge是pillow库中一个非常重要的模块，提供了大量用于图像处理的方法
"""
from PIL import Image

from src import App

image_file = App.resource_file("opencv/green-spiral.jpg")

# 打开图像文件
im = Image.open(image_file)

# 图像格式
print(im.format)
# 图片大小，格式为(宽度,高度)
print(im.size)
# 查看像素高度
print(im.height, "/", im.width)

# 显示图像
# im.show()


# 查看图像直方图
# ﻿如果图像包含多个通道，则返回所有通道的直方图
im.histogram()
# 查看第一个通道的直方图
im.histogram()[:256]

# 读取像素值 返回值 ﻿(255, 248, 220) #返回值分别表示红、绿、蓝三原色分量的值
im.getpixel((150, 80))
# 第二个参数用来指定目标像素的颜色值
im.putpixel((100, 50), (128, 30, 120))
