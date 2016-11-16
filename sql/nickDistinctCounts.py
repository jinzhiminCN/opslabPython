#!/usr/bin/python
# coding:utf-8

import pymysql
import threading


class ProducerThread(threading.Thread):
    count_sql = "select  count(distinct nick) counts from tt_data_%d"

    def __init__(self, start, end):
        threading.Thread.__init__(self)
        self.__start = start
        self.__end = end

    def run(self):
        count = 0
        try:
            select_conn = pymysql.connect(host="127.0.0.1", user="root", password="wyb2212852",
                                          database="tencent", charset="utf8")
            for i in range(self.__start, self.__end, 1):
                mscur = select_conn.cursor()
                mscur.execute(self.count_sql % i)
                count += mscur.fetchall()[0][0]

        except Exception, ex:
            error = str(Exception) + ":" + str(ex)
            print error

        print count


if __name__ == '__main__':
    for i in range(1, 750, 75):
        ProducerThread(i, i + 10).start()

        # 统计结果有8000w