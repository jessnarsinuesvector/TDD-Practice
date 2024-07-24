from pathlib import Path
from unittest import TestCase

from RomanNumerals.src.converter import Converter
from RomanNumerals.src.utils import Utils


class TestConverter(TestCase):
    def setUp(self):
        roman_numeral_map_file_path = Path.resolve(Path(__file__).parent.parent.resolve() / 'src/data'
                                                                                            '/roman_numeral_map.json')
        self.utils = Utils()
        self.converter = Converter(roman_numeral_map_file_path, self.utils)

    def test_can_convert_simple_roman_numerals(self):
        self.assertEqual(self.converter.convert("I"), 1)

    def test_can_convert_sequences_through_subtraction(self):
        self.assertEqual(self.converter.convert("IV"), 4)

    def test_can_convert_sequences_through_addition(self):
        self.assertEqual(self.converter.convert("MCMLXXXIX"), 1989)
