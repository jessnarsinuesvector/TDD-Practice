from unittest import TestCase, mock
from unittest.mock import patch

from RomanNumerals.src.utils import Utils


class TestUtils(TestCase):

    def setUp(self):
        self.utils = Utils()

    def test_can_load_numeral_map_file(self):
        with patch('builtins.open',
                   mock.mock_open(read_data='{"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}')):
            self.assertEqual(self.utils.load_numeral_map("some_path"),
                             {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000})

    def test_can_throw_error_when_loading_invalid_numeral_map_file(self):
        self.assertRaises(BaseException, lambda: self.utils.load_numeral_map('some_non_existent_path'))
