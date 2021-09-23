from unittest import TestCase
import json
import os
from books import write_json_file


class TestWriteJsonFile(TestCase):
    def setUp(self):
        self.file_name = "test_file.json"
        self.content = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "", "shelf": "1", "category": "Architecture", "subject": "Architectural History"},  {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}]

    def test_write_json_file_write_correctly(self):
        try:
            write_json_file(self.file_name, self.content)
            with open(self.file_name) as json_file:
                actual = json.load(json_file)
            self.assertEqual(self.content, actual)
        except FileNotFoundError:
            self.fail()
        finally:
            if os.path.exists("test_file.json"):
                os.remove("test_file.json")

    def test_write_json_file_write_empty_file(self):
        try:
            write_json_file(self.file_name, [])
            with open(self.file_name) as json_file:
                actual = json.load(json_file)
            self.assertEqual([], actual)
        except FileNotFoundError:
            self.fail()
        finally:
            if os.path.exists("test_file.json"):
                os.remove("test_file.json")

