import pymysql
import re
import threading


filehand = open("/data/qdata1.txt", "w", 1)

mutex = threading.Lock()


class ProducerThread(threading.Thread):
    __pchinese = re.compile(ur"[\u4e00-\u9fa5]+?|[\w]+?")

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
                                 password="wyb2212852",
                                 database="0psdb", charset="utf8")
        runlog = open(self.getName() + "run.log", "w", 1)
        errorlog = open(self.getName() + "error.log", "w", 1)

        pstr = "%s -> %d - %d"
        insert_sql = "INSERT INTO 0psdb.tt_tencent(id,nick,counts) VALUES"
        select_sql = "select qid,nick,count(*) from tt_data t where  t.qid >= %d and " \
                     "t.qid < %d group by qid,nick"

        for top in range(self.__start, self.__end, 1000):
            print pstr % (self.getName(), top, top + 1000)
            runlog.write(pstr % (self.getName(), top, top + 1000))
            try:
                mscur = myconn.cursor()
                mscur.execute(select_sql % (top, top + 1000))
                lst = mscur.fetchall()
                lst_result = []
                for data in lst:
                    nick = self.handle_name(data[1])
                    if nick != '-':
                        lst_result.append("(%d,'%s',%d)" % (data[0], nick, data[2]))

                if lst_result:
                    strs = ','.join(lst_result) + ';'
                    mycur = myconn.cursor()
                    mycur.execute(insert_sql + " " + strs);
                    myconn.commit()
            except Exception, ex:
                error = str(Exception) + ":" + str(ex)
                errorlog.write(error + "\t" + select_sql % (top, top + 1000))


if __name__ == "__main__":
    for i in range(0, 1500000000, 5000000):
        ProducerThread(i, i + 5000000).start()