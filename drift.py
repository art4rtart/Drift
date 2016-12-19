# -----------------------------------------------------------------------------------
from pico2d import *
from math import *
# -----------------------------------------------------------------------------------
import framework
import start_state
import title_state
import pause_state
import init

# -----------------------------------------------------------------------------------
from road import Road1, Road2, Road3, Road4
from obstacle import Obstacle, Cone, Stick, Crashed, Stop, Tree
from item import Beer, Box, Cell, Question, Missile, Stealth, Launch, Speedup
from car import Car
from ufo import Ufo
from interface import Volume, Wasted
# -----------------------------------------------------------------------------------
name = "Drift"
# -----------------------------------------------------------------------------------
font = None
car, road = None, None
roadMoveRAD, distance = None, None
back, frame = None, None
volume, wasted, state = None, None, None
box, beer, cell, question, ufo, missile, stealth = None, None, None, None, None, None, None
beers, boxes, cells, missiles, stealthes = None, None, None, None, None
obstacle, cone, stick, crashed, tree, stop = None, None, None, None, None, None
road1, road2, road3, road4, speedup = None, None, None, None, None
launch, launches = None, None
drunk = None
font_0, font_1 = None, None


def create_world():
    global drunk
    global car, road, font_0, font_1, back, obstacle, state, frame
    global beer, cell, question, ufo, volume, wasted, launches
    global cone, stick, crashed, tree, stop
    global boxes, beers, cells, missiles, stealthes
    global speedup, road1, road2, road3, road4
    # -------------------------------------
    init.car_x, init.car_y = 237, 130  # 차량 초기화
    init.road_x, init.road_y = 280, 0  # 도로 초기화
    init.angle_0, init.angle_1 = 0, 0  # 각도 초기화
    init.PI = 3.14  # 3.14 pi
    # -------------------------------------
    init.drift_state = 0  # 드리프트 상태 초기화
    init.stageEnd = 0  # 스테이지 상태
    # -------------------------------------
    init.driftCount = 0  # 드리프트 횟수 카운트
    init.mouseCount = 0  # 클릭 횟수 카운트
    # -------------------------------------
    init.life = 1
    init.moveBack = 0
    init.carMoveStatus, init.carMoveLine = 0, 0
    init.tempT, init.tempTime = 0, 0
    init.mileage = 0
    # -------------------------------------
    init.ufoMoveX, init.ufoMoveY = 0, 0
    init.questionMark = 0
    # --------------------------------------
    init.wasted_state = 0
    init.tempRe = 0
    car.explode_frame = 0
    ufo.explode_frame = 0
    # ---------------------------------------
    init.clear_state = 0
    init.soundCount = 0
    init.cellCount, init.beerCount = 0, 0
    road1.time = 0
    init.tempT = 0
    road1.speed = 320
    init.stealth_state = 0
    init.ufoCount = 0
    init.missileCount = 0
    init.stealthCount = 0
    init.drunk_count = 0
    init.drunk_time = 0
    init.drunk_dir = 1

    beers = [Beer() for i in range(5)]
    boxes = [Box() for i in range(50)]
    cells = [Cell() for i in range(5)]
    missiles = [Missile() for i in range(5)]
    stealthes = [Stealth() for i in range(5)]
    launches = [Launch() for i in range(5)]

    init.dis = 0
    init.launch_update = 0
    init.launchX, init.launchY = 800, 0

    init.ufoDirX = 1
    init.ufoDirY = 1


def enter():
    global car, road, font_0, font_1, back, obstacle, state, frame
    global beer, cell, question, ufo, volume, wasted, launches
    global cone, stick, crashed, tree, stop
    global boxes, beers, cells, missiles, stealthes
    global speedup, road1, road2, road3, road4

    road4 = Road4()
    road1 = Road1()
    road2 = Road2()
    road3 = Road3()

    car = Car()
    speedup = Speedup()
    beers = [Beer() for i in range(5)]
    boxes = [Box() for i in range(50)]
    cells = [Cell() for i in range(5)]
    missiles = [Missile() for i in range(5)]
    stealthes = [Stealth() for i in range(5)]
    cone = Cone()
    stick = Stick()
    stop = Stop()
    crashed = Crashed()
    tree = Tree()
    ufo = Ufo()
    launches = [Launch() for i in range(5)]
    question = Question()
    volume = Volume()
    wasted = Wasted()
    obstacle = Obstacle()

    font_0 = load_font("PWChalk.TTF", 25)
    font_1 = load_font("PWChalk.TTF", 20)
    state = load_image("state.png")
    back = load_image("back.png")
    frame = load_image("frame.png")
    framework.reset_time()


def exit():
    pass


def pause():
    pass


def resume():
    pass


# -----------------------------------------------------------------------------------

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                create_world()
                framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                framework.change_state(pause_state)
                init.playgame = 0

        if init.life == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                car.drift.play()
                if init.cellCount < 5:
                    if init.mouseCount % 2 == 1:
                        init.drift_state, init.driftCount = 1, 1
                        init.roadMoveRAD = -5
                        init.angle_0 = 90

                    elif init.mouseCount % 2 == 0:
                        init.drift_state, init.driftCount = 2, 2
                        init.roadMoveRAD = 6
                        init.angle_1 = 270

            if init.drift_state == 2 or init.drift_state == 0:
                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
                        init.carMoveStatus = 1

                elif (event.type, event.key) == (SDL_KEYUP, SDLK_z):
                    init.carMoveStatus = 0

                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
                    init.carMoveStatus = 2
                elif (event.type, event.key) == (SDL_KEYUP, SDLK_x):
                    init.carMoveStatus = 0

            if (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
                init.mouseCount += 1

            # custom mode
            # if (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            #    road1.speed += 100

            # if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            #    road1.speed -= 100

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_v):
            start_state.volume -= 4

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_v):
            start_state.volume -= 4

        if init.wasted_state == 1:
            if event.type == SDL_MOUSEMOTION:
                if event.x > 310 and event.x < 495 and event.y > 228 and event.y < 271:
                    init.tempRe = 1

        if init.clear_state == 1:
            if event.type == SDL_MOUSEMOTION:
                if event.x > 310 and event.x < 495 and event.y > 228 and event.y < 271:
                    init.tempRe = 1

        if init.tempRe == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                create_world()

        if init.stealth_mode == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT):
                init.stealth_state = 1

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if init.missileCount > 0 and init.questionMark == 1:
                init.launch_update = 1
                init.missileCount = 0


def update(frame_time):
    # game function ---------------------------------
    game_function(frame_time)

    # object -----------------------------------------
    car.update(frame_time)
    ufo.update(frame_time)

    # collide ---------------------------------------
    road_collide(frame_time)
    item_collide(frame_time)
    obstacle_collide(frame_time)
    ufo_collide(frame_time)

    # interface -------------------------------------
    wasted.update(frame_time)
    volume.update(frame_time)

    start_state.bgm.set_volume(start_state.volume)

    if start_state.volume > 20:
        start_state.volume -= 1


def draw(frame_time):
    clear_canvas()

    # background ----------------------------------------
    for i in range(100):
        back.draw(400, 300 + (i * 600) - init.moveBack)

    # object --------------------------------------------
    road_draw()
    car_draw()
    item_draw()
    obstacle_draw()

    if init.beerCount == 5 and init.drunk_count < 2:
        Beer.drunk.opacify(init.drunk_time)
        Beer.drunk.draw(400, 300)


    # interface ------------------------------------------
    interface_draw()

    for launch in launches:
        launch.update(frame_time)

    update_canvas()


# -----------------------------------------------------------------------------------
def road_draw():
    road1.draw()
    road2.draw()
    road4.draw()
    road3.draw()
    speedup.draw()


def car_draw():
    car.draw()
    car.draw_bb()


def interface_draw():
    clear = load_image("clear.png")

    volume.draw()
    wasted.draw()
    state.draw(875, 300)

    if init.clear_state == 1:
        clear.draw(400, 380)

    frame.draw(500, 300)
    font_0.draw(740, 550, "SPEED", (255, 255, 255))
    font_0.draw(870, 550, "%3.0f" % (road1.speed / 5), (255, 0, 0))
    font_0.draw(920, 550, "KM/H", (255, 255, 255))
    font_0.draw(740, 500, "TIME", (255, 255, 255))
    font_0.draw(880, 500, "%3.0f" % road1.time, (255, 0, 0))
    font_0.draw(940, 500, "HR", (255, 255, 255))
    font_0.draw(740, 450, "SCORE", (255, 255, 255))
    if init.car_x > 9900 - init.road_y:
        font_0.draw(860, 450, "%3.0f" % ((road1.speed / 5 * init.tempT) + init.mileage + (init.tempTime * road1.speed)),
                    (255, 0, 0))
    else:
        font_0.draw(860, 450, "%3.0f" % init.mileage, (255, 0, 0))
    font_0.draw(940, 450, "KM", (255, 255, 255))
    font_0.draw(755, 320, "----ITEM LIST----", (255, 255, 255))
    font_1.draw(815, 235, " X %d" % init.boxCount, (0, 255, 255))
    font_1.draw(815, 155, " X %d" % init.missileCount, (0, 255, 255))
    font_1.draw(815, 80, " X %d" % init.stealthCount, (0, 255, 255))
    font_1.draw(940, 235, " X %d" % init.cellCount, (255, 170, 255))
    font_1.draw(940, 150, " X %d" % init.beerCount, (255, 170, 255))


def item_draw():
    global box, cell, beer, missile, stealth, launch

    for launch in launches:
        launch.draw()
        launch.draw_bb()

    for box in boxes:
        box.draw()
        box.draw_bb()

    for beer in beers:
        beer.draw()
        beer.draw_bb()

    for cell in cells:
        cell.draw()
        cell.draw_bb()

    for missile in missiles:
        missile.draw()
        missile.draw_bb()

    for stealth in stealthes:
        stealth.draw()
        stealth.draw_bb()

    if init.questionMark == 0:
        question.draw()
        question.draw_bb()

    if init.questionMark == 1:
        ufo.draw()
        ufo.draw_bb()


def obstacle_draw():
    global cone, stick, stop, obstacle, launch

    cone.draw()
    cone.draw_bb_1()
    cone.draw_bb_2()
    cone.draw_bb_3()
    cone.draw_bb_4()
    cone.draw_bb_5()

    stick.draw()
    stick.draw_bb_1()
    stick.draw_bb_2()
    stick.draw_bb_3()
    stick.draw_bb_4()
    stick.draw_bb_5()

    stop.draw()
    stop.draw_bb_1()
    stop.draw_bb_2()
    stop.draw_bb_3()
    stop.draw_bb_4()
    stop.draw_bb_5()

    obstacle.draw()
    obstacle.draw_bb_1()
    obstacle.draw_bb_2()
    obstacle.draw_bb_3()

    crashed.draw()
    crashed.draw_bb()

    tree.draw()

    if init.beerCount == 5:
        if init.drunk_time < 1:
            init.drunk_time += 0.02 * init.drunk_dir

        if init.drunk_time > 0.9:
            init.drunk_dir *= -1

        if init.drunk_time < 0:
            init.drunk_dir *= -1
            init.drunk_count += 1


def game_function(frame_time):
    # rotation calculate --------------------------------------------------------------
    if init.driftCount == 1:
        init.road_x += init.roadMoveRAD * cos(-init.angle_0 * (init.PI / 180))
        init.road_y += init.roadMoveRAD * sin(-init.angle_0 * (init.PI / 180))
        init.angle_0 += 10

        if init.angle_0 > 180:
            init.roadMoveRAD = 0

    if init.driftCount == 2:
        init.road_x += init.roadMoveRAD * sin(init.angle_1 * (init.PI / 180))
        init.road_y += init.roadMoveRAD * cos(init.angle_1 * (init.PI / 180))
        init.angle_1 += 10

        if init.angle_1 > 360:
            init.roadMoveRAD = 0

    if init.stageEnd == 0:
        if init.carMoveStatus == 1:
            init.road_x += 7
        if init.carMoveStatus == 2:
            init.road_x -= 7
        # init.moveBack += 3

    if init.road_y > 20300:           # 종료 조건
        init.car_y += init.distance
        init.stageEnd = 1
        init.clear_state = 1

    # mileage calculate ----------------------------------------------------------------
    if init.stageEnd == 0:
        road1.time += frame_time

        if init.car_x > 9900 - init.road_y and init.car_x < 15500 - init.road_y:
            init.tempT += frame_time

        if init.car_x > 15500 - init.road_y and init.car_x < 20300 - init.road_y:
            init.tempTime += frame_time

        init.distance = road1.speed * frame_time

        if init.driftCount == 0 or init.driftCount == 2:
            init.road_y += init.distance
        elif init.driftCount == 1:
            init.road_x -= init.distance

        if init.car_x < 9900 - init.road_y:
            init.mileage = road1.speed / 5 * road1.time

        ufo.x, ufo.y = 0, 0

    # item flicker -------------------------------------------------------------------
    if init.itemTime < 1.1:
        init.itemTime -= 0.05 * init.itemDir

    if init.itemTime < 0:
        init.itemDir *= -1

    if init.itemTime > 1:
        init.itemTime = 1
        init.itemDir *= -1

# ---------------------------------------------------------------------------------------


def road_collide(frame_time):

    if init.road_x > 300 and init.road_y < 1500 or init.road_x < 180 and init.road_y < 1390:
        init.life = 0
        init.drift_state = 3
    if init.road_x < 280 and init.road_x > 196 and init.road_y > 1500:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_x > 126 and init.road_y > 1500 and init.road_y < 2700 or init.road_x < 0 and init.road_y < 2630:
        init.life = 0
        init.drift_state = 3
    if init.road_x < 126 and init.road_x > 0 and init.road_y > 2850:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 2800 and init.road_y < 3350 and init.road_x > -30:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 2700 and init.road_y < 3600 and init.road_x < -200:
        init.life = 0
        init.drift_state = 3
    if init.road_x > -220 and init.road_x < -30 and init.road_y > 3750:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 3800 and init.road_y < 2670 and init.road_x > -260:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 3600 and init.road_y < 4400 and init.road_x < -385:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -240 and init.road_x > -385 and init.road_y > 4640:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 4530 and init.road_y < 5400 and init.road_x < -632:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 4710 and init.road_y < 5680 and init.road_x > -484:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -484 and init.road_x > -632 and init.road_y > 5640:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 5530  and init.road_y < 6080 and init.road_x < -1080:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 5600 and init.road_y < 6250  and init.road_x > -920:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -920 and init.road_x > -1080 and init.road_y > 6250:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 5600  and init.road_y < 6260 and init.road_x < -1253:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 6315 and init.road_y < 6445 and init.road_x > -1123:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -1123 and init.road_x > -1253 and init.road_y > 6445:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 5600 and init.road_y < 7138 and init.road_x < -1435:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 6500  and init.road_y < 7345 and init.road_x > -1285 :
        init.life = 0
        init.drift_state = 3
    if init.road_x < -1285 and init.road_x > -1435 and init.road_y > 7345:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 7230  and init.road_y < 7320 and init.road_x < -1605:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 7320 and init.road_y < 7510 and init.road_x > -1460:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -1460 and init.road_x > -1605 and init.road_y > 7510:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 7410   and init.road_y < 15715 and init.road_x < -2155:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 7585 and init.road_y < 15910 and init.road_x > -2000:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -2000 and init.road_x > -2155 and init.road_y > 15910:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 15815 and init.road_y < 15905 and init.road_x < -2705:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 15910 and init.road_y < 16090 and init.road_x > -2545:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -2545 and init.road_x > -2705 and init.road_y > 16090:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 16000  and init.road_y < 16090 and init.road_x < -2875:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 16090 and init.road_y < 16270 and init.road_x > -2715:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -2715 and init.road_x > -2875 and init.road_y > 16270:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 16180  and init.road_y < 17335 and init.road_x < -3240:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 16340  and init.road_y < 17540 and init.road_x > -3075:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -3075  and init.road_x > -3240 and init.road_y > 17540:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 17438  and init.road_y < 17690 and init.road_x < -3595 :  # 왼쪽
        init.life = 0
        init.drift_state = 3
    if init.road_y > 17605  and init.road_y < 17895 and init.road_x > -3445:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -3445  and init.road_x > -3595 and init.road_y > 17895:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 17790 and init.road_y < 18235 and init.road_x < -4135:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 17965 and init.road_y < 18430 and init.road_x > -3990:
        init.life = 0
        init.drift_state = 3
    if init.road_x < -3990 and init.road_x > -4135 and init.road_y > 18430:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------
    if init.road_y > 18330  and init.road_y < 20120 and init.road_x < -4320:
        init.life = 0
        init.drift_state = 3
    if init.road_y > 18515 and init.road_y < 20120 and init.road_x > -4160:
        init.life = 0
        init.drift_state = 3
    # --------------------------------------------------------------------


def item_collide(frame_time):
    global cell, beer, box, missile, stealth, launch

    if collide(car, question):
        beer.sound.play()
        init.questionMark = 1

    for box in boxes:
        if collide(car, box):
            beer.sound.play()
            boxes.remove(box)
            init.boxCount += 1

    for beer in beers:
        if collide(car, beer):
            beer.sound.play()
            beers.remove(beer)
            init.beerCount += 1

    for cell in cells:
        if collide(car, cell):
            beer.sound.play()
            cells.remove(cell)
            init.cellCount += 1

    for missile in missiles:
        if collide(car, missile):
            beer.sound.play()
            missiles.remove(missile)
            init.missileCount += 1

    for stealth in stealthes:
        if collide(car, stealth):
            beer.sound.play()
            stealthes.remove(stealth)
            init.stealthCount += 1

    if init.stealthCount == 5:
        init.stealth_mode = 1

    if init.stealth_state == 1:
        init.stealthCount = 0
        if init.tempS > 0.5:
            init.tempS -= 0.1

    for stealth in stealthes:
        stealth.update(frame_time)


def obstacle_collide(frame_time):

    if collide_1(car, cone):
        init.life = 0
        init.drift_state = 3

    if collide_2(car, cone):
        init.life = 0
        init.drift_state = 3

    if collide_3(car, cone):
        init.life = 0
        init.drift_state = 3

    if collide_4(car, cone):
        init.life = 0
        init.drift_state = 3

    if collide_5(car, cone):
        init.life = 0
        init.drift_state = 3

    if collide(car, crashed):
        init.life = 0
        init.drift_state = 3

    if collide_1(car, stick):
        init.life = 0
        init.drift_state = 3

    if collide_2(car, stick):
        init.life = 0
        init.drift_state = 3

    if collide_3(car, stick):
        init.life = 0
        init.drift_state = 3

    if collide_4(car, stick):
        init.life = 0
        init.drift_state = 3

    if collide_5(car, stick):
        init.life = 0
        init.drift_state = 3

    if collide_1(car, stop):
        init.life = 0
        init.drift_state = 3

    if collide_2(car, stop):
        init.life = 0
        init.drift_state = 3

    if collide_3(car, stop):
        init.life = 0
        init.drift_state = 3

    if collide_4(car, stop):
        init.life = 0
        init.drift_state = 3

    if collide_5(car, stop):
        init.life = 0
        init.drift_state = 3

    if collide_1(car, obstacle):
        init.life = 0
        init.drift_state = 3

    if collide_2(car, obstacle):
        init.life = 0
        init.drift_state = 3

    if collide_3(car, obstacle):
        init.life = 0
        init.drift_state = 3


def ufo_collide(frame_time):
    if collide(car, ufo):
        if init.stealth_mode == 0:
            init.life = 0
            init.drift_state = 3
            init.ufoDirX = 0
            init.ufoDirY = 0

    for launch in launches:
        if collide(ufo, launch):
            init.questionMark = 0
            init.launchX, init.launchY = -100, -100
            init.missile_crash = 1
            init.ufoDirX = 0
            init.ufoDirY = 0
            car.crashed.play()


# ---------------------------------------------------------------------------------------


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_1(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_1()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_2(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_2()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_3(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_3()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_4(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_4()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_5(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_5()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


