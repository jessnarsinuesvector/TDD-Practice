import logging
from collections import Counter

from src.validator_rules.rule import Rule
from src.utils import Utils


class RuleValidNumeralRepetitionLimit(Rule):
    def __init__(self, limit: int, map_file_path: str, utils: Utils):
        super()
        self.description = "Should follow Roman Numeral repetition limit."
        self.utils = utils
        self.numeral_map: dict = self.utils.load_numeral_map(map_file_path)
        self.limit = limit
        self.log = logging.getLogger(__name__)
        self.restricted_to_one = [ "V", "L", "D" ]

    def is_valid(self, input_str: str) -> bool:
        validation_result = True
        current_char = input_str[0]
        current_count = 1

        for char in input_str[1:]:
            if char == current_char:
                current_count += 1
                if current_char in self.restricted_to_one and current_count > 1:
                    validation_result = False
            else:
                current_char = char
                current_count = 1

        # Check the last sequence
        if current_count > self.limit or (current_char in self.restricted_to_one and current_count > 1):
            validation_result = False

        return validation_result
