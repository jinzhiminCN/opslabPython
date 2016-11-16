#! /usr/bin/python
# coding:utf-8


import fileinput

list1 = []

with open("count.txt") as f:
    list1 = f.readlines()

count = 0
for data in list1:
    #print data
    count += int(data)

print count
