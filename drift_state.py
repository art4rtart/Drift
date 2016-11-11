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
back = None                 #배경
obstacle = None             #장애물
state = None                #상태

# -------------------------------------
carX, carY = 245, 130       # 차량 초기화
roadX, roadY = 280, 0       # 도로 초기화
angle_0, angle_1 = 0, 0     # 각도 초기화
PI = 3.14                   # 3.14 pi
# -------------------------------------
drift_state = 0             # 드리프트 상태 초기화
stageClear = 0              # 스테이지 상태
# -------------------------------------
driftCount = 0              # 드리프트 횟수 카운트
mouseCount = 0              # 클릭 횟수 카운트
# -------------------------------------
life = 1
moveBack = 0

carMoveStatus, carMoveLine = 0, 0
rightWall, leftWall = 277, 350

class Road:
    road1, road2, road3, road4 = None, None, None, None
    speedup = None

    def __init__(self):
        self.time = 0.0                         # 시간 초기화
        self.speed = 320                        # 처음 속도 320 - 200 = 120km

        if Road.road1 == None:
            Road.road1 = load_image('road1.png')

        if Road.road2 == None:
            Road.road2 = load_image('road2.png')

        if Road.road3 == None:
            Road.road3 = load_image('road3.png')

        if Road.road4 == None:
            Road.road4 = load_image('road4.png')

        if Road.speedup == None:
            Road.speedup = load_image('speedup.png')

    def update(self, frame_time):
        global roadX, roadY, driftCount, life, distance

        if stageClear == 0:
            self.time += frame_time

        distance = self.speed * frame_time

        if driftCount == 0 or driftCount == 2:
            if stageClear == 0:
                roadY += distance
        if driftCount == 1:
            roadX -= distance

    def draw(self):
        for i in range(10):
            Road.road1.draw(roadX, 75 + (i * 150) - roadY)

        # 1번
        Road.road2.draw(roadX + 1, 1575 - roadY)
        Road.road3.draw(roadX + 181, 1575 - roadY)

        for i in range(8):
            Road.road1.draw(roadX + 181, 1755 + (i * 150) - roadY)

        # 2번
        Road.road2.draw(roadX + 182, 2901 - roadY)
        Road.road3.draw(roadX + 362, 2901 - roadY)

        for i in range(5):
            Road.road1.draw(roadX + 362, 3075 + (i * 150) - roadY)

        # 3번
        Road.road2.draw(roadX + 362, 3800 - roadY)
        Road.road3.draw(roadX + 542, 3800 - roadY)


        for i in range(5):
            Road.road1.draw(roadX + 542, 3975 + (i * 150) - roadY)

        # 4번
        Road.road2.draw(roadX + 542, 4700 - roadY)
        Road.road4.draw(roadX + 720, 4700 - roadY)
        Road.road3.draw(roadX + 800, 4700 - roadY)

        for i in range(6):
            Road.road1.draw(roadX + 800, 4875 + (i * 150) - roadY)

        # 5번
        Road.road2.draw(roadX + 800, 5700 - roadY)
        Road.road4.draw(roadX + 980, 5700 - roadY)
        Road.road4.draw(roadX + 1060, 5700 - roadY)
        Road.road3.draw(roadX + 1240, 5700 - roadY)

        for i in range(3):
            Road.road1.draw(roadX + 1240, 5875 + (i * 150) - roadY)

        # 6번
        Road.road2.draw(roadX + 1240, 6325 - roadY)
        Road.road3.draw(roadX + 1420, 6325 - roadY)
        Road.road2.draw(roadX + 1420, 6505 - roadY)
        Road.road3.draw(roadX + 1600, 6505 - roadY)

        for i in range(5):
            Road.road1.draw(roadX + 1600, 6675 + (i * 150) - roadY)

        # 7번
        Road.road2.draw(roadX + 1600, 7400 - roadY)
        Road.road3.draw(roadX + 1780, 7400 - roadY)
        Road.road2.draw(roadX + 1780, 7580 - roadY)
        Road.road4.draw(roadX + 1960, 7580 - roadY)
        Road.road4.draw(roadX + 2140, 7580 - roadY)
        Road.road3.draw(roadX + 2320, 7580 - roadY)

        for i in range(55): # feel the speed 구간
            Road.road1.draw(roadX + 2320, 7760 + (i * 150) - roadY)

        #8번
        Road.road2.draw(roadX + 2102, 15900 - roadY)
        Road.road4.draw(roadX + 2252, 15900 - roadY)
        Road.road4.draw(roadX + 2402, 15900 - roadY)
        Road.road3.draw(roadX + 2552, 15900 - roadY)
        Road.road2.draw(roadX + 2552, 16050 - roadY)
        Road.road3.draw(roadX + 2702, 16050 - roadY)
        Road.road2.draw(roadX + 2702, 16200 - roadY)
        Road.road4.draw(roadX + 2852, 16200 - roadY)
        Road.road3.draw(roadX + 3002, 16200 - roadY)

        for i in range(7):
            Road.road1.draw(roadX + 3002, 16350 + (i * 150) - roadY)

        Road.road2.draw(roadX + 3002, 17400 - roadY)
        Road.road4.draw(roadX + 3152, 17400 - roadY)
        Road.road3.draw(roadX + 3302, 17400 - roadY)
        Road.road1.draw(roadX + 3302, 17550 - roadY)


        Road.road2.draw(roadX + 3302, 17700 - roadY)

        Road.road4.draw(roadX + 3452, 17700 - roadY)
        Road.road4.draw(roadX + 3602, 17700 - roadY)
        Road.road3.draw(roadX + 3752, 17700 - roadY)

        Road.road1.draw(roadX + 3752, 17850 - roadY)
        Road.road1.draw(roadX + 3752, 18000 - roadY)
        Road.road2.draw(roadX + 3752, 18150 - roadY)
        Road.road3.draw(roadX + 3902, 18150 - roadY)

        for i in range(20):
            Road.road1.draw(roadX + 3902, 18300 + (i * 150) - roadY)

        #speedup 구간
        Road.speedup.draw(roadX, 400 - roadY)
        Road.speedup.draw(roadX + 150, 2000 - roadY)
        Road.speedup.draw(roadX + 450, 4000 - roadY)
        Road.speedup.draw(roadX + 750, 5000 - roadY)
        Road.speedup.draw(roadX + 1200, 6000 - roadY)
        Road.speedup.draw(roadX + 2100, 7900 - roadY)

        Road.speedup.draw(roadX + 2100, 9900 - roadY)

        Road.speedup.draw(roadX + 2100, 15500 - roadY) # slow down

        Road.speedup.draw(roadX + 3000, 16450 - roadY)
        Road.speedup.draw(roadX + 3750, 17850 - roadY)
        Road.speedup.draw(roadX + 3900, 18500 - roadY)

class Car:
    def __init__(self):
        self.image = load_image('car.png')
        self.right = load_image('moveR.png')
        self.direct = load_image('moveD.png')
        self.explode = load_image('explode.png')
        self.right_frame, self.direct_frame, self.explode_frame = 0, 0, 0

    def update(self, frame_time):
        pass

    def draw(self):
        global drift_state, carMoveRAD, carX, carY

        if drift_state == 0:
            if life >= 1:
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

        if life == 0:
            self.explode.clip_draw(self.explode_frame * 100, 0, 90, 100, carX, carY)
            self.explode_frame += 1
            delay(0.03)

class Obstacle:
    cone = None
    tree1, tree2 = None, None
    def __init__(self):
        if Obstacle.cone == None:
            Obstacle.cone = load_image('cone.png')

        if Obstacle.tree1 == None:
            Obstacle.tree1 = load_image('tree1.png')

        if Obstacle.tree2 == None:
            Obstacle.tree2 = load_image('tree2.png')

        self.image = load_image('crashed.png')
        self.ac1 = load_image('ac.png')
        self.ac2 = load_image('ac2.png')
        self.stick = load_image('stick.png')
        self.work = load_image('work.png')
        self.stop = load_image('stop.png')


    def update(self, frame_time):
        pass



    def draw(self):
        Obstacle.cone.draw(roadX - 35, 800 - roadY)
        Obstacle.cone.draw(roadX + 35, 1400 - roadY)
        for i in range(42):
            Obstacle.tree1.draw(roadX + 1970, 7750 + (i * 200) - roadY)
        for i in range(42):
            Obstacle.tree2.draw(roadX + 1970, 7650 + (i * 200) - roadY)

        self.image.draw(roadX + 100, 2500 - roadY)
        self.ac1.draw(roadX + 240, 3200 - roadY)
        self.ac2.draw(roadX + 360, 3500 - roadY)
        self.stick.draw(roadX + 412, 4200 - roadY)
        self.work.draw(roadX + 412, 4350 - roadY)
        self.stop.draw(roadX + 784, 5150 - roadY)
        self.stop.draw(roadX + 784, 5300 - roadY)


def enter():
    global car, road, font, back, obstacle, state
    road = Road()
    car = Car()
    obstacle = Obstacle()
    font = load_font('PWChalk.TTF', 25)
    state = load_image('state.png')
    back = load_image('back.png')
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
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_z):
            carMoveStatus = 0

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):                            # 칼치기
            carMoveStatus = 2
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_x):
            carMoveStatus = 0

        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):        # 드리프트
            if mouseCount % 2 == 1:
                drift_state, driftCount = 1, 1
                carMoveRAD = -5
                angle_0 = 90
            elif mouseCount % 2 == 0:
                drift_state, driftCount = 2, 2
                carMoveRAD = 6
                angle_1 = 270

        if (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            mouseCount += 1

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            road.speed += 100

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            road.speed -= 100

def update(frame_time):
    global roadX, roadY, rightWall, leftWall
    global carX, carY
    global angle_0, angle_1, PI, carMoveRAD
    global life
    global moveBack, stageClear

    print(7500 - roadY)

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

    if roadY > 20000:           #종료 조건
        carY += distance
        stageClear = 1



    if carMoveStatus == 1:
        roadX += 5

    if carMoveStatus == 2:
        roadX -= 5

    if stageClear == 0:
        moveBack += 3

def draw(frame_time):
    global road, car, obstacle
    global moveBack
    clear_canvas()

    for i in range(100):
        back.draw(400, 300 + (i * 600) - moveBack)

    road.draw()
    obstacle.draw()
    car.draw()

    state.draw(875, 300)

    font.draw(740, 550, "SPEED", (255, 255, 255))
    font.draw(880, 550, "%3.0f" % (road.speed / 3), (255, 0, 0))
    font.draw(930, 550, "KM/S", (255, 255, 255))

    font.draw(740, 500, "TIME", (255, 255, 255))
    font.draw(890, 500, "%3.0f" % road.time, (255, 0, 0))
    font.draw(940, 500, "SEC", (255, 255, 255))

    font.draw(740, 450, "MILEAGE", (255, 255, 255))
    if carX > 15500 - roadY:
        font.draw(880, 450, "%3.0f" % (6000 + road.speed / 3 * road.time), (255, 0, 0))
    else:
        font.draw(880, 450, "%3.0f" % (road.speed / 3 * road.time), (255, 0, 0))
    font.draw(950, 450, "KM", (255, 255, 255))

    update_canvas()





