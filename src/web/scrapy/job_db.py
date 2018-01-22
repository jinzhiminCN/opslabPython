# ecoding:utf-8

import pymysql

if __name__ == "__main__":
    conn=pymysql.connect(host="127.0.0.1", user="root",
                        password="123456",
                        database="opslab_db", charset="utf8")
    select_sql = """select * from (select (minvalue + maxvalues)/2 xz,counts from(
            select cast(SUBSTRING_INDEX(zwyx_s, '-',1) as UNSIGNED INTEGER) as minvalue,cast(SUBSTRING_INDEX(zwyx_s, '-',-1) 
            as UNSIGNED INTEGER) as maxvalues,zwyx_s,counts from (
            select zwyx_s,count(*) counts from t_spider_jobs where zwyx_s <>'' group by zwyx_s
            )f  where f.counts > 20
            ) tt) tts where tts.xz > %s and tts.xz < %s """
    
    for i in range(1000,100000,1000):
        select_cursor=conn.cursor()
        select_cursor.execute(select_sql,(i,i+1000))
        lst = select_cursor.fetchall()
        sum = 0
        for data in lst:
            sum = sum + data[1]
        
        if not sum <= 0:
            print(i,'-',i+1000,'-',sum)
