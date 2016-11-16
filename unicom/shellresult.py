#!/usr/bin/python
# coding:gbk

import sys, os, shutil


out = open("C:/Users/Administrator/Desktop/shellresut_result.txt", "w")

with open('C:/Users/Administrator/Desktop/shellresult.txt') as f:
    for line in f:
        ff = line.strip('\n')
        if ff.endswith(".V3", 3):
            out.write(ff + "\n")