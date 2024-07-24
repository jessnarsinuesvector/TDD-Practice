from TicTacToe.src.input_controller import InputController


class ResultChecker:
    def __init__(self, input_controller: InputController):
        self.input_controller = input_controller

    def has_player_won(self) -> str:
        return_val = ""
        if self.__is_horizontal_same() or self.__is_vertical_same() or self.__is_diagonal_same():
            return_val = "win"
        elif self.__is_slots_full():
            return_val = "draw"
        return return_val

    def __is_slots_full(self):
        if "" not in self.input_controller.get_slot_state():
            return True
        return False

    def __is_horizontal_same(self) -> bool:
        return_val = False
        slot_state = self.input_controller.get_slot_state()
        for i in range(0, 8, 3):
            row_chars=""
            for n in range(i + 3):
                row_chars += slot_state[n]
            if row_chars in ["XXX", "OOO"]:
                return_val = True
                break
        return return_val

    def __is_vertical_same(self) -> bool:
        return_val = False
        slot_state = self.input_controller.get_slot_state()
        horizon_slot_diff = 3
        for i in range(3):
            column_chars = ""
            for n in range(3):
                column_chars += slot_state[i + n*horizon_slot_diff]
            if column_chars in ["XXX", "OOO"]:
                return_val = True
                break

        return return_val

    def __is_diagonal_same(self) -> bool:
        return_val = False
        slot_state = self.input_controller.get_slot_state()
        for i in [0,2]:
            if slot_state[i] == "":
                break
            diag_slot_diff = 4 - i
            diagonal_chars = ""
            for n in range(3):
                diagonal_chars += slot_state[i + n*diag_slot_diff]
            if diagonal_chars in ["XXX", "OOO"]:
                return_val = True
                break
        return return_val
