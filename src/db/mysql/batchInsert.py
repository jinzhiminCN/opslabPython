#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import pymysql
import logging
import json

"""PyMysql批量插入方法,失败的记录会记录到文件中"""

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s- [%(levelname)s-%(levelno)s] > %(name)s: %(message)s",
    filename="insert.log",
    filemode="a",
)

if __name__ == "__main__":
    file = ""

    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)"

    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="tencent",
            charset="utf8",
        )
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()

        # 一个tuple或者list
        params = []
        with open(file, "r", encoding="UTF-8") as ff:
            for line in ff.readlines():
                print(line)
                params.append(("xiaoming", 31, "boy"))

                if len(params) == 100:
                    try:
                        cursor.executemany(sql, params)
                        conn.commit()
                    except:
                        conn.rollback()
                        logging.error(
                            "BatchInsertError:" + json.dumps(params, ensure_ascii=False)
                        )
                    finally:
                        params = []
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()
