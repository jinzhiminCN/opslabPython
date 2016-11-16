#!/usr/bin/python
# coding:utf-8

from stu.logger.module import process
from stu.logger.module import Logger, ThreadProcess

if __name__ == "__main__":
    log = Logger.getLog(__name__)
    log.info("info")
    log.debug("debug")
    log.error("error")
    process.run()

    # 事实证明logging模块是多线程安全的
    for i in xrange(50):
        ThreadProcess.ThreadProcess("Thread" + str(i)).start()