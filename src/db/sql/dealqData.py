#!/usr/bin/python
# coding:utf-8


"""将nick中一些火星文已经一些标点符号等全部过滤"""

import pymysql
import re
import threading
import time
from Queue import Queue

filehand = open("/data/qdata1.txt", "w", 1)

mutex = threading.Lock()


class ProducerThread(threading.Thread):
    __pchinese = re.compile(r"[\u4e00-\u9fa5]+?|[\w]+?")

    def __init__(self, queues, start, end):
        threading.Thread.__init__(self)
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
                                 password="123456",
                                 database="0psdb",
                                 charset="utf8")
        pstr = "%s -> %d - %d"
        for top in range(self.__start, self.__end, 1000):
            select_sql = "select qid,nick,count(*) from tt_data t " \
                         "where  t.qid >= " + str(top) + " and t.qid < " \
                         + str(top + 1000) + " group by qid,nick"
            print(pstr % (self.getName(), top, top + 1000))
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
            except Exception as e:
                print(e)


class ConsumerThread(threading.Thread):
    def __init__(self, queues):
        threading.Thread.__init__(self, name="Producer")
        self.queue = queues

    def run(self):
        while True:
            strs = self.queue.get()
            self.queue.task_done()
            if strs:
                with mutex:
                    print('Producer is running')
                    filehand.write(strs.encode("utf-8") + '\n')
                    filehand.flush()


if __name__ == "__main__":
    queue = Queue(5000)
    # #启动处理线程
    for i in range(0, 500, 1):
        ConsumerThread(queue).start()

    ##启动生产线程
    for i in range(0, 1500000000, 4000000):
        ProducerThread(queue, i, i + 4000000).start()
        time.sleep(1)



