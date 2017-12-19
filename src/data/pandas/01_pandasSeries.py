
# coding:UTF-8

"""pandas 是基于 Numpy 构建的含有更高级数据结构和工具的数据分析包
类似于 Numpy 的核心是 ndarray，pandas 也是围绕着 Series 和 DataFrame
两个核心数据结构展开的 。
Series 和 DataFrame 分别对应于一维的序列和二维的表结构"""

import numpy as np
import pandas as pd

# 大概就是说Series结构是基于NumPy的ndarray结构，是一个一维的标签矩阵（感觉跟python里的字典结构有点像）
# Series 可以看做一个定长的有序字典。基本任意的一维数据都可以用来构造 Series 对象
s = pd.Series([1, 2, 3.0, 'abc'])
print(s)

# 创建

# 1. pd.Series([list],index=[list]) //以list为参数，index可选，若不填默认从0开始
ss = pd.Series(['a', 'b', 'c', 'd'], index=[1, 2, 3, 4])
print(ss)
# 2. pd.Series({dict}) 以字典的方式创建
sss = pd.Series({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
print(sss)

# 取值
print("index value")
# s[index] 或者 s[index的list]
print(ss[1])
# 取index为1和三的元素
print(ss[[1, 3]])
# 取index为1到3之间的元素
print(ss[1:3])
# head(n)和tail(n) 取出头n行或者尾n行
print(ss.head(1))
print(ss.tail(2))
# 取出index返回list
print(ss.index)
# 取values 返回list
print(ss.values)

v = pd.Series([4, 3, 3, 2, 2, 2, 1, np.nan])
print('len() Series长度，包括NaN:\n\t', len(v))
print("shape() 矩阵形状:\n\t", np.shape(v))
print("count() Series长度，不包括NaN:\n\t", v.count())
print("unique() 剔除重复的values:\n\t", v.unique())
print("value_counts() 统计value值出现次数:\n\t", v.value_counts())
print("查看每一列的数据结构:\n\t", v.dtypes)
# 加运算
# 相同index的value相加，若index并非共有的则该index对应value变为NaN
s1 = pd.Series([1, 2, 3, 4], index=[1, 2, 3, 4])
s2 = pd.Series([4, 3, 2, 1])
print(s1 + s2)

s3 = pd.Series(['a', 'b', 'c', 'd'], index=[1, 2, 3, 4])
s4 = pd.Series(['a', 'b', 'c', 'd'])
print(s3 + s4)
