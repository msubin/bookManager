from unittest import TestCase
from unittest.mock import patch
import io
from books import print_book_search


class TestPrintBookSearch(TestCase):
    def setUp(self):
        self.data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour",
                      "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Lambert", "title": "Building Seagram", "publisher": "Yale", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"},  {"author": "Gustafson", "title": "Craft Perception and Practice 2", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Mather", "title": "Cyberstorm", "publisher": "Harper Collins", "shelf": "1", "category": "Fiction", "subject": "SF"}, {"author": "Davis", "title": "History of Vancouver", "publisher": "Harbour", "shelf": "1", "category": "History", "subject": "Vancouver"}]
        self.empty_data = []
        self.one_data = [{'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_book_search_print_correctly(self, mock_output):
        print_book_search(self.data)
        expected = """The result has 6 book(s).\n1. {'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}\n2. {'author': 'Lambert', 'title': 'Building Seagram', 'publisher': 'Yale', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}\n3. {'author': 'Gustafson', 'title': 'Craft Perception and Practice 1', 'publisher': 'Ronsdale Press', 'shelf': '1', 'category': 'Art', 'subject': 'Craft'}\n4. {'author': 'Gustafson', 'title': 'Craft Perception and Practice 2', 'publisher': 'Ronsdale Press', 'shelf': '1', 'category': 'Art', 'subject': 'Craft'}\n5. {'author': 'Mather', 'title': 'Cyberstorm', 'publisher': 'Harper Collins', 'shelf': '1', 'category': 'Fiction', 'subject': 'SF'}\n6. {'author': 'Davis', 'title': 'History of Vancouver', 'publisher': 'Harbour', 'shelf': '1', 'category': 'History', 'subject': 'Vancouver'}
"""
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_book_search_print_empty_data(self, mock_output):
        print_book_search(self.empty_data)
        expected = "The result has 0 book(s).\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_book_search_print_one_data(self, mock_output):
        print_book_search(self.one_data)
        expected = "The result has 1 book(s).\n1. {'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}\n"
        self.assertEqual(expected, mock_output.getvalue())