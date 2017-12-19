# coding:utf-8

import logging

from src.conf import App


def logger(modeule_name):
    """Initialize logging module."""
    logger = logging.getLogger(modeule_name)
    formatter = logging.Formatter('%(asctime)s-(%(name)s)-[%(levelname)s] %(message)s')
    logger.setLevel(logging.DEBUG)

    # Create a file handler to store error messages
    fhdr = logging.FileHandler(App.BASE_TEMP + "./info.log", mode='w')
    fhdr.setLevel(logging.ERROR)
    fhdr.setFormatter(formatter)

    # Create a stream handler to print all messages to console
    chdr = logging.StreamHandler()
    chdr.setFormatter(formatter)

    logger.addHandler(fhdr)
    logger.addHandler(chdr)

    return logger
