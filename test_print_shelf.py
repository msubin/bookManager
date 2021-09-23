from unittest import TestCase
from unittest.mock import patch
import io
from books import print_shelf


class TestPrintShelf(TestCase):
    def setUp(self):
        self.data_one_shelf = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Lambert", "title": "Building Seagram", "publisher": "Yale", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Gustafson", "title": "Craft Perception and Practice 2", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Mather", "title": "Cyberstorm", "publisher": "Harper Collins", "shelf": "1", "category": "Fiction", "subject": "SF"}, {"author": "Davis", "title": "History of Vancouver", "publisher": "Harbour", "shelf": "1", "category": "History", "subject": "Vancouver"}]
        self.data_multiple_shelf = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
        self.empty_data = []

    def test_print_shelf_return_correctly_multiple_shelves(self):
        expected = ['1', '3', '33', 'Gaby', 'Students']
        self.assertEqual(expected, print_shelf(self.data_multiple_shelf))

    def test_print_shelf_return_correctly_one_shelf(self):
        expected = ['1']
        self.assertEqual(expected, print_shelf(self.data_one_shelf))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shelf_print_correctly(self, mock_output):
        print_shelf(self.data_multiple_shelf)
        expected = "1. 1\n2. 3\n3. 33\n4. Gaby\n5. Students\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shelf_print_one_shelf_correctly(self, mock_output):
        print_shelf(self.data_one_shelf)
        expected = "1. 1\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shelf_with_empty_data(self, mock_output):
        print_shelf(self.empty_data)
        expected = ""
        self.assertEqual(expected, mock_output.getvalue())