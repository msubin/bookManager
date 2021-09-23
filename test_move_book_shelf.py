from unittest import TestCase
from unittest.mock import patch
import io
from books import move_book_shelf


class TestMoveBookShelf(TestCase):
    def setUp(self):
        self.data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.book = {"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_shelf_move_correctly_within_data(self, mock_output):
        actual = move_book_shelf(self.book, "33", self.data)
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "33", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual("Michael Graves Images of a Grand Tour is now on 33 shelf.\n", mock_output.getvalue())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_shelf_move_to_str_shelf(self, mock_output):
        actual = move_book_shelf(self.book, "Gaby", self.data)
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "Gaby", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual("Michael Graves Images of a Grand Tour is now on Gaby shelf.\n", mock_output.getvalue())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_shelf_move_to_str_shelf_with_title_format_of_name(self, mock_output):
        actual = move_book_shelf(self.book, "gaby", self.data)
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "Gaby", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual("Michael Graves Images of a Grand Tour is now on Gaby shelf.\n", mock_output.getvalue())
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_shelf_move_to_shelf_not_in_data(self, mock_output):
        actual = move_book_shelf(self.book, "45", self.data)
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "45", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual("Michael Graves Images of a Grand Tour is now on 45 shelf.\n", mock_output.getvalue())
        self.assertEqual(expected, actual)