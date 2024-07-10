from pathlib import Path
from unittest import TestCase

from src.rules.valid_roman_numerals import RuleValidRomanNumerals


class TestRuleValidRomanNumerals(TestCase):
    def setUp(self):
        roman_numeral_map_file_path = Path.resolve(Path(__file__).parent.parent.parent.resolve() / 'src/data/roman_numeral_map.json')
        self.rule = RuleValidRomanNumerals(roman_numeral_map_file_path)

    def test_can_load_numeral_map_file(self):
        self.assertNotEqual(self.rule.numeral_map, {})

    def test_can_throw_error_when_loading_invalid_numeral_map_file(self):

        self.assertRaises(BaseException, lambda: RuleValidRomanNumerals('some path'))

    def test_can_validate_non_roman_numerals_as_false(self):
        self.assertFalse(self.rule.is_valid("A"))

    def test_can_validate_roman_numerals_as_true(self):
        self.assertTrue(self.rule.is_valid("I"))
