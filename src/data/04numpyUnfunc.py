
# coding:UTF-8

"""ufunc是universal function的缩写，它是一种能对数组的每个元素进行操作的函数。"""

import numpy as np

x = np.linspace(0, 2*np.pi, 10)
print(x)

# 对数组中的元素计算sin值
y = np.sin(x)
print(y)