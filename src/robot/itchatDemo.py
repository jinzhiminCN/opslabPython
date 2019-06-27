# coding:UTF-8
# version 3.4

import itchat
import json
from itchat.content import *


# 这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
@itchat.msg_register(TEXT)
def on_message(msg):
    print("reveived message text: %s" % json.dumps(msg))


# 带对象参数注册, 对应消息对象将调用该方法，其中isFriendChat表示好友之间，isGroupChat表示群聊，isMapChat表示公众号
@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True,isMpChat=True)
def on_message1(msg):
    print("reveived message text: %s" % json.dumps(msg))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print("reveived message file: %s" % json.dumps(msg))


# 群消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_message2(msg):
    print("reveived message text: %s" % json.dumps(msg))


if __name__ == '__main__':
    itchat.auto_login(True)

    # 获取完整的好友列表
    print("好友列表:")
    for friend in itchat.get_friends():
        print("\t%s"%json.dumps(friend))


    # 公众号
    print("公众号列表:")
    for mps in itchat.get_mps():
        print("\t%s"%json.dumps(mps))

    # 群聊信息
    print("群聊信息:")
    for chatrooms in itchat.get_chatrooms():
        print("\t%s"%json.dumps(chatrooms))
        #memberList = itchat.update_chatroom(chatrooms[''])
    itchat.run()
