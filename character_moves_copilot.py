from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    print("Move rectangle")

    # move right (left to right)
    for x in range(50, 750 + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.05)

    # move up (bottom to top)
    for y in range(90, 550 + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, y)
        delay(0.05)

    # move left (right to left)
    for x in range(750, 50 - 1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        delay(0.05)

    # move down (top to bottom)
    for y in range(550, 90 - 1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, y)
        delay(0.05)

def move_circle():
    print("Move circle")
    # circle motion
    cx, cy = 400, 300  # center position
    r = 200  # radius

    for deg in range(0, 360 + 1, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.05)

while True:
    move_rectangle()
    move_circle()

close_canvas()
