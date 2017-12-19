
# coding:UTF-8


import cv2

RESOURCE_PATH = "/Users/mac/workspace/opslabPython/resource"

img = cv2.imread(RESOURCE_PATH + "/opencv/1.jpg", 0)
print(img.shape)
print(img.size)
