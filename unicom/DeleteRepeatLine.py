#!/usr/bin/python
# coding:gbk

import os

out = open("./data/noRepeatLine.txt", "w")

lines = set()

with open('./data/result.txt') as f:
    for line in f:
        tt = line.strip('\n').split(":")
        ll = ':'.join(tt[0:2]) + ":" + tt[6]
        if ll not in lines:
            out.write(ll + "\n")
            lines.add(ll)
