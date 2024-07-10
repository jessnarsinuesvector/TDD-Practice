import logging


class Validator:
    def __init__(self):
        self._rules = []
        self.log = logging.getLogger(__name__)

    def add_rule(self, rule):
        if rule not in self._rules:
            self._rules.append(rule)

    def get_rules(self):
        return self._rules

    def validate(self, input_str: str):
        validation_result = True
        for rule in self.get_rules():
            if not rule.is_valid(input_str):
                self.log.error("Input violation: {}".format(rule.description))
                validation_result = False
        return validation_result
