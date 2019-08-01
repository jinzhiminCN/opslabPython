#! /usr/bin/python
# coding=UTF-8
# version:python3.x


import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 页面分享js获取相关信息 
# //获取音标
# $(".trans-other-wrap").find(".dictionary-spell").text();
# //获取单词翻译结果
# $(".trans-other-wrap").find(".dictionary-comment").text()
# //获取记忆技巧 词根词缀
# $(".trans-other-wrap").find(".dictionary-memory").text()
# //获取例句
# $(".trans-other-wrap").find(".double-sample").text()
# //同反义词
# $(".trans-other-wrap .synonym-item").find("div[class='para-syn']").text();
# //词根词缀
# $(".trans-other-wrap .ras-item").find("div[class='ras-title']").text();
js_script = """
var trans = $(".trans-other-wrap");
if(trans){
    var obj = {
        'yd':trans.find(".dictionary-spell").text(),
        'sy':trans.find(".dictionary-comment").text(),
        'jy':trans.find(".dictionary-memory").text(),
        'lj':trans.find(".double-sample").text(),
        'ty':trans.find(".synonym-item").find("div[class='para-syn']").text(),
        'cz':trans.find(".ras-item").find("div[class='ras-title']").text()
    };
    return obj;

return "Error";
"""

def is_exists_element(webdriver, selector):
    """判断元素是否存在"""
    try:
        webdriver.find_element_by_css_selector(selector)
        return True
    except:
        return False


if __name__ == "__main__":
    """由于完整的信息只有在PC端浏览器才能动态展现,因此采用selenium + chrome方式"""
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('user-agent="' + USER_AGENT + '"')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://fanyi.baidu.com/')
    # driver.find_element_by_id("loginname").clear()
    # driver.find_element_by_id("loginname").send_keys(loginname)
    # driver.find_element_by_name("password").send_keys(password)
    # driver.find_element_by_css_selector('.btn_32px').click()
    time.sleep(5)

    driver.get('https://fanyi.baidu.com/#en/zh/resolution')
    driver.implicitly_wait(10)
    while True:
        if is_exists_element(driver,".dictionary-comment"):
            trans = driver.execute_script(js_script)
            if(trans):
                print("翻译结果",trans)
        else:
            driver.implicitly_wait(10)
    time.sleep(120)


