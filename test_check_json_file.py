from unittest import TestCase
import pathlib
import os
from books import check_json_file


class TestCheckJsonFile(TestCase):
    def test_check_json_file_create_file_correctly(self):
        check_json_file("somebooks.json", "somebooks.xls", "Books")
        path = pathlib.Path("somebooks.json")
        self.assertTrue(path.is_file())

    def test_check_json_file_file_located_correctly(self):
        check_json_file("somebooks.json", "somebooks.xls", "Books")
        path = pathlib.Path("somebooks.json")
        self.assertTrue(path.parent.is_dir())

    def test_check_json_file_new_file(self):
        try:
            check_json_file("test_excel.json", "test_excel.xls", "Books")
            path = pathlib.Path("test_excel.json")
            self.assertTrue(path.is_file())
            self.assertTrue(path.parent.is_dir())
        except UnicodeDecodeError:
            pass
        finally:
            if os.path.exists("test_excel.json"):
                os.remove("test_excel.json")
