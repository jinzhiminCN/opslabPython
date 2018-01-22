
# encoding=utf-8

# thread library
# thread library
import threading
import time

count = 0


# Thred code
def threadTest():
    global count
    for i in range(10000):
        count += 1
        if count % 1000 == 0:
            print(count)


#
for i in range(10):
    threading.Thread(target=threadTest).start()

time.sleep(3)

print(count)
