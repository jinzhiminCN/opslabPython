

# coding:UTF-8


import cv2
import os
from src import App

RESOURCE_PATH = (os.getcwd()).replace("src/opencv","resource")

img = cv2.imread(RESOURCE_PATH + "/opencv/test.png")
cv2.imshow('image', img)
k = cv2.waitKey(0)

# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()
# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
