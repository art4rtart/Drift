from pico2d import *
from road import Road1
import init
import drift

road = None


class Car:
    crashed = None
    init = None

    def __init__(self):
        self.image = load_image("car.png")
        self.right = load_image("moveR.png")
        self.direct = load_image("moveD.png")
        self.explode = load_image("explode.png")
        self.right_frame, self.direct_frame, self.explode_frame = 0, 0, 0

        if Car.crashed == None:
            Car.crashed = load_wav("crash.ogg")
            Car.crashed.set_volume(50)

        if Car.init == None:
            Car.drift = load_wav("drift.wav")
            Car.drift.set_volume(50)

    def update(self, frame_time):
        if init.car_x > 400 - init.road_y:
            drift.road1.speed = 400
        if init.car_x > 2000 - init.road_y:
            drift.road1.speed = 450
        if init.car_x > 4000 - init.road_y:
            drift.road1.speed = 530
        if init.car_x > 5000 - init.road_y:
            drift.road1.speed = 700
        if init.car_x > 6000 - init.road_y:
            drift.road1.speed = 800
        if init.car_x > 7900 - init.road_y:
            drift.road1.speed = 900

        if init.car_x > 9900 - init.road_y:
            drift.road1.speed = 1400

        if init.car_x > 15500 - init.road_y:
            drift.road1.speed = 700
            init.stealth_mode = 0
            init.stealth_state = 0
            init.tempS = 1

        if init.car_x > 16450 - init.road_y:
            drift.road1.speed = 750
        if init.car_x > 17850 - init.road_y:
            drift.road1.speed = 800


    def draw(self):
        if init.drift_state == 0:
            if init.life >= 1:
                self.image.draw(init.car_x, init.car_y)
                self.image.opacify(init.tempS)

        elif init.drift_state == 1:
            self.right.clip_draw(self.right_frame * 100, 0, 100, 100, init.car_x, init.car_y)
            self.right.opacify(init.tempS)
            if self.right_frame < 5:
                self.right_frame += 1
            if self.right_frame > 5:
                self.right_frame = 6
            self.direct_frame = 0

        elif init.drift_state == 2:
            self.direct.clip_draw(self.direct_frame * 100, 0, 100, 100, init.car_x, init.car_y)
            self.direct.opacify(init.tempS)
            if self.direct_frame < 5:
                self.direct_frame += 1
            if self.direct_frame > 5:
                self.direct_frame = 6
            self.right_frame = 0

        if init.life == 0:
            self.explode.clip_draw(self.explode_frame * 100, 0, 90, 100, init.car_x, init.car_y)
            self.explode_frame += 1
            init.stageEnd = 1
            if init.soundCount < 0.5:
                Car.crashed.play()
            init.soundCount += 1

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if init.driftCount == 0 or init.driftCount == 2:
            return init.car_x - 30, init.car_y - 50, init.car_x + 30, init.car_y + 50
        if init.driftCount == 1:
            return init.car_x - 50, init.car_y - 30, init.car_x + 50, init.car_y + 30
