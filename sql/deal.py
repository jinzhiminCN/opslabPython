#!/usr/bin/python
# coding:utf-8


"""将nick中一些火星文已经一些标点符号等全部过滤"""

import pymysql
import re
from threading import Thread
from Queue import Queue


class ProducerThread(Thread):
    __pchinese = re.compile(ur"[\u4e00-\u9fa5]+?|[\w]+?")

    def __init__(self, queues, start, end):
        Thread.__init__(self)
        self.queue = queues
        self.__start = start
        self.__end = end

    def handle_name(self, nick):
        m = self.__pchinese.findall(nick)
        if m:
            return ''.join(m)
        else:
            return '-'

    def run(self):
        myconn = pymysql.connect(host="127.0.0.1", user="root",
                                 password="wyb2212852",
                                 database="0psdb",
                                 charset="utf8")
        pstr = "%s -> %d - %d"
        for top in range(self.__start, self.__end, 1000):
            select_sql = "select qid,nick,count(*) from tt_data t " \
                         "where  t.qid >= " + str(top) + " and t.qid < " \
                         + str(top + 1000) + " group by qid,nick"
            print pstr % (self.getName(), top, top + 1000)
            try:

                mscur = myconn.cursor()
                mscur.execute(select_sql)
                lst = mscur.fetchall()
                lst_result = []
                for data in lst:
                    nick = self.handle_name(data[1])
                    if nick != '-':
                        lst_result.append("(%d,'%s',%d)" % (data[0], nick, data[2]))

                if lst_result:
                    strs = ','.join(lst_result) + ';'
                    self.queue.put(strs)
            except Exception, e:
                print e


class ConsumerThread(Thread):
    filehand = open("/data/qdata1.txt", "w", 1)

    def __init__(self, queues):
        Thread.__init__(self, name="Producer")
        self.queue = queues

    def run(self):
        while True:
            strs = self.queue.get()
            self.queue.task_done()
            if strs:
                self.filehand.write(strs.encode("utf-8") + '\n')


if __name__ == "__main__":
    queue = Queue(5000)

    # #启动生产线程
    for i in range(0, 1500000000, 5000000):
        ProducerThread(queue, i, i + 5000000).start()
    ##启动处理线程
    ConsumerThread(queue).start()


