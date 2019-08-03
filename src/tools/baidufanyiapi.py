#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import json

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


myurl = '/api/trans/vip/translate'
q = 'resolution'
fromLang = 'en'
toLang = 'zh'


salt = random.randint(32768, 65536)

df = pd.read_excel("C:\\Users\\Administrator\\Desktop\\worden.xlsx")
allData = pd.DataFrame(df)
for index, row in allData.iterrows():
    word = row['英语词汇(英语)']
    sign = md5str(appid+q+str(salt)+secretKey)
    myurl = myurl+'?appid='+appid+'&q='+parse.urlencode(word)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        response = requests.get("http://api.fanyi.baidu.com/"+myurl)
        if response.status_code == 200:
            trans = json.loads(response.content.decode("UTF-8"))
            if 'trans_result' in trans:
                print(q,trans['trans_result'][0]['dst'])
        else:
            print(response.status_code)
    except Exception as e:
        print(e)

