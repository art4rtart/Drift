import framework
from pico2d import *

import title_state
import drift
import autobhan
import manual
import ranking_state

name = "PauseState"
image = None
r1, r2 = None, None
rk1, rk2 = None, None
q1, q2 = None, None
select_status = 0

def enter():
    global image
    global r1, r2, rk1, rk2, q1, q2

    image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\pause_image.png")

    r1 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\interface\\r1.png")
    r2 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\interface\\r2.png")

    rk1 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\interface\\rk1.png")
    rk2 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\interface\\rk2.png")

    q1 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\interface\\q1.png")
    q2 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\interface\\q2.png")


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
                game_framework.quit()

        if event.type == SDL_MOUSEMOTION:

            if event.x > 102 and event.x < 237 and event.y > 63 and event.y < 125:
                select_status = 1

            elif event.x > 103 and event.x < 221 and event.y > 165 and event.y < 221:
                select_status = 2

            elif event.x > 100 and event.x < 183 and event.y > 259 and event.y < 320:
                select_status = 3

            else:
                select_status = 0

        if select_status == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if title_state.game_mode == 1:
                    game_framework.push_state(drift_state)
                elif title_state.game_mode == 2:
                    game_framework.push_state(about_state)
                elif title_state.game_mode == 3:
                    game_framework.push_state(manual_state)

        elif select_status == 2:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                game_framework.push_state(ranking_state)

        elif select_status == 3:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                game_framework.push_state(title_state)
                drift_state.createWorld()

def update(frame_time):
    pass


def draw(frame_time):
    global image
    global back
    clear_canvas()

    image.draw(500, 300)

    if select_status == 0:
        r1.draw(170, 500)
        rk1.draw(172, 400)
        q1.draw(144, 300)

    elif select_status == 1:
        r2.draw(170, 500)
        rk1.draw(172, 400)
        q1.draw(144, 300)

    elif select_status == 2:
        r1.draw(170, 500)
        rk2.draw(172, 400)
        q1.draw(144, 300)

    elif select_status == 3:
        r1.draw(170, 500)
        rk1.draw(172, 400)
        q2.draw(144, 300)

    update_canvas()



