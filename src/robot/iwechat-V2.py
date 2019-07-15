#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import hashlib
import json
import logging
import threading
import urllib

import redis
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


def get_message(message, userid):
    """聊天处理"""
    print("reveived message form %s text: %s" % (userid,json.dumps(message)))
    result = ""
    itchat.send(result, userid)


def md5str(*args):
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()





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


# 参数    类型  Text键值
# TEXT  文本  文本内容
# MAP   地图  位置文本
# CARD  名片  推荐人字典
# NOTE  通知  通知文本
# SHARING   分享  分享名称
# PICTURE   图片/表情   下载方法
# RECODING  语音  下载方法
# ATTACHMENT    附件  下载方法
# VIDEO 小视频 下载方法
# FRIENDS   好友邀请    添加好友所需参数
# Useless   无用信息    ‘UselessMsg'

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing', "Useless"])
def ignore_msg(msg):
    """覆盖原有的消息回复，设置未忽略"""
    print("reveived message text: %s" % json.dumps(msg))


@itchat.msg_register(['Text'])
def text_reply(msg):
    """回复文本消息"""
    get_message(msg['Text'], msg['FromUserName'])



@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    """发送的是语音/视频等,需要保存至本地"""
    print("reveived message:", msg['Type'])
    msg.download(bastPath + msg['FileName'])
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


@itchat.msg_register('Text', isGroupChat=True, isMpChat=True)
def text_reply(msg):
    """记录微信群和公众号的聊天记录"""
    print("reveived message text: %s" % json.dumps(msg))


@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.get_contract()
    itchat.send('Nice to meet you!', msg['RecommendInfo']['UserName'])


@sched.scheduled_job('interval', hours=6)
def friend_info():
    """获取微信全部好友的信息"""
    jedis = redis.Redis(host='127.0.0.1', port=6379)
    friends = itchat.get_friends(update=True)[1:]
    for f in friends[1:]:
        finfo = {'UserName': f["UserName"],
                 'NickName': f["NickName"],
                 'RemarkName': f["RemarkName"],
                 'Sex': f["Sex"],
                 'addr': f["Province"] + "-" + f["City"],
                 'Signature': f["Signature"],
                 'HeadImgUrl': f["HeadImgUrl"]}

        redisKey = md5str(f['UserName'])
        ss = jedis.get(redisKey)
        if ss:
            uu = json.loads(ss)
            if uu['NickName'] != finfo['NickName']:
                send_one_person("嗯，新换的微信名字很不错", uu['UserName'])
            if uu['Signature'] != finfo['Signature']:
                send_one_person("嗯，新欢的微信签名看着很有道理的样子", uu['UserName'])
            if uu['HeadImgUrl'] != finfo['HeadImgUrl']:
                send_one_person("嗯，新欢的微信头像很就像你的人一样 一向那么有品位啊！", uu['UserName'])

        jedis.set(redisKey, json.dumps(finfo, ensure_ascii=False))


def startsched():
    sched.start()


if __name__ == '__main__':
    global bastPath
    bastPath = "c:/data/itchat/"

    threading.Thread(target=startsched, name="sched").start()
    itchat.auto_login(hotReload=True)

    itchat.run()


