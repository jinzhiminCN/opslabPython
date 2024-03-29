#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import pymysql
import logging
import json
import re

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s- [%(levelname)s-%(levelno)s] > %(name)s: %(message)s",
    filename="insert.log",
    filemode="a",
)


def contains(strs, lst):
    for l in lst:
        if l:
            if l in strs:
                return True

    return False


if __name__ == "__main__":
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="datas",
            charset="utf8",
        )

        file = "C:\\Users\\Administrator\\Desktop\\worden_yd.txt"
        update = "update t_enword_info set duanyu = '%s'  where word='%s'"
        with open(file, "r", encoding="UTF-8") as fs:
            for line in fs.readlines():
                tt = line.split("===>")
                word = tt[0]
                worddict = json.loads(tt[1])

                if worddict and len(worddict) > 0:
                    fanyi = worddict["fanyi"]
                    fushu = worddict["fushu"]
                    duany = worddict["duany"]
                    liju = str(worddict["liju"]).replace("\n", "")

                    if duany:
                        print(word, duany)
                        update_sql = update % (duany, word)
                        print(update_sql)
                        try:
                            mycur = conn.cursor()
                            mycur.execute(update_sql)
                            conn.commit()
                        except Exception as es:
                            logging.error("InsertError:" + update_sql)

                word = ""
                wordRoot = ""
    except Exception as e:
        logging.error("ConnectError:"+e)
