# coding:utf-8
from src import App


def run():
    log = App.logger(__name__)
    log.info("process is running")