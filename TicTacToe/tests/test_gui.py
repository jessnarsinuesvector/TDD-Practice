from tkinter import Canvas, TclError, StringVar
from unittest import TestCase
from unittest.mock import patch, Mock

from TicTacToe.src.gui import GUI
from TicTacToe.src.input_controller import InputController
from TicTacToe.src.result_checker import ResultChecker


class TestGUI(TestCase):
    def setUp(self):
        slot_state = [""] * 9
        self.input_controller = InputController(slot_state)
        self.result_checker = ResultChecker(self.input_controller)
        self.gui = GUI(self.input_controller, self.result_checker)

    def test_can_create_canvas(self):
        self.assertEqual(type(self.gui.create_canvas()), Canvas)

    def test_can_draw_elements_on_canvas(self):
        canvas = self.gui.create_canvas()
        self.gui.draw_elements_on_canvas(canvas)
        self.assertEqual(canvas.find_all(), (1,2,3,4))

    def test_can_destroy_canvas(self):
        canvas = self.gui.create_canvas()
        self.gui.draw_elements_on_canvas(canvas)
        self.gui.destroy_canvas(canvas)
        with self.assertRaises(TclError):
            canvas.find_all()

    def test_can_set_slot_state_on_click(self):
        btn_txt_var = StringVar()
        self.gui.clicked(0,btn_txt_var)
        self.assertEqual("X", self.gui.input_controller.get_slot_state()[0])

    def test_can_set_button_text_on_click(self):
        btn_txt_var = StringVar()
        self.gui.clicked(0,btn_txt_var)
        self.assertEqual("X", btn_txt_var.get())

    def test_can_switch_input_on_click_if_no_player_has_won(self):
        btn_txt_var = StringVar()
        self.gui.clicked(0,btn_txt_var)
        self.assertEqual("O", self.gui.current_input)
