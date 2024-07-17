from pathlib import Path
from unittest import TestCase

from src.validator_rules.valid_numeral_repetition_limit import RuleValidNumeralRepetitionLimit
from src.utils import Utils


class TestValidNumeralRepetitionLimit(TestCase):
    def setUp(self):
        self.limit = 3
        roman_numeral_map_file_path = Path.resolve(Path(__file__).parent.parent.parent.resolve() / 'src/data'
                                                                                                   '/roman_numeral_map.json')
        self.utils = Utils()
        self.rule = RuleValidNumeralRepetitionLimit(self.limit, roman_numeral_map_file_path, self.utils)

    def test_can_load_numeral_map_file(self):
        self.assertNotEqual(self.rule.numeral_map, {})

    def test_can_validate_false_if_limit_is_violated(self):
        self.assertFalse(self.rule.is_valid("XXXX"))

    def test_can_validate_false_if_numeral_is_restricted_to_one(self):
        self.assertFalse(self.rule.is_valid("LL"))

    def test_can_validate_true_if_limit_is_not_violated(self):
        self.assertTrue(self.rule.is_valid("XXX"))
