from pathlib import Path
from unittest import TestCase

from src.rules.valid_roman_numerals import RuleValidRomanNumerals
from src.utils import Utils


class TestRuleValidRomanNumerals(TestCase):
    def setUp(self):
        roman_numeral_map_file_path = Path.resolve(Path(__file__).parent.parent.parent.resolve() / 'src/data'
                                                                               '/roman_numeral_map.json')
        self.utils = Utils()
        self.rule = RuleValidRomanNumerals(roman_numeral_map_file_path, self.utils)

    def test_can_load_numeral_map_file(self):
        self.assertNotEqual(self.rule.numeral_map, {})

    def test_can_validate_false_if_input_is_non_roman_numerals(self):
        self.assertFalse(self.rule.is_valid("A"))

    def test_can_validate_true_if_input_is_roman_numerals(self):
        self.assertTrue(self.rule.is_valid("I"))
