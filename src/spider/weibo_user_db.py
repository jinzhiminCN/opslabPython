#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import pymysql
import re


def todb():
    insert = "insert into spider_weibo_userinfo(userid,username,homepage) VALUES(%s,%s,%s)"
    try:
        myconn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="datas", charset="utf8")
        with open("C:\\Users\\Administrator\\Desktop\\weibo_HT_XNJY_user.txt", encoding="UTF-8") as ff:
            for line in ff:
                try:
                    line = line.strip().replace("\\r\\n", "")
                    tt = line.split(",")
                    uid = tt[0].replace("/u/", "").replace("/", "")
                    name = tt[1]
                    if re.match("\d{10}", uid):
                        homepage = "https://weibo.com/u/" + uid
                    else:
                        homepage = "https://weibo.com/" + uid
                    param = (uid, name, homepage)
                    mycur = myconn.cursor()
                    mycur.execute(insert, param)
                    myconn.commit()
                except Exception as e:
                    print("error:", e)
    except Exception as ex:
        print("error:", ex)
    finally:
        if myconn:
            myconn.close()


if __name__ == '__main__':
    todb()
