
# coding:UTF-8

import pandas as pd

# pandas的索引函数主要有三种:
#   1.loc标签索引，行和列的名称
#   2.iloc整数索引（绝对位置索引）,绝对意义上的几行激烈，起始索引为0
#   3.ix是iloc和loc的合体
#   4.at是loc的快捷方式
#   5.iat是iloc的快捷方式
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'], 'c': ["A", "B", "C"]})
print(df)

# 选择某一行
print("选择某一行:\n", df.loc[1, :])
print("选择某一行:\n", df.loc[0])
