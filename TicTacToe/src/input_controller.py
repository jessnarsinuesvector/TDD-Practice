class InputController:
    def __init__(self, slot_state: list[str]):
        self.__slot_state = slot_state
        pass

    def switch_input(self, last_input: str) -> str:
        return "X" if last_input == "O" else "O"

    def get_slot_state(self):
        return self.__slot_state

    def set_slot_state(self, input_str: str, slot_num: int):
        if self.get_slot_state()[slot_num] != "":
            raise IOError("Slot #{} is not empty!".format(slot_num))
        try:
            self.__slot_state[slot_num] = input_str
        except IndexError as e:
            raise IndexError("{} in slot #{} is not acceptable".format(input_str, slot_num))

    def clear_slot_state(self):
        slot_length = len(self.get_slot_state())
        self.__slot_state = [""] * slot_length