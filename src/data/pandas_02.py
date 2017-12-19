
# coding:UTF-8

"""pandas 是基于 Numpy 构建的含有更高级数据结构和工具的数据分析包
类似于 Numpy 的核心是 ndarray，pandas 也是围绕着 Series 和 DataFrame
两个核心数据结构展开的 。
Series 和 DataFrame 分别对应于一维的序列和二维的表结构"""

from pandas import Series,DataFrame
import pandas as pd

# Series 可以看做一个定长的有序字典。基本任意的一维数据都可以用来构造 Series 对象
s = Series([1,2,3.0,'abc'])
print(s)