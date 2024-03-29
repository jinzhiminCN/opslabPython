
# coding:UTF-8

import cv2
from src import App


from matplotlib import pyplot as plt

img = cv2.imread(setting.resouce_path("/opencv/timg.jpg"), 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
