__author__ = 'ps'
import pymysql
import re
import threading

select_sql = "SELECT qID,nick,QuId FROM 0psdb.tt_data t where t.qid > %d and t.qid < %d;"

print_log = "%s (%d:%d) -> %d-%d :%d"


class ProducerThread(threading.Thread):
    __pchinese = re.compile(u"[\u4e00-\u9fa5]+?|[\w]+?")

    def __init__(self, start, end):
        threading.Thread.__init__(self)
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
                                 database="0psdb", charset="utf8")
        for top in range(self.__start, self.__end, 1000):
            try:
                mscur = myconn.cursor()
                mscur.execute(select_sql % (top, top + 1000))
                lst = mscur.fetchall()
                print(print_log % (self.getName(), self.__start, self.__end, top, top + 1000, len(lst)))
                # lst_result = []
                # for data in lst:
                # nick = self.handle_name(data[1])
                #     if nick != '-':
                #         lst_result.append("(%d,'%s',%d)" % (data[0], nick, data[2]))
                # if lst_result:
                #     strs = ','.join(lst_result) + ';'
                #     mycur = myconn.cursor()
                #     mycur.execute(insert_sql+" "+strs);
                #     myconn.commit()
            except Exception as ex:
                error = str(Exception) + ":" + str(ex)
                print (error)


if __name__ == "__main__":
    tt = 1
    for i in range(0, 2000000, 500000):
        ProducerThread(i, i + 500000).start()

