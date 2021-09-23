from unittest import TestCase
from unittest.mock import patch
import io
from books import library


class TestLibrary(TestCase):
    @patch('builtins.input', side_effect=[3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_library_exit_service(self, mock_output, input_int):
        with self.assertRaises(SystemExit) as cm:
            library()
            self.assertEqual("Thanks for your visit. Have a nice day!", mock_output.getvalue())
            self.assertEqual(cm.exception, 0)