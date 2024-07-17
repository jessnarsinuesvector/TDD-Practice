from unittest import TestCase, mock

from src.validator_rules.rule import Rule
from src.validator import Validator

class TestValidator(TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_can_add_rule(self):
        mocked_rule = mock.Mock()
        self.validator.add_rule(mocked_rule)
        self.assertTrue(mocked_rule in self.validator._rules)

    def test_can_get_rules(self):
        mocked_rule = mock.Mock()
        self.validator.add_rule(mocked_rule)
        rules = self.validator.get_rules()
        self.assertTrue(mocked_rule in rules)

    def test_can_validate_input_against_rules(self):
        class MockedRule1(Rule):
            def is_valid(self, some_input: str):
                if some_input == "I":
                    return True
                return False

        class MockedRule2(Rule):
            def is_valid(self, some_input: str):
                if some_input != "X":
                    return True
                return False

        self.validator.add_rule(MockedRule1())
        self.validator.add_rule(MockedRule2())
        self.assertTrue(self.validator.validate("I"))
        self.assertFalse(self.validator.validate("X"))