import random
import json
import os

from pico2d import *

import framework
import title_state
import pause_state

name = "MainState"

image = None

def enter():
    global image
    image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\autobhan.png")

def exit():
    pass

def pause():
    pass


def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.change_state(title_state)

def update(frame_time):
    pass

def draw(frame_time):
    clear_canvas()

    image.draw(500, 300)

    update_canvas()





