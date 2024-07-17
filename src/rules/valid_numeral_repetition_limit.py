import logging
from collections import Counter

from src.rules.rule import Rule
from src.utils import Utils


class RuleValidNumeralRepetitionLimit(Rule):
    def __init__(self, limit: int, map_file_path: str, utils: Utils):
        super()
        self.description = "Should follow Roman Numeral repetition limit."
        self.utils = utils
        self.numeral_map: dict = self.utils.load_numeral_map(map_file_path)
        self.limit = limit
        self.log = logging.getLogger(__name__)

    def is_valid(self, input_str: str) -> bool:
        validation_result = True
        input_str_split = list(input_str)
        counter = Counter(input_str_split)
        for numeral, count in counter.items():
            if self.numeral_map[numeral] % 5 == 0:
                if count > 1:
                    print(
                        "Numeral {} is repeated {} times which against the limit of 1".format(numeral, count, self.limit))
                    validation_result = False
            elif count > self.limit:
                print(
                    "Numeral {} is repeated {} times which against the limit of {}".format(numeral, count, self.limit))
                validation_result = False

        return validation_result
