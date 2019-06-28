#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import json
import logging
import requests
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import json
import urllib.request


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

global My
global friends
apsched = BlockingScheduler()

def get_message(message, userid):
    """图灵聊天机器人"""
    req = {
        "perception": {
            "inputText":
                {
                    "text": message
                },

            "selfInfo":
                {
                    "location":
                        {
                            "city": "西宁",
                            "province": "青海省",
                            "street": "夏都路"
                        }
                }
        },
        "userInfo": {
            "apiKey": 'd581d2e107f34ad3b589951a22ba6bff',
            "userId": userid
        }
    }
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request("http://openapi.tuling123.com/openapi/api/v2",
                                       data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)
    results_text = response_dic['results'][0]['values']['text']
    return results_text




@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    print("reveived message text: %s" % json.dumps(msg))
    result = get_message(msg['Text'], msg['FromUserName'])
    itchat.send('%s: %s' % (msg['Type'], result), msg['FromUserName'])


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    # "发送的是语音/视频等,需要保存至本地"
    msg.download("C:/tmp/itchat/" + msg['FileName'])
    print("reveived message text: %s" % json.dumps(msg))
    if 'Recording' == msg['Type']:
        itchat.send('我现在没带耳机,语音不方便，麻烦发文字。谢谢！', msg['FromUserName'])
    if 'Attachment' == msg['Type']:
        # 附件
        itchat.send('文件已经收到', msg['FromUserName'])
    if 'Picture' == msg['Type']:
        itchat.send('😄😄😄', msg['FromUserName'])
    if 'Video' == msg['Type']:
        # 视频
        itchat.send('😄😄😄', msg['FromUserName'])


@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.get_contract()
    itchat.send('Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register('Text', isGroupChat=True, isMpChat=True)
def text_reply(msg):
    print("reveived message text: %s" % json.dumps(msg))



@apsched.scheduled_job('cron', id='get_weather_info', day_of_week='mon-fri', hour=7, minute=30)
def get_weather_info():
    """获取北京天气，格式化字符串，周一至周五早8点定时发送"""
    try:
        # 获取API信息
        weather = requests.get('http://t.weather.sojson.com/api/weather/city/101010100')
        w = weather.json().get('data').get('forecast')[1]
        # 格式化天气消息
        today_weather = "今日天气：\n温度：%s/%s\n%s:%s\n空气指数：%s\n日出时间：%s\n日落时间：%s\n天气：%s\n%s" % \
                        (w.get('low'), w.get('high'), w.get('fx'), w.get('fl'),
                         w.get('aqi'), w.get('sunrise'), w.get('sunset'), w.get('type'), w.get('notice'))
        # 发送格式化后天气
        print(today_weather)
    except Exception as e:
        logging.warning(e)
        logging.warning('天气发送失败！')


# 获取微信全部好友的信息
def friend_info(f):
    return {'UserName': f["UserName"],
            'NickName': f["NickName"],
            'RemarkName': f["RemarkName"],
            'Sex': f["Sex"],
            'addr': f["Province"] + "-" + f["City"],
            'Signature': f["Signature"],
            'HeadImgUrl': f["HeadImgUrl"]}





if __name__ == '__main__':
    # apsched.start()
    itchat.auto_login(hotReload=True)

    friends = itchat.get_friends(update=True)[0:]
    My = friends[0]
    itchat.run()






    # https://www.cnblogs.com/loleina/p/5623968.html
    #https://www.cnblogs.com/geeklove01/p/8034456.html
    #https://www.cnblogs.com/changbaishan/p/8761588.html
    #https://baijiahao.baidu.com/s?id=1623142149220169146&wfr=spider&for=pc
    #https://blog.csdn.net/jerry_1126/article/details/76409042
    #https://www.liangzl.com/get-article-detail-38547.html
    #https://www.jb51.net/article/156692.htm
    #https://pypi.org/project/itchat/1.0.11/
    #https://itchat.readthedocs.io/zh/latest/
    #https://www.bbsmax.com/A/1O5EBbO8d7/
    #https://blog.csdn.net/weixin_44510615/article/details/88088505
    #https://www.cnblogs.com/taixiang/p/9124822.html
    #https://www.cnblogs.com/birdofparadise/p/8916298.html
    #https://blog.csdn.net/weixin_42353331/article/details/86595539
    #https://www.cnblogs.com/jiaoyu121/p/6944398.html