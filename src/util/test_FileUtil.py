from unittest import TestCase


from src.util import FileUtil


class TestZip_dir(TestCase):
    def test_zip_dir(self):
        FileUtil.zip_dir("c:/tools", "c:/tools.zip")
        pass

    def test_unzip_file(self):
        pass