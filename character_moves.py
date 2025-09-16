from numpy import character
from pico2d import *

open_canvas()

boy = load_image('character.png')

def move_rectangle():
    print("Move rectangle")
    pass


def move_circle():
    print("Move circle")
    clear_canvas_now()
    boy.draw_now(400, 300)
    delay(0.1)

    pass


while True:
    move_circle()
    move_rectangle()

    # break


close_canvas()