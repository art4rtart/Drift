from pico2d import *
from math import *

def handle_events():
    global running
    global x, y, r
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 30
            elif event.key == SDLK_LEFT:
                x = x - 30
            elif event.key == SDLK_UP:
                y = y + 30
            elif event.key == SDLK_DOWN:
                y = y - 30
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a:
                # 반지름 값이 200 이 된다면 더이상 증가하지 않게 한다.
                if(r < 200):
                    r = r + 20
                elif(r > 200):
                    r = r + 0
            elif event.key == SDLK_d:
                # 반지름 값이 20 이 된다면 더이상 감소하지 않게 한다.
                if(r > 20):
                    r = r - 20
                elif(r < 20):
                    r = r + 0

        if event.type == SDL_MOUSEMOTION:
              x, y = event.x, 600 - event.y

open_canvas()
character = load_image('run_animation.png')

running = True
x = 400
y = 300
frame = 0
r = 100

a = 0

hide_cursor()
while (running ):
    clear_canvas()


    character.clip_draw(frame * 100, 0, 100, 100, (x + cos( a * (math.pi / 180)) * r) , y + sin( a * (math.pi / 180)) * r)

    update_canvas()

    a = a + 1 # 삼각형을 그린 후 1도 씩 증가

    frame = (frame + 1) % 8

    if(a == 360): # 360도가 되면 다시 0도 부터 시작한다.
        a = 0

    delay(0.005)
    handle_events()

close_canvas()

