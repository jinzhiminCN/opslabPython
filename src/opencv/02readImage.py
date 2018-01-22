

# coding:UTF-8


import cv2

RESOURCE_PATH = "/Users/mac/workspace/opslabPython/resource"
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
