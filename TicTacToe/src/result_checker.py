from TicTacToe.src.input_controller import InputController


class ResultChecker:
    def __init__(self, input_controller: InputController):
        self.input_controller = input_controller

    def has_player_won(self) -> bool:
        return_val = False
        if self.__is_horizontal_same() or self.__is_vertical_same() or self.__is_diagonal_same():
            return_val = True
        return return_val

    def __is_horizontal_same(self) -> bool:
        return_val = False
        slot_state = self.input_controller.get_slot_state()
        vertical_slot_diff = 1
        for i in range(0, 8, 3):
            if slot_state[i] == slot_state[i + vertical_slot_diff] and slot_state[i] == slot_state[i + vertical_slot_diff * 2]:
                return_val = True
                break

        return return_val

    def __is_vertical_same(self) -> bool:
        return_val = False
        slot_state = self.input_controller.get_slot_state()
        horizon_slot_diff = 3
        for i in range(3):
            if slot_state[i] == slot_state[i + horizon_slot_diff] and slot_state[i] == slot_state[i + horizon_slot_diff * 2]:
                return_val = True
                break

        return return_val

    def __is_diagonal_same(self) -> bool:
        return_val = False
        slot_state = self.input_controller.get_slot_state()
        for i in [0,2]:
            diag_slot_diff = 4 - i
            if slot_state[i] == slot_state[i + diag_slot_diff] and slot_state[i] == slot_state[i + diag_slot_diff * 2]:
                return_val = True
                break
        # for s in [[0,4,8], [2,4,6]]:
        #     win_requirement = slot_state[s[0]] * 3
        #     current_state = ""
        #     for i in s:
        #         current_state += slot_state[i]
        #     if win_requirement == current_state:
        #         return_val = True
        #         break

        return return_val
