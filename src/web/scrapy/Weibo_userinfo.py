# coding:utf-8

import random
import time

from selenium import webdriver

js_userinfo = """
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
    return s.replace(/\s/g,"");
}
var li = document.getElementsByClassName("card11");
var ss =""
for (var i in li){
    ss +=textContent(li[i])+"##";
}
return ss;
"""


def userInfo(user_uid):
    uid = user_uid.replace("/u/", "")
    driver.get('https://m.weibo.cn/p/index?containerid=23028'+uid
               +'_-_INFO&title=%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99&luicode=10000011&lfid=23028'+uid)

    time.sleep(round(random.random(), 1))
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,550);")
    res = driver.execute_script(js_userinfo)
    print("===>" + res)


if __name__ == "__main__":
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName":"iPhone 8 Plus"})
    # chrome_options.add_argument("--user-agent=iphone 6 plus")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('user-agent="' + USER_AGENT + '"')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()

    userInfo("/u/3200592325")

    time.sleep(5000)
