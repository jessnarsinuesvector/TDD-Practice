from unittest import TestCase

from src.rules.valid_numeral_repetition_limit import ValidNumeralRepetitionLimit


class TestValidNumeralRepetitionLimit(TestCase):
    def setUp(self):
        self.limit = 3
        self.rule = ValidNumeralRepetitionLimit(self.limit)

    def test_can_validate_false_if_limit_is_violated(self):
        self.assertFalse(self.rule.is_valid("XXXX"))

    def test_can_validate_false_if_numeral_is_restricted_to_one(self):
        self.assertFalse(self.rule.is_valid("LL"))

    def test_can_validate_true_if_limit_is_not_violated(self):
        self.assertTrue(self.rule.is_valid("XXX"))
