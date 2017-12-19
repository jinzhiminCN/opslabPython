# coding:utf-8

import pandas as pd
from conf import App

"""写入文件"""

# 写入excel
write = pd.ExcelWriter(App.BASE_TEMP + "excel-comp-data.xlsx")
df1 = pd.DataFrame(data={'col1': [1, 1], 'col2': [2, 2]})
df1.to_excel(write, 'sheet-test')
write.save()
