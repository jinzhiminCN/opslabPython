#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pymongo
import json
import os
import threading


conn = pymongo.MongoClient("mongodb://localhost:27017/")
iboss = conn["iboss"]
mobile_table = iboss["mobile_table"]
with open("c:/mobile.txt", 'r',encoding="gbk") as f:
    line_list = []
    for line in f:
        tt = line.strip().split(",")
        line_info = {"mobile":tt[0].strip("\""),"name":tt[1].strip("\"")}
        line_list.append(line_info)
        if(len(line_list) == 1000):
            x = mobile_table.insert_many(line_list)
            print(threading.current_thread().getName(),x.inserted_ids)
            line_list = []
            






