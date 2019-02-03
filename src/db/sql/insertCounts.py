#!/usr/bin/python
# coding:utf-8

import pymysql
from xpinyin import Pinyin
import jieba.posseg as pseg
import re


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


pinyin = Pinyin()

conn = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                       database="tencent", charset="utf8")

insert_sql = "insert into fuzz.tbl_nick_%d values (%s)"

values = "('%s','%s','%s',%s','%s',%s,%d)"

select_sql = "select  nick,count(*) counts from tt_data_%d group by nick"

selec_cur = conn.cursor()
selec_cur.execute(select_sql % 1)
lst = selec_cur.fetchall()
lst_result = []
for data in lst:
    nick = data[0]
    cn_nick = get_cnname(nick)
    en_nick = get_enname(nick)
    digit = get_digit(nick)
    nick_qp = pinyin.get_pinyin(cn_nick, '')
    nick_jp = pinyin.get_initials(cn_nick, '').lower()
    counts = data[1]
    value = values % (nick, cn_nick, nick_qp, nick_jp, en_nick, digit, counts)
    lst_result.append(value)

if lst_result:
    insert = insert_sql % (1, ','.join(lst_result) + ';')
    # insert_cur = conn.cursor()
    # insert_cur.execute(insert_sql)



