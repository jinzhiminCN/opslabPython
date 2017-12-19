
# encoding:UTF-8

#
# First fork example
#

import os
import time

print("before forking my pid", os.getpid())

if os.fork():
    print("parent pid:", os.getpid())
else:
    print("child pid:", os.getpid())

time.sleep(2)
print("is over")
