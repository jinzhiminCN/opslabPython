# coding:utf-8
from src.conf import Logger


def run():
    log = Logger.logger(__name__)
    log.info("process is running")