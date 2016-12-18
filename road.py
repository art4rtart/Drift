from pico2d import*
import init

count = 0

class Road1:
    road = None

    def __init__(self):
        self.time = 0.0                         # 시간 초기화
        self.speed = 320                        # 처음 속도 320 - 200 = 120km

        if Road1.road == None:
            Road1.road = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\road\\road1.png")

    def update(self, frame_time):
        global count
        count += 1

        print(count)

    def draw(self):
        for i in range(10):
            Road1.road.draw(init.road_x, 75 + (i * 150) - init.road_y)

        for i in range(8):
            Road1.road.draw(init.road_x + 181, 1755 + (i * 150) - init.road_y)

        for i in range(5):
            Road1.road.draw(init.road_x + 362, 3075 + (i * 150) - init.road_y)

        for i in range(5):
            Road1.road.draw(init.road_x + 542, 3975 + (i * 150) - init.road_y)

        for i in range(6):
            Road1.road.draw(init.road_x + 800, 4875 + (i * 150) - init.road_y)

        for i in range(3):
            Road1.road.draw(init.road_x + 1239, 5880 + (i * 150) - init.road_y)

        for i in range(5):
            Road1.road.draw(init.road_x + 1600, 6680 + (i * 150) - init.road_y)

        for i in range(55): # feel the speed 구간
            Road1.road.draw(init.road_x + 2320, 7760 + (i * 150) - init.road_y)

        for i in range(7):
            Road1.road.draw(init.road_x + 3400, 16520 + (i * 150) - init.road_y)

        for i in range(20):
            Road1.road.draw(init.road_x + 4480, 18680 + (i * 150) - init.road_y)

        Road1.road.draw(init.road_x + 3760, 17780 - init.road_y)
        Road1.road.draw(init.road_x + 4300, 18140 - init.road_y)
        Road1.road.draw(init.road_x + 4300, 18320 - init.road_y)


class Road2:
    road = None

    def __init__(self):
        if Road2.road == None:
            Road2.road = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\road\\road2.png")

    def update(self, frame_time):
        pass

    def draw(self):
        # 1번
        Road2.road.draw(init.road_x + 1, 1575 - init.road_y)

        # 2번
        Road2.road.draw(init.road_x + 182, 2901 - init.road_y)

        # 3번
        Road2.road.draw(init.road_x + 362, 3800 - init.road_y)

        # 4번
        Road2.road.draw(init.road_x + 542, 4700 - init.road_y)

        # 5번
        Road2.road.draw(init.road_x + 800, 5700 - init.road_y)
        Road2.road.draw(init.road_x + 1240, 6325 - init.road_y)
        Road2.road.draw(init.road_x + 1420, 6505 - init.road_y)

        # 7번
        Road2.road.draw(init.road_x + 1600, 7400 - init.road_y)
        Road2.road.draw(init.road_x + 1780, 7580 - init.road_y)

        #8번
        Road2.road.draw(init.road_x + 2320, 15980 - init.road_y)
        Road2.road.draw(init.road_x + 2860, 16160 - init.road_y)
        Road2.road.draw(init.road_x + 3040, 16340 - init.road_y)
        Road2.road.draw(init.road_x + 3400, 17600 - init.road_y)
        Road2.road.draw(init.road_x + 3760, 17960 - init.road_y)
        Road2.road.draw(init.road_x + 4300, 18500 - init.road_y)


class Road3:
    road = None

    def __init__(self):
        if Road3.road == None:
            Road3.road = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\road\\road3.png")

    def update(self, frame_time):
        pass

    def draw(self):
        Road3.road.draw(init.road_x + 181, 1575 - init.road_y)
        Road3.road.draw(init.road_x + 362, 2901 - init.road_y)
        Road3.road.draw(init.road_x + 542, 3800 - init.road_y)
        Road3.road.draw(init.road_x + 800, 4700 - init.road_y)
        Road3.road.draw(init.road_x + 1240, 5700 - init.road_y)
        Road3.road.draw(init.road_x + 1420, 6325 - init.road_y)
        Road3.road.draw(init.road_x + 1600, 6505 - init.road_y)
        Road3.road.draw(init.road_x + 1780, 7400 - init.road_y)
        Road3.road.draw(init.road_x + 2320, 7580 - init.road_y)
        Road3.road.draw(init.road_x + 2860, 15980 - init.road_y)
        Road3.road.draw(init.road_x + 3040, 16160 - init.road_y)
        Road3.road.draw(init.road_x + 3400, 16340 - init.road_y)
        Road3.road.draw(init.road_x + 3760, 17600 - init.road_y)
        Road3.road.draw(init.road_x + 4300, 17960 - init.road_y)
        Road3.road.draw(init.road_x + 4480, 18500 - init.road_y)


class Road4:
    road = None

    def __init__(self):
        if Road4.road == None:
            Road4.road = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\road\\road4.png")

    def update(self, frame_time):
        pass

    def draw(self):
        # 4번
        Road4.road.draw(init.road_x + 720, 4700 - init.road_y)

        # 5번
        Road4.road.draw(init.road_x + 980, 5700 - init.road_y)
        Road4.road.draw(init.road_x + 1060, 5700 - init.road_y)

        # 7번
        Road4.road.draw(init.road_x + 1960, 7580 - init.road_y)
        Road4.road.draw(init.road_x + 2140, 7580 - init.road_y)

        #8번
        Road4.road.draw(init.road_x + 2500, 15980 - init.road_y)
        Road4.road.draw(init.road_x + 2680, 15980 - init.road_y)
        Road4.road.draw(init.road_x + 3220, 16340 - init.road_y)
        Road4.road.draw(init.road_x + 3580, 17600 - init.road_y)
        Road4.road.draw(init.road_x + 3940, 17960 - init.road_y)
        Road4.road.draw(init.road_x + 4120, 17960 - init.road_y)


# road_x, road_y