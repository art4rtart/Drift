import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state


name = "DriftState"

boy = None
grass = None
font = None
car = None
road = None
roadY = 0
distance = 0

class Road:
    image = None

    def __init__(self):
        self.image = load_image('road.png')
        self.time = 0.0
        self.speed = 320

    def update(self, frame_time):
        global distance, roadY
        self.time += frame_time
        distance = self.speed * frame_time
        print("거리: %f 시간: %f" % (roadY / 10, self.time))

        roadY += distance

    def draw(self):
        for i in range(10):
            self.image.draw(350, 75 + (i * 150) - roadY)

class Car:
    def __init__(self):
        self.image = load_image('car.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(315, 100)


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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.change_state(pause_state)


def update(frame_time):
    road.update(frame_time)
    car.update(frame_time)



def draw(frame_time):
    global road, car
    clear_canvas()
    road.draw()
    car.draw()
    update_canvas()





