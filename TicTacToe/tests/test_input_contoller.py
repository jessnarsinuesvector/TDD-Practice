from unittest import TestCase

from TicTacToe.src.input_controller import InputController


class TestInputController(TestCase):
    def setUp(self):
        self.slot_state = [""] * 9
        self.input_controller = InputController(self.slot_state)

    def test_can_switch_input_successfully(self):
        self.assertEqual(self.input_controller.switch_input("X"), "O")

    def test_can_get_slot_state(self):
        self.assertEqual(self.input_controller.get_slot_state(), self.slot_state)

    def test_can_set_slot_state(self):
        for input_str, slot_num in [["X", 7], ["O",0]]:
            self.input_controller.set_slot_state(input_str, slot_num)
            actual = self.input_controller.get_slot_state()
            self.assertEqual(actual[slot_num], input_str)

    def test_can_handle_setting_wrong_slot_num(self):
        with self.assertRaises(IndexError):
            self.input_controller.set_slot_state("X", 9)

    def test_can_handle_setting_non_empty_slot(self):
        self.input_controller.set_slot_state("X", 0)
        with self.assertRaises(IOError):
            self.input_controller.set_slot_state("Y", 0)

    def test_can_clear_slot_state(self):
        self.input_controller.set_slot_state("X", 0)
        self.input_controller.clear_slot_state()
        actual = self.input_controller.get_slot_state()
        self.assertEqual(actual, [""] * 9)