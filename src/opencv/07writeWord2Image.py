
# coding:UTF-8

"""向图像中输出文字"""

import cv2
from etc import setting

# Load an color image in grayscale
image = cv2.imread(setting.resouce_path("/opencv/4.jpg"), 0)

# font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font

# y = image.height / 2 # y position of the text
# x = image.width / 4 # x position of the text
#
# cv2.PutText(image,"Hello World !", (x,y), cv2.RGB(255, 255, 255)) #Draw the text
image_height = int(image.shape[0] -20)
image_width = int(image.shape[1] -450)

cv2.putText(image, 'Hello World', (image_height, image_width), 0, 0.5, (0, 0, 255), 2)
cv2.imshow('Hello World', image)  # Show the image

k = cv2.waitKey(0)

# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()
# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('messigray.png', image)
    cv2.destroyAllWindows()