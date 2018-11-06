#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import re
import requests
from src import App

"""
发现一组url的title信息
"""

headers = {
    'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
    'Referer': 'http://www.10086.cn',
    'Accept-Language': 'zh-cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate'
}

rr = re.compile(r'<title>.*?</title>')
file = App.resource_file("C:/Users/Administrator/Desktop/111.txt")
with open(file) as f:
    for line in f:
        line = line.strip()
        r = requests.get(line, headers=headers)
        if r.status_code == 200:
            try:
                title = rr.findall(r.text)[0]
                print(line.replace("\n","") +" => " +title.replace("<title>","").replace("</title>",""))
            except  Exception as e:
                print("error count :"+e)
                pass
        else:
            print(line,r.status_code)