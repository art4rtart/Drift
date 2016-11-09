import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

name = "DriftState"


font = None
car, road = None, None
grass = None

carX, carY = 315, 100
roadX, roadY = 350, 0
distance = 0
carMoveStatus, carMoveLine = 0, 0
rightWall, leftWall = 277, 350

class Road:
    road1, road2, road3 = None, None, None

    def __init__(self):
        self.road1 = load_image('road1.png')
        self.road2 = load_image('road2.png')
        self.road3 = load_image('road3.png')
        self.time = 0.0
        self.speed = 320

    def update(self, frame_time):
        global distance, roadY
        self.time += frame_time
        distance = self.speed * frame_time
        print("거리: %f 시간: %f" % (roadY / 20, self.time))

        roadY += distance

    def draw(self):
        for i in range(10):
            self.road1.draw(roadX, 75 + (i * 150) - roadY)

        self.road2.draw(roadX + 1, 1550 - roadY)
        self.road3.draw(roadX + 152, 1550 - roadY)

        for i in range(10):
            self.road1.draw(roadX + 151, 1700 + (i * 150) - roadY)


class Car:
    def __init__(self):
        self.image = load_image('car.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(carX, carY)


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


def handle_events(frame_time):
    global roadX, carMoveStatus, carMoveLine

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

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            carMoveStatus = 1
            carMoveLine = -1

def update(frame_time):
    global roadX, rightWall, leftWall

    road.update(frame_time)
    car.update(frame_time)

#칼치기--------------------------------------------------------
    if carMoveStatus == 1:
        if (roadX < rightWall):
            roadX = rightWall

        if (roadX > leftWall):
            roadX = leftWall

        roadX += carMoveLine

#---------------------------------------------------------------
    if roadY > 1430:
        leftWall = 200
        rightWall = 127

def draw(frame_time):
    global road, car, grass
    clear_canvas()

    grass.draw(400,300)
    road.draw()
    car.draw()
    update_canvas()





