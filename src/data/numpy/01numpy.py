
# coding:UTF-8

import numpy as np

"""numPy 是用 C 实现的一个用于数字和矩阵计算的库"""


# array 函数接受两个参数，第一个是要被转换成 array 的 list，第二个是转换后元素的类型，可以省略
arr = np.array([1, 2, 3, 4], int)
print(arr)
print(arr[1:])
print(arr[:2])

arr1 = np.array([[1, 2, 3], [2, 1, 3]], int)
print(arr1)
print(arr1[1][1])
# 多维度切片
print("第一行" + str(arr1[0, :]))
print("第一列" + str(arr1[:, 0]));
# 显示二维数组的各个维度
print(arr1.shape)


# 数组的copy和fill
arr2 = np.array([1, 2, 3], float)
arr3 = arr2.copy()

print(arr2)
print(arr3)
arr3.fill(0)
# 用0来填充数组
print(arr3)

# array的置换
arr4 = np.array([[1, 2, 3, 4, 5, 6]], int)
print(arr4)
# 通过reshape来该边数组的维度
arr5 = arr4.reshape(3, 2)
print(arr5)
# 数组置换
arr6 = arr5.transpose()
print(arr6)

# 将多维数组合并成一维数组
arr7 = arr6.flatten()
print(arr7)
