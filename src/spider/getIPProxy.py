#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

#coding:utf-8

from bs4 import BeautifulSoup
import requests
import telnetlib
import random

"""
获取免费的代理IP
https://www.xicidaili.com
http://www.data5u.com/
http://www.xsdaili.com/
http://www.89ip.cn/
https://www.kuaidaili.com
"""




headers = {
    'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
    'Referer': 'https://www.baidu.com',
    'Accept-Language': 'zh-cn',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;.NET CLR 2.0.50727)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate'
}


def cip(x,y):
    """验证代理是否可用"""
    try:
        telnetlib.Telnet(x, port=y, timeout=5)
        return True
    except:
        return False


def xici_http():
    """获取西辞的HTTP代理"""
    http_list = []
    for  i in range(1,2):
        if i == 1:
            IPURL ="https://www.xicidaili.com/wt"
        else:
            IPURL = "https://www.xicidaili.com/wt/"+str(i)

        r=requests.get(IPURL, headers=headers)
        if r.status_code != 200:
            print("XICI_HTTP URL ERROR")
            return

        soup=BeautifulSoup(r.text,features="html.parser")
        trs = soup.select("#ip_list tr.odd")
        for tr in trs:
            td = tr.find_all("td")
            ip = td[1].get_text()
            port = td[2].get_text()
            protol = td[5].get_text().lower()
            if cip(ip,port):
                http_list.append("%s://%s:%s"%(protol,ip.strip(),port.strip()))

    return http_list

def xici_https():
    """获取西辞的HTTPS代理"""
    https_list = []
    for i in range(1,2):
        if i == 1:
            IPURL = "https://www.xicidaili.com/wn"
        else:
            IPURL = "https://www.xicidaili.com/wn" + str(i)

        r=requests.get(IPURL, headers=headers)
        if r.status_code != 200:
            print("XICI_HTTP URL ERROR")
            return

        soup=BeautifulSoup(r.text,features="html.parser")
        trs = soup.select("#ip_list tr.odd")
        for tr in trs:
            td = tr.find_all("td")
            ip = td[1].get_text()
            port = int(td[2].get_text())
            protol = td[5].get_text()
            https_list.append("%s://%s:%d"%(protol,ip.strip(),port.strip()))

    return https_list



def kuai_http():
    """获取西辞的HTTP代理"""
    http_list = []
    for i in range(1,2):
        if i == 1:
            IPURL = "https://www.kuaidaili.com/free/inha/"
        else:
            IPURL = "https://www.kuaidaili.com/free/inha/%d/" %  i

        r = requests.get(IPURL, headers=headers)
        if r.status_code != 200:
            print("XICI_HTTP URL ERROR")
            return

        soup = BeautifulSoup(r.text, features="html.parser")
        trs = soup.select("#list tr")
        for tr in trs:
            td = tr.find_all("td")
            if len(td) == 7:
                ip = td[0].get_text()
                port = td[1].get_text()
                protol = td[3].get_text().lower()
                if cip(ip, port):
                    http_list.append("%s://%s:%s" % (protol, ip.strip(), port.strip()))
    return http_list





def to_reqeusts_format(list):
    result = []
    for ip in list:
        if ip.startswith("http://"):
            result.append({'http':ip})
        if ip.startswith("https://"):
            result.append({'https':ip})

    return result




if __name__ == '__main__':
    # http_list = kuai_http()
    # http_list += xici_http()
    # reqeusts_ips  = to_reqeusts_format(http_list)
    # print(reqeusts_ips)
    reqeusts_ips = [{'http': 'http://183.148.149.66:9999'}, {'http': 'http://111.177.181.38:9999'},
               {'http': 'http://110.52.235.250:9999'}, {'http': 'http://1.197.203.78:9999'},
               {'http': 'http://117.131.99.210:53281'}, {'http': 'http://139.196.90.80:80'},
               {'http': 'http://111.181.68.201:9999'}, {'http': 'http://119.101.117.35:9999'},
               {'http': 'http://119.101.112.129:9999'},
               {'http': 'http://119.101.118.225:9999'}, {'http': 'http://110.52.235.244:9999'},
               {'http': 'http://110.52.235.84:9999'},
               {'http': 'http://119.101.114.132:9999'}, {'http': 'http://218.75.70.3:8118'},
               {'http': 'http://119.101.115.84:9999'},
               {'http': 'http://119.101.112.112:9999'}, {'http': 'http://110.52.235.203:9999'},
               {'http': 'http://110.52.235.73:9999'},
               {'http': 'http://110.52.235.87:9999'}]

    print(requests.get('http://icanhazip.com', headers=headers, proxies=random.choice(reqeusts_ips)).text)
