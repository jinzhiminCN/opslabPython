#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import hashlib
import json
import random
import re
import redis
import requests
import time
import urllib3
from urllib import parse


from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
urllib3.disable_warnings()
headers={
    'Host': 'm.weibo.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'MWeibo-Pwa': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer': 'https://m.weibo.cn/p/index?containerid=1008086d597f546b905732fb52734a84d99311_-_soul&luicode=10000011&lfid=1008086d597f546b905732fb52734a84d99311_-_main',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate'
}

sched = BlockingScheduler()
trimHtml = re.compile(r'<[^>]+>',re.S)


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()

def superHuati(url,id):
    """id默认为传1"""
    requesturl = url
    if id != "1":
        requesturl += "&since_id="+id

    print(requesturl)
    response = requests.get(requesturl,headers=headers,verify=False)
    if response.status_code != 200:
        print("请求异常:",response.status_code)
        return
    text = response.text.replace("\\t", "").replace("\\n", "")\
                .replace("\\r", "").replace("\\/", "/").replace("\\\\'", "'")

    data = json.loads(text)
    since_id = ""
    if data['ok'] == 1:
        try:
            cards = data['data']['cards'][0]['card_group']
            print("==========>",len(cards))
            for card in cards:
                create = card['mblog']['created_at']
                userid = card['mblog']['user']['id']
                username = card['mblog']['user']['screen_name']
                mid =card['mblog']['mid']
                content = trimHtml.sub('', card['mblog']['text'])
                reposts_count = card['mblog']['reposts_count']
                comments_count = card['mblog']['comments_count']
                attitudes_count = card['mblog']['attitudes_count']
                print(create,userid,username,mid,content,reposts_count,comments_count,attitudes_count)



            if "since_id" in data['data']['pageInfo']:
                since_id = str(data['data']['pageInfo']['since_id'])
            else:
                scheme = data['data']['scheme']
                params = parse.parse_qs( parse.urlparse( scheme ).query )
                since_id = params['since_id'][0]
            print("============>",since_id)
            if since_id:
                superHuati(url,since_id)
        except Exception as e:
            print(data)
            print(e)

    else:
        print(data)


@sched.scheduled_job('interval', minutes=30)
def getSuperHuaTi():
    # 西宁交友 超级话题
    jedis = redis.Redis(host='10.232.14.216', port=6379, password="xwsptyapp")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone 8 Plus"})
    # #chrome_options.add_argument('--headless')
    # # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('lang=zh_CN.UTF-8')
    # # chrome_options.add_argument('user-agent="' + USER_AGENT + '"')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.get('https://m.weibo.cn/p/index?containerid=1008086d597f546b905732fb52734a'
    #            '84d99311_-_soul&luicode=10000011&lfid=1008086d597f546b905732fb52734a8'
    #            '4d99311_-_main')

    superHuati("https://m.weibo.cn/api/container/getIndex?containerid=1008086d597f546b"
                 "905732fb52734a84d99311_-_soul&luicode=10000011&lfid=1008086d597f546b905"
                 "732fb52734a84d99311_-_main",
                "1"
        )

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone 8 Plus"})
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn";

    driver.get('https://m.weibo.cn/p/index?containerid=1008086d597f546b905732fb52734a84d99311_-_soul&luicode=10000011&lfid=1008086d597f546b905732fb52734a84d99311_-_main')
    cookies = driver.get_cookies()
    print(cookies)
    getSuperHuaTi()
    #sched.start()