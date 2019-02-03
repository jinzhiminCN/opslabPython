
# coding:UTF-8
sql = "insert into dicts.tbl_cnnick_%d(cn_nick,nick_qp,nick_jp,counts) select cn_nick,nick_qp," \
      "nick_jp,sum(counts) from dict.tbl_nick_%d t where t.cn_nick <> '' group by t.cn_nick;\n"

try:
    h_file = open("/data/cnnick.sql", 'w', 1)
    try:
        for i in range(1, 401, 1):
            h_file.write(sql % (i, i))
    finally:
        h_file.close()
except IOError:
    print("IOError")