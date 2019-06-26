# coding:utf-8

import random
import time

from selenium import webdriver

loginname = "xxxx"
password = "xxx"

# 通过js获取页面元素
js_script = """function getToday() {
    var date = new Date();
    var seperator1 = "-";
    var seperator2 = ":";
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate;
    return currentdate;
}
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
    return s;
}
function GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}
var page = GetQueryString('page');
var divs = document.getElementsByTagName("div");
var length = divs.length;
var weibo_list = new Array();
var user_list = new Array();
for(var i=0;i<length;i++){
    var div = divs[i];
    var types = div.getAttribute('action-type');
    if(types=='feed_list_item'){
        var mid = div.getAttribute('mid');
        var sub_divs = div.getElementsByTagName("div");
        var sub_length = sub_divs.length;
        var mvalue = "";
        for(var j=0;j<sub_length;j++){
            var sub_div = sub_divs[j];
            var sub_types =  sub_div.getAttribute('node-type');
            if(sub_types =='feed_list_content' || sub_types  =="feed_list_reason"){
                mvalue = textContent(sub_div).replace(/^\s\s*/, '').replace(/\s\s*$/, '');
                var a_list = sub_div.getElementsByTagName("a");
                var a_length = a_list.length;
                for(var ali =0;ali<a_length;ali++){
                    var link = a_list[ali];
                    if(link.hasAttribute('usercard')){
                        var userName = link.getAttribute('usercard').substr(5,);
                        var userInfo = link.getAttribute('href')
                        user_list.push({userName: userName, userInfo: userInfo});
                    }
                }
            }
        }


        var mfrom = div.getElementsByClassName("WB_from")[0].innerText.split('来自');
        var createtime = mfrom[0];
        if(createtime.startsWith('今天')){
            createtime = createtime.trim().replace('今天',getToday());
        }else if(!createtime.startsWith('20')){
            createtime = '2017-'+createtime;
        }else{
            createtime = createtime;
        }
        weibo_list.push({mid: mid,createtime:createtime,fromclient:mfrom[1], mvalue: mvalue});
    }
}
var page_info = {'info':'parse info >'+page,'weibo_list':weibo_list,'user_list':user_list};
return page_info;"""


def is_exists_element(webdriver, selector):
    """判断元素是否存在"""
    try:
        webdriver.find_element_by_css_selector(selector)
        return True
    except:
        return False


if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('user-agent="' + USER_AGENT + '"')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://m.weibo.cn/p/1006062093964404')
    # driver.find_element_by_id("loginname").clear()
    # driver.find_element_by_id("loginname").send_keys(loginname)
    # driver.find_element_by_name("password").send_keys(password)
    # driver.find_element_by_css_selector('.btn_32px').click()
    time.sleep(5)

    WEIBOFILE = open("c:/weibo/weibo_daqinghai.txt", "a+", encoding='utf_8')
    USERFILE = open("c:/weibo/weibo_daqinghai_user.txt", "a+", encoding='utf_8')
    LOGGERFILE = open("c:/weibo/weibo_log.txt", "a+", encoding='utf_8')

    #driver.get("https://weibo.com/daqinghai?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1372#feedtop")
    driver.implicitly_wait(10)
    while True:
        scoll = 1000
        while scoll < 20000:
            scoll += 200
            driver.execute_script("window.scrollTo(0," + str(scoll) + ")")
            time.sleep(round(random.random(), 1))

        if not is_exists_element(driver, ".next"):
            time.sleep(3)
        else:
            weibo = driver.execute_script(js_script)
            print(weibo.get('info'))
            LOGGERFILE.write(weibo.get('info') + "\r\n")
            LOGGERFILE.flush()

            for wb in weibo.get('weibo_list'):
                WEIBOFILE.write(str(wb).strip() + "\r\n")
                WEIBOFILE.flush()
            for us in weibo.get('user_list'):
                USERFILE.write(str(us) + "\r\n")
                USERFILE.flush()

            try:
                driver.find_element_by_css_selector(".next").click()
            except:
                LOGGERFILE.write('get next page error\r\n')
                LOGGERFILE.flush()
                time.sleep(60 * 5)
