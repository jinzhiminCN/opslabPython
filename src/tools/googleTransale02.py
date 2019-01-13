#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon
import random

import requests
import json
import execjs  # 必须，需要先用pip 安装，用来执行js脚本



class Py4Js():
    def __init__(self):
        self.ctx = execjs.compile(""" 
    function TL(a) { 
    var k = ""; 
    var b = 406644; 
    var b1 = 3293161072;       
    var jd = "."; 
    var $b = "+-a^+6"; 
    var Zb = "+-3^+b+-f";    
    for (var e = [], f = 0, g = 0; g < a.length; g++) { 
        var m = a.charCodeAt(g); 
        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
        e[f++] = m >> 18 | 240, 
        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
        e[f++] = m >> 6 & 63 | 128), 
        e[f++] = m & 63 | 128) 
    } 
    a = b; 
    for (f = 0; f < e.length; f++) a += e[f], 
    a = RL(a, $b); 
    a = RL(a, Zb); 
    a ^= b1 || 0; 
    0 > a && (a = (a & 2147483647) + 2147483648); 
    a %= 1E6; 
    return a.toString() + jd + (a ^ b) 
  };      
  function RL(a, b) { 
    var t = "a"; 
    var Yb = "+"; 
    for (var c = 0; c < b.length - 2; c += 3) { 
        var d = b.charAt(c + 2), 
        d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
        d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
    } 
    return a 
  } 
 """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def buildUrl(text, tk):
    baseUrl = 'https://translate.google.cn/translate_a/single'
    baseUrl += '?client=t&'
    baseUrl += 's1=auto&'
    baseUrl += 't1=zh-CN&'
    baseUrl += 'h1=zh-CN&'
    baseUrl += 'dt=at&'
    baseUrl += 'dt=bd&'
    baseUrl += 'dt=ex&'
    baseUrl += 'dt=ld&'
    baseUrl += 'dt=md&'
    baseUrl += 'dt=qca&'
    baseUrl += 'dt=rw&'
    baseUrl += 'dt=rm&'
    baseUrl += 'dt=ss&'
    baseUrl += 'dt=t&'
    baseUrl += 'ie=UTF-8&'
    baseUrl += 'oe=UTF-8&'
    baseUrl += 'otf=1&'
    baseUrl += 'pc=1&'
    baseUrl += 'ssel=0&'
    baseUrl += 'tsel=0&'
    baseUrl += 'kc=2&'
    baseUrl += 'tk=' + str(tk) + '&'
    baseUrl += 'q=' + text
    return baseUrl


def translate(text):
    header = {
        'authority': 'translate.google.cn',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '',
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;.NET CLR 2.0.50727)',
        'x-client-data': 'CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE='
    }
    proxies = [{'http': 'http://183.148.149.66:9999'}, {'http': 'http://111.177.181.38:9999'},
               {'http': 'http://110.52.235.250:9999'}, {'http': 'http://1.197.203.78:9999'},
               {'http': 'http://117.131.99.210:53281'}, {'http': 'http://139.196.90.80:80'},
               {'http': 'http://111.181.68.201:9999'}, {'http': 'http://119.101.117.35:9999'}, {'http': 'http://119.101.112.129:9999'},
               {'http': 'http://119.101.118.225:9999'}, {'http': 'http://110.52.235.244:9999'}, {'http': 'http://110.52.235.84:9999'},
               {'http': 'http://119.101.114.132:9999'}, {'http': 'http://218.75.70.3:8118'}, {'http': 'http://119.101.115.84:9999'},
               {'http': 'http://119.101.112.112:9999'}, {'http': 'http://110.52.235.203:9999'}, {'http': 'http://110.52.235.73:9999'},
               {'http': 'http://110.52.235.87:9999'}]
    url = buildUrl(text, js.getTk(text))
    res = ''
    try:
        r = requests.get(url,headers=header,proxies=random.choice(proxies))

        result = json.loads(r.text)
        if result[7] != None:
            # 如果我们文本输错，提示你是不是要找xxx的话，那么重新把xxx正确的翻译之后返回
            try:
                correctText = result[7][0].replace('<b><i>', ' ').replace('</i></b>', '')
                print(correctText)
                correctUrl = buildUrl(correctText, js.getTk(correctText))
                correctR = requests.get(correctUrl)
                newResult = json.loads(correctR.text)
                res = newResult[0][0][0]
            except Exception as e:
                print(e)
                res = result[0][0][0]

        else:
            res = result[0][0][0]
    except Exception as e:
        res = ''
        print(url)
        print("翻译" + text + "失败")
        print("错误信息:")
        print(e)
    finally:
        return res



if __name__ == '__main__':
    js = Py4Js()
    res = translate('DiskPart verifies only that the partition is capable of containing the operating system startup files. DiskPart does not check the contents of the partition. If you mistakenly mark a partition as active and it does not contain the operating system startup files, your computer might not start.')
    print(res)
