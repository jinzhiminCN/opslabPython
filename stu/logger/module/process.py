# coding:utf-8
from stu.logger.module import Logger


def run():
    log = Logger.getLog(__name__)
    log.info("process is running")