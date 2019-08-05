#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import time
import requests
import random
from lxml import etree
import pandas as pd

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
           "Accept-Encoding": "gzip",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "Referer": "https://www.baidu.com/",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
           }

"""根据单词查询组成词根词缀"""


def getWordRoot(word):
    wordRoots = ""
    try:
        xpath = "//div[@id='article']/h2"
        qh_search = "https://www.youdict.com/root/search?wd="+word
        r = requests.get(qh_search, headers=headers,timeout=5)
        if r.status_code == 200:
            # 使用lxml转换为html格式的数据
            html = etree.HTML(r.content.decode("UTF-8"))
            h2 = html.xpath("//div[@id='article']/h2")
            for i, j in enumerate(h2):
                txpath = "string(" + xpath + "[" + str(i + 1) + "])"
                # print(txpath)
                wordRoots += "\n" + html.xpath(txpath)

            return wordRoots
        else:
            time.sleep(60)
            return "Error"
            #return getWordRoot(word)
    except Exception as e:
        print(e)
        time.sleep(60)
    return "Error"





if __name__ == '__main__':

    df = pd.read_excel("C:\\Users\\Administrator\\Desktop\\worden.xlsx")
    allData = pd.DataFrame(df)
    for index, row in allData.iterrows():
        if index < 2083:
            continue

        word = str(row['英语词汇(英语)'])
        dst = str(allData.loc[index, '词根词缀'])
        if len(word) > 4:
            # 只处理3个字母以上单词的词根词缀
            wordRoots = getWordRoot(word)
            print(index, "==>", word, "===>", wordRoots)
            allData.loc[index, '词根词缀'] = dst + wordRoots
            time.sleep(round(random.uniform(2, 10), 1))

        if index % 100 == 0:
            allData.to_excel('C:\\Users\\Administrator\\Desktop\\2.xlsx', header=True)
