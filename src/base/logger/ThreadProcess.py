# coding:utf-8

import threading

from src.conf import Logger


class ThreadProcess(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
        self.log = Logger.logger(__name__)

    def run(self):
        thread_name = threading.currentThread().getName()
        info = "%s -> %d"
        for i in range(1, 10, 1):
            self.log.info(info % (thread_name, i))
