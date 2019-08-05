#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import json

import requests
import hashlib
import random
import time

appid = '20190802000323508'
secretKey = 'YmVP_3TnfqUFMIK8ZLui'


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()


myurl = '/api/trans/vip/translate'
fromLang = 'en'
toLang = 'zh'
WEIBOFILE = open("C:/Users/Administrator/Desktop/weibo_111.txt", "a", encoding='utf_8')
with open("C:/Users/Administrator/Desktop/weibo_daqinghai.txt", 'r', encoding='UTF-8') as ff:
    for line in ff.readlines():
        q = line.split(",")[0].strip()
        qcount = line.split(",")[1].strip()

        salt = random.randint(32768, 65536)
        sign = md5str(appid + q + str(salt) + secretKey)
        myurl = myurl + '?appid=' + appid + '&q=' + q + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        try:
            response = requests.get("http://api.fanyi.baidu.com/" + myurl)
            if response.status_code == 200:
                print("trans :", q,response.status_code,response.text)
                trans = json.loads(response.content.decode("UTF-8"))
                if 'trans_result' in trans:
                    dst = trans['trans_result'][0]['dst']
                    print(q, dst)
                    WEIBOFILE.write(q + "=>" + dst + "=>" + qcount + "\n")
            else:
                time.sleep(60)
        except Exception as e:
            print(e)

        time.sleep(2)
        WEIBOFILE.flush()





