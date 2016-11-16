#! /usr/bin/python
# coding:UTF-8


'''
    @Digest:统计如家信息表的记录总数
'''
import re
import string
import pymssql
import pymysql

msconn = pymssql.connect(host="127.0.0.1", user="sa", password="wyb2212852", database="shifenzheng", charset='utf8')
myconn = pymysql.connect(host="127.0.0.1", user="root", password="wyb2212852", database="0psdb", charset="utf8")

pchinese = re.compile('([\u4e00-\u9fa5]+)+?')
contrl = re.compile('([\u0000-\u001F]+)+?')
regs = re.compile(u"[`~!@#$%^&*()_+<>?:,./|\\\\;'，。、‘：“《》？~！@#￥%……（）]")
reg_tel = re.compile("\d{11}")
regex_email = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)


def remove_punctuation(text):
    text = re.sub(contrl, '', text)
    text = text.replace(string.punctuation, "")
    text = re.sub(regs, '', text)
    return text


def isMail(email):
    if regex_email.search(email):
        return email.strip()
    return '-'


def findtelnum(mobile, tel):
    telnum = mobile
    if not telnum.strip():
        telnum = tel
    res = reg_tel.findall(telnum)
    if res:
        telnum = res[0]
    else:
        telnum = '-'
    if len(telnum) > 11:
        print telnum
    return telnum


filehand = open("log.txt", "w", 1)
# file = open("rujia.sql", "w", 1)

table = "[shifenzheng].[dbo].[cdsgus]"
count_sql = "select count(*) from " + table
cur = msconn.cursor()
count_sql = "select COUNT(*) FROM " + table
cur.execute(count_sql)
count = cur.fetchall()[0][0]
for top in range(1, count, 1000):
    select_sql = "SELECT replace(ctfid,' ',''),[Name],[Address],[Mobile],[Tel],[EMail] FROM " + \
                 table + " where [ID] >" + str(top) + " and [ID] <" + str(top + 1000) + \
                 " and (len(replace(ctfid,' ','')) = 15 or len(replace(ctfid,' ','')) = 18)"
    print "running ->" + str(top) + "-" + str(top + 1000)
    mscur = msconn.cursor()
    mscur.execute(select_sql)
    list = mscur.fetchall()
    insert_sql = "INSERT INTO 0psdb.tt_card(cardnum,name,address,telnum,email) VALUES"
    for data in list:
        try:
            nick = data[1].strip()
            address = data[2].strip()
            insert_sql += "('" + data[0] + "','" + remove_punctuation(nick) + "','" + remove_punctuation(
                address) + "','" \
                          + findtelnum(data[3], data[4]) + "','" + isMail(data[5]) + "'),"
        except UnicodeDecodeError:
            pass

    #file.write(insert_sql[:-1].encode("utf-8") + ";\n")
    #file.flush()
    try:
        mycur = myconn.cursor()
        mycur.execute(insert_sql[:-1])
        myconn.commit()
    except Exception, ex:
        error = str(Exception) + ":" + str(ex)
        filehand.write("error-sql->" + insert_sql[:-1].encode("utf-8") + ";\n")

msconn.close()

