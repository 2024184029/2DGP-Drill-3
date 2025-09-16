from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

g_width, g_height = grass.w, grass.h
c_width, c_height = character.w, character.h

GRASS_Y = 0
SURFACE_Y = GRASS_Y + g_height

start_x = 400
start_y = SURFACE_Y + 30

x_min = c_width // 2
y_min = start_y - c_height // 2
y_max = 600 - c_height // 2
x_max = 800 - c_width // 2

rect_right = x_max
rect_left = x_min
rect_top = y_max
rect_bottom = y_min

dx = min(200, x_max - start_x)
dy = min(150, y_max - start_y)

max_r = min(start_x - x_min, x_max - start_x, y_max - (start_y + c_height // 2))

def move_to_start():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(start_x, start_y)
    delay(0.01)

def move_rectangle():
    move_to_start()
    steps = 100

    for t in range(steps + 1):
        x = start_x + (rect_right - start_x) * t / steps
        y = start_y
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    for t in range(steps + 1):
        x = rect_right
        y = start_y + (rect_top - start_y) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    for t in range(2 * steps + 1):
        x = rect_right - (rect_right - rect_left) * t / (2 * steps)
        y = rect_top
        clear_canvas_now();
        grass.draw_now(400, 30);
        character.draw_now(x, y);
        delay(0.01)

    for t in range(steps + 1):
        x = rect_left
        y = rect_top - (rect_top - start_y) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    for t in range(steps + 1):
        x = rect_left + (start_x - rect_left) * t / steps
        y = start_y
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def move_triangle():
    move_to_start()
    p0 = (start_x, start_y)
    p1 = (start_x - dx, start_y)
    p2 = (start_x, start_y + dy)
    p3 = (start_x + dx, start_y)
    steps = 100

    for t in range(steps + 1):
        x = p0[0] + (p1[0] - p0[0]) * t / steps
        y = p0[1] + (p1[1] - p0[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    for t in range(steps + 1):
        x = p1[0] + (p2[0] - p1[0]) * t / steps
        y = p1[1] + (p2[1] - p1[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    for t in range(steps + 1):
        x = p2[0] + (p3[0] - p2[0]) * t / steps
        y = p2[1] + (p3[1] - p2[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    for t in range(steps + 1):
        x = p3[0] + (p0[0] - p3[0]) * t / steps
        y = p3[1] + (p0[1] - p3[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def move_circle():
    move_to_start()
    cx = start_x
    cy = start_y + 120
    r = 110
    if cy + r > y_max:
        r = y_max - cy
    steps = 400
    for i in range(steps):
        deg = 270 - (360 * i / steps)
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        x = max(x_min, min(x, x_max))
        y = max(y_min, min(y, y_max))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    move_to_start()

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
