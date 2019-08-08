#! /usr/bin/python
# coding=UTF-8
# version:python3.x


import pandas as pd
import pymysql


if __name__ == '__main__':
    insert_sql = "insert into t_enword_info  values('%s','%s','%s','%s','%s',%s,%d,%d)"

    try:
        conn = pymysql.connect(host="127.0.0.1",
                               user="root", password="123456",
                               database="tencent",
                               charset="utf8")

        df = pd.read_excel("C:\\Users\\Administrator\\Desktop\\worden.xlsx")
        allData = pd.DataFrame(df)
        for index, row in allData.iterrows():
            word = str(row['英语词汇(英语)'])
            wordsy = str(row['英语词汇(汉语)'])
            wordci = str(row['词根词缀'])
            wordty = str(row['同反义词'])
            wordbj = str(row['比较级及分词复数'])
            wordlj = str(row['例句'])
            wordcx = row['常规出现次序']
            wordicx = row['IT出现次数']

            tt = insert_sql % (word, wordsy, wordci, wordty, wordbj, wordlj, wordcx, wordicx)

            try:
                mycur = conn.cursor()
                mycur.execute(tt)
                conn.commit()
            except Exception as ex:
                error = str(Exception) + ":" + str(ex)
    except Exception as e:
        print(e)



