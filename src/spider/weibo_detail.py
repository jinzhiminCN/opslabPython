#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# coding:utf-8

import random
import time

from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
loginname = "xxxx"
password = "xxx"

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
return unique1(userlist);
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


@sched.scheduled_job('interval', minutes=30)
def getPLUSERLIST():
    # 西宁交友 超级话题
    with open("c:/weibo/weibo_PL_user.txt", "a+", encoding='utf_8') as USERLIST:
        with open("c:/weibo/weibo_daqinghai.txt", encoding="UTF-8") as ff:
            for line in ff:
                if line.strip().replace("\\r\\n", ""):
                    tt = line.split(",", 4)
                    mid = tt[2].replace("'", "").replace("mid:", "").strip()
                    driver.get('https://m.weibo.cn/detail/' + mid)
                    driver.implicitly_wait(3)
                    scoll = 100
                    for i in range(10):
                        scoll += 100
                        js = "window.scrollTo(0," + str(scoll) + ");"
                        driver.execute_script(js)
                        time.sleep(round(random.random(), 1))

                    weibo = driver.execute_script(js_script)
                    print(mid + "=====>" + str(len(weibo)))
                    for us in weibo:
                        driver.get('https://m.weibo.cn/n/' + us)
                        driver.implicitly_wait(2)
                        userId = driver.execute_script(js_userid)
                        USERLIST.write(str(us) + ',' + userId + "\r\n")

                    USERLIST.flush()


if __name__ == "__main__":
    global driver
    # mobile_emulation =
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 8 Plus"})
    #chrome_options.add_argument("--user-agent=iphone 6 plus")
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('user-agent="' + USER_AGENT + '"')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    #getSuperHuaTi()
    getPLUSERLIST()


