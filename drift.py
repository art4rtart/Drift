from pico2d import *
from math import *

#class------------------------------------------------------------------------------
class Car:
    def __init__(self):
        self.image = load_image('lambo.png')

    def update(self):
        self.y -= carSpeed

    def draw(self):
        self.image.draw(carX, carY)

class Road1:
    def __init__(self):
        self.y = 100
        self.image = load_image('road1.png')

    def update(self):
        if(life == 1):
            self.y -= curSpeedY

    def draw(self):
        for i in range(0, 6):
            self.image.draw(roadX, self.y + (200 * i))
            self.image.draw(roadX + 201, self.y + 1201 + (200 * i)) # 1번째 직선도로

        for i in range(0, 3):
            self.image.draw(roadX + 601, self.y + 2700 + (200 * i)) # 1번째 직선도로 3300
            self.image.draw(roadX + 801, self.y + 3500 + (200 * i)) # 3번째 직선도로 4100 + 100

        for i in range(0,8):
            self.image.draw(roadX + 801, self.y + 3500 + (200 * i)) # 4번째 직선도로
            self.image.draw(roadX + 2200, self.y + 12400 + (200 * i))


        for i in range(0,30):
            self.image.draw(roadX + 1401, self.y + 5600 + (200 * i))

class Road2:
    def __init__(self):
        self.y = 1200
        self.image = load_image('road2.png')

    def update(self):
        if(life == 1):
            self.y -= curSpeedY

    def draw(self):
        self.image.draw(roadX, self.y)

        for i in range (0, 2):
            self.image.draw(roadX + 200 + (200 * i), self.y + 1200 + (200 * i))

        self.image.draw(roadX + 600, self.y + 2200)


#3번째코스
        self.image.draw(roadX + 800, self.y + 4000)
        self.image.draw(roadX + 1000, self.y + 4200)
        self.image.draw(roadX + 1200, self.y + 4400)

#4번째코스
        self.image.draw(roadX + 1400, self.y + 10500)
        self.image.draw(roadX + 1600, self.y + 10700)
        self.image.draw(roadX + 1800, self.y + 10900)
        self.image.draw(roadX + 2000, self.y + 11100)

class Road3:
     def __init__(self):
         self.y = 1200
         self.image = load_image('road3.png')

     def update(self):
         if (life == 1):
             self.y -= curSpeedY

     def draw(self):
         self.image.draw(roadX + 200, self.y)
         self.image.draw(roadX + 400, self.y + 1200)
         self.image.draw(roadX + 600, self.y + 1400)
         self.image.draw(roadX + 800, self.y + 2200)

# 3번째코스
         self.image.draw(roadX + 1000, self.y + 4000)
         self.image.draw(roadX + 1200, self.y + 4200)
         self.image.draw(roadX + 1400, self.y + 4400)

#4번째코스
         self.image.draw(roadX + 1600, self.y + 10500)
         self.image.draw(roadX + 1800, self.y + 10700)
         self.image.draw(roadX + 2000, self.y + 10900)
         self.image.draw(roadX + 2200, self.y + 11100)

class BoostRoad:
    def __init__(self):
        self.image = load_image('speedboost.png')
        self.y = 600

    def update(self):
        self.y -= curSpeedY

    def draw(self):
        self.image.draw(roadX, self.y)
        self.image.draw(roadX + 800, self.y + 3600)
        self.image.draw(roadX + 1400, self.y + 6000)

class Obstacle:
    def __init__(self):
        self.image1 = load_image('control.png')
        self.image2 = load_image('cone.png')
        self.image3 = load_image('stone.png')
        self.image4 = load_image('one.png')
        self.image5 = load_image('back3.png')

    def update(self):
        pass

    def draw(self):
        self.image4.draw(roadX + 245, roadY + 300)
        self.image1.draw(roadX + 150, roadY + 800)

        self.image2.draw(roadX + 550, roadY + 1600)
        self.image4.draw(roadX + 645, roadY + 1900)

        self.image3.draw(roadX + 1350, roadY + 7000)
        self.image3.draw(roadX + 1450, roadY + 7400)
        self.image1.draw(roadX + 1350, roadY + 8000)




        self.image5.draw(roadX + 1455, roadY + 8500)

#key--------------------------------------------------------------------------------
def handle_events():
    global running
    global carX, carY
    global carCurrentStatus, carCurrentImage
    global carSpeed, curSpeedX, curSpeedY, upgradeY
    global carMoveStatus, moveLine, carMoveCount
    global driftframe
    global life
    global a, b, z

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


        if(life == 1):
            if event.type == SDL_MOUSEBUTTONDOWN: # 드리프트
                carCurrentStatus = 2
                carCurrentImage = 2
                driftframe = 0
                a = 180
                b = 270
                curSpeedX = curSpeedY
                curSpeedY = 0
                z = 0.01
                carY = carY + 10

            if event.type == SDL_MOUSEBUTTONUP: # 직진
                carCurrentStatus = 1
                carCurrentImage = 3
                driftframe = 0
                a = 180
                b = 270
                curSpeedX = 0
                curSpeedY = carSpeed
                z = 0.01

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_z: # 왼쪽 칼치기
                    carMoveStatus = 1
                    moveLine = 10
                    carMoveCount = 0

                elif event.key == SDLK_x: # 오른쪽 칼치기
                    carMoveStatus = 2
                    moveLine = 10
                    carMoveCount = 0

            elif event.key == SDLK_ESCAPE:
                running = False



#------------------------------------------------------------------------------------
open_canvas(1000,800)
#image load -------------------------------------------------------------------------
car = load_image('car.png') # 자동차
carDriftRight = load_image('lamboRight.png') #오른쪽 드리프트
carDriftBack = load_image('lamboLeft.png') #직진 드리프트
carCrash = load_image('explode1.png') #폭팔 이미지
background = load_image('back2.png') #배경
#------------------------------------------------------------------------------------

running = True

#자동차 위치
carX, carY = 400, 200

#도로 위치
roadX, roadY = 450, 1300

#배경 정보
Width, Height, count = 500, 400, 1

#자동차 현재 속도
carSpeed, driftSpeed = 3, 5
curSpeedX = carSpeed
curSpeedY = carSpeed

#자동차 정보
carCurrentStatus, carCurrentImage = 1, 1

#차선변경
carMoveStatus, carMoveCount, moveLine = 0, 0, 0

#프레임 변수
driftframe, crashframe = 0, 0

#목숨상태
life = 1

#각도, 드리프트 속도, 각종 변수
a, b, drifX, driftY, z = 180, 270, 0, 0, 0.003

#임시변수----------------------
upgradeY = 600
temp = 20

#도로, 자동차 클래스
car = Car()
road1 = Road1()
road2 = Road2()
road3 = Road3()
boost = BoostRoad()
obstacle = Obstacle()

while ( running ):
    clear_canvas()

    for i in range (0,10):
        background.draw(Width, Height + (i * Height * 2) - count)
    if(life == 1):
        count += 1

    road1.draw()
    road2.draw()
    road3.draw()
    boost.draw()
    obstacle.draw()

#update----------------------------------------------------------------------
    roadY -= curSpeedY
    driftX = carX + 20
    driftY = carY + 20

    road1.update()
    road2.update()
    road3.update()
    boost.update()
    obstacle.update()

    if carY > roadY + 11500:
        count += 0
        life = 0
        carY += carSpeed + 5

#충돌체크---------------------------------------------------------------------
    if( carCurrentStatus == 1): # 차가 직진할때

        if carY + 40 < roadY - 200: # 첫번째코스
            if carX + 25 > roadX + 100 or carX - 25 > roadX + 100 or carX - 25 < roadX - 100 :  # 오른쪽면 충돌체크
                curSpeedY = 0
                carCurrentImage = 4

        if (carY + 40 > roadY and carX < roadX + 100) \
                or (carY + 40 < roadY + 800 and carX + 25 > roadX + 300) \
                or (carY + 40 > roadY + 1200 and carX + 25 < roadX + 300) \
                or (carY + 40 > roadY + 1400 and carX + 25 < roadX + 500) \
                or (carY + 40 < roadY + 1200 and carX + 25 > roadX + 500) \
                or (carY + 40 < roadY + 2000 and carX + 25 > roadX + 700) \
                or (carY + 40 > roadY + 2200 and carX + 25 < roadX + 700) \
                or (carY + 40 < roadY + 3800 and carX + 25 > roadX + 900)\
                or (carY + 40 > roadY + 4000 and carX + 25 < roadX + 900) \
                or (carY + 40 > roadY + 4200 and carX + 25 < roadX + 1100) \
                or (carY + 40 > roadY + 4400 and carX + 25 < roadX + 1300) \
                or (carY + 40 < roadY + 10300 and carX + 50 > roadX + 1500)\
                or (carY + 40 > roadY + 10500 and carX > roadX + 1300 and carX < roadX + 1500)\
                or (carY + 40 > roadY + 10700 and carX > roadX + 1500 and carX < roadX + 1700)\
                or (carY + 40 > roadY + 10900 and carX > roadX + 1700 and carX < roadX + 1900)\
                or (carY + 40 > roadY + 11100 and carX > roadX + 1900 and carX < roadX + 2100):
                curSpeedY = 0
                carCurrentImage = 4
#장애물
        if (carY + 40 > roadY + 7950 and carY + 40 < roadY + 8100 and carX - 25 < roadX + 1350) \
            or (carY + 40 > roadY + 6950 and carY + 40 < roadY + 7100 and carX - 25 < roadX + 1350) \
            or (carY + 40 > roadY + 7350 and carY + 40 < roadY + 7500 and carX + 40 > roadX + 1400) \
            or (carY + 40 > roadY + 250 and carY + 40 < roadY + 400 and carX + 25 > roadX + 180) \
            or (carY + 40 > roadY + 750  and carY + 40 < roadY + 900 and carX - 25 < roadX + 150)\
            or (carY + 40 > roadY + 8250 and carY + 40 < roadY + 8750 and carX + 40 > roadX + 1400)\
            or (carY + 40 > roadY + 1550 and carY + 40 < roadY + 1750 and carX + 25 < roadX + 550)\
            or (carY + 40 > roadY + 1850 and carY + 40 < roadY + 2000 and carX + 25 > roadX + 600):
            curSpeedY = 0
            carCurrentImage = 4
#속도 가속---------------------------------------------------------------------
        upgradeY -= carSpeed

        if carY + 40 > upgradeY:
            curSpeedY = 10
            curSpeedX = 0
            driftSpeed = 5
            z = 0.01

        if carY + 40 > upgradeY + 1100:
            curSpeedY = 15
            curSpeedX = 0
            driftSpeed = 7
            z = 0.01

        if carY + 40 > upgradeY + 1600:
            curSpeedY = 19
            curSpeedX = 0
            driftSpeed = 7
            z = 0.01
# 칼치기-----------------------------------------------------------------------
        if carMoveStatus == 1:
            roadX += moveLine
            carMoveCount = carMoveCount + 1
            if(carMoveCount > 6.5):
                moveLine = 0

        if carMoveStatus == 2:
            roadX -= moveLine
            carMoveCount = carMoveCount + 1
            if(carMoveCount > 6.5):
                moveLine = 0

#------------------------------------------------------------------------------

    elif(carCurrentStatus == 2): # car driving right
        roadX = roadX - curSpeedX

        if (carY + 40 < roadY - 200 and carX + 25 > roadX + 100) \
            or (carY + 40 < roadY + 1000 and carX + 50 > roadX + 300) \
            or (carY + 40 < roadY + 1200 and carX + 50 > roadX + 500) \
            or (carY + 40 < roadY + 2000 and carX + 50 > roadX + 700) \
            or (carY + 40 < roadY + 3200 and carX + 50 > roadX + 900)\
            or (carY + 40 < roadY + 4000 and carX + 50 > roadX + 1100)\
            or (carY + 40 < roadY + 4200 and carX + 50 > roadX + 1300)\
            or (carY + 40 < roadY + 4200 and carX + 50 > roadX + 1500)\
            or(carY + 40 < roadY + 10500 and carX + 50 > roadX + 1700)\
            or(carY + 40 < roadY + 10700 and carX + 50 > roadX + 1900)\
            or(carY + 40 < roadY + 10900 and carX + 50 > roadX + 2100):
            curSpeedX = 0
            carCurrentImage = 4



#animation------------------------------------------------------------------

    if(carCurrentImage == 1): # car driving image
        car.draw()

    if(carCurrentImage == 2): # car drift right animation
        carDriftRight.clip_draw(driftframe * 100, 0, 100, 100, ((carX + 20)+ cos(a * (math.pi / 180)) * 10), carY + 20 + sin(a * (math.pi / 180)) * 10)
        if(driftframe < 5):
            driftframe = driftframe + 1
        a = a - 15
        if a < 90:
            a = 0

    if(carCurrentImage == 3): # car drift left animation
        carDriftBack.clip_draw(driftframe * 100, 0, 100, 100, (carX + cos(b * (math.pi / 180)) * 20) + 30, carY + sin(b * (math.pi / 180)) * 20)
        if (driftframe < 5):
            driftframe = driftframe + 1
        if b < 390:
            b += 15

    if carCurrentImage == 4: # car crash animation
        carCrash.clip_draw(crashframe * 100, 0, 100, 100, carX, carY + 50)
        if(crashframe < 15):
            crashframe = crashframe + 1
        life = 0
        carSpeed = 0
        curSpeedY = 0
        upgradeY = 0

#----------------------------------------------------------------------------

    delay(z)

    update_canvas()
    handle_events()

close_canvas()

