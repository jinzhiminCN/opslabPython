#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

 
import pandas as pd


excel = u'C:\\Users\\Administrator\\Desktop\\语音翻番包\\套餐对应语音翻番包列表.xlsx'
insertSQL ="insert into T_SYSCONFIG(KEY,NAME,STARTTIME,ENDTIME,CONTENT) values('YYFBB%s','语音翻倍包',sysdate,sysdate+10000,'%s');"

df=pd.read_excel(excel,sheet_name='DATA')
data=df.ix[:,['套餐编码','翻番包月费','翻番包包含语音分钟数']].values
#print("获取到所有的值:\n{0}".format(data))
for line in data:
    print(insertSQL %(str(line[0]),"{\"ff\":"+str(line[1])+",\"minute\":"+str(line[2])+"}"))