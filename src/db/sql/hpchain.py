#!/usr/bin/python
# codeing:utf-8

import os


def handleFile(file_name):
    with open(file_name) as ff:
        print ("processing " + ff.name)
        for line in ff:
            print (line)


def iterPath(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            handleFile(f)


if __name__ == "__main__":
    path = "D:/db/HP China"
    iterPath(path)