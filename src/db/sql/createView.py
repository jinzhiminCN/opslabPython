
# coding:UTF-8
#sql ="create  table tt_cnnick_%d as select cn_nick,nick_qp,nick_jp,sum(counts) counts from tbl_cnnick_%d group by cn_nick;\n"
sql = "insert into tt_nick select cn_nick,counts from tt_cnnick_%d;\n"

try:
    h_file = open("/data/nick.sql", 'w', 1)
    try:
        for i in range(1, 101, 1):
            h_file.write(sql % (i))
    finally:
        h_file.close()
except IOError:
    print("IOError")