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
        self.restricted_sequences = [ "VX", "LL" ]

    def is_valid(self, input_str: str) -> bool:
        validation_result = True
        print(input_str)

        input_list = list(input_str)
        for i in range(1, len(input_list)):
            right_numeral = input_list[i]
            right_value = self.numeral_map[right_numeral]
            for j in range(i):
                left_numeral = input_list[j]
                left_value = self.numeral_map[left_numeral]
                print("{} vs {}".format(left_numeral, right_numeral))
                # check if within restricted sequences
                current_sequence = "{}{}".format(left_numeral, right_numeral)
                if current_sequence in self.restricted_sequences:
                    print("{} is not a valid roman numeral sequence".format(current_sequence))
                    validation_result = False

                # check if left < right
                elif left_value < right_value:
                    numeral_map_keys = list(self.numeral_map.keys())
                    left_numeral_map_index = numeral_map_keys.index(left_numeral)
                    right_numeral_map_index = numeral_map_keys.index(right_numeral)
                    # numerals on the right should not have numerals on the left
                    # that are more than 1 index away

                    # X[X][L]
                    allowable_numeral_index_difference = 1

                    # [X]X[L]
                    if i - j > 1:
                        allowable_numeral_index_difference = 0

                    if left_numeral_map_index - right_numeral_map_index > allowable_numeral_index_difference:
                        print("{} is not a valid roman numeral sequence".format(current_sequence))
                        validation_result = False

                # check if left[1] < right


        return validation_result

