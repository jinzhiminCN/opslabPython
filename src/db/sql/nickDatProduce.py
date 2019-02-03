#!/usr/bin/python
# coding:utf-8

import pymysql
import jieba.posseg as pseg
import re
import time
from xpinyin import Pinyin


def get_cnname(var_nick):
    """获得nick中的文中名字"""
    result = ""
    if var_nick:
        words = pseg.cut(var_nick)
        for word, flag in words:
            if 'nr' == flag:
                result += word
    if len(result) > 6:
        result = ''
    return result


def get_enname(var_nick):
    """获取nick中出现的英文字母"""
    regx = re.compile(r'[a-zA-Z]{3,8}')
    lst = regx.findall(var_nick)
    if lst:
        return lst[0]
    else:
        return ''


def get_digit(var_nick):
    """获取nick中出现的数字"""
    regx = re.compile(r'\d{3,8}')
    lst = regx.findall(var_nick)
    if lst:
        return lst[0]
    else:
        return ''


if __name__ == "__main__":
    pinyin = Pinyin()
    insert_sql = "INSERT INTO dict.tbl_nick_%d(nick,cn_nick,nick_qp,nick_jp,english,digit,counts) values %s"
    template = "('%s','%s','%s','%s','%s','%s',%d)"
    select_sql = "select  nick, counts from fuzz.tbl_nick_%d"

    try:
        sconn = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                                database="fuzz", charset="utf8")

        iconn = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                                database="dict", charset="utf8")

        selec_cur = sconn.cursor()
        for i in range(1, 2, 1):
            count = selec_cur.execute(select_sql % i)
            print("table->%d:%d" % (i, count))
            for ii in range(1, count, 1000):
                lst = selec_cur.fetchmany(1000)
                print(" %d analyzing ..." % ii)

                lst_result = []
                for data in lst:
                    nick = data[0]
                    cn_nick = get_cnname(nick)
                    en_nick = get_enname(nick)
                    digit = get_digit(nick)
                    nick_qp = pinyin.get_pinyin(cn_nick, '')
                    if len(nick_qp) > 20:
                        nick_qp = ''
                    nick_jp = pinyin.get_initials(cn_nick, '').lower()
                    counts = data[1]
                    lst_result.append(template % (nick, cn_nick, nick_qp, nick_jp, en_nick, digit, counts))

                if lst_result:
                    values = insert_sql % (i, ','.join(lst_result))
                    # print values
                    icur = iconn.cursor()
                    icur.execute(values)
                    icur.close()
                    iconn.commit()


    except Exception as e:
        print(e)
