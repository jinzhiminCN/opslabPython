
# coding:UTF-8

import numpy as np
import pandas as pd

"""将DataFrame中的一列字符串分割成俩列字符串"""

# 在列表中切割字符串
b = ["5-9*13", "6-10*14", "7-11*15", "8-12*16"]
for i in range(len(b)):
    b[i] = b[i].split("-", 1)

print(b)

# 将DataFrame中的一列分割成俩列
df = pd.DataFrame({"a": ["1", "2", "3", "4"],
                   "b": ["5-9", "6-10", "7-11", "8-12"]})

print(df)

df['b'], df['c'] = df['b'].str.split('-', 1).str
print(df)

# 系列和索引配有一组字符串处理方法。
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
# 大小写转换 lower/upper
print(s.str.lower())
print(s.str.upper())
# 显示字符串的长度
print(s.str.len())

idx = pd.Index([' jack', 'jill ', ' jesse ', 'frank'])
# 取出俩边的空格
print(idx.str.strip())
# 去除左边的空格
print(idx.str.lstrip())
# 去除右边的空格
print(idx.str.rstrip())

# 将列名先去空，再小写，再将空格替换为"_"
df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df)

# 字符串分割
s2 = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
# 以_拆分，返回的是列表
print(s2.str.split('-'))
# 元素可以通过str.get()方法来获取
print(s2.str.split('_').str.get(1))
# 也可以通过str[]来获取
print(s2.str.split('_').str[1])
# 可以通过设置expand参数直接返回一个数据框
print(s2.str.split('_', expand=True))
# 可以通过设置n参数来设置分割点的个数
print(s2.str.split('_', expand=True, n=1))
# rsplit想对与split来说是从相反的方向(reverse direction)来分割
print(s2.str.rsplit('_', expand=True, n=1))

# 像replace和findall这样的方法可以使用正则表达式
s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', '', np.nan, 'CABA', 'dog', 'cat'])
print(s3.str.replace('^.a|dog', 'XX-XX ', case=False))

# 提取字符串
# 如果提取的规则结果有多组，则会返回数据框，不匹配的返回NaN
pd.Series(['a1', 'b2', 'c3']).str.extract('([ab])(\d)', expand=False)

# 注意正则表达式中的任何捕获组名称将用于列名，否则捕获的组名将被当作列名
pd.Series(['a1', 'b2', 'c3']).str.extract('(?P<letter>[ab])(?P<digit>\d)', expand=False)

# 参数expand=True在一组返回值的情况下，返回数据框
pd.Series(['a1', 'b2', 'c3']).str.extract('[ab](\d)', expand=True)

# 参数expand=False在一组返回值的情况下，返回序列(Series)
pd.Series(['a1', 'b2', 'c3']).str.extract('[ab](\d)', expand=False)

# 参数expand=True作用在索引上时，一组数据返回数据框
s = pd.Series(["a1", "b2", "c3"], ["A11", "B22", "C33"])
s.index.str.extract("(?P<letter>[a-zA-Z])", expand=True)

# 参数expand=False作用在索引上时，一组数据返回索引
s.index.str.extract("(?P<letter>[a-zA-Z])", expand=False)

# 提取所有匹配的字符串
# extract只返回第一个匹配到的字符
s = pd.Series(["a1a2", "b1", "c1"], index=["A", "B", "C"])
two_groups = '(?P<letter>[a-z])(?P<digit>[0-9])'
s.str.extract(two_groups, expand=True)

# extractall将匹配所有返回的字符
s.str.extractall(two_groups)

# 测试是否包含某规则
pattern = r'[a-z][0-9]'
pd.Series(['1', '2', '3a', '3b', '03c']).str.contains(pattern)

# match, contains, startswith, and endswith可以设置缺失值是True还是false
s4 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s4.str.contains('A', na=False)

# 提取伪变量
s = pd.Series(['a', 'a|b', np.nan, 'a|c'])
s.str.get_dummies(sep='|')

# 获取复杂索引
idx = pd.Index(['a', 'a|b', np.nan, 'a|c'])
idx.str.get_dummies(sep='|')

# 如果连接的是两个序列，则会对应
print(pd.Series(['a', 'b', 'c']).str.cat(['A', 'B', 'C'], sep=','))

# 否则则会连接自身序列里的值
print(pd.Series(['a', 'b', 'c']).str.cat(sep=','))

# 也可以同时连接复合列表
print(pd.Series(['a', 'b']).str.cat([['x', 'y'], ['1', '2']], sep=','))
