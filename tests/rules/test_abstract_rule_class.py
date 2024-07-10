from unittest import TestCase

from src.rules.rule import Rule

class TestAbstractRuleClass(TestCase):
    def setUp(self):
        self.abstractRule = Rule("some rule", "some rule description")

    def test_can_have_properties(self):
        # may have a lot more properties
        self.assertTrue(False not in [
            self.abstractRule.description is not None
        ])

    def test_can_have_isValid_method(self):
        self.assertRaises(NotImplementedError,lambda: self.abstractRule.is_valid("something"))
