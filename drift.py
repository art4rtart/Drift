from pico2d import *
import random

#자동차 위치
carX, carY = 450, 250

#도로 위치
roadX = 500
roadY = 1300

#class------------------------------------------------------
class Road1:
    def __init__(self):
        self.y = 100
        self.image = load_image('road1.png')

    def update(self):
        self.y -= curSpeedY

    def draw(self):
        for i in range(0, 6):
            self.image.draw(roadX, self.y + (200 * i))
            self.image.draw(roadX + 201, self.y + 1201 + (200 * i))

        for i in range(0, 3):
            self.image.draw(roadX + 600, self.y + 2700 + (200 * i)) # 3300
            self.image.draw(roadX + 800, self.y + 3500 + (200 * i)) # 4100 + 100

        for i in range(0,10):
            self.image.draw(roadX + 800, self.y + 3500 + (200 * i)) # 3번째 직선
            #self.image.draw(roadX + 1200, self.y + 4500 + (200 * i))
            pass

class Road2:
    def __init__(self):
        self.y = 1200
        self.image = load_image('road2.png')

    def update(self):
        self.y -= curSpeedY

    def draw(self):
        self.image.draw(roadX, self.y)
        self.image.draw(roadX + 201, self.y + 1201)
        self.image.draw(roadX + 401, self.y + 1400)

        self.image.draw(roadX + 600, self.y + 2200)
        #self.image.draw(roadX + 800, self.y + 3000)
        #self.image.draw(roadX + 1000, self.y + 3200)

class Road3:
     def __init__(self):
         self.y = 1201
         self.image = load_image('road3.png')

     def update(self):
         self.y -= curSpeedY

     def draw(self):
         self.image.draw(roadX + 200, self.y)
         self.image.draw(roadX + 400, self.y + 1201)
         self.image.draw(roadX + 600, self.y + 1400)
         self.image.draw(roadX + 800, self.y + 2200) # 더하기 1300
         #self.image.draw(roadX + 1000, self.y + 3000)
         #self.image.draw(roadX + 1200, self.y + 3200)

class Car:
    def __init__(self):
        self.image = load_image('car.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(carX, carY)

#class------------------------------------------------------

def handle_events(): #키 값
    global running
    global carX, carY
    global carCurrentStatus, carCurrentImage
    global frame
    global curSpeedX, curSpeedY
    global carMoveStatus, moveLine, carMoveCount
    global frame1
    global life

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
                frame = 0
                frame1 = 0
                curSpeedX = 30
                curSpeedY = 0

            if event.type == SDL_MOUSEBUTTONUP: # 직진
                carCurrentStatus = 1
                carCurrentImage = 3
                frame = 0
                frame1 = 0
                curSpeedX = 5
                curSpeedY = 30

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
#이미지로딩---------------------------------------------
car = load_image('car.png') # 자동차
carDriftRight = load_image('driftR.png') #오른쪽 드리프트
carDriftBack = load_image('driftB.png') #직진 드리프트
carCrash = load_image('explode.png') #폭팔 이미지
background = load_image('back.png') #배경
# -------------------------------------------------------

running = True

#배경 위치
Width, Height = 1700, 2500

#자동차 현재 속도
curSpeedY = 30

#자동차 현재 상태
carCurrentStatus = 1
carCurrentImage = 1
carCrashImage = 0

#칼치기 변수
carMoveStatus = 0
carMoveCount = 0
moveLine = 15

#class--------------------------
road1 = Road1()
road2 = Road2()
road3 = Road3()
car = Car()

roads1 = [Road1() for i in range(100)]
roads2 = [Road2() for i in range(1)]
roads3 = [Road3() for i in range(1)]

#임시 변수----------------------
tempcount = 1
tempz = 0
frame = 0
frame1 = 0
life = 1
#-------------------------------

while ( running ):
    clear_canvas()

    background.draw(600, 400 - tempcount)
    tempcount += 1

    for road in roads1:
        road.update()
        road.draw()

    for road in roads2:
        road.update()
        road.draw()

    for road in roads3:
        road.update()
        road.draw()

        roadY -= curSpeedY

#충돌체크---------------------------------------------------------------------
    if( carCurrentStatus == 1): # 차가 직진할때


        if carY + 40 < roadY - 200: # 첫번째코스
            if carX + 25 > roadX + 100 or carX - 25 > roadX + 100:  # 오른쪽면 충돌체크
                curSpeedY = 0
                carCurrentImage = 4
            elif carX - 25 < roadX - 100: # 왼쪽면
                curSpeedY = 0
                carCurrentImage = 4


        if (carY + 40 > roadY and carX < roadX + 100) \
                or (carY + 40 < roadY + 1000 and carX + 25 > roadX + 300) \
                or (carY + 40 > roadY + 1200 and carX + 25 < roadX + 300) \
                or (carY + 40 > roadY + 1400 and carX + 25 < roadX + 500) \
                or (carY + 40 < roadY + 1200 and carX + 25 > roadX + 500) \
                or (carY + 40 < roadY + 2000 and carX + 25 > roadX + 700) \
                or (carY + 40 > roadY + 2200 and carX + 25 < roadX + 700) \
                or (carY + 40 > roadY + 2000 and carX + 25 > roadX + 900):

                # 첫번째 코스 윗면 & 두번째코스 왼쪽면
                # 두번째코스 오른면
                # 두번째구간 첫째윗면
                # 두번째 코스 둘째윗면
                # 두번째코스 첫째오른옆면
                # 두번째코스 둘째오른옆면
                # 세번째코스 윗면
                # 세번째코스 옆면
                curSpeedY = 0
                carCurrentImage = 4


        if carY + 40 > roadY + 4200:
            curSpeedY = 0
            carCurrentImage = 4


# 칼치기-----------------------------------------------------------------------
        if carMoveStatus == 1:
            carX -= moveLine
            carMoveCount = carMoveCount + 1
            if(carMoveCount > 8):
                moveLine = 0

        if carMoveStatus == 2:
            carX += moveLine
            carMoveCount = carMoveCount + 1
            if(carMoveCount > 8):
                moveLine = 0

#---------------------------------------------------------------------------------
    elif(carCurrentStatus == 2): # car driving right
        roadX = roadX - curSpeedX

#crash----------------------------------------------------------------------
        #모든 오른 벽면
        if (carY + 40 < roadY - 200 and carX + 25 > roadX + 100) \
            or (carY + 40 < roadY + 1000 and carX + 25 > roadX + 300) \
            or (carY + 40 < roadY + 1200 and carX + 25 > roadX + 500) \
            or (carY + 40 < roadY + 2000 and carX + 25 > roadX + 700) \
            or (carY + 40 < roadY + 3200 and carX + 25 > roadX + 900):
            curSpeedX = 0
            carCurrentImage = 4


#animation------------------------------------------------------------------

    if(carCurrentImage == 1): # car driving image
        car.draw()

    if(carCurrentImage == 2): # car drift right animation
        carDriftRight.clip_draw(frame * 100, 0, 100, 100, carX, carY)
        if(frame < 5):
            frame = frame + 1

    if(carCurrentImage == 3): # car drift left animation
        carDriftBack.clip_draw(frame * 100, 0, 100, 100, carX, carY)
        if(frame < 5):
            frame = frame + 1

    if carCurrentImage == 4: # car crash animation
        carCrash.clip_draw(frame1 * 100, 0, 100, 100, carX, carY + 50)
        if(frame1 < 7):
            frame1 = frame1 + 1
        life = 0
#----------------------------------------------------------------------------

    delay(0.001)

    update_canvas()
    handle_events()

close_canvas()

