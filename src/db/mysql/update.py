#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import re
import logging
import pymysql
import pandas as pd

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s- [%(levelname)s-%(levelno)s] > %(name)s: %(message)s",
    filename="insert.log",
    filemode="a",
)

def contains(strs,lst):
    for l in lst:
        if l:
            if l in strs:
                return True
    return False


if __name__ == "__main__":
    file = ""

    sql = "update  t_enword_info  set wordroot='%s' where word ='%s'"

    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="datas",
            charset="utf8",
        )

        df = pd.read_excel("C:\\data\\2.xlsx")
        allData = pd.DataFrame(df)
        for index, row in allData.iterrows():
            word = str(row['英语词汇(英语)'])
            wordRoot = str(row['词根词缀'])
            if wordRoot != 'nan':
                if wordRoot.startswith('nan'):
                    wordRoot = wordRoot[3:]

                wordRoot = wordRoot.replace("\n"," ")
                roots = re.findall('[a-zA-Z]+',wordRoot)
                if contains(word,roots):
                    print(word,wordRoot,roots)
                    update = sql %(wordRoot,word)
                    try:
                        mycur = conn.cursor()
                        mycur.execute(update)
                        conn.commit()
                    except Exception as es:
                        logging.error("InsertError:"+update)

            word =''
            wordRoot=''

    except Exception as e:
        print(e)
