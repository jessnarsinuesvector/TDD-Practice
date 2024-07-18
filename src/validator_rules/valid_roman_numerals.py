import json
import logging

from src.validator_rules.rule import Rule
from src.utils import Utils


class RuleValidRomanNumerals(Rule):

    def __init__(self, map_file_path: str, utils: Utils):
        super()
        self.utils = utils
        self.description = "Should only contain valid Roman Numerals."
        self.numeral_map: dict = self.utils.load_numeral_map(map_file_path)
        self.log = logging.getLogger(__name__)

    def is_valid(self, input_str: str):
        validation_result = True
        for i in input_str:
            if i not in self.numeral_map.keys():
                validation_result = False

        return validation_result
