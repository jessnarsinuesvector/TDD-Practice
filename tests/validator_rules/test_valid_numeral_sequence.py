from pathlib import Path
from unittest import TestCase

from src.validator_rules.valid_numeral_sequence import RuleValidNumeralSequence
from src.utils import Utils


class TestValidNumeralSequence(TestCase):
    def setUp(self):
        roman_numeral_map_file_path = Path.resolve(Path(
            __file__).parent.parent.parent.resolve() / 'src/data'
                                                       '/roman_numeral_map.json')
        self.utils = Utils()
        self.rule = RuleValidNumeralSequence(roman_numeral_map_file_path, self.utils)

    def test_can_validate_false_if_left_character_is_more_than_two_levels_lower(self):
        for i in ["IM", "XC", "XM", "IXL"]:
            print(i)
            self.assertFalse(self.rule.is_valid(i))

    def test_can_validate_false_if_sequence_is_within_restricted_sequences(self):
        for i in ["VV", "VX", "LL", "LC", "DD", "DM"]:
            self.assertFalse(self.rule.is_valid(i))

    def test_can_validate_false_if_left_character_is_one_level_lower_but_repeats_more_than_once(self):
        self.assertFalse(self.rule.is_valid("XXL"))

    def test_can_validate_true_if_sequence_is_valid(self):
        self.assertTrue(self.rule.is_valid("XL"))
        self.assertTrue(self.rule.is_valid("IX"))

    def test_can_validate_true_if_single_numeral_only(self):
        self.assertTrue(self.rule.is_valid("I"))