#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pymongo
import json
import os

conn = pymongo.MongoClient("mongodb://localhost:27017/")
iboss = conn["iboss"]
interface = iboss["interface_log"]

map ="function(){emit(this.inter,1);}"
reduce = "function(key,values){return Array.sum(values)}"

resut = interface.map_reduce(map,reduce,"result").find()
for res in resut:
    print(res)