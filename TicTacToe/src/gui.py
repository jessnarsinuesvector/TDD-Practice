
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


window = Tk()

window.geometry("781x569")
window.configure(bg="#FFFFFF")




global current_input
current_input = "X"
slot_state = [""] * 9
input_controller = InputController(slot_state)
result_checker = ResultChecker(input_controller)



def clicked(slot_num, btn_text_obj: StringVar):
    print("Clicked slot {}".format(slot_num))
    try:
        global current_input
        input_controller.set_slot_state(current_input, slot_num)
        btn_text_obj.set(current_input)

    except Exception as e:
        raise e
    if result_checker.has_player_won():
        messagebox.showinfo("TicTacToe!", "{} has won!".format(current_input))
        global canvas
        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=569,
            width=781,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        draw_canvas(canvas)
        input_controller.clear_slot_state()
    else:
        current_input = input_controller.switch_input(current_input)

def draw_canvas(canvas: Canvas):
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
    btn0 = Button(canvas, textvariable=btn_text0, command=lambda: clicked(0, btn_text0), height=7, width=21)
    btn0.place(x=51.0, y=20.0)

    btn_text1 = StringVar()
    btn1 = Button(canvas, textvariable=btn_text1, command=lambda: clicked(1, btn_text1), height=7, width=21)
    btn1.place(x=313, y=20)

    btn_text2 = StringVar()
    btn2 = Button(canvas, textvariable=btn_text2, command=lambda: clicked(2, btn_text2), height=7, width=21)
    btn2.place(x=576, y=20)

    btn_text3 = StringVar()
    btn3 = Button(canvas, textvariable=btn_text3, command=lambda: clicked(3, btn_text3), height=7, width=21)
    btn3.place(x=51, y=220)

    btn_text4 = StringVar()
    btn4 = Button(canvas, textvariable=btn_text4, command=lambda: clicked(4, btn_text4), height=7, width=21)
    btn4.place(x=313, y=220)

    btn_text5 = StringVar()
    btn5 = Button(canvas, textvariable=btn_text5, command=lambda: clicked(5, btn_text5), height=7, width=21)
    btn5.place(x=576, y=220)

    btn_text6 = StringVar()
    btn6 = Button(canvas, textvariable=btn_text6, command=lambda: clicked(6, btn_text6), height=7, width=21)
    btn6.place(x=51, y=420)

    btn_text7 = StringVar()
    btn7 = Button(canvas, textvariable=btn_text7, command=lambda: clicked(7, btn_text7), height=7, width=21)
    btn7.place(x=313, y=420)

    btn_text8 = StringVar()
    btn8 = Button(canvas, textvariable=btn_text8, command=lambda: clicked(8, btn_text8), height=7, width=21)
    btn8.place(x=576, y=420)

    window.resizable(False, False)

def destroy_canvas(canvas: Canvas):
    canvas.destroy()

global canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=569,
    width=781,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
draw_canvas(canvas)