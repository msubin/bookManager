from unittest import TestCase
import os
import json
from books import save_json


class TestSaveJson(TestCase):
    def setUp(self):
        self.content = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "", "shelf": "1", "category": "Architecture", "subject": "Architectural History"},  {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}]

    def test_save_json_save_correctly(self):
        try:
            save_json("test_file.json", self.content)
            with open("test_file.json", "r") as file_object:
                saved_content = json.load(file_object)
                self.assertEqual(self.content, saved_content)
        finally:
            if os.path.exists("test_file.json"):
                os.remove("test_file.json")

    def test_save_json_save_empty(self):
        try:
            save_json("test_file.json", [])
            with open("test_file.json", "r") as file_object:
                saved_content = json.load(file_object)
                self.assertEqual([], saved_content)
        finally:
            if os.path.exists("test_file.json"):
                os.remove("test_file.json")