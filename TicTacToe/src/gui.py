from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, messagebox

from TicTacToe.src.input_controller import InputController
from TicTacToe.src.result_checker import ResultChecker

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/TicTacToe/src/gui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class GUI:
    def __init__(self, input_controller: InputController, result_checker: ResultChecker):
        self.window = Tk()
        self.window.geometry("781x569")
        self.window.configure(bg="#FFFFFF")

        self.current_input = "X"
        self.input_controller = input_controller
        self.result_checker = result_checker

    def create_canvas(self):
        new_canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=569,
            width=781,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        return new_canvas

    def draw_elements_on_canvas(self, canvas: Canvas):
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            257.0,
            -1.0,
            258.00002487178193,
            569.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            520.0,
            -1.0,
            521.000024871782,
            569.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            0.0,
            387.0,
            784.0,
            387.00006853945683,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            -1.0,
            180.0,
            784.0,
            181.00006853945683,
            fill="#000000",
            outline="")
        # ---- BUTTONS ------
        btn_text0 = StringVar()
        btn0 = Button(canvas, textvariable=btn_text0, command=lambda: self.clicked(0, btn_text0), height=7, width=21)
        btn0.place(x=51.0, y=20.0)

        btn_text1 = StringVar()
        btn1 = Button(canvas, textvariable=btn_text1, command=lambda: self.clicked(1, btn_text1), height=7, width=21)
        btn1.place(x=313, y=20)

        btn_text2 = StringVar()
        btn2 = Button(canvas, textvariable=btn_text2, command=lambda: self.clicked(2, btn_text2), height=7, width=21)
        btn2.place(x=576, y=20)

        btn_text3 = StringVar()
        btn3 = Button(canvas, textvariable=btn_text3, command=lambda: self.clicked(3, btn_text3), height=7, width=21)
        btn3.place(x=51, y=220)

        btn_text4 = StringVar()
        btn4 = Button(canvas, textvariable=btn_text4, command=lambda: self.clicked(4, btn_text4), height=7, width=21)
        btn4.place(x=313, y=220)

        btn_text5 = StringVar()
        btn5 = Button(canvas, textvariable=btn_text5, command=lambda: self.clicked(5, btn_text5), height=7, width=21)
        btn5.place(x=576, y=220)

        btn_text6 = StringVar()
        btn6 = Button(canvas, textvariable=btn_text6, command=lambda: self.clicked(6, btn_text6), height=7, width=21)
        btn6.place(x=51, y=420)

        btn_text7 = StringVar()
        btn7 = Button(canvas, textvariable=btn_text7, command=lambda: self.clicked(7, btn_text7), height=7, width=21)
        btn7.place(x=313, y=420)

        btn_text8 = StringVar()
        btn8 = Button(canvas, textvariable=btn_text8, command=lambda: self.clicked(8, btn_text8), height=7, width=21)
        btn8.place(x=576, y=420)

        self.window.resizable(False, False)

    def destroy_canvas(self, canvas: Canvas):
        canvas.destroy()

    def clicked(self, slot_num, btn_text_obj: StringVar):
        try:
            print("Clicked slot {}: {}".format(slot_num, self.current_input))
            self.input_controller.set_slot_state(self.current_input, slot_num)
            btn_text_obj.set(self.current_input)

        except Exception as e:
            raise e
        result = self.result_checker.has_player_won()
        if result in ["draw", "win"]:
            message = result
            if result == "win":
                message = "{} has won!".format(self.current_input)
            messagebox.showinfo("TicTacToe!", message)
            canvas = self.create_canvas()
            self.draw_elements_on_canvas(canvas)
            self.input_controller.clear_slot_state()
        else:
            self.current_input = self.input_controller.switch_input(self.current_input)
