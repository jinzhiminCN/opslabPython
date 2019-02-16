# coding:UTF-8
# python3.x


"""Imagge是pillow库中一个非常重要的模块，提供了大量用于图像处理的方法
"""
from PIL import Image

from src import App

image_file = App.resource_file("/opencv/green-spiral.jpg")

im = Image.open(image_file)

# 图像缩放
# im = im.resize((100,100))
# im.show()

#
# 图像保存
im.save(App.temp__file("/green-spiral.jpg"))

#逆时针旋转90度
im = im.rotate(90)
im.show()
#逆时针旋转180度
im = im.transpose(Image.ROTATE_180)
im.show()
#水平翻转
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.show()
#垂直翻转
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show()

# ﻿图像裁剪与粘贴

#定义裁剪区域
box = (120, 194, 220, 294)
# 裁剪
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
# 粘贴
im.paste(region,box)
im.show()