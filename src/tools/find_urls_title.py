#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import re, time
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
    'Referer': 'http://www.10086.cn',
    'Accept-Language': 'zh-cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate'
}

rr = re.compile(r'<title>.*?</title>')
with open("C:/Users/Administrator/Desktop/1111111111.txt") as f:
    for line in f:

        if line.replace("\n","").endswith("html"):
            r = requests.get(line, headers=headers)
            if r.status_code == 200:
                try:
                    html = r.text.encode('iso-8859-1').decode('utf-8')
                    title = rr.findall(html)[0]
                    print(line.replace("\n","") +" => " +title.replace("<title>","").replace("</title>",""))
                except  Exception as e:
                    # print("error count :"+filepath)
                    pass