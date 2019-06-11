# coding:utf-8

import pandas as pd
import xlrd

from src import App

"""利用pandas处理excel"""



# 遍历excel的sheet
excel_book = xlrd.open_workbook(App.resource_file("data/excel-comp-sheetdata.xlsx"))
for sheet in excel_book.sheets():
    print("\t%s => " % sheet.name)

# 将excel数据导入到pandas数据框架中
df = pd.read_excel(App.resource_file("data/excel-comp-data.xlsx"))

print(type(df))

# 获取sheet的前5行记录
print(df.head())

# 遍历第一个sheet的中全部name列值
names = df[u'name']
print(type(names))
for name in names:
    print(name)

# 直接读取某一列数据
print("=" * 80 + ">")
print(df.name)

excel_data = pd.DataFrame(df)
print(excel_data)



# 读取指定的sheet
# sheetname该参数的名称可能在不同的版本中不太一致，使用时需注意
_df = pd.read_excel(App.resource_file("data/excel-comp-sheetdata.xlsx"), sheetname="Sheet2")
print(_df.head())