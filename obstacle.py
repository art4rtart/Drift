from pico2d import *
import init


class Obstacle:
    def __init__(self):
        self.ac1 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\ac1.png")
        self.ac2 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\ac2.png")
        self.work = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\work.png")
        self.x1, self.y1 = 270, 3200
        self.x2, self.y2 = 430, 3500
        self.x3, self.y3 = 500, 4320

    def update(self, frame_time):
        pass

    def draw(self):
        self.ac1.draw(init.road_x + self.x1, self.y1 - init.road_y)
        self.ac2.draw(init.road_x + self.x2, self.y2 - init.road_y)
        self.work.draw(init.road_x + self.x3, self.y3 - init.road_y)

    def get_bb_1(self):
        return init.road_x + self.x1 - 40, self.y1 - init.road_y - 40, init.road_x + self.x1 + 40, self.y1 - init.road_y + 40

    def get_bb_2(self):
        return init.road_x + self.x2 - 40, self.y2 - init.road_y - 40, init.road_x + self.x2 + 40, self.y2 - init.road_y + 40

    def get_bb_3(self):
        return init.road_x + self.x3 - 40, self.y3 - init.road_y - 60, init.road_x + self.x3 + 40, self.y3 - init.road_y + 60

    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())


class Cone:
    cone = None

    def __init__(self):
        if Cone.cone == None:
            Cone.cone = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\cone.png")
        self.x1, self.y1 = -40, 800
        self.x2, self.y2 = 40, 1400
        self.x3, self.y3 = 1190, 6200
        self.x4, self.y4 = 1560, 7140
        self.x5, self.y5 = 4520, 7290
        self.x6, self.y6 = 2270, 8200

    def update(self, frame_time):
        pass

    def draw(self):
        Cone.cone.draw(init.road_x + self.x1, self.y1 - init.road_y)
        Cone.cone.draw(init.road_x + self.x2, self.y2 - init.road_y)
        Cone.cone.draw(init.road_x + self.x3, self.y3 - init.road_y)
        Cone.cone.draw(init.road_x + self.x4, self.y4 - init.road_y)
        Cone.cone.draw(init.road_x + self.x5, self.y5 - init.road_y)

    def get_bb_1(self):
        return init.road_x + self.x1 - 25, self.y1 - init.road_y - 40, init.road_x + self.x1 + 25, self.y1 - init.road_y + 40

    def get_bb_2(self):
        return init.road_x + self.x2 - 25, self.y2 - init.road_y - 40, init.road_x + self.x2 + 25, self.y2 - init.road_y + 40

    def get_bb_3(self):
        return init.road_x + self.x3 - 25, self.y3 - init.road_y - 40, init.road_x + self.x3 + 25, self.y3 - init.road_y + 40

    def get_bb_4(self):
        return init.road_x + self.x4 - 25, self.y4 - init.road_y - 40, init.road_x + self.x4 + 25, self.y4 - init.road_y + 40

    def get_bb_5(self):
        return init.road_x + self.x5 - 25, self.y5 - init.road_y - 40, init.road_x + self.x5 + 25, self.y5 - init.road_y + 40


    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())

    def draw_bb_4(self):
        draw_rectangle(*self.get_bb_4())

    def draw_bb_5(self):
        draw_rectangle(*self.get_bb_5())


class Stick:
    stick = None

    def __init__(self):
        if Stick.stick == None:
            Stick.stick = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\stick.png")
        self.x1, self.y1 = 3440, 16900
        self.x2, self.y2 = 3360, 17320
        self.x3, self.y3 = 3970, 18050
        self.x4, self.y4 = 4440, 18800
        self.x5, self.y5 = 4520, 19270

    def update(self, frame_time):
        pass

    def draw(self):
        Stick.stick.draw(init.road_x + self.x1, self.y1 - init.road_y)
        Stick.stick.draw(init.road_x + self.x2, self.y2 - init.road_y)
        Stick.stick.draw(init.road_x + self.x3, self.y3 - init.road_y)
        Stick.stick.draw(init.road_x + self.x4, self.y4 - init.road_y)
        Stick.stick.draw(init.road_x + self.x5, self.y5 - init.road_y)

    def get_bb_1(self):
        return init.road_x + self.x1 - 35, self.y1 - init.road_y - 40, init.road_x + self.x1 + 35, self.y1 - init.road_y + 40

    def get_bb_2(self):
        return init.road_x + self.x2 - 35, self.y2 - init.road_y - 40, init.road_x + self.x2 + 35, self.y2 - init.road_y + 40

    def get_bb_3(self):
        return init.road_x + self.x3 - 35, self.y3 - init.road_y - 40, init.road_x + self.x3 + 35, self.y3 - init.road_y + 40

    def get_bb_4(self):
        return init.road_x + self.x4 - 35, self.y4 - init.road_y - 40, init.road_x + self.x4 + 35, self.y4 - init.road_y + 40

    def get_bb_5(self):
        return init.road_x + self.x5 - 35, self.y5 - init.road_y - 40, init.road_x + self.x5 + 35, self.y5 - init.road_y + 40

    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())

    def draw_bb_4(self):
        draw_rectangle(*self.get_bb_4())

    def draw_bb_5(self):
        draw_rectangle(*self.get_bb_5())


class Crashed:
    crashed = None
    def __init__(self):
        if Crashed.crashed == None:
            Crashed.crashed = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\crashed.png")
        self.x, self.y = 100, 2500

    def update(self, frame_time):
        pass

    def draw(self):
        Crashed.crashed.draw(init.road_x + self.x, self.y - init.road_y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return init.road_x + self.x - 40, self.y - init.road_y - 40, init.road_x + self.x + 40, self.y - init.road_y + 40


class Stop:
    stop = None
    def __init__(self):
        if Stop.stop == None:
            Stop.stop = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\stop.png")
        self.x1, self.y1 = 2280, 8600
        self.x2, self.y2 = 2360, 9200
        self.x3, self.y3 = 2280, 9800
        self.x4, self.y4 = 758, 5150
        self.x5, self.y5 = 758, 5300

    def update(self, frame_time):
        pass

    def draw(self):
        Stop.stop.draw(init.road_x + self.x1, self.y1 - init.road_y)
        Stop.stop.draw(init.road_x + self.x2, self.y2 - init.road_y)
        Stop.stop.draw(init.road_x + self.x3, self.y3 - init.road_y)
        Stop.stop.draw(init.road_x + self.x4, self.y4 - init.road_y)
        Stop.stop.draw(init.road_x + self.x5, self.y5 - init.road_y)

    def get_bb_1(self):
        return init.road_x + self.x1 - 35, self.y1 - init.road_y - 30, init.road_x + self.x1 + 35, self.y1 - init.road_y + 30

    def get_bb_2(self):
        return init.road_x + self.x2 - 35, self.y2 - init.road_y - 30, init.road_x + self.x2 + 35, self.y2 - init.road_y + 30

    def get_bb_3(self):
        return init.road_x + self.x3 - 35, self.y3 - init.road_y - 30, init.road_x + self.x3 + 35, self.y3 - init.road_y + 30

    def get_bb_4(self):
        return init.road_x + self.x4 - 35, self.y4 - init.road_y - 30, init.road_x + self.x4 + 35, self.y4 - init.road_y + 30

    def get_bb_5(self):
        return init.road_x + self.x5 - 35, self.y5 - init.road_y - 30, init.road_x + self.x5 + 35, self.y5 - init.road_y + 30

    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())

    def draw_bb_4(self):
        draw_rectangle(*self.get_bb_4())

    def draw_bb_5(self):
        draw_rectangle(*self.get_bb_5())


class Tree:
    tree1, tree2 = None, None
    def __init__(self):
        if Tree.tree1 == None:
            Tree.tree1 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\tree1.png")

        if Tree.tree2 == None:
            Tree.tree2 = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\obstacle\\tree2.png")

    def update(self, frame_time):
        pass

    def draw(self):
        for i in range(42):
            Tree.tree1.draw(init.road_x + 2190, 7850 + (i * 200) - init.road_y)
        for i in range(42):
            Tree.tree2.draw(init.road_x + 2190, 7750 + (i * 200) - init.road_y)