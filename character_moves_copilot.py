from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

g_width, g_height = grass.w, grass.h
c_width, c_height = character.w, character.h

# 이동 가능한 범위 계산
x_min = c_width // 2
x_max = 800 - c_width // 2
y_min = 30 + g_height + c_height // 2  # grass top + 캐릭터 반높이
y_max = 600 - c_height // 2

# 이동 가능한 영역의 정중앙
center_x = (x_min + x_max) // 2
center_y = (y_min + y_max) // 2

# 원/삼각형 반지름 (캐릭터가 화면 밖, grass 아래로 안 나가게)
max_r = min(center_x - x_min, x_max - center_x, center_y - y_min, y_max - center_y)


def move_rectangle():
    # 사각형의 네 변을 따라 이동 (시작점: 왼쪽 아래)
    for x in range(x_min, x_max + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y_min)
        delay(0.01)
    for y in range(y_min, y_max + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x_max, y)
        delay(0.01)
    for x in range(x_max, x_min - 1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y_max)
        delay(0.01)
    for y in range(y_max, y_min - 1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x_min, y)
        delay(0.01)

def move_triangle():
    r = max_r
    points = []
    for i in range(3):
        angle = math.radians(90 - i * 120)  # 90도에서 시작, 시계방향
        x = center_x + r * math.cos(angle)
        y = center_y + r * math.sin(angle)
        points.append((x, y))
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 3]
        for t in range(0, 101):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01)

def move_circle():
    r = max_r
    for deg in range(0, 360 + 1, 3):
        rad = math.radians(-deg)  # 시계방향
        x = center_x + r * math.cos(rad)
        y = center_y + r * math.sin(rad)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
