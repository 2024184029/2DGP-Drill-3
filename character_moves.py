from numpy import character
from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

# 캐릭터 사각 운동, 삼각 운동, 원운동을 무한 반복
# 점진적 개발에 따른 커밋이 이루어지면서 개발되고, 모든 기능을 만족하면 3점

def move_top():
    print('Move top')
    for x in range(770, 30 - 1, -5):
        draw_boy(x, 550)


def move_right():
    print('Move right')
    for y in range(90, 550 + 1, 5):
        draw_boy(770, y)


def move_bottom():
    print('Move bottom')
    for x in range(30, 770 + 1, 5):
        draw_boy(x, 90)


def move_left():
    print('Move left')
    for y in range(550, 90 - 1, -5):
        draw_boy(30, y)


def move_rectangle():
    print("Move rectangle")

    draw_boy(400, 80)

    for x in range(400 + 5, 770 + 1, 5):
        draw_boy(x, 80)

    move_right()

    move_top()

    move_left()

    for x in range(30, 400, 5):
        draw_boy(x, 80)


def move_circle():
    print("Move circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300

        draw_boy(x, y)

def move_triangle():
    print("Move triangle")

    draw_boy(400, 80)

    move_bottom()



def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.01)


while True:
    # move_circle()
    move_rectangle()

    break

close_canvas()