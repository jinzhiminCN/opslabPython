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
from selenium.webdriver.support.wait import WebDriverWait
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# 通过js获取页面元素
js_script = """
//获取微博评论的人
function textContent(elt) {
    var child, type, s = "";
    for (child = elt.firstChild; child != null; child = child.nextSibling) {
        type = child.nodeType;
        if (3 === type || 4 === type) {
            s += child.nodeValue;
        }
        if (1 === type) {
            s += textContent(child);
        }
    }
    return s.replace("@",'');
}
function hasClass(obj,searchClass){
    var className=obj.getAttribute("class");
    var pattern=new RegExp("(^|\\s)"+searchClass+"(\\s|$)");
    return pattern.test(className);
}
function sleep(n) {
    var start = new Date().getTime();
    while(true)  if(new Date().getTime()-start > n) break;
}
var pl = parseInt(textContent(document.getElementsByClassName("tab-item cur")[0]).replace(/[^0-9]/ig,""));
var userlist = new Array();
var divs = document.getElementsByClassName("comment-content")[0].getElementsByTagName("H4");
for(var i=0;i<divs.length;i++){
    if(hasClass(divs[i],"m-text-cut")){
        userlist.push(textContent(divs[i]))
    }
}
var links = document.getElementsByClassName("comment-content")[0].getElementsByTagName("a");
for(var i=0;i<links.length;i++){
    link = links[i]
    href = link.getAttribute('href')
    if(!href){
        userlist.push(textContent(link))
    }
    if(href && href.indexOf("/n/") == 0){
        userlist.push(textContent(link))
    }
}
function unique1(array){
  var n = [];
  for(var i = 0; i < array.length; i++){

    if (n.indexOf(array[i]) == -1) n.push(array[i]);
  }
  return n;
}
var result = {"text":textContent(document.getElementsByClassName("weibo-text")[0]),"pl":pl,"user":unique1(userlist)};

return result;
"""

js_userlist = """
function textContent(elt) {
    var child, type, s = "";
    for (child = elt.firstChild; child != null; child = child.nextSibling) {
        type = child.nodeType;
        if (3 === type || 4 === type) {
            s += child.nodeValue;
        }
        if (1 === type) {
            s += textContent(child);
        }
    }
    return s.replace("@",'');
}
var userlist = new Array();
var divs = document.getElementsByClassName("comment-content")[0].getElementsByTagName("H4");
for(var i=0;i<divs.length;i++){
    if(hasClass(divs[i],"m-text-cut")){
        userlist.push(textContent(divs[i]))
    }
}
var links = document.getElementsByClassName("comment-content")[0].getElementsByTagName("a");
for(var i=0;i<links.length;i++){
    link = links[i]
    href = link.getAttribute('href')
    if(!href){
        userlist.push(textContent(link))
    }
    if(href && href.indexOf("/n/") == 0){
        userlist.push(textContent(link))
    }
}
function unique1(array){
  var n = [];
  for(var i = 0; i < array.length; i++){

    if (n.indexOf(array[i]) == -1) n.push(array[i]);
  }
  return n;
}
"""

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
def saveUpdateWeibo(weibo):
    """保存微博"""
    INSERT_WEIBO = "INSERT INTO T_SPIDER_WEIBO(mid,createtime,client,content,uid) values (%s,%s,%s,%s,%s)"
    insert_cursor = conn.cursor()
    try:
        insert_cursor.execute(
            INSERT_WEIBO,
            (weibo['mid'], weibo['createtime'], weibo['fromclient'], weibo['mvalue'], "")
        )
    except Exception as err:
        print("insert row >", weibo)
    finally:
        conn.commit()
    insert_cursor.close()


def saveUpdateUserInfo(userinfo):
    """保存用户信息"""
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



    driver.get('https://m.weibo.cn/detail/4206576749064081')
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lite-page-tab"))
    )
    result = driver.execute_script(js_script)
    print(result)


    if result['pl'] > 20:
        scoll = 100
        count = int(result['pl'] / 10)
        print(count)
        for i in range(count):
            print(i)
            scoll += 100
            driver.execute_script("window.scrollTo(0," + str(scoll) + ");")
            time.sleep(round(random.uniform(0.5,3.0),1))

    # for uname in result['user']:
    #     redisKey = "WBUSER#" + md5str(uname)
    #     user = {'userName':uname}
    #     if not jedis.get(redisKey):
    #         driver.get('https://m.weibo.cn/n/' + uname)
    #         WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "profile-cover"))
    #         )
    #         uid = driver.execute_script(js_userid).replace('/u/', '').replace('/', '')
    #         if uid:
    #             user['uid'] = uid
    #             redisKey = "WBUSER#" + md5str(user['userName'])
    #             jedis.set(redisKey, json.dumps(user, ensure_ascii=False), ex=2 * 3600)
    #             time.sleep(0.6)
    #         if uid and existsUserInfo(uid, uname):
    #             print("====>", uid, uname)
    #             saveUpdateUserInfo(uid,uname)






if __name__ == "__main__":
    global conn
    conn = pymysql.connect(host="127.0.0.1", user="root",
                           password="123456",
                           database="datas", charset="utf8")
    # getSuperHuaTi()
    WeiboDetails()
