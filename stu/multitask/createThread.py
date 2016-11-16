#!/usr/bin/python
# ecoding:utf-8

from threading import Thread


class ProducerThread(Thread):
    def __init__(self, start, end):
        Thread.__init__(self)
        self.__start = start
        self.__end = end

    def run(self):
        for top in range(self.__start, self.__end, 1):
            print self.getName() + '=>' + str(top)


if __name__ == "__main__":
    for i in range(0, 1500000000, 50000000):
        ProducerThread(i, i + 50000000).start()