import logging
from pathlib import Path

from src.converter import Converter
from src.utils import Utils
from src.validator import Validator
from src.validator_rules.valid_numeral_repetition_limit import RuleValidNumeralRepetitionLimit
from src.validator_rules.valid_numeral_sequence import RuleValidNumeralSequence
from src.validator_rules.valid_roman_numerals import RuleValidRomanNumerals

if __name__ == "__main__":

    input_strs = [
        # "III",
        # "IX",
        # "XL",
        # "DI",
        # "MCMLXXXIX",
        # "A",
        # "IL",
        # "IM",
        # "VV",
        # "VX",
        # "LL",
        # "DD",
        # "DM"
        # "IMXL"
        "I",
        "II",
        "III",
        "IV",
        "V",
        "VI",
        "VII",
        "IX",
        "X",
        "XI",
        "XX",
        "IL",
        "L",
        "C",
        "D",
        "M",
        "MCMLXXXIX",
        "XLIX"
    ]



    # load all rules
    roman_numeral_map_file = Path(__file__).parent / 'src/data/roman_numeral_map.json'
    utils = Utils()
    rules = [
        RuleValidNumeralSequence(roman_numeral_map_file, utils),
        RuleValidRomanNumerals(roman_numeral_map_file, utils),
        RuleValidNumeralRepetitionLimit(3, roman_numeral_map_file, utils)
    ]
    validator = Validator()
    for rule in rules:
        validator.add_rule(rule)
    converter = Converter(roman_numeral_map_file, utils)

    for input_str in input_strs:
        print("{} -> {}".format(input_str, converter.convert(input_str))) if validator.validate(input_str) else None
