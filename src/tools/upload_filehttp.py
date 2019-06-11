#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import requests
import base64

if __name__ == '__main__':



    # curl -F "upfile=@/Users/yugj/Documents/hell/test/classes.dex" http://localhost:8000
    #
    files = {"014.jpg": open(u"D:\\图片\\中国风\\014.jpg", "rb").read()
             ,"1353930166177.jpg": open(u"D:\\图片\\中国风\\1353930166177.jpg", "rb").read()}
    res = requests.request("POST", "http://localhost:9090/upload", data=None, files=files)
    print(res.status_code,"===>",res.text)


    proxies = {'http': 'http://127.0.0.1:8888'}
    head = {'Path':base64.b64encode('../../../../banner'.encode('utf-8'))}
    payload = {'path': '/banner'}
    files = {"server1.conf": open(u"c:\\server1.conf", "rb").read()}
    res = requests.request("POST", "http://localhost:9090/upload", proxies=proxies,headers=head, data=None, files=files)
    print(res.status_code, "===>", res.text)