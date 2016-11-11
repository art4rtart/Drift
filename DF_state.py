import random
import json
import os

from pico2d import *
from math import *

import game_framework
import title_state
import pause_state

name = "DriftState"

font = None
car, road = None, None
carMoveRAD = None           # 반지름
distance = None             # 거리

# -------------------------------------
carX, carY = 315, 130       # 차량 초기화
roadX, roadY = 350, 0       # 도로 초기화
angle_0, angle_1 = 0, 0     # 각도 초기화
PI = 3.14                   # 3.14 pi
# -------------------------------------
drift_state = 0             # 드리프트 상태 초기화
# -------------------------------------
driftCount = 0                  # 드리프트 횟수 카운트
mouseCount = 0              # 클릭 횟수 카운트
# -------------------------------------

carMoveStatus, carMoveLine = 0, 0
rightWall, leftWall = 277, 350

class Road:
    road1, road2, road3, road4 = None, None, None, None

    def __init__(self):
        self.time = 0.0                         # 시간 초기화
        self.speed = 1500                        # 처음 속도 320 - 200 = 120km

        if Road.road1 == None:
            Road.road1 = load_image('road1.png')

        if Road.road2 == None:
            Road.road2 = load_image('road2.png')

        if Road.road3 == None:
            Road.road3 = load_image('road3.png')

        if Road.road4 == None:
            Road.road4 = load_image('road4.png')

    def update(self, frame_time):
        global distance, roadX, roadY, driftCount

        self.time += frame_time
        distance = self.speed * frame_time

        if driftCount == 0 or driftCount == 2:
            roadY += distance

        if driftCount == 1:
            roadX -= distance
            roadY -= 0

    def draw(self):
        for i in range(10):
            Road.road1.draw(roadX, 75 + (i * 150) - roadY)

        # 한번
        Road.road2.draw(roadX + 1, 1550 - roadY)
        Road.road3.draw(roadX + 152, 1550 - roadY)

        for i in range(8):
            Road.road1.draw(roadX + 151, 1700 + (i * 150) - roadY)

        # 두번
        Road.road2.draw(roadX + 152, 2900 - roadY)
        Road.road3.draw(roadX + 302, 2900 - roadY)


        for i in range(5):
            Road.road1.draw(roadX + 301, 3050 + (i * 150) - roadY)

        # 3번
        Road.road2.draw(roadX + 302, 3800 - roadY)
        Road.road3.draw(roadX + 452, 3800 - roadY)


        for i in range(5):
            Road.road1.draw(roadX + 451, 3950 + (i * 150) - roadY)

        # 4번
        Road.road2.draw(roadX + 452, 4700 - roadY)
        Road.road4.draw(roadX + 602, 4700 - roadY)
        Road.road3.draw(roadX + 752, 4700 - roadY)

        # roadx 증가 150 roady, 150


        for i in range(6):
            Road.road1.draw(roadX + 752, 4850 + (i * 150) - roadY)

        # 5번
        Road.road2.draw(roadX + 752, 5700 - roadY)
        Road.road4.draw(roadX + 902, 5700 - roadY)
        Road.road4.draw(roadX + 1052, 5700 - roadY)
        Road.road3.draw(roadX + 1202, 5700 - roadY)

        for i in range(3):
            Road.road1.draw(roadX + 1202, 5850 + (i * 150) - roadY)

        # 6번
        Road.road2.draw(roadX + 1202, 6300 - roadY)
        Road.road3.draw(roadX + 1352, 6300 - roadY)
        Road.road2.draw(roadX + 1352, 6450 - roadY)
        Road.road3.draw(roadX + 1502, 6450 - roadY)

        for i in range(5):
            Road.road1.draw(roadX + 1502, 6600 + (i * 150) - roadY)

        # 7번
        Road.road2.draw(roadX + 1502, 7350 - roadY)
        Road.road3.draw(roadX + 1652, 7350 - roadY)
        Road.road2.draw(roadX + 1652, 7500 - roadY)
        Road.road4.draw(roadX + 1802, 7500 - roadY)
        Road.road4.draw(roadX + 1952, 7500 - roadY)
        Road.road3.draw(roadX + 2102, 7500 - roadY)


        for i in range(55): # feel the speed 구간
            Road.road1.draw(roadX + 2102, 7650 + (i * 150) - roadY)

        #8번 the last 구간
        Road.road2.draw(roadX + 2102, 15900 - roadY)
        Road.road4.draw(roadX + 2252, 15900 - roadY)
        Road.road4.draw(roadX + 2402, 15900 - roadY)
        Road.road3.draw(roadX + 2552, 15900 - roadY)
        Road.road2.draw(roadX + 2552, 16050 - roadY)
        Road.road3.draw(roadX + 2702, 16050 - roadY)
        Road.road2.draw(roadX + 2702, 16200 - roadY)
        Road.road4.draw(roadX + 2852, 16200 - roadY)
        Road.road3.draw(roadX + 3002, 16200 - roadY)

        for i in range(20): # finish
            Road.road1.draw(roadX + 3002, 16350 + (i * 150) - roadY)




































class Car:
    def __init__(self):
        self.image = load_image('car.png')
        self.right = load_image('moveR.png')
        self.direct = load_image('moveD.png')
        self.right_frame = 0
        self.direct_frame = 0

    def update(self, frame_time):
        pass

    def draw(self):
        global drift_state, carMoveRAD, carX, carY

        if drift_state == 0:
            self.image.draw(carX, carY)

        elif drift_state == 1:
            self.right.clip_draw(self.right_frame * 100, 0, 100, 100, carX, carY)
            if self.right_frame < 5:
                self.right_frame += 1
            if self.right_frame > 5:
                self.right_frame = 6
            self.direct_frame = 0

        elif drift_state == 2:
            self.direct.clip_draw(self.direct_frame * 100, 0, 100, 100, carX, carY)
            if self.direct_frame < 5:
                self.direct_frame += 1
            if self.direct_frame > 5:
                self.direct_frame = 6
            self.right_frame = 0

def enter():
    global car, road, font
    road = Road()
    car = Car()
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()

def exit():
    global road, car, font

    del(road)
    del(car)
    del(font)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global carMoveRAD, PI, angle_0, angle_1
    global carX, carY, roadX, roadY
    global drift_state, carMoveStatus
    global mouseCount, driftCount
    global carMoveLine

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.change_state(pause_state)

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):                            # 칼치기
            carMoveStatus = 1
            carMoveLine = 1
            carX -= 10

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):                            # 칼치기
            carMoveStatus = 2
            carMoveLine = -1
            carX += 10

        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):        # 드리프트
            if mouseCount % 2 == 1:
                drift_state, driftCount = 1, 1
                carMoveRAD = -5
                angle_0 = 90

            elif mouseCount % 2 == 0:
                drift_state, driftCount = 2, 2
                carMoveRAD = 7
                angle_1 = 270

        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            mouseCount += 1

def update(frame_time):
    global roadX, roadY, rightWall, leftWall
    global carX, carY
    global angle_0, angle_1, PI, carMoveRAD

    road.update(frame_time)
    car.update(frame_time)

    if driftCount == 1:

        roadX += carMoveRAD * cos(-angle_0 * (PI / 180))
        roadY += carMoveRAD * sin(-angle_0 * (PI / 180))
        angle_0 += 10

        if angle_0 > 180:
            carMoveRAD = 0

    if driftCount == 2:


        roadX += carMoveRAD * sin(angle_1 * (PI / 180))
        roadY += carMoveRAD * cos(angle_1 * (PI / 180))
        angle_1 += 10

        if angle_1 > 360:
            carMoveRAD = 0

    print(roadY) # 18000 일때 roady stop, carY go

def draw(frame_time):
    global road, car
    clear_canvas()

    road.draw()
    car.draw()

    update_canvas()





