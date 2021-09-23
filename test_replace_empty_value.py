from unittest import TestCase
from books import replace_empty_value


class TestReplaceEmptyValue(TestCase):
    def setUp(self):
        self.data_no_empty = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Lambert", "title": "Building Seagram", "publisher": "Yale", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Gustafson", "title": "Craft Perception and Practice 2", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Mather", "title": "Cyberstorm", "publisher": "Harper Collins", "shelf": "1", "category": "Fiction", "subject": "SF"}, {"author": "Davis", "title": "History of Vancouver", "publisher": "Harbour", "shelf": "1", "category": "History", "subject": "Vancouver"}]
        self.data_some_empty = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.empty_list = []

    def test_replace_empty_value_no_empty_list(self):
        self.assertEqual(self.data_no_empty, replace_empty_value(self.data_no_empty))

    def test_replace_empty_value_replace_correctly(self):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "None", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "None", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, replace_empty_value(self.data_some_empty))

    def test_replace_empty_value_empty_list(self):
        self.assertEqual([], replace_empty_value(self.empty_list))
