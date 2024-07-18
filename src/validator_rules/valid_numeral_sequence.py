import logging

from src.validator_rules.rule import Rule
from src.utils import Utils


class RuleValidNumeralSequence(Rule):
    def __init__(self, map_file_path: str, utils: Utils):
        super()
        self.utils = utils
        self.description = "Should follow valid Roman Numeral sequence."
        self.numeral_map: dict = self.utils.load_numeral_map(map_file_path)
        self.numeral_map = dict(sorted(self.numeral_map.items(), key=lambda item: item[1], reverse=True))
        self.log = logging.getLogger(__name__)

    def is_valid(self, input_str: str) -> bool:
        input_list = list(input_str)

        # I -> True
        if len(input_str) < 2:
            return True

        # XC | XM -> False --- FFFFKKK TTHHIIIS!!!
        # HOW DO I MAKE A RULE OUT OF IT???
        for i in ["IM", "XC", "XM"]:
            if i in input_str:
                return False

        validation_result = True
        input_values = [self.numeral_map[i] for i in input_list]

        max_len = len(input_values)
        for i in range(1, max_len):
            center_val = input_values[i]
            left_val = input_values[i - 1]
            # VV -> False
            if "5" in list(str(center_val)):
                if center_val == left_val:
                    validation_result = False
                elif left_val < (center_val / 2):
                    validation_result = False
            # VX -> False
            elif "5" in list(str(left_val)):
                if center_val > left_val:
                    validation_result = False

            if i < max_len - 1:
                right_val = input_values[i + 1]
                if center_val < right_val:
                    # XXL -> False
                    if center_val >= left_val:
                        validation_result = False

        return validation_result
