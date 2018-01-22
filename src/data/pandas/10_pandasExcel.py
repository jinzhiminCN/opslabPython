# coding:utf-8

import pandas as pd
import xlrd

from src import App

"""利用pandas处理excel"""

# 遍历excel的sheet
excel_book = xlrd.open_workbook(App.BASE_DATA + "excel-comp-data.xlsx")
for sheet in excel_book.sheets():
    print("\t%s => " % sheet.name)

# 遍历excel的sheet
excel_book = xlrd.open_workbook(App.BASE_DATA + "excel-comp-sheetdata.xlsx")
for sheet in excel_book.sheets():
    print("\t%s => " % sheet.name)

# 将excel数据导入到pandas数据框架中
df = pd.read_excel(App.BASE_DATA + "excel-comp-data.xlsx")

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

