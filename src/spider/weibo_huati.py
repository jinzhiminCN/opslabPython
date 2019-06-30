#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# coding:utf-8
import hashlib
import json

import random
import time
import redis

from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()


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

var divs = document.getElementsByTagName("div");
var length = divs.length;
var weibo_list = new Array();
var user_list = new Array();
for(var i=0;i<length;i++){
    var div = divs[i];
    var types = div.getAttribute('action-type');
    if(types=='feed_list_item'){
    	var mid = div.getAttribute('mid');

        var a_list = div.getElementsByTagName("a");
        for(var ali =0;ali<a_list.length;ali++){
            var link = a_list[ali];
            if(link.hasAttribute('usercard')){
                var userName = link.getAttribute('nick-name');
                var userInfo = link.getAttribute('href')
                user_list.push({userName: userName, userInfo: userInfo});
            }
		}

		var sub_divs = div.getElementsByTagName("div");
       	for(var j=0;j<sub_divs.length;j++){
            var sub_div = sub_divs[j];
            var sub_types =  sub_div.getAttribute('node-type');
            if(sub_types =='feed_list_content' || sub_types  =="feed_list_reason"){
                mvalue = textContent(sub_div).replace(/^\s\s*/, '').replace(/\s\s*$/, '');
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
//console.table(page_info.weibo_list);
//console.table(page_info.user_list);
return page_info;
"""


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()


@sched.scheduled_job('interval', minutes=30)
def getSuperHuaTi():
    # 西宁交友 超级话题
    jedis = redis.Redis(host='localhost', port=6379)

    driver.get('https://weibo.com/p/1008086d597f546b905732fb52734a84d99311/super_index')
    driver.implicitly_wait(20)

    scoll = 100
    for i in range(10):
        scoll += 120
        driver.execute_script("window.scrollTo(0," + str(scoll) + ");")
        time.sleep(round(random.random(), 1))

    weibo = driver.execute_script(js_script)
    for wb in weibo.get('weibo_list'):
        if wb['mid']:
            jedis.set("WEIBO#" + wb['mid'], json.dumps(wb, ensure_ascii=False))
    for us in weibo.get('user_list'):
        if us['userName']:
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
    #driver.maximize_window()
    #getSuperHuaTi()
    #sched.start()
    getSuperHuaTi()


