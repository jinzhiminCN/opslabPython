#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# coding:utf-8
import hashlib
import json
import random
import time

import pymysql
import redis
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.support.wait import WebDriverWait

sched = BlockingScheduler()

# 通过js获取页面元素
js_userid = """
　　　　var url = document.location.toString();
　　　　var arrUrl = url.split("//");
　　　　var start = arrUrl[1].indexOf("/");
　　　　var relUrl = arrUrl[1].substring(start);
　　　　if(relUrl.indexOf("?") != -1){
　　　　　　relUrl = relUrl.split("?")[0];
　　　　}
　　　　return relUrl;
"""


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()

def saveUpdate(userinfo):
    insert = "REPLACE  into t_spider_weibouser(kid,userid,username) VALUES(%s,%s,%s)"
    insert_cursor = conn.cursor()
    kid = md5str(userinfo['uid']+userinfo['userName'])
    try:
        insert_cursor.execute(
            insert,
            (kid, userinfo['uid'],userinfo['userName'])
        )
    except Exception as err:
        print("insert row >", userinfo,err)
    finally:
        conn.commit()
    insert_cursor.close()

def existsUserInfo(uid,uname):
    select = "select * from t_spider_weibouser t where t.kid =%s;"
    select_cursor = conn.cursor()
    kid = md5str(uid + uname)
    try:
        user = select_cursor.execute(
            select,
            (kid)
        )
        row_1 = select_cursor.fetchone()
        if row_1:
            return True
        return False
    except Exception as err:
        print("select row >", err)
    finally:
        conn.commit()
        select_cursor.close()

@sched.scheduled_job('interval', minutes=30)
def WeiboDetails():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 8 Plus"})
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    jedis = redis.Redis(host='localhost', port=6379)



    keys = jedis.keys("WBUSER#*")
    for key in keys:
        try:
            us = json.loads(jedis.get(key))
            uname = us['userName']

            uid = ''

            if 'uid' in us:
                uid = us['uid'].replace('/u/','').replace('/','')
            if 'userInfo' in us:
                uid = us['userInfo'].split('?')[0].replace('https://weibo.com/u/','').replace('/','')
            if not uid:
                driver.get('https://m.weibo.cn/n/' + uname)
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "profile-cover"))
                    # or
                    # EC.presence_of_element_located((By.XPATH, '//html/body/div/p[@class="h5-4con"]'))
                )
                uid = driver.execute_script(js_userid).replace('/u/', '').replace('/', '')
                if uid :
                    us['uid'] = uid
                    redisKey = "WBUSER#" + md5str(us['userName'])
                    jedis.set(redisKey, json.dumps(us, ensure_ascii=False), ex=2 * 3600)
                    time.sleep(0.6)

            if uid and existsUserInfo(uid,uname):
                print("====>",uid,uname)
                saveUpdate(us)


        except Exception as err:
            print("Exception",err, us)


if __name__ == "__main__":
    global conn
    conn = pymysql.connect(host="127.0.0.1", user="root",
                      password="123456",
                      database="datas", charset="utf8")
    # getSuperHuaTi()
    WeiboDetails()
