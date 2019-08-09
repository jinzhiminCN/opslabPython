#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import os
import time

print("before forking my pid", os.getpid())

if os.fork():
    print("parent pid:", os.getpid())
else:
    print("child pid:", os.getpid())

time.sleep(2)
print("is over")
