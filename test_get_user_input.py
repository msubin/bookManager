from unittest import TestCase
from unittest.mock import patch
import io
from books import get_user_input


class TestGetUserInput(TestCase):
    @patch('builtins.input', side_effect="hi")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_input_value_error(self, mock_output, input_str):
        with self.assertRaises(StopIteration):
            with self.assertRaises(ValueError):
                get_user_input()
                self.assertEqual("Please enter the number.\n", mock_output.getvalue())

    @patch('builtins.input', side_effect=["15"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_input_out_of_range(self, mock_output, input_int):
        with self.assertRaises(IndexError):
            get_user_input()
            self.assertEqual("Please enter 1, 2, or 3.\n", mock_output.getvalue())

    @patch('builtins.input', side_effect="1")
    def test_get_user_input_option_1(self, input_int):
        self.assertEqual("search", get_user_input())

    @patch('builtins.input', side_effect="2")
    def test_get_user_input_option_2(self, input_int):
        self.assertEqual("move", get_user_input())

    @patch('builtins.input', side_effect="3")
    def test_get_user_input_option_3(self, input_int):
        self.assertEqual("exit", get_user_input())
