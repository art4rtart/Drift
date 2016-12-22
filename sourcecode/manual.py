import random
import os

from pico2d import *

import framework
import title_state
import pause_state

name = "MainState"

back = None
keyboard = None

def enter():
    global back, keyboard, font
    font = load_font("overWatch.TTF")
    back = load_image("manual.png")


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

    back.draw(500, 300)
    update_canvas()






