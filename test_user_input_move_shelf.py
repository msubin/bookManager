from unittest import TestCase
from unittest.mock import patch
import io
from books import user_input_move_shelf


class TestUserInputMoveShelf(TestCase):
    def setUp(self):
        self.data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]

    @patch('builtins.input', side_effect=["1", "am", "hi"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_move_shelf_value_error(self, mock_output, input_info):
        with self.assertRaises(StopIteration):
            with self.assertRaises(ValueError):
                user_input_move_shelf(self.data)
                self.assertEqual("Please enter the number.\n", mock_output.getvalue())

    @patch('builtins.input', side_effect=["1", "ze", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_move_shelf_index_error(self, mock_output, input_info):
        with self.assertRaises(StopIteration):
            with self.assertRaises(IndexError):
                user_input_move_shelf(self.data)
                self.assertEqual("Sorry, we don't have such books.\n", mock_output.getvalue())

    @patch('builtins.input', side_effect=["1", "am", "1", "2"])
    def test_user_input_move_shelf_move_correctly(self, input_info):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "3", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, user_input_move_shelf(self.data))

    @patch('builtins.input', side_effect=["1", "am", "1", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_move_shelf_print_correctly(self, mock_output, input_info):
        expected_output = """Which book do you want to move?\nThe result has 1 book(s).\n1. {'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}\n1. 1\n2. 3\n3. 33\n4. Gaby\n5. Students\nMichael Graves Images of a Grand Tour is now on 3 shelf.\n"""
        user_input_move_shelf(self.data)
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('builtins.input', side_effect=["2", "house", "1", "4"])
    def test_user_input_move_shelf_move_to_str_shelf(self, input_info):
        expected = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "Gaby", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.assertEqual(expected, user_input_move_shelf(self.data))