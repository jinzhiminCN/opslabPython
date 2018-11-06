# coding:UTF-8
# python3.x


"""Imagge是pillow库中一个非常重要的模块，提供了大量用于图像处理的方法
"""
from PIL import Image

from src import App

image_file = App.resource_file("/opencv/green-spiral.jpg")

im = Image.open(image_file)

# 将彩色图像分离为同样大小的红、绿、蓝三分量子图
r, g, b = im.split()

r.show()
g.show()
b.show()

#参数为缩略图尺寸
im.thumbnail((100, 100))
im.show()

