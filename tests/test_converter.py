from unittest import TestCase

from src.converter import Converter


class TestConverter(TestCase):
    def setUp(self):
        self.converter = Converter()

    def test_can_convert_simple_roman_numerals(self):
        self.assertEqual(self.converter.convert("I"), 1)

    def test_can_convert_sequences_through_subtraction(self):
        self.assertEqual(self.converter.convert("IV"), 4)

    def test_can_convert_sequences_through_addition(self):
        self.assertEqual(self.converter.convert(""))