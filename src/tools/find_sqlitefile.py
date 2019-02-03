#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import os
import sqlite3

def find_sqlite_file(path):
    """查找指定文件下的sqlite数据库文件"""
    lst = []
    for root, dirs, files in os.walk(path):
        for name in files:
            ff = os.path.join(root, name)
            try:
                with open(ff, "rb") as temp:
                    prefix = ''.join(['%02x' % b for b in bytes(temp.read(10))])
                    if prefix.startswith("53514c6974652066"):
                        try:
                            conn = sqlite3.connect(ff)
                            cursor = conn.cursor()
                            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                            if (len(cursor.fetchall()) > 0):
                                lst.append(ff.replace("\\","/"))
                        except:
                            pass
                        finally:
                            conn.close()
            except:
                pass


    return lst


if __name__ == '__main__':
    lst = find_sqlite_file("C:/Users/Administrator")
    for f in lst:
        print(f)