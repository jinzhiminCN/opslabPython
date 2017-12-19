
# coding:UTF-8

import numpy as np
import pandas as pd

dates = pd.date_range('20161001', periods=6)
# 创建DataFrame
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

print("=查询每一列的数据结构" + "=" * 20 + ">\n", df.dtypes)

print("=查看基本统计属性预览" + "=" * 20 + ">\n", df.describe())

print("=行列转换" + "=" * 20 + ">\n", df.T)

print("=根据某一列的数值进行排序" + "=" * 20 + ">\n", df.sort_values(by='A', ascending=False))

# 选择/切片
print("=选择单独的一列，返回Series与df.A的效果相当:\n", df['A'])

# 位置切片
print("=位置切片:\n", df[0:3])
print("=通过索引切片:\n", df['20161001':'20161003'])
