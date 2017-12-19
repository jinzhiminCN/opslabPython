
# coding:UTF-8
# python3.x

import cv2 as cv

RESOURCE_PATH = "/Users/mac/workspace/opslabPython/resource"
# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread(RESOURCE_PATH + "/opencv/1.jpg")
# 创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.waitKey(0)

# 释放窗口
cv.destroyAllWinbredows()
