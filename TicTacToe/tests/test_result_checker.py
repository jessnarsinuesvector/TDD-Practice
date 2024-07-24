from unittest import TestCase

from TicTacToe.src.input_controller import InputController
from TicTacToe.src.result_checker import ResultChecker


class TestResultChecker(TestCase):
    def setUp(self):
        slot_state = [""] * 9
        self.input_controller = InputController(slot_state)
        self.result_checker = ResultChecker(self.input_controller)

    def test_can_return_true_if_three_same_inputs_in_rows(self):
        for s in [[0,1,2], [3,4,5], [6,7,8]]:
            for i in s:
                self.input_controller.set_slot_state("X", i)
            self.assertEqual("win", self.result_checker.has_player_won())
            self.input_controller.clear_slot_state()

    def test_can_return_true_if_three_same_inputs_in_columns(self):
        for s in [[0,3,6], [1,4,7], [2,5,8]]:
            for i in s:
                self.input_controller.set_slot_state("X", i)
            self.assertEqual(self.result_checker.has_player_won(), "win")
            self.input_controller.clear_slot_state()

    def test_can_return_true_if_three_same_inputs_in_diagonal(self):
        for s in [[0,4,8], [2,4,6]]:
            for i in s:
                self.input_controller.set_slot_state("X", i)
            self.assertEqual(self.result_checker.has_player_won(), "win")
            self.input_controller.clear_slot_state()

    def test_can_return_draw_if_slots_are_full_and_no_winners(self):
        slot_set = ["X","O","X","X","O","X","O","X","O"]
        for i in range(len(slot_set)):
            self.input_controller.set_slot_state(slot_set[i], i)
        self.assertEqual(self.result_checker.has_player_won(), "draw")