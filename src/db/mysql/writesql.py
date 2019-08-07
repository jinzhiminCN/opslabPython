#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import pymysql
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s- [%(levelname)s-%(levelno)s] > %(name)s: %(message)s",
    filename="insert.log",
    filemode="a",
)

if __name__ == "__main__":
    file = ""

    sql = "insert into t_enword_info('%s','%s','%s','%s''%s','%s',%d,%d)"

    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="tencent",
            charset="utf8",
        )
        
        with open(file, "r", encoding="utf-8") as ff:
            for line in ff.readlines():
                print(line)
                try:
                    mycur = conn.cursor()
                    mycur.execute(line)
                    conn.commit()
                except Exception as es:
                    logging.error("InsertError:"+line)
                  
    except Exception as e:
        print(e)
