# coding:utf-8

import pandas as pd

from src import App

"""使用pandas读取完整的数据"""




df = pd.read_excel(App.resource_file("data/excel-comp-sheetdata.xlsx"))

# 读取全部数据
all_data = pd.DataFrame(df)
print("=all data" + "=" * 80 + ">\n", all_data)

# 遍历行
for index, row in df.iterrows():
    print(row['account'],row['city'])

# # 设置account列为索引类
# all_data = all_data.set_index('account')
# row = all_data.ix[211829]
# print("=row info" + "=" * 80 + ">\n" + str(type(row)))
# print(row)
