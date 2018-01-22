__author__ = 'ps'
import pymysql

create_sql = \
    "CREATE TABLE %s (qID int(11) NOT NULL," \
    "nick varchar(40) NOT NULL, QuId int(11)" \
    " NOT NULL,  KEY IDX_TT_DATA_QID (qID))" \
    " ENGINE=MyISAM DEFAULT CHARSET=utf8;"

if __name__ == "__main__":
    myconn = pymysql.connect(host="192.168.0.5", user="root",
                             password="root",
                             database="tencent",
                             charset="utf8")
    tt = 1
    for i in range(0, 1500000000, 2000000):
        table_name = "tt_data_" + str(tt)
        tt += 1
        create_table = create_sql % (table_name)
        print create_table
        mycur = myconn.cursor()
        mycur.execute(create_table)
        myconn.commit()
