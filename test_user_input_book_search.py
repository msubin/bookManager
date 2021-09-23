from unittest import TestCase
from unittest.mock import patch
import io
from books import user_input_book_search


class TestUserInputBookSearch(TestCase):
    def setUp(self):
        self.data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]

    @patch('builtins.input', side_effect=["Hi", "fall"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_book_search_value_error(self, mock_output, input_info):
        with self.assertRaises(StopIteration):
            with self.assertRaises(ValueError):
                user_input_book_search(self.data)
                self.assertEqual("Please enter the number.\n", mock_output.getvalue())

    @patch('builtins.input', side_effect=["33", "fall"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_book_search_index_error(self, mock_output, input_info):
        with self.assertRaises(IndexError):
            user_input_book_search(self.data)
            self.assertEqual("Please enter the number from 1 to 6.\n", mock_output.getvalue())

    @patch('builtins.input', side_effect=["1", "ze"])
    def test_user_input_book_search_empty_result(self, input_info):
        expected = []
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["1", "al"])
    def test_user_input_book_search_search_author(self, input_info):
        expected = [{"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["2", "michael"])
    def test_user_input_book_search_search_title(self, input_info):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"},]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["3", "starch"])
    def test_user_input_book_search_search_publisher(self, input_info):
        expected = [{"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["3", "none"])
    def test_user_input_book_search_search_none_publisher(self, input_info):
        expected = [{"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["4", "33"])
    def test_user_input_book_search_search_shelf(self, input_info):
        expected = [{"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["4", "gaby"])
    def test_user_input_book_search_search_str_shelf(self, input_info):
        expected = [{"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["5", "archi"])
    def test_user_input_book_search_search_category(self, input_info):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}]
        self.assertEqual(expected, user_input_book_search(self.data))

    @patch('builtins.input', side_effect=["6", "sf"])
    def test_user_input_book_search_search_subject(self, input_info):
        expected = [{"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"},
             {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}]
        self.assertEqual(expected, user_input_book_search(self.data))