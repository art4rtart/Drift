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
grass = None

carX, carY = 315, 130
roadX, roadY = 350, 0
distance = 0
carMoveStatus, carMoveLine = 0, 0
rightWall, leftWall = 277, 350
PI = 3.14

class Road:
    road1, road2, road3 = None, None, None

    def __init__(self):
        self.road1 = load_image('road1.png')
        self.road2 = load_image('road2.png')
        self.road3 = load_image('road3.png')
        self.time = 0.0
        self.speed = 320

    def update(self, frame_time):
        global distance, roadX, roadY, sCount
        self.time += frame_time
        distance = self.speed * frame_time
        #print("거리: %f 시간: %f" % (roadY / 20, self.time))

        if sCount == 0 or sCount == 2:
            roadY += distance

        if sCount == 1:
            roadX -= distance


    def draw(self):
        for i in range(10):
            self.road1.draw(roadX, 75 + (i * 150) - roadY)

        self.road2.draw(roadX + 1, 1550 - roadY)
        self.road3.draw(roadX + 152, 1550 - roadY)

        for i in range(10):
            self.road1.draw(roadX + 151, 1700 + (i * 150) - roadY)

drift_state = 0

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
        global drift_state

        if drift_state == 0:
            self.image.draw(carX, carY)

        elif drift_state == 1:
            self.right.clip_draw(self.right_frame * 100, 0, 100, 100, carX + r1 * cos(a * (PI / 180)), carY + r2 * sin(a * (PI/180)))
            if self.right_frame < 5:
                self.right_frame += 1
            if self.right_frame > 5:
                self.right_frame = 6
            self.direct_frame = 0

        elif drift_state == 2:
            self.direct.clip_draw(self.direct_frame * 100, 0, 100, 100, carX + r2 * sin(-b * (PI / 180)), carY + r1 * cos(-b * (PI / 180)))
            if self.direct_frame < 5:
                self.direct_frame += 1
            if self.direct_frame > 5:
                self.direct_frame = 6
            self.right_frame = 0





def enter():
    global car, road, font, grass
    road = Road()
    car = Car()
    font = load_font('ENCR10B.TTF')
    grass = load_image('grass.png')
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


sCount = 0
z = 0
mouseCount = 0

def handle_events(frame_time):
    global roadX, carMoveStatus, carMoveLine
    global roadX, roadY, r1, r2, a, PI
    global carX, carY
    global sCount
    global drift_state
    global z
    global mouseCount, b

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.change_state(pause_state)

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            carMoveStatus = 1
            carMoveLine = 1
            carX -= 10

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            carMoveStatus = 2
            carMoveLine = -1
            carX += 10

        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if(mouseCount % 2 == 1):
                drift_state = 1
                sCount = 1
                r1 = 7
                r2 = 0
                a = 90

            elif mouseCount % 2 == 0:
                drift_state = 2
                sCount = 2
                r1 = 0
                r2 = 7
                b = 270


        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            mouseCount += 1
            z = 0

r1 = 0 # 반지름
r2 = 0
a = 0 # 회전 각도
b = 0


def update(frame_time):
    global roadX, rightWall, leftWall, a, b
    global carX, carY, a, PI, r1, r2

    road.update(frame_time)
    car.update(frame_time)

    if sCount == 1:
        carX += r1 * cos(a * (PI / 180))
        carY += r1 * sin(a * (PI / 180))
        a -= 15

        if a < 0:
            r1 = 0

    if sCount == 2:
        carX += r2 * sin(-b * (PI / 180))
        carY += r2 * cos(-b * (PI / 180))
        print(b)
        b += 15

        if(b > 360):
            r2 = 0





    delay(0.05)




#칼치기--------------------------------------------------------

#---------------------------------------------------------------


def draw(frame_time):
    global road, car, grass
    clear_canvas()

    grass.draw(400,300)
    road.draw()

    car.draw()

    update_canvas()





