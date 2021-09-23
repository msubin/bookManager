from unittest import TestCase
from books import book_search


class TestBookSearch(TestCase):
    def setUp(self):
        self.data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.special_data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Asimov (ed) et al", "title": "Isaac Asimov Presents The Greatest SF Stories 13 (1951)", "publisher": "Daw", "shelf": "13", "category": "Fiction", "subject": "SF"}]

    def test_book_search_by_author_empty_result(self):
        self.assertEqual([], book_search("author", "ze", self.data))

    def test_book_search_by_author(self):
        expected = [{"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, book_search("author", "al", self.data))

    def test_book_search_by_author_with_special_char(self):
        expected = [{"author": "Asimov (ed) et al", "title": "Isaac Asimov Presents The Greatest SF Stories 13 (1951)", "publisher": "Daw", "shelf": "13", "category": "Fiction", "subject": "SF"}]
        self.assertEqual(expected, book_search("author", "(ed)", self.special_data))

    def test_book_search_by_title(self):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour",
                     "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, ]
        self.assertEqual(expected, book_search("title", "michael", self.data))

    def test_book_search_by_int_title(self):
        expected = [{"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, book_search("title", "3", self.data))

    def test_book_search_by_publisher(self):
        expected = [{"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}]
        self.assertEqual(expected, book_search("publisher", "starch", self.data))

    def test_book_search_by_empty_publisher(self):
        expected = [{"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}]
        self.assertEqual(expected, book_search("publisher", "none", self.data))

    def test_book_search_by_shelf(self):
        expected = [{"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}]
        self.assertEqual(expected, book_search("shelf", "33", self.data))

    def test_book_search_by_str_shelf(self):
        expected = [{"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}]
        self.assertEqual(expected, book_search("shelf", "gaby", self.data))

    def test_book_search_by_partial_str_shelf(self):
        expected = [{"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, book_search("shelf", "st", self.data))

    def test_book_search_by_category(self):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}]
        self.assertEqual(expected, book_search("category", "archi", self.data))

    def test_book_search_by_subject(self):
        expected = [{"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}]
        self.assertEqual(expected, book_search("subject", "sf", self.data))
