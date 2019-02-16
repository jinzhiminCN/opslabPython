# coding:UTF-8
# python3.x


"""Imagge是pillow库中一个非常重要的模块，提供了大量用于图像处理的方法
"""
from PIL import Image
from PIL import ImageFilter

from src import App

image_file = App.resource_file("/opencv/green-spiral.jpg")

im = Image.open(image_file)

# ﻿创建滤波器，使用不同的卷积核
im = im.filter(ImageFilter.DETAIL)
im.show()

# 边缘增强
im2 = im.filter(ImageFilter.EDGE_ENHANCE)
im2.show()

# 边缘增加
im3 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im3.show()


# 图像模糊
im4 = im.filter(ImageFilter.BLUR)
im4.show()

# 高斯模糊
im5 = im.filter(ImageFilter.GaussianBlur)
im5.show()

# 中值滤波
im6 = im.filter(ImageFilter.MedianFilter)
im6.show()