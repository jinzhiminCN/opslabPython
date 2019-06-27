#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import json
import logging
import requests
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler


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

sched = BlockingScheduler()


def send_one_group(msg, g_name):
    """
    给某个组发送消息
    :param msg:
    :param g_name:
    :return:
    """
    rooms = itchat.search_chatrooms(g_name)
    if rooms is not None:
        user_name = rooms[0]['UserName']
        itchat.send(msg, toUserName=user_name)
    else:
        print("None group found")


def send_all_group(msg):
    """
    给所有组发送消息
    :param msg:
    :return:
    """
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for r in rooms:
            user_name = r['UserName']
            itchat.send(msg, toUserName=user_name)
        else:
            print("None group found")


def send_one_person(msg, p_name):
    """
    给某个人发消息
    :param msg:
    :param p_name:
    :return:
    """
    persons = itchat.search_friends(p_name)
    if persons is not None:
        user_name = persons[0]['UserName']
        itchat.send_msg(msg, toUserName=user_name)
    else:
        print("None person found")


def send_all_person(msg):
    """
    给所有人发消息
    :param msg:
    :return:
    """
    persons = itchat.get_friends()
    if persons is not None:
        for p in persons:
            user_name = p['UserName']
            itchat.send(msg, toUserName=user_name)
        else:
            print("None person found")


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    print("reveived message text: %s" % json.dumps(msg))
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    # "发送的是语音/视频等,需要保存至本地"
    msg.download("C:/tmp/itchat/"+msg['FileName'])
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


@itchat.msg_register('Text', isGroupChat=True,isMpChat=True)
def text_reply(msg):
    print("reveived message text: %s" % json.dumps(msg))


# 获取北京天气，格式化字符串，周一至周五早8点定时发送，此时女友还未出门
# @sched.scheduled_job('cron', id='get_weather_info', day_of_week='mon-fri', hour=14, minute=21)
def get_weather_info():
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
            'addr': f["Province"]+"-"+f["City"],
            'Signature':f["Signature"],
            'HeadImgUrl': f["HeadImgUrl"]}





if __name__ == '__main__':
    get_weather_info()
    # global MyID
    # global myUserName
    # global mysex
    # itchat.auto_login(hotReload=True)
    # friends = itchat.get_friends(update=True)[0:]
    # My = friends[0]
    # MyID = My["UserName"]
    # myUserName = My['NickName']
    # myUserUin = My['Uin']
    # mysignature = My['Signature']
    # mysex = My['Sex']
    # # # print(friends[1:])
    # # for f in friends[1:]:
    # #     ## print(f)
    # #     print(json.dumps( friend_info(f),ensure_ascii=False ))
    # itchat.run()


#https://www.cnblogs.com/loleina/p/5623968.html
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