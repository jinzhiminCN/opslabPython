# coding:UTF-8
# python3.x

import cv2 as cv

from src import App

# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
img_file = App.resource_file("/opencv/1.jpg")
print(img_file)
img = cv.imread(img_file)
# 创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.waitKey(0)

# 释放窗口
cv.destroyAllWinbredows()
