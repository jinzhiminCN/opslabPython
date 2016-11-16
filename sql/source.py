#! /usr/bin/python
# coding:UTF-8
try:
    h_file = open("/data/nick/all.sql", 'w', 1)
    try:
        for i in range(10, 401, 1):
            h_file.write("source /data/nick/tbl_nick_%d;\n" % i)
    finally:
        h_file.close()
except IOError:
    print "IOError"