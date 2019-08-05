#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import pandas as pd

"""使用pandas读取完整的数据"""


def load_dict(file):
    dic = {}
    with open(file, 'r', encoding='UTF-8') as ff:
        for line in ff.readlines():
            line = line.strip().split(",")
            dic[line[0]] = line[1]
    return dic


itdic = load_dict("C:\\Users\\Administrator\\Desktop\\worden.txt")
print("itdic load successful,length:", len(itdic))

df = pd.read_excel("C:\\Users\\Administrator\\Desktop\\worden.xlsx")

# 读取全部数据
allData = pd.DataFrame(df)

itdiccount = []
cgdic = []
# 遍历行
for index, row in allData.iterrows():
    word = row['英语词汇(英语)']
    cgdic.append(word)
    count = 0
    if word in itdic.keys():
        count = itdic.get(word)

    itdiccount.append(count)

print(itdiccount)
print("cgdic len:",len(cgdic))
allData['IT出现次数'] = itdiccount


for key in itdic.keys():
    if key not in cgdic:
        print("新增单词:",key)
        allData = allData.append({"英语词汇(英语)": key, '英语词汇(汉语)': '', '词根词缀': '', '同反义词': '', '比较级及分词复数': '', '例句': '', '常规出现次序': '',
                  'IT出现次数': itdic.get(key) }, ignore_index=True)

allData.to_excel('C:\\Users\\Administrator\\Desktop\\1.xlsx', sheet_name='Sheet1', header=True)