#! /usr/bin/python
# coding:utf-8

'''
    @Digest:讲扣扣群数据库从Mssql转换到mysql
'''
import sys, re
import fileinput
import pymssql
import pymysql
import string


reload(sys)
sys.setdefaultencoding('utf-8')

pchinese = re.compile('([\u4e00-\u9fa5]+)+?')
contrl = re.compile('([\u0000-\u001F]+)+?')
regs = re.compile(u"[`~!@#$%^&*()_+<>?:,./|\\\\;'，。、‘：“《》？~！@#￥%……（）]")


def remove_punctuation(text):
    text = re.sub(contrl, '', nick)
    text = text.replace(string.punctuation, "")
    text = re.sub(regs, '', nick)
    return text


msconn = pymssql.connect(host="127.0.0.1", user="sa", password="wyb2212852", database="GroupData1", charset='utf8')
myconn = pymysql.connect(host="127.0.0.1", user="root", password="wyb2212852", database="0psdb", charset="utf8")

filehand = open("log.text", "w", 1)

x = 1
for i in range(1, 12):
    for y in range(1, 101):
        table = "[GroupData" + str(i) + "].[dbo].[Group" + str(x) + "]"
        x += 1

        cur = msconn.cursor()
        count_sql = "select COUNT(*) FROM " + table
        cur.execute(count_sql)
        count = cur.fetchall()[0][0]
        if count:
            print table + "->" + str(count)
            for top in range(1, count, 1000):
                select_sql = "SELECT [QQNum],[Nick],[QunNum] FROM " + table + " where [ID] >" + str(
                    top) + " and [ID] <" + str(top + 1000)
                #print select_sql
                mscur = msconn.cursor()
                mscur.execute(select_sql)
                list = mscur.fetchall()
                insert_sql = "INSERT INTO 0psdb.tt_data VALUES"
                for data in list:
                    try:
                        nick = unicode(data[1].encode("latin1"), "gbk", 'ignore').strip()
                        insert_sql += "(" + str(data[0]) + ",'" + remove_punctuation(nick) + "'," + str(data[2]) + "),"
                    except UnicodeDecodeError:
                        m = pchinese.findall(re.sub(contrl, '', data[0]))
                        insert_sql += "(" + str(data[0]) + ",'" + ''.m + "'," + str(data[2]) + "),"
                #print insert_sql[:-1]
                try:
                    mycur = myconn.cursor()
                    mycur.execute(insert_sql[:-1])
                    myconn.commit()
                except Exception, ex:
                    error = str(Exception) + ":" + str(ex)
                    filehand.write(error + "\n")
        count = 0

msconn.close()
myconn.close()
filehand.close()






