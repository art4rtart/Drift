from pico2d import *
import random
import init


class Ufo:
    image = None

    def __init__(self):
        if Ufo.image == None:
            Ufo.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\event\\ufo.png")

        self.x, self.y = 500, 500
        self.ufoRand = random.randint(1, 4)
        self.explode = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\event\\explode.png")
        self.explode_frame = 0

    def update(self, frame_time):
        if init.questionMark == 1:
            if self.ufoRand == 1:
                init.ufoMoveX -= 5 * init.ufoDirX
                init.ufoMoveY -= 5 * init.ufoDirY
            if self.ufoRand == 2:
                init.ufoMoveX += 5 * init.ufoDirX
                init.ufoMoveY += 5 * init.ufoDirY
            if self.ufoRand == 3:
                init.ufoMoveX -= 5 * init.ufoDirX
                init.ufoMoveY += 5 * init.ufoDirY
            if self.ufoRand == 4:
                init.ufoMoveX += 5 * init.ufoDirX
                init.ufoMoveY -= 5 * init.ufoDirY

            if self.x + init.ufoMoveX > 700 or self.x + init.ufoMoveX < 0:
                init.ufoDirX *= -1

            if self.y + init.ufoMoveY > 600 or self.y + init.ufoMoveY < 0:
                init.ufoDirY *= -1

    def draw(self):
        if init.missile_crash != 1:
            Ufo.image.draw(self.x + init.ufoMoveX, self.y + init.ufoMoveY)

        elif init.missile_crash == 1:
            delay(0.01)
            self.explode.clip_draw(self.explode_frame * 100, 0, 90, 100, self.x + init.ufoMoveX, self.y + init.ufoMoveY)
            self.explode_frame += 1
            if self.explode_frame < 16:
                init.ufoCount += 1
                if init.ufoCount > 3:
                    init.questionMark = 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x + init.ufoMoveX - 40, self.y + init.ufoMoveY - 40, self.x + init.ufoMoveX + 40, self.y + init.ufoMoveY + 40