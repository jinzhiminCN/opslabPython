#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# coding:utf-8
import hashlib

import pymysql
import requests

import time
from lxml import etree
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
           "Accept-Encoding": "gzip",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "Referer": "https://www.baidu.com/",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
           }



def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()

@sched.scheduled_job('interval', minutes=30)
def main():
    insert = "insert into t_spider_nihaowu(kid,content) VALUES(%s,%s)"
    try:
        myconn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="datas", charset="utf8")
        count = 0
        for i in range(100):
            res = requests.get(url='https://www.nihaowua.com/', headers=headers, timeout=10)
            res.encoding = 'utf-8'
            selector = etree.HTML(res.text)
            xpath_reg = "//section/div/*/text()"
            results = selector.xpath(xpath_reg)
            content = results[0]
            count += 1
            print('********正在爬取中，这是第{}次爬取********'.format(count))
            try:
                kid = md5str(content)
                param = (kid, content)
                mycur = myconn.cursor()
                mycur.execute(insert, param)
                myconn.commit()
            except Exception as e:
                print("error:", e)

            time.sleep(10)

    except Exception as ex:
        print("error:", ex)
    finally:
        if myconn:
            myconn.close()




if __name__ == '__main__':
    sched.start()