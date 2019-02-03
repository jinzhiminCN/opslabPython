#!/usr/bin/python
# coding:utf-8

import os


def countline(file_name):
    count = 0
    with open(file_name) as ff:
        for line in ff:
            count += 1
    return count


count = 0
for root, dirs, files in os.walk("D:/db/DNF"):
    for file in files:
        ff = os.path.join(root, file)
        count += countline(ff)
        print
        ff + "->" + str(countline(ff))

print
"合计:" + str(count)
