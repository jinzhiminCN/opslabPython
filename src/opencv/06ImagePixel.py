
# coding:UTF-8

"""处理图像的像素"""

import cv2
from etc import setting


img = cv2.imread(setting.resouce_path("/opencv/44.jpg"))
height = img.shape[0]
width = img.shape[1]
for i in range(height):
    for j in range(width):
        print(img[i][j],end=' '),
    print()


# modify pixel
for i in range(height):
    for j in range(width):
        img[i][j] =[0,139,0]


cv2.imshow('Hello World', img)

k = cv2.waitKey(0)

# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()
