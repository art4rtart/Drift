import framework
from pico2d import *

import press_any_key

name = "StartState"
image = None
kpu, game, bgm = None, None, None
status = 0
volume = 64

logo_time = 0.0

def enter():
    global kpu, game, bgm
    open_canvas(1000, 600, sync=True)
    kpu = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\kpu_credit.png")
    game = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\game_credit.png")
    bgm = load_music("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\sound\\loveU.ogg")


def exit():
    global image
    del(image)


def update(frame_time):
    global name, status
    global logo_time

    if (logo_time > 0.1):
        status = 1

    if (logo_time > 0.2):
        logo_time = 0
        framework.push_state(press_any_key)

    logo_time += frame_time


def draw(frame_time):
    global image
    global status

    clear_canvas()

    if status == 0:
        kpu.draw(500, 300)
        bgm.set_volume(volume)
        bgm.repeat_play()
    else:
        game.draw(500, 300)

    update_canvas()


def handle_events(frame_time):
    events = get_events()


def pause(): pass


def resume(): pass




