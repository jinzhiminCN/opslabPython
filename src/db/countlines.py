# coding:utf-8

from src.conf import App

count = 0
with open(App.BASE_DATA + "/db/linecount.txt") as f:
    for line in f:
        count += int(line)

print(count)
