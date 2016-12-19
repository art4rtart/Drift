import framework
from pico2d import *

name = "TitleState"
image = None
back = None

def enter():
    global image
    global back

    back = load_image("background_image.png")
    image = load_image("pause_image.png")

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
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()

def update(frame_time):
    pass


def draw(frame_time):
    global image
    global back
    clear_canvas()
    back.draw(500,350)
    image.draw(500, 350)
    update_canvas()



