#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import time
import requests
import random
from lxml import etree
import pandas as pd
import json

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
           "Accept-Encoding": "gzip",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "Referer": "https://www.baidu.com/",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
           }

"""根据单词查询组成词根词缀"""


def getWord(word):
    try:
        qh_search = "http://www.cgdict.com/index.php?w=" + word + "&app=cigen&ac=word"
        r = requests.get(qh_search, headers=headers)
        if r.status_code == 200:
            # 使用lxml转换为html格式的数据
            html = etree.HTML(r.content.decode("UTF-8"))
            content = str(html.xpath("string(//div[@class='cleft'])"))
            if "作为词根的常见用法" in content:
                wdef = str(html.xpath("string(//div[@class='main-title-b']/following-sibling::div[@class='wdef'][2])")) \
                    .strip()
            else:
                print("+++++++++++>")
                wdef = str(html.xpath("string(//div[@class='main-title-b']/following-sibling::div[@class='wdef'][1])")) \
                    .strip()

            if "同义词" in content:
                tjyc = str(html.xpath("string(//div[@class='cleft']/div[@class='wdef'][last()-1])")).strip()
            else:
                tjyc = ""

            cigen = str(html.xpath("string(//div[@class='cright']/div/div[@calss='wcigen'])")).strip()
            liju = str(html.xpath("string(//div[@class='cleft']/div[@class='wdef'][last()])")).strip()

            return {"wdef": wdef, "tjyc": tjyc, "liju": liju,"cg":cigen}
        else:
            time.sleep(60)
            return getWord(word)
    except Exception as e:
        print(e)
        time.sleep(60)
    return "Error"


if __name__ == '__main__':
    with open("C:\\Users\\Administrator\\Desktop\\worden.txt","a+",encoding="UTF-8") as ff:
        df = pd.read_excel("C:\\Users\\Administrator\\Desktop\\worden.xlsx")
        allData = pd.DataFrame(df)
        for index, row in allData.iterrows():
            word = str(row['英语词汇(英语)'])
            sy = getWord(word)
            print(word, "===>", json.dumps(sy, ensure_ascii=False))
            ff.write(word+"===>"+json.dumps(sy, ensure_ascii=False)+"\n")
            time.sleep(round(random.uniform(2, 10), 1))

