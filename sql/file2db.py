#!/usr/bin/python
# coding:utf-8

import os
import pymysql

myconn = pymysql.connect(host="127.0.0.1", user="root", password="wyb2212852", database="0psdb", charset="utf8")


def processFile(file_name):
    insert_sql = "INSERT INTO `0psdb`.`tt_site_temp`(`email`,`nick`,`password`,`site`)VALUES"

    with open(file_name) as ff:
        for line in ff:
            line = line.replace("(", "").replace(")", "").replace("'", "")
            lst = line.split("	")
            temp = "('" + lst[0] + "','" + '-' + "','" + islst[1] + "','www.17173.com');"
            try:
                mycur = myconn.cursor()
                mycur.execute(insert_sql + temp)
                myconn.commit()
            except Exception, ex:
                error = str(Exception) + ":" + str(ex)


def countline(file_name):
    count = 0
    with open(file_name) as ff:
        for line in ff:
            count += 1

            #do simething
    return count


if __name__ == "__main__":
    file1 = ur"D:\db\1717-1.txt"
    print "file1 ->" + str(countline(file1))
    processFile(file1)
    #processFile(file2)
