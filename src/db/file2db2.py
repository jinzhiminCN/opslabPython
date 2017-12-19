#!/usr/bin/python
# coding:utf-8

import os
import pymysql
import re
import chardet


pchinese = re.compile('([\u4e00-\u9fa5]+)+?')
contrl = re.compile('([00-1F]+)+?')

regex_email = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)

myconn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="0psdb", charset="utf8")


def filecoding(file_name):
    '''get file encoding wtih chardet'''
    encoding = ""
    size = os.path.getsize(file_name)
    with open(file_name) as ff:
        if size > 1024 * 100:
            data = ff.read(1024 * 100)
        else:
            data = ff.read()

    if data:
        encoding = chardet.detect(data)['encoding']

    return encoding


def isMail(email):
    #替换非ascii字符
    email = re.sub('[^\x00-\x7F]', '', email)
    if regex_email.search(email):
        return email.strip()
    return '-'


def strip(text):
    text = text.strip()
    if text.startswith("'"):
        text = text[1:]
    if text.endswith("'"):
        text = text[:len(text) - 1]
    return text.strip()


def processFile(file_name, encoding):
    insert_sql = "INSERT INTO `0psdb`.`tt_site_temp`(`email`,`nick`,`password`,`site`) VALUES(%s,%s,%s,%s)"

    with open(file_name) as ff:
        for line in ff:
            #process sql-file
            #line = re.sub("\\s","",line)[1:len(line)-2]

            lst = line.split(",")
            if len(lst) >= 2:
                param = ()
                try:
                    name = lst[2].decode(encoding).encode("utf-8")
                    param = (strip(isMail(lst[1])), strip(name), strip(lst[3]), "日月神教裤子")

                except (UnicodeDecodeError, IndexError) as ex:
                    print ("error:" + line)
                    print (ex)
                    param = ()

                if param:
                    try:
                        mycur = myconn.cursor()
                        mycur.execute(insert_sql, param)
                        myconn.commit()
                    except Exception as ex:
                        error = str(Exception) + ":" + str(ex)
                        print("sql error->" + line + "\n\t" + insert_sql + "param->" + str(param))
                    finally:
                        pass
                        #print "sql->"+insert_sql+"param->"+str(param)


def countline(file_name):
    count = 0
    with open(file_name) as ff:
        for line in ff:
            count += 1

            #do simething
    return count


if __name__ == "__main__":
    file1 = u"D:\db\日月神教裤子.sql"
    encoding = filecoding(file1)
    print ("file1 ->" + str(countline(file1)) + "ecoding:" + encoding)
    processFile(file1, "utf-8")

    #processFile(file2)
