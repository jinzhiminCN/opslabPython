#!/usr/bin/python
# coding:utf-8

import pymysql
import jieba.posseg as pseg
import re
import threading
import time
from xpinyin import Pinyin

pinyin = Pinyin()


def get_cnname(var_nick):
    """获得nick中的文中名字"""
    result = ""
    if var_nick:
        words = pseg.cut(var_nick)
        for word, flag in words:
            if 'nr' == flag:
                result += word
    return result


def get_enname(var_nick):
    """获取nick中出现的英文字母"""
    if var_nick:
        return re.sub('[^a-zA-Z]', '', var_nick)
    else:
        return ''


def get_digit(var_nick):
    """获取nick中出现的数字"""
    if var_nick:
        return re.sub('[^0-9]', '', var_nick)
    else:
        return ''


class ProducerThread(threading.Thread):
    pinyin = Pinyin()
    insert_sql = "insert into fuzz.tbl_nick_%d values %s"
    values = "('%s','%s','%s','%s','%s',%s,%d)"
    select_sql = "select  nick,count(*) counts from tt_data_%d group by nick"

    def __init__(self, start):
        threading.Thread.__init__(self)
        self.__start = start

    def run(self):
        print(self.getName() + " is starting....")
        try:
            conn = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                                   database="tencent", charset="utf8")
            rfile = open(self.getName() + ".sql", "w", 1)
            selec_cur = conn.cursor()

            selec_cur.execute(self.select_sql % self.__start)
            lst = selec_cur.fetchall()
            print(self.getName() + " analyzing ...")
            for data in lst:
                nick = data[0]
                cn_nick = get_cnname(nick)
                en_nick = get_enname(nick)
                digit = get_digit(nick)
                nick_qp = pinyin.get_pinyin(cn_nick, '')
                nick_jp = pinyin.get_initials(cn_nick, '').lower()
                counts = data[1]
                tt = self.values % (nick, cn_nick, nick_qp, nick_jp, en_nick, digit, counts)
                value = self.insert_sql % (self.__start, tt)
                # print value
                rfile.write(value.encode("utf-8") + '\n')
        except Exception as e:
            print(e)

        print(self.getName() + " is ending....")


if __name__ == "__main__":
    for i in range(1, 750, 1):
        ProducerThread(i).start()
        time.sleep(60 * 10)
