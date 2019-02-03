# coding:utf-8

import re
import threading
import time

import pymysql

from src import App


INSERT_SQL = "INSERT INTO tencent.%s(qid,nick,quid) VALUES "
errorlog = open(App.BASE_TEMP + "error.log", "w", 1)
mutex = threading.Lock()


class ProducerThread(threading.Thread):
    select_sql = "select qid,nick,quid from 0psdb.tt_data t where t.qid > %d and t.qid < %d;"

    runlog = "%s -> %d - %d"
    pchinese = re.compile(u"[\u4e00-\u9fa5]+?|[\w]+?")

    def __init__(self, table_name, start, end):
        threading.Thread.__init__(self)
        self.__start = start
        self.__end = end
        self.__trehadName = "%s (%d:%d:%s)" % (self.getName(), start, end, table_name)
        self.__tableName = INSERT_SQL % table_name

    def handle_name(self, nick):
        if nick:
            nick = nick.lower()
            m = self.pchinese.findall(nick)
            if m:
                return ''.join(m)
            else:
                return '-'
        else:
            return '-'

    def run(self):
        try:
            select_conn = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                                          database="0psdb", charset="utf8")
            insert_conn = pymysql.connect(host="192.168.0.5", user="root", password="root",
                                          database="tencent", charset="utf8")
            for top in range(self.__start, self.__end, 500):
                print(self.runlog % (self.__trehadName, top, top + 500))
                selec_cur = select_conn.cursor()
                selec_cur.execute(self.select_sql % (top, top + 500))
                lst = selec_cur.fetchall()
                lst_result = []
                for data in lst:
                    nick = self.handle_name(data[1])
                    if nick and nick != '-':
                        lst_result.append("(%d,'%s',%d)" % (data[0], nick, data[2]))
                if lst_result:
                    strs = ','.join(lst_result) + ';'
                    insert_cur = insert_conn.cursor()
                    insert_cur.execute(self.__tableName + " " + strs)
        except Exception as ex:
            error = str(Exception) + ":" + str(ex)
            with mutex:
                errorlog.write(self.__trehadName + error + "\t" +
                               self.select_sql % (top, top + 500) + "\n")
                errorlog.flush()


if __name__ == "__main__":
    threadstr = "tt_data_%d ->%d:%d\n"
    thread_info = open("thread.log", "w", 1)
    tt = 180
    # for s in range(0, 2000000, 500000):
    # ProducerThread("tt_data_"+str(tt), s, s + 500000).start()
    for i in range(358000000, 1500000000, 2000000):
        for s in range(0, 2000000, 500000):
            thread_info.write(threadstr % (tt, i + s, i + s + 500000))
            thread_info.flush()
            ProducerThread("tt_data_" + str(tt), i + s, i + s + 500000).start()
            time.sleep(10)

        time.sleep(30)
        tt += 1
