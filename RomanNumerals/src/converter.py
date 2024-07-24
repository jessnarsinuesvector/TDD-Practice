from RomanNumerals.src.utils import Utils


class Converter:
    def __init__(self, map_file_path: str, utils: Utils):
        self.utils = utils
        self.numeral_map = self.utils.load_numeral_map(map_file_path)

    def convert(self, input_str: str) -> int:
        input_list = list(input_str)

        # if len(input_list) == 1:
        #     return self.numeral_map[input_list[0]]

        total = 0
        for i in range(len(input_list)):
            this_value = self.numeral_map[input_list[i]]
            if i == len(input_list) - 1:
                total += this_value
            else:
                right_value = self.numeral_map[input_list[i + 1]]
                if this_value < right_value:
                    total -= this_value
                else:
                    total += this_value

        return total
