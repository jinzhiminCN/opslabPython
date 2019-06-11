#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import _thread
import os
import random
import shutil
import uuid
import zipfile


def del_path(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_path(c_path)
        else:
            os.remove(c_path)
    os.rmdir(path)


def find_sqlite_file(path, dir):
    """查找指定文件下的sqlite数据库文件"""
    with open(dir + "/sqlite.index", "a+", encoding="utf-8") as f:
        for root, dirs, files in os.walk(path):
            for name in files:
                ff = os.path.join(root, name).replace("\\","/")
                try:
                    with open(ff, "rb") as temp:
                        prefix = ''.join(['%02x' % b for b in bytes(temp.read(10))])
                        if prefix.startswith("53514c6974652066"):
                            fs = ff.replace("\\", "/")
                            nf = str(uuid.uuid1())
                            dstf = (dir + "/" + nf).replace("\\","/")
                            print(fs, dstf)
                            f.write(fs + '==>' + nf + "\n")
                            _thread.start_new_thread(shutil.copy, (fs, dstf))
                            # 读写校验
                            # try:
                            #     conn = sqlite3.connect(ff)
                            #     cursor = conn.cursor()
                            #     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                            #     if (len(cursor.fetchall()) > 0):
                            #
                            # except Exception as e:
                            #     print("Exception:", e)
                            # finally:
                            #     conn.close()
                except Exception as e:
                    print("Exception:", e)


def zip_dir(dirname, zipfilename):
    filelist = []
    f = zipfile.ZipFile(zipfilename, "w", zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(dirname):
        for name in files:
            ff = os.path.join(root, name)
            filelist.append(ff)
            arcname = ff[len(dirname):]
            f.write(ff, arcname)

    f.close()


if __name__ == '__main__':
    """在C盘中查找所以有的sqlite文件并打成随机的zip"""
    dir = "c:/" + ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
    os.mkdir(dir)
    find_sqlite_file("c:/", dir)
    zip_dir(dir,dir+".zip")
    del_path(dir)

