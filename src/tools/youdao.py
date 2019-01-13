#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

import urllib.request
import urllib.parse
import json

line = input('你想翻译啥:')
# line ="这只是个测试"
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
data = {}
data['i'] = line
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1517799189818'
data['sign'] = '8682192c0707c52ecdffbc98f77a17ac'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'



data = urllib.parse.urlencode(data).encode('utf-8')

proxy_handler = urllib.request.ProxyHandler({'http': 'http://113.53.29.218:30736/'})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open(url)
html = response.read().decode('utf-8')
html = response.read().decode('utf-8')

translate_results = json.loads(html)
# 找到翻译结果，load函数能将str转换成dict类型
translate_results = translate_results['translateResult'][0][0]['tgt']
# 打印翻译信息
print("翻译的结果是：%s" % translate_results)
