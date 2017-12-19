
# encoding:utf-8


from unittest import TestCase

from stu.File import ZipManager

__author__ = '0opslab'


class TestZipManager(TestCase):
    def test_zip_dir(self):
        ZipManager.zip_dir("c:/tools", "c:/tools.zip")
        pass

    def test_unzip_file(self):
        pass