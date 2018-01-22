
# coding:UTF-8

"""pandas 是基于 Numpy 构建的含有更高级数据结构和工具的数据分析包
类似于 Numpy 的核心是 ndarray，pandas 也是围绕着 Series 和 DataFrame
两个核心数据结构展开的 。
Series 和 DataFrame 分别对应于一维的序列和二维的表结构"""

import numpy as np
import pandas as pd

# 创建
# pd.DataFrame(param)
#   1.二维array
#   2.Series列表
#   3.value为Series的字典

# 二维array创建
s1 = np.array([1, 2, 3, 4])
s2 = np.array([5, 6, 7, 8])
df = pd.DataFrame([s1, s2])
print("用二维数组创建DataFrame\n", df)

# Series创建
s3 = pd.Series(s1)
s4 = pd.Series(s2)
df1 = pd.DataFrame([s3, s4])
print("用Series列表创建DataFrame\n", df1)

# value为Series的字典结构
s5 = pd.Series(s1)
s6 = pd.Series(s2)
df2 = pd.DataFrame({'a': s5, 'b': s6})
print("用value为Series的字段结构创建\n", df2)

# 属性
#   1.columns:每个colmuns对应的keys
#   2.shape:形状
#   3.index:返回index列表
#   4.value:返回value二维array
#   5.head(n)/tail(n):返回头或尾n行

print("遍历DataFrame的columns字段")
for column in df2.columns:
    print(column)

print("遍历DataFrame的index信息:")
for index in df.index:
    print(index)

print("DataFrmae的形状:", df.shape)
