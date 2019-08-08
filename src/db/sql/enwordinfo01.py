#! /usr/bin/python
# coding=UTF-8
# version:python3.x


import pymsql
import json

if __name__ == '__main__':
    # Field	Type	Null	Key	Default	Extra
    # wordtf	varchar(1000)	YES		\N	
    # wordroot	varchar(1000)	YES		\N	
    # wordbjc	varchar(1000)	YES		\N	
    # word	varchar(100)	NO	PRI	\N	
    # transzh	varchar(1000)	YES		\N	
    # itsort	int(10)	YES		\N	
    # example	varchar(4000)	YES		\N	
    # comsort	int(10)	YES		\N	
    file = "E:\\worden-11111.txt"
    update_sql = "update t_enword_info set transzh='%s', wordtf='%s',example='%s' where word ='%s';"

    try:
        conn = pymysql.connect(host="127.0.0.1",
                               user="root", password="123456",
                               database="tencent",
                               charset="utf8")

        with open(file,"r",encoding="UTF-8") as ff:
            for line in ff.readlines():
                tt = line.split("===>")
                word = tt[0]
                wordinfo = json.loads(tt[1])
                wdef = wordinfo['wdef']
                tjyc = wordinfo['tjyc']
                liju = wordinfo['liju'].replace("'","\'")
                sql = update_sql %(wdef,tjyc,liju,word)
                print(word)
                try:
                    mycur = conn.cursor()
                    mycur.execute(sql)
                    conn.commit()
                except Exception as ex:
                    error = str(Exception) + ":" + str(ex)
    except Exception as e:
        print(e)
