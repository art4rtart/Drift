import game_framework
from pico2d import *

import title_state
import pause_state
import DF_state # drift
import AT_state # autobhan
import TA_state # time attack

name = "RankingState"
image = None

def enter():
    global image
    image = load_image('scoreboard.png')

def exit():
    global image
    del(image)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global select_status
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                    game_framework.push_state(pause_state)



def update(frame_time):
    pass


def draw(frame_time):
    global image
    global back
    clear_canvas()

    image.draw(500, 300)

    update_canvas()



