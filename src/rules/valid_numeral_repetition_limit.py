import logging
from collections import Counter

from src.rules.rule import Rule


class ValidNumeralRepetitionLimit(Rule):
    def __init__(self, limit: int):
        super()
        self.description = "Should follow Roman Numeral repetition limit."
        self.limit = limit
        self.log = logging.getLogger(__name__)
        self.restricted_to_one = [ "L" ]

    def is_valid(self, input_str: str) -> bool:
        validation_result = True
        input_str_split = list(input_str)
        counter = Counter(input_str_split)
        for numeral, count in counter.items():
            if numeral in self.restricted_to_one:
                if count > 1:
                    print(
                        "Numeral {} is repeated {} times which against the limit of 1".format(numeral, count, self.limit))
                    validation_result = False
            elif count > self.limit:
                print(
                    "Numeral {} is repeated {} times which against the limit of {}".format(numeral, count, self.limit))
                validation_result = False

        return validation_result
