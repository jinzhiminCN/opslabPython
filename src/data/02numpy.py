
# coding:UTF-8

import numpy as np

# 多数组联合
a = np.array([1, 2, 3, 4], int)
b = np.array([5, 6, 7, 8], int)
c = np.concatenate((a, b))
print("多个组联合:" + str(c))

a = np.array([[1, 2], [3, 4]], int)
b = np.array([[5, 6], [7, 8]], int)
c = np.concatenate((a, b))
print("多个组联合:" + str(c))