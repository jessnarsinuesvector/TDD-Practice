from unittest import TestCase

from TicTacToe.src.input_controller import InputController
from TicTacToe.src.result_checker import ResultChecker


class TestResultChecker(TestCase):
    def setUp(self):
        slot_state = [""] * 9
        self.input_controller = InputController(slot_state)
        self.result_checker = ResultChecker(self.input_controller)

    def test_can_return_true_if_three_same_inputs_in__rows(self):
        for s in [[0,1,2], [3,4,5], [6,7,8]]:
            for i in s:
                self.input_controller.set_slot_state("X", i)
            self.assertTrue(self.result_checker.has_player_won())
            self.input_controller.clear_slot_state()

    def test_can_return_true_if_three_same_inputs_in_columns(self):
        for s in [[0,3,6], [1,4,7], [2,5,8]]:
            for i in s:
                self.input_controller.set_slot_state("X", i)
            print(self.input_controller.get_slot_state())
            self.assertTrue(self.result_checker.has_player_won())
            self.input_controller.clear_slot_state()

    def test_can_return_true_if_three_same_inputs_in_diagonal(self):
        for s in [[0,4,8], [2,4,6]]:
            for i in s:
                self.input_controller.set_slot_state("X", i)
            self.assertTrue(self.result_checker.has_player_won())
            self.input_controller.clear_slot_state()

