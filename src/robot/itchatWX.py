#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import random
import itchat
import time
import datetime
from itchat.content import TEXT
from itchat.content import *


def send_move():
    # nickname = input('please input your firends\' nickname : ' )
    # 想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    # users = itchat.search_friends(name=nickname)
    users = itchat.search_friends(name='聊群')  # 使用备注名来查找实际用户名
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    itchat.send("该起来动一下了！", toUserName=userName)
    print('succeed')


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text(msg):
    group = itchat.get_chatrooms(update=True)
    from_user = ''
    for g in group:
        # if g['NickName'] == '全时履约一体化':#从群中找到指定的群聊
        # from_group = g['UserName']
        #     for menb in g['MemberList']:
        #         #print(menb['NickName'])
        #         if menb['NickName'] == "履约助手":#从群成员列表找到用户,只转发他的消息
        #             from_user = menb['UserName']
        #             break
        if g['NickName'] == '系统保障组':  #把消息发到这个群
            to_group = g['UserName']
            itchat.send(msg, to_group)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录
    flag = 0
    while True:
        # send_move()
        random_int = random.randint(300, 500)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +
              "下次系统信息预警在" + str(random_int) + "s后")
        group_text("系统检测检测正常")
        time.sleep(random_int)
