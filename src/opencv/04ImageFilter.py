

# coding:UTF-8


import cv2 as cv

image = cv.imread('D:/image/test.png', 0)
cv.imshow("Original", image)

grey = cv.CreateImage((image.width, image.height), 8, 1)  # 8depth, 1 channel so grayscale
cv.CvtColor(image, grey, cv.CV_RGBA2GRAY)  # Convert to gray so act as a filter
cv.imshow('Greyed', grey)

# 平滑变换
smoothed = cv.CloneImage(image)
cv.Smooth(image, smoothed, cv.CV_MEDIAN)  # Apply a smooth alogrithm with the specified algorithm cv.MEDIAN

