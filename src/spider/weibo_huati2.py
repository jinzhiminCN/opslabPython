#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import hashlib
import json
import random
import time
import redis


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# 通过js获取页面元素
js_script = """
//提交超级话题页面的微博已经用户信息
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
    jedis = redis.Redis(host='127.0.0.1', port=6379)

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    # chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome(chrome_options=chrome_options)


    # arr = {"https://weibo.com/p/100808407c7d0d4dcd45b13cdc39a9c7ea56c7/super_index",
    #        "https://weibo.com/p/10080899bfa5537669aa719ca0c2116f52458a/super_index",
    #        "https://weibo.com/p/100808a96cbbe5419dad60e26fac1f87e343a1/super_index",
    #        "https://weibo.com/p/1008086d597f546b905732fb52734a84d99311/super_index"}
    arr = {"https://weibo.com/p/100808407c7d0d4dcd45b13cdc39a9c7ea56c7/super_index"}
    for ht in arr:
        driver.get(ht)
        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CLASS_NAME, "WB_frame_c"))
            )
            scoll = 100
            ISDO = True
            while ISDO:
                scoll += 100
                driver.execute_script("window.scrollTo(0," + str(scoll) + ");")
                time.sleep(round(random.random(), 1))
                if EC.presence_of_element_located((By.CLASS_NAME, "W_pages")):
                    ISDO = False

            weibo = driver.execute_script(js_script)
            for wb in weibo.get('weibo_list'):
                if wb['mid']:
                    jedis.set("WEIBO#" + wb['mid'], json.dumps(wb, ensure_ascii=False))
            for us in weibo.get('user_list'):
                if us['userName']:
                    redisKey = "WBUSER#" + md5str(us['userName'])
                    jedis.set(redisKey, json.dumps(us, ensure_ascii=False))
        except Exception as e:
            print(e)




if __name__ == "__main__":
    sched.start()



