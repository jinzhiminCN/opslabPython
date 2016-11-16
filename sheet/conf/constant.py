#!/usr/bin/python
# coding:utf-8


'''
    @Digest:定义一些全局的变量，之后在需要的from conf import constant然后可以constant.x直接获取
'''

host = "http://135.255.9.112:8055/qhsheet"

headers = {
'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
'Referer': host,
'Accept-Language': 'zh-cn',
'User-Agent': ' Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Host': host,
'Content-Length': '85',
'Connection': 'Keep-Alive',
'Pragma': 'no-cache'
}





