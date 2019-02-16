# coding:UTF-8
# python3.x


"""Imagge是pillow库中一个非常重要的模块，提供了大量用于图像处理的方法
"""
from PIL import ImageGrab

from src import App

image_file = App.resource_file("/temp/test.jpg")

# 获取屏幕指定区域的图像
im = ImageGrab.grab((0,0,100,200))
im.show()

# 或全屏截图
im = ImageGrab.grab()
im.show()