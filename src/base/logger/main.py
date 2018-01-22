#!/usr/bin/python
# coding:utf-8


from src.base.logger import ThreadProcess,process
from src.conf import Logger

if __name__ == "__main__":
    log = Logger.logger(__name__)
    log.info("info")
    log.debug("debug")
    log.error("error")
    process.run()

    # 事实证明logging模块是多线程安全的
    for i in range(50):
        ThreadProcess.ThreadProcess("Thread" + str(i)).start()
