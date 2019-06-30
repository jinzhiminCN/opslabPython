#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import hashlib
import json
import random
import re
from telnetlib import EC

import pymysql
import redis
import requests
import time
import urllib3
from urllib import parse


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.support.wait import WebDriverWait

urllib3.disable_warnings()




sched = BlockingScheduler()
trimHtml = re.compile(r'<[^>]+>',re.S)


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()

def saveUpdateWeibo(weibo):
    """保存微博"""
    INSERT_WEIBO = "INSERT INTO T_SPIDER_WEIBO(mid,createtime,client,content,uid,uname,reposts,comments,attitudes) " \
                   "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    insert_cursor = conn.cursor()
    try:
        insert_cursor.execute(
            INSERT_WEIBO,
            (weibo['mid'], weibo['createtime'], weibo['fromclient'], weibo['content'], weibo['userid'],
             weibo['username'],weibo['reposts'],weibo['comments'],weibo['attitudes'])
        )
    except Exception as err:
        print("insert row >",err)
        print("insert data>",weibo)
    finally:
        conn.commit()
    insert_cursor.close()


def superHuati(ht,url,id):

    driver.get(ht)
    headers = {
        'Host': 'm.weibo.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Referer': 'https://m.weibo.cn/p/index?containerid=1008086d597f546b905732fb52734a84d99311_-_soul&luicode=10000011&lfid=1008086d597f546b905732fb52734a84d99311_-_main',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'cookies': cookiesstr
    }

    requesturl = url
    if id != "1":
        requesturl += "&since_id="+id
    headers['Referer']=url

    print(requesturl)
    try:
        response = requests.get(requesturl,headers=headers,verify=False)
        if response.status_code != 200:
            print("请求异常:",response.status_code)
            return
        text = response.text.replace("\\t", "").replace("\\n", "")\
                    .replace("\\r", "").replace("\\/", "/").replace("\\\\'", "'")

        data = json.loads(text)
        if data['ok'] == 1:
            try:
                cards = data['data']['cards'][0]['card_group']
                print("==========>",len(cards))
                for card in cards:
                    weibo = {}
                    weibo['fromclient'] = ''
                    weibo['createtime'] = card['mblog']['created_at']
                    weibo['userid'] = card['mblog']['user']['id']
                    weibo['username'] = card['mblog']['user']['screen_name']
                    weibo['mid'] =card['mblog']['mid']
                    weibo['content'] = trimHtml.sub('', card['mblog']['text'])
                    weibo['reposts'] = card['mblog']['reposts_count']
                    weibo['comments'] = card['mblog']['comments_count']
                    weibo['attitudes'] = card['mblog']['attitudes_count']
                    saveUpdateWeibo(weibo)


                if "since_id" in data['data']['pageInfo']:
                    since_id = str(data['data']['pageInfo']['since_id'])
                # else:
                #     scheme = data['data']['scheme']
                #     params = parse.parse_qs( parse.urlparse( scheme ).query )
                #     since_id = params['since_id'][0]
                print("============>",since_id)
                if since_id:
                    time.sleep(10)
                    superHuati(ht,url,since_id)
            except Exception as e:
                print(data)
                print(e)
    except Exception as e:
        print(e)



@sched.scheduled_job('interval', minutes=30)
def getSuperHuaTi():

    arry = [
        # 西宁分享
        "100808407c7d0d4dcd45b13cdc39a9c7ea56c7",

        # 西宁交友
        "1008086d597f546b905732fb52734a84d99311",

        # 西宁打听
        "10080899bfa5537669aa719ca0c2116f52458a",

        # 西宁求助
        "10080849fa099dca8055f87475e0747b40e41d",

        # 西宁房产
        "100808a90a1edb94318eb011f23c03a2e5822f"
    ]
    for arr in arry:
        ht = "https://m.weibo.cn/p/"+arr+"/super_index?jumpfrom=weibocom"
        api = "https://m.weibo.cn/api/container/getIndex?containerid="+arr+"_-_soul&luicode=10000011&lfid="+arr+"_-_main"
        time.sleep(60)
        superHuati(ht,api,"1")

if __name__ == "__main__":
    global cookiesstr
    global driver
    global conn


    loginName = "15110990584"
    password = "wyb2212852"



    conn = pymysql.connect(host="127.0.0.1", user="root",
                           password="123456",
                           database="datas", charset="utf8")



    login_url = "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone 8 Plus"})
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get(login_url)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "loginAction"))
    )
    time.sleep(3)
    driver.find_element_by_id("loginName").clear()
    driver.find_element_by_id("loginName").send_keys(loginName)
    driver.find_element_by_id("loginPassword").send_keys(password)
    driver.find_element_by_id("loginAction").click()


    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "main-wrap"))
    )
    time.sleep(5)
    cookies = driver.get_cookies()[0]
    print(cookies)

    cookiess =""
    for k in cookies:
        cookiess += k+"="+str(cookies[k])+"; "

    cookiesstr = cookiess[:len(cookiess)]
    getSuperHuaTi()
    #sched.start()