#!/usr/bin/python
# coding:utf-8

import sys, os

out = open("C:/Users/Administrator/Desktop/upload.txt", "w")

with open('C:/Users/Administrator/Desktop/holly.log') as f:
    for line in f:
        if "/gdbh/upload/" in line and "file.size0" in line:
            print '.',
            out.write(line)


