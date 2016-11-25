import game_framework
from pico2d import *

import main_state

name = "TitleState"
image = None
back = None

def enter():
    global image
    global back

    back = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\background_image.png")
    image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\pause_image.png")

def exit():
    global image
    del(image)


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
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)



def update(frame_time):
    pass


def draw(frame_time):
    global image
    global back
    clear_canvas()
    back.draw(500,350)
    image.draw(500, 350)
    update_canvas()



