
# coding:UTF-8

import cv2
from src import App

img_file = App.resource_file("/opencv/timg.jpg")
im=cv2.imread(img_file, 0)

sobx = cv2.CreateImage(cv2.GetSize(im), cv2.IPL_DEPTH_16S, 1)
#Sobel with x-order=1
cv2.Sobel(im, sobx, 1, 0, 3)

soby = cv2.CreateImage(cv2.GetSize(im), cv2.IPL_DEPTH_16S, 1)
#Sobel withy-oder=1
cv2.Sobel(im, soby, 0, 1, 3)

cv2.Abs(sobx, sobx)
cv2.Abs(soby, soby)

result = cv2.CloneImage(im)
#Add the two results together.
cv2.Add(sobx, soby, result)

cv2.Threshold(result, result, 100, 255, cv2.CV_THRESH_BINARY_INV)

cv2.ShowImage('Image', im)
cv2.ShowImage('Result', result)

cv2.WaitKey(0)