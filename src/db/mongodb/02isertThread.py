#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pymongo
import json
import os
import threading

def parse_file(file):
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    iboss = conn["iboss"]
    interface = iboss["interface_log"]
    with open(file, 'r',encoding="utf-8") as f:
        line_list = []
        for line in f:
            res = json.loads(str(line[line.find('{'):]))
            line_list.append(res)
            if(len(line_list) == 1000):
                x = interface.insert_many(line_list)
                print(threading.current_thread().getName(),x.inserted_ids)
                line_list = []
            






for fpathe,dirs,fs in os.walk("C:/DATA/crmDetail_689186.log.201808_log_bak/"):
    for ff in fs:
        file =  os.path.join(fpathe,ff)
        t=threading.Thread(target=parse_file,args=(file,))
        t.start()


while 1:
   pass

