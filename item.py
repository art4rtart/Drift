from pico2d import *
import random
import init


class Beer:
    image = None

    def __init__(self):
        if Beer.image == None:
            Beer.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\beer.png")

        self.x = random.randint(850, 850)
        self.y = random.randint(4700, 5600)

    def update(self, frame_time):
        pass

    def draw(self):
        Beer.image.draw(init.road_x + self.x, self.y - init.road_y)
        Beer.image.opacify(init.itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 25, self.y - init.road_y - 25, init.road_x + self.x + 25, self.y - init.road_y + 25


class Box:
    image = None

    def __init__(self):
        if Box.image == None:
            Box.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\box.png")
        # self.box = load_image('box.png')
        self.x = random.randint(2290, 2310)
        self.y = random.randint(11000, 15400)

    def update(self, frame_time):
        pass

    def draw(self):
        Box.image.draw(init.road_x + self.x, self.y - init.road_y)
        Box.image.opacify(init.itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 25, self.y - init.road_y - 25, init.road_x + self.x + 25, self.y - init.road_y + 25


class Cell:
    image = None

    def __init__(self):
        if Cell.image == None:
            Cell.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\cell.png")
        # self.cell = load_image('cell.png')
        self.x = random.randint(220, 220)
        self.y = random.randint(1900, 2800)

    def update(self, frame_time):
        pass

    def draw(self):
        Cell.image.draw(init.road_x + self.x, self.y - init.road_y)
        Cell.image.opacify(init.itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 25, self.y - init.road_y - 25, init.road_x + self.x + 25, self.y - init.road_y + 25


class Question:
    image = None

    def __init__(self):
        self.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\question.png")
        self.x, self.y = 2360, 9600

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(init.road_x + self.x, self.y - init.road_y)
        self.image.opacify(init.itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 30, self.y - 30 - init.road_y, init.road_x + self.x + 30, self.y + 30 - init.road_y


class Missile:
    image = None

    def __init__(self):
        if Missile.image == None:
            Missile.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\missile.png")
        self.x, self.y = random.randint(590, 590), random.randint(4000, 4600)

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(init.road_x + self.x, self.y - init.road_y)
        self.image.opacify(init.itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 30, self.y - 30 - init.road_y, init.road_x + self.x + 30, self.y + 30 - init.road_y


class Stealth:
    image = None

    def __init__(self):
        if Stealth.image == None:
            Stealth.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\stealth.png")
        self.x, self.y = random.randint(2370, 2370), random.randint(8250, 8650)

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(init.road_x + self.x, self.y - init.road_y)
        self.image.opacify(init.itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 30, self.y - 30 - init.road_y, init.road_x + self.x + 30, self.y + 30 - init.road_y


class Speedup:
    up = None
    down = None

    def __init__(self):
        if Speedup.up == None:
            Speedup.up = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\event\\up.png")

        if Speedup.down == None:
            Speedup.down = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\event\\down.png")

    def update(self, frame_time):
        pass

    def draw(self):
        #speedup 구간
        Speedup.up.draw(init.road_x, 400 - init.road_y)
        Speedup.up.draw(init.road_x + 180, 2000 - init.road_y)
        Speedup.up.draw(init.road_x + 540, 4000 - init.road_y)
        Speedup.up.draw(init.road_x + 800, 5000 - init.road_y)
        Speedup.up.draw(init.road_x + 1235, 6000 - init.road_y)
        Speedup.up.draw(init.road_x + 2320, 7900 - init.road_y)
        Speedup.up.draw(init.road_x + 2320, 9900 - init.road_y)
        Speedup.up.draw(init.road_x + 3400, 16500 - init.road_y)
        Speedup.up.draw(init.road_x + 3760, 17800 - init.road_y)

        #slowdown구간
        Speedup.down.draw(init.road_x + 2320, 15500 - init.road_y)  # slow down

class Launch():
    image = None
    
    def __init__(self):
        if Launch.image == None:
            Launch.image = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\item\\launch.png")

    def update(self, frame_time):

        if init.dis != 0:
            init.dis = (init.ufoMoveY - init.launchY) / (init.ufoMoveX - init.launchX)

        if init.launch_update == 1 and init.missileCount > 0:
            if init.dis != 0:
                print(init.launchX, init.launchY)
                if init.ufoMoveX > init.launchX:
                    init.launchX += 2
                if init.ufoMoveX < init.launchX:
                    init.launchX -= 2

                if init.ufoMoveY > init.launchY:
                    init.launchY += 2
                if init.ufoMoveY < init.launchY:
                    init.launchY -= 2

    def draw(self):
        Launch.image.draw(init.launchX, init.launchY)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40