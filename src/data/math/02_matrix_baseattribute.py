# coding:utf-8

"""矩阵（Matrix）是人为约定的一种数据的表示方法，在图像处理、
人工智能等领域，使用矩阵来表示和处理数据非常常见。
"""
import inspect

import numpy as np

# 定义矩阵 两种形式完全等效
a = np.matrix('5 2 7;1 3 4')
print(type(a))
print('\n'.join(['%s:%s' % item for item in a.__dict__.items()]))

print(getattr(a, 'A'))

print(getattr(a, 'conj'))

print(inspect.getmembers(a, inspect.ismethod))
