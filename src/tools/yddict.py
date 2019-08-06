#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import time
import requests
import random
from lxml import etree
import re
import json
import pandas as pd

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://dict.youdao.com/w/eng/beautaiful/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

"""根据单词查询组成词根词缀"""


def trim(strs):
    return re.sub(r"\s{2,}", " ", str(strs), flags=re.UNICODE)


def translate(word):
    try:
        qh_search = "https://dict.youdao.com/w/" + word + "/#keyfrom=dict2.top"
        headers["Referer"] = "'http://dict.youdao.com/w/eng/" + word + "/'"
        r = requests.get(qh_search, headers=headers)
        if r.status_code == 200:
            # 使用lxml转换为html格式的数据
            htmlContent = r.content.decode("UTF-8")
            html = etree.HTML(htmlContent)
            # 英标
            yinbiao = trim(html.xpath("string(//div[@class='baav'])"))
            # 翻译
            fanyi = trim(html.xpath("string(//div[@id='phrsListTab']/*/ul)"))

            # 复数比较
            fushu = trim(html.xpath("string(//div[@id='phrsListTab']/*/p[@class='additional'])"))

            # 短语
            duany = trim(html.xpath("string(//div[@id='webPhrase']/p[@class='wordGroup'])"))

            # 例句
            liju = trim(html.xpath("string(//div[@id='bilingual']/ul)"))

            return {"yinbiao": yinbiao, "fanyi": fanyi, "fushu": fushu, "duany": duany, "liju": liju}
        else:
            print("TrannslateError:", r.status_code)
    except Exception as e:
        print("TranslateException:", e)

    return "Error"


if __name__ == '__main__':

    with open("C:\\data\\worden_yd.txt", "a+", encoding="UTF-8") as ff:
        df = pd.read_excel("C:\\data\\worden4.xlsx")
        allData = pd.DataFrame(df)
        for index, row in allData.iterrows():
            word = str(row['英语词汇(英语)'])
            if len(word) > 3:
                trans = translate("provide")
                result = json.dumps(trans, ensure_ascii=False).replace("\n"," ")
                print(word, "===>", result)
                ff.write(word + "===>" + result + "\n")
                time.sleep(round(random.uniform(3, 10), 1))
