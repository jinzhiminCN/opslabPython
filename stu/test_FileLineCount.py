#! /usr/bin/python
# encoding:utf-8


from unittest import TestCase
from stu.File import FileLineCount

__author__ = 'neptune'


class TestFileLineCount(TestCase):
    def test_zip_dir(self):
        print FileLineCount.countfiles("c:/tools/")
        print FileLineCount.countfilelines("c:/tools")
        pass