#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import json
import time
import requests
import hashlib
import random
import pandas as pd
from urllib import parse

appid = '20190802000323508'
secretKey = 'YmVP_3TnfqUFMIK8ZLui'


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()


def trans(word):
    myurl = '/api/trans/vip/translate'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = md5str(appid + word + str(salt) + secretKey)
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(
        word) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        response = requests.get("http://api.fanyi.baidu.com/" + myurl)
        if response.status_code == 200:
            tran = json.loads(response.content.decode("UTF-8"))
            if 'trans_result' in tran:
                return str(tran['trans_result'][0]['dst'])
        else:
            time.sleep(60)
            return trans(word)
    except Exception as e:
        print(e)
        time.sleep(60)

    return trans(word)


df = pd.read_excel("C:\\Users\\Administrator\\Desktop\\worden.xlsx")
allData = pd.DataFrame(df)
for index, row in allData.iterrows():
    word = str(row['英语词汇(英语)'])
    dst = str(allData.loc[index, '英语词汇(汉语)'])
    newdst = trans(word)
    if dst == 'nan':
        dst = ''
    if newdst != dst:
        dst = dst + ";" + newdst
    print(index, "==>", word, "===>", dst)

    allData.loc[index, '英语词汇(汉语)'] = dst + newdst
    time.sleep(round(random.uniform(1,10),1))

    if index % 100 == 0:
        allData.to_excel('C:\\Users\\Administrator\\Desktop\\1.xlsx', header=True)
