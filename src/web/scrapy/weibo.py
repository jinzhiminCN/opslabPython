# coding:utf-8
import hashlib
import json

import random
import time
import redis

from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
loginname = "xxxx"
password = "xxx"

# 通过js获取页面元素
js_script = """
function dateFtt(fmt,date) {
 var o = {
 "M+" : date.getMonth()+1,
 "d+" : date.getDate(),
 "h+" : date.getHours(),
 "m+" : date.getMinutes(),
 "s+" : date.getSeconds(),
 "q+" : Math.floor((date.getMonth()+3)/3),
 "S" : date.getMilliseconds()
 };
 if(/(y+)/.test(fmt))
 fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length));
 for(var k in o)
 if(new RegExp("("+ k +")").test(fmt))
 fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
 return fmt;
}
function deteminute(res){
    var ss = res;
    if (res.indexOf("今天") > -1) {
        var now = new Date;
        ss = res.replace("今天",dateFtt('yyyy-MM-dd',now));
    }
    if(res.indexOf("分钟前") >0){
        var now = new Date;
        now.setMinutes (now.getMinutes () - parseInt(res));
        ss= dateFtt('yyyy-MM-dd hh:mm:ss',now);
    }
    if(res.indexOf("小时前") > 0){
        var now = new Date;
        now.setMinutes (now.getHours () - parseInt(res));
        ss= dateFtt('yyyy-MM-dd hh:mm:ss',now);
    }
    console.log("====>"+res+"===>"+ss);
    return ss;

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
        if(!createtime.startsWith('20')){
            createtime = deteminute(createtime);
        }else{
            createtime = createtime;
        }
        weibo_list.push({mid: mid,createtime:createtime,fromclient:mfrom[1], mvalue: mvalue});
    }
}
var page_info = {'weibo_list':weibo_list,'user_list':user_list};
console.table(page_info.weibo_list);
console.table(page_info.user_list);
return page_info;
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


@sched.scheduled_job('interval', seconds=30)
def daqinghaiwang():
    jedis = redis.Redis(host='10.232.14.216', port=6379, password="xwsptyapp")
    driver.get('https://weibo.com/daqinghai?is_all=1')
    driver.implicitly_wait(10)
    time.sleep(5)
    scoll = 100
    while scoll < 20000:
        scoll += 100
        js = "window.scrollTo(0," + str(scoll) + ");"
        driver.execute_script(js)
        time.sleep(round(random.random(), 1))

    weibo = driver.execute_script(js_script)
    for wb in weibo.get('weibo_list'):
        jedis.set("WEIBO#" + wb['mid'], json.dumps(wb, ensure_ascii=False))
    for us in weibo.get('user_list'):
        driver.get('https:' + us['userInfo'])
        driver.implicitly_wait(3)
        userId = driver.execute_script(js_userid)
        us['uid'] = userId.repalce("/u/", "").replace("/", "")
        redisKey = "WBUSER#" + md5str(us['userName'])
        jedis.set(redisKey, json.dumps(us, ensure_ascii=False))


if __name__ == "__main__":
    global driver

    # mobile_emulation = {"deviceName":"iPhone 8 Plus"}
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #chrome_options.add_argument("--user-agent=iphone 6 plus")
    #chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('user-agent="' + USER_AGENT + '"')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    sched.start()


