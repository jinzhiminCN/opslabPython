
# coding:UTF-8

'''
	DOWNLOAD code from 
		http://www.programcreek.com/python/index/module/list
'''
import sys, os, requests, threading, time, re, logging
from threading import Thread, Condition
from bs4 import BeautifulSoup

headers = {
    'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
    'Referer': 'http://www.programcreek.com',
    'Accept-Language': 'zh-cn',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;.NET CLR 2.0.50727)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate'
}


def getLog(modeule_name):
    """Initialize logging module."""
    logger = logging.getLogger(modeule_name)
    formatter = logging.Formatter('%(asctime)s-(%(name)s)-[%(levelname)s] %(message)s')
    logger.setLevel(logging.DEBUG)

    # Create a file handler to store error messages
    fhdr = logging.FileHandler("./info.log", mode='w')
    fhdr.setLevel(logging.ERROR)
    fhdr.setFormatter(formatter)

    # Create a stream handler to print all messages to console 
    chdr = logging.StreamHandler()
    chdr.setFormatter(formatter)

    logger.addHandler(fhdr)
    logger.addHandler(chdr)

    return logger


# Handler Thread
class Handler(threading.Thread):
    def __init__(self, name, queue, log):
        threading.Thread.__init__(self, name=name)
        self.data = queue
        self.log = log

    def download(self, item):
        thread_name = threading.currentThread().getName()
        log.info('%s-%s' % (thread_name, 'starting'))
        time.sleep(10)
        log.info('%s-%s' % (thread_name, 'ending'))

    def run(self):
        thread_name = threading.currentThread().getName()

        print thread_name + " is starting..."
        while True:
            item = []
            condition.acquire()
            if not self.data:
                condition.wait()
            else:
                # 此处直接处理多线程就会卡住及同一时间只有一个线程在执行
                #self.download(self.data.pop())
                item = self.data.pop()
                condition.notify()
            condition.release()
            if item:
                self.download(item)

            time.sleep(1)


MAX_NUM = 1000
condition = Condition()

if __name__ == "__main__":
    queue = []
    for i in xrange(40):
        queue.append(['download' + str(i), 'http://www.baidu.com/list' + str(i)])
    log = getLog(__name__)
    for i in xrange(40):
        Handler("Thread" + str(i), queue, log).start()
        time.sleep(1)


