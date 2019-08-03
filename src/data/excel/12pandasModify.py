# coding:utf-8

import pandas as pd
from src import App

"""写入文件"""

# 写入excel
df = pd.read_excel(App.resource_file("data/excel-comp-sheetdata.xlsx"))

# 读取全部数据
all_data = pd.DataFrame(df)
print(all_data.loc[14,'name'])
all_data.loc[14,'name']='McDermott PLCA'
all_data.to_excel('C:\\Users\\Administrator\\Desktop\\1.xlsx', header=True,index=False)


