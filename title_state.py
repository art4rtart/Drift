import game_framework
from pico2d import *

import DF_state # drift
import AT_state # autobhan
import TA_state # time attack

name = "TitleState"
image = None
d1, d2 = None, None
a1, a2 = None, None
t1, t2 = None, None
e1, e2 = None, None
select_status = 0
game_mode = 0

def enter():
    global image, d1, d2, a1, a2, t1, t2, e1, e2
    global back

    image = load_image('select_image.png')

    d1 = load_image('drift1.png')
    d2 = load_image('drift2.png')

    a1 = load_image('a1.png')
    a2 = load_image('a2.png')

    t1 = load_image('t1.png')
    t2 = load_image('t2.png')

    e1 = load_image('e1.png')
    e2 = load_image('e2.png')

def exit():
    global image
    del(image)


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global select_status
    global game_mode

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            if event.type == SDL_MOUSEMOTION:
                if event.x > 636 and event.x < 733 and event.y > 72 and event.y < 127:
                    select_status = 1
                    game_mode = 1

                elif event.x > 636 and event.x < 844 and event.y > 162 and event.y < 218:
                    select_status = 2
                    game_mode = 2

                elif event.x > 636 and event.x < 863 and event.y > 250 and event.y < 307:
                    select_status = 3
                    game_mode = 3

                elif event.x > 640 and event.x < 709 and event.y > 347 and event.y < 403:
                    select_status = 4

                else:
                    select_status = 0

            if select_status == 1 and game_mode == 1:
                if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                    game_framework.push_state(DF_state)

            elif select_status == 2 and game_mode == 2:
                if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                    game_framework.push_state(AT_state)

            elif select_status == 3 and game_mode == 3:
                if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                    game_framework.push_state(TA_state)

            elif select_status == 4:
                if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                    game_framework.quit()

def update(frame_time):
    pass


def draw(frame_time):
    global image, select_status
    clear_canvas()

    image.draw(500, 300)

    if select_status == 0:
        d1.draw(680, 500)
        a1.draw(740, 400)
        t1.draw(746, 315)
        e1.draw(675, 215)

    elif select_status == 1:
        d2.draw(680, 500)
        a1.draw(740, 400)
        t1.draw(746, 315)
        e1.draw(675, 215)

    elif select_status == 2:
        d1.draw(680, 500)
        a2.draw(740, 400)
        t1.draw(746, 315)
        e1.draw(675, 215)

    elif select_status == 3:
        d1.draw(680, 500)
        a1.draw(740, 400)
        t2.draw(746, 315)
        e1.draw(675, 215)

    elif select_status == 4:
        d1.draw(680, 500)
        a1.draw(740, 400)
        t1.draw(746, 315)
        e2.draw(675, 215)



    update_canvas()



