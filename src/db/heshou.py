#!/usr/bin/python
# coding:utf-8

import os
import pymysql

myconn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="0psdb", charset="utf8")


def processFile(file_name):
    insert_sql = "INSERT INTO `0psdb`.`tt_site`(`email`,`nick`,`password`,`site`)VALUES"

    with open(file_name) as ff:
        for line in ff:
            line = line.replace("(", "").replace(")", "").replace("'", "")
            lst = line.split(",")
            temp = "('" + lst[3] + "','" + lst[1] + "','" + lst[2] + "','heishou.org');"
            try:
                mycur = myconn.cursor()
                mycur.execute(insert_sql + temp)
                myconn.commit()
            except Exception as ex:
                error = str(Exception) + ":" + str(ex)


def countline(file_name):
    count = 0
    with open(file_name) as ff:
        for line in ff:
            count += 1

            # do simething
    return count


if __name__ == "__main__":
    file1 = u"D:\db\黑手\1.txt"
    file2 = u"D:\db\黑手\2.txt"
    print("file1 ->" + str(countline(file1)))
    print("file2 ->" + str(countline(file2)))
    # processFile(file1)
    # processFile(file2)
