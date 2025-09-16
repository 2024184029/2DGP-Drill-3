from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

g_width, g_height = grass.w, grass.h
c_width, c_height = character.w, character.h

# 잔디 표면 정중앙 (모든 운동의 시작/끝)
start_x = 400
start_y = 30 + g_height + c_height // 2

# 경계 계산 (캐릭터가 화면 밖/grass 아래로 안 나가게)
x_min = c_width // 2
y_min = start_y
y_max = 600 - c_height // 2
x_max = 800 - c_width // 2

# 사각형 최대 크기 (start_x, start_y에서 시작/끝)
rect_right = x_max
rect_left = x_min
rect_top = y_max
rect_bottom = y_min

# 삼각형 dx, dy (느낌대로, 경계 내 최대)
dx = min(200, x_max - start_x)
dy = min(150, y_max - start_y)

# 원 반지름 (시작점이 원의 아래쪽, 중심은 위쪽)
max_r = min(start_x - x_min, x_max - start_x, y_max - (start_y + c_height // 2))


def move_to_start():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(start_x, start_y)
    delay(0.01)

def move_rectangle():
    move_to_start()
    # 각 변의 길이 계산
    right_len = rect_right - start_x
    top_len = rect_top - start_y
    left_len = rect_right - rect_left
    bottom_len = rect_top - start_y
    # 각 변을 100프레임으로 이동
    steps = 100
    # 오른쪽
    for t in range(steps + 1):
        x = start_x + (rect_right - start_x) * t / steps
        y = start_y
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 위
    for t in range(steps + 1):
        x = rect_right
        y = start_y + (rect_top - start_y) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 왼쪽
    for t in range(steps + 1):
        x = rect_right - (rect_right - rect_left) * t / steps
        y = rect_top
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 아래
    for t in range(steps + 1):
        x = rect_left
        y = rect_top - (rect_top - start_y) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 시작점으로 복귀
    for t in range(steps + 1):
        x = rect_left + (start_x - rect_left) * t / steps
        y = start_y
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def move_triangle():
    move_to_start()
    # p0: 시작점(잔디 표면 중앙)
    # p1: 왼쪽 잔디 표면
    # p2: 위쪽 꼭짓점
    # p3: 오른쪽 잔디 표면
    p0 = (start_x, start_y)
    p1 = (start_x - dx, start_y)
    p2 = (start_x, start_y + dy)
    p3 = (start_x + dx, start_y)
    steps = 100
    # p0 -> p1 (왼쪽)
    for t in range(steps + 1):
        x = p0[0] + (p1[0] - p0[0]) * t / steps
        y = p0[1] + (p1[1] - p0[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # p1 -> p2 (위쪽)
    for t in range(steps + 1):
        x = p1[0] + (p2[0] - p1[0]) * t / steps
        y = p1[1] + (p2[1] - p1[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # p2 -> p3 (오른쪽)
    for t in range(steps + 1):
        x = p2[0] + (p3[0] - p2[0]) * t / steps
        y = p2[1] + (p3[1] - p2[1]) * t / steps
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # p3 -> p0 (중앙)
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
    steps = 400  # 원은 400프레임(사각형 전체와 비슷하게)
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
