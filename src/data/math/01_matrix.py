# coding:utf-8

"""矩阵（Matrix）是人为约定的一种数据的表示方法，在图像处理、人工智能等领域，使用矩阵来表示和处理数据非常常见。
"""
import numpy as np

# 定义矩阵 两种形式完全等效
a = np.matrix('5 2 7;1 3 4')
a1 = np.matrix([[5, 2, 7], [1, 3, 4]])

b = np.matrix('5 2 7 6;1 3 4 2;8 2 -2 3')
b1 = np.matrix([[5, 2, 7, 6], [1, 3, 4, 2], [8, 2, -2, 3]])
print(a)
print(a1)
print(b)
print(b1)


# 要把一个 matrix 对象转换为 ndarray 对象，可以直接用 getA() 方法。
# 而把 ndarray 对象转成 matrix 对象可以用 asmatrix() 方法
b = a.getA()
print(b)
# <type 'numpy.ndarray'>
print(type(b))
c = np.asmatrix(b)
print(c)
# <class 'numpy.matrixlib.defmatrix.matrix'>
print(type(c))

# 矩阵的加法与减法
# 两个矩阵相加减，即它们相同位置的元素相加减！
# 注意：只有对于两个行数、列数分别相等的矩阵（即同型矩阵），加减法运算才有意义，即加减运算是可行的．
# 很容易看出，矩阵的加法满足交换律和结合律，即 A+B=B+AA+B=B+A， (A+B)+C=A+(B+C)(A+B)+C=A+(B+C)
a = np.matrix('1 0 1;1 2 1;2 1 1')
b = np.matrix('-1 0 -1;-1 -2 -1;-2 -1 -1')
c = a + b
d = a - b
print(a)
print(b)
print(c)
print(d)

# 矩阵乘法
# 矩阵乘以一个常数，就是所有位置都乘以这个数。
a = np.matrix('1 0 1;1 2 1;2 1 1')
b = a * 5
print(b)

# 矩阵乘矩阵
# 第一个矩阵第一行的每个数字（2和1），各自乘以第二个矩阵第一列对应位置的数字（1和1），然后将乘积相加（ 2 x 1 + 1 x 1）
# 矩阵的本质就是线性方程式，两者是一一对应关系。
a = np.matrix('2 1;4 3')
b = np.matrix('1 2;1 0')
print(a)
print(b)
print(a *b)

# 行列式
# 一个n×n的正方矩阵A的行列式记为  或者  ,一个2×2矩阵的行列式可表示如下
# det([a,b][c,d]) = ad -bc
# 一个n×n矩阵的行列式等于其任意行（或列）的元素与对应的代数余子式乘积之和
mat = np.array([[1,2],[3,4]])
print("mat的行列式:",np.linalg.det(mat))

mbt = np.matrix('-1 0 -1;-1 -2 -1;-2 -1 -1')
print("mat的行列式:",np.linalg.det(mbt))

# 矩阵并没有一个直接叫除法的操作。但有个与之相似的运算，叫做求逆运算。
# 设A是数域上的一个n阶方阵，若在相同数域上存在另一个n阶矩B，使得： AB=BA=E。 
# 则我们称B是A的逆矩阵，而A则被称为可逆矩阵。其中，E为单位矩阵。
# 典型的矩阵求逆方法有：利用定义求逆矩阵、初等变换法、伴随阵法、恒等变形法等。
