#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

"""
从windows的官方文章
"""
import re, time
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
    'Referer': 'https://www.baidu.com',
    'Accept-Language': 'zh-cn',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;.NET CLR 2.0.50727)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate'
}

base_url = 'https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/%s'
response = requests.get(base_url % 'windows-commands', headers=headers)
soup = BeautifulSoup(response.content,features="html.parser")

for a in soup.find_all('a', attrs={"data-linktype":"relative-path"}):
    cmd = a.get_text()
    if ":"  in cmd or " " in cmd:
        continue

    url = base_url % cmd
    print(cmd,"=>",url)