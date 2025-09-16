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
    # 오른쪽
    for x in range(start_x, rect_right + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, start_y)
        delay(0.01)
    # 위
    for y in range(start_y, rect_top + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(rect_right, y)
        delay(0.01)
    # 왼쪽
    for x in range(rect_right, rect_left - 1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, rect_top)
        delay(0.01)
    # 아래
    for y in range(rect_top, start_y - 1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(rect_left, y)
        delay(0.01)
    # 시작점으로 복귀
    for x in range(rect_left, start_x + 1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, start_y)
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
    # p0 -> p1 (왼쪽)
    for t in range(0, 101):
        x = p0[0] + (p1[0] - p0[0]) * t / 100
        y = p0[1] + (p1[1] - p0[1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # p1 -> p2 (위쪽)
    for t in range(0, 101):
        x = p1[0] + (p2[0] - p1[0]) * t / 100
        y = p1[1] + (p2[1] - p1[1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # p2 -> p3 (오른쪽)
    for t in range(0, 101):
        x = p2[0] + (p3[0] - p2[0]) * t / 100
        y = p2[1] + (p3[1] - p2[1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # p3 -> p0 (중앙)
    for t in range(0, 101):
        x = p3[0] + (p0[0] - p3[0]) * t / 100
        y = p3[1] + (p0[1] - p3[1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def move_circle():
    move_to_start()
    # 원 중심을 start_x, start_y + 120으로, 반지름을 110으로 설정 (조금 더 큰 원)
    cx = start_x
    cy = start_y + 120
    r = 110
    # cy + r이 y_max를 넘지 않도록 보정
    if cy + r > y_max:
        r = y_max - cy
    # 시작점이 원의 아래쪽(270도), 시계방향 한 바퀴
    for deg in range(270, 270 - 360, -3):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        # 경계 체크: 화면 밖/grass 아래로 안 나가게
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
