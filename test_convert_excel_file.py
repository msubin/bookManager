from unittest import TestCase
from collections import OrderedDict
from books import convert_excel_file


class TestConvertExcelFile(TestCase):
    def test_convert_excel_file_convert_test_file(self):
        expected = [OrderedDict([('author', 'Whitman'), ('title', 'Canadian Small Cent Collection 1920 to DATE'), ('publisher', 'Whitman'), ('category', 'Numismatics'), ('subject', 'Canadian'), ('shelf', '1')]), OrderedDict([('author', 'Kurtz'), ('title', 'The Transcdental Temptation A Critique of Religion and the Paranormal'), ('publisher', 'Prometheus'), ('category', 'Philosophy'), ('subject', 'Religious'), ('shelf', '3')]), OrderedDict([('author', 'Liu'), ('title', 'The Wandering Earth'), ('publisher', 'Head of Zeus'), ('category', 'Fiction'), ('subject', 'SF (Chinese)'), ('shelf', 'Gaby')]), OrderedDict([('author', 'Bakewell'), ('title', 'At the existential café'), ('publisher', 'Vintage Canada'), ('category', 'Philosophy'), ('subject', 'Existentialism'), ('shelf', 'Reading')])]
        self.assertEqual(expected, convert_excel_file("test_excel.xls", "Books"))

    def test_convert_excel_file_convert_file_with_three_attributes(self):
        expected = [OrderedDict([('author', 'Whitman'), ('title', 'Canadian Small Cent Collection 1920 to DATE'), ('publisher', 'Whitman'), ('category', 'Numismatics'), ('subject', 'Canadian'), ('shelf', '1')])]
        self.assertEqual(expected, convert_excel_file("test_excel.xls", "one_dict"))

    def test_convert_excel_file_convert_empty_sheet(self):
        self.assertEqual([], convert_excel_file("test_excel.xls", "empty_list"))

    def test_convert_excel_file_invalid_format(self):
        self.assertRaises(TypeError)

    def test_convert_excel_file_int_shelf(self):
        result = convert_excel_file("test_excel.xls", "test_shelf")
        self.assertEqual("1", result[0]["shelf"])

