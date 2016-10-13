from pico2d import *
import random

global tempx

#자동차 위치
x = 450
y = 250

#맵 위치
tempx = 500

#class------------------------------------------------------
class Road1:
    def __init__(self):
        self.y = 100
        self.image = load_image('road1.png')

    def update(self):
        self.y -= curSpeed

    def draw(self):
        for i in range(0, 6):
            self.image.draw(tempx, self.y + (200 * i))
            self.image.draw(tempx + 201, self.y + 1201 + (200 * i))

        for i in range(0, 3):
            self.image.draw(tempx + 600, self.y + 2700 + (200 * i)) # 3300
            self.image.draw(tempx + 800, self.y + 3500 + (200 * i)) # 4100 + 100

        for i in range(0,15):
            self.image.draw(tempx + 800, self.y + 3500 + (200 * i)) # 3번째 직선
            #self.image.draw(tempx + 1200, self.y + 4500 + (200 * i))
            pass

class Road2:
    def __init__(self):
        self.y = 1200
        self.image = load_image('road2.png')

    def update(self):
        self.y -= curSpeed

    def draw(self):
        self.image.draw(tempx, self.y)
        self.image.draw(tempx + 201, self.y + 1201)
        self.image.draw(tempx + 401, self.y + 1400)

        self.image.draw(tempx + 600, self.y + 2200)
        #self.image.draw(tempx + 800, self.y + 3000)
        #self.image.draw(tempx + 1000, self.y + 3200)

class Road3:
     def __init__(self):
         self.y = 1201
         self.image = load_image('road3.png')

     def update(self):
         self.y -= curSpeed

     def draw(self):
         self.image.draw(tempx + 200, self.y)
         self.image.draw(tempx + 400, self.y + 1201)
         self.image.draw(tempx + 600, self.y + 1400)
         self.image.draw(tempx + 800, self.y + 2200) # 더하기 1300
         #self.image.draw(tempx + 1000, self.y + 3000)
         #self.image.draw(tempx + 1200, self.y + 3200)

class Car:
    def __init__(self):
        self.x = 450
        self.y = 250
        self.image = load_image('car.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

#class------------------------------------------------------

def handle_events(): #키 값
    global running
    global x, y
    global status, carCurrentImage
    global frame, temp
    global carMoveStatus, moveLine, carMoveCount, curSpeed
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
                status = 2
                carCurrentImage = 2
                frame = 0
                frame1 = 0
                temp = 30
                curSpeed = 0

        if(life == 1):
            if event.type == SDL_MOUSEBUTTONUP: # 직진
                status = 1
                carCurrentImage = 3
                frame = 0
                frame1 = 0
                temp = 5
                curSpeed = 30

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_z: # 왼쪽 칼치기
                if(status == 1):
                    carMoveStatus = 1
                    moveLine = 10
                    carMoveCount = 0

                elif(status == 2):
                    carMoveStatus = 3
                    moveLine = 10
                    carMoveCount = 0

            elif event.key == SDLK_x: # 오른쪽 칼치기
                if(status == 1):
                    carMoveStatus = 2
                    moveLine = 10
                    carMoveCount = 0

                elif(status == 2):
                    carMoveStatus = 4
                    moveLine = 10
                    carMoveCount = 0

            elif event.key == SDLK_ESCAPE:
                running = False














#------------------------------------------------------------------------------------
open_canvas(1000,800)

#이미지로딩---------------------------------------------
car = load_image('car.png')
carDriftRight = load_image('driftR.png')
carDriftBack = load_image('driftB.png')
carCrash = load_image('explode.png')
background = load_image('back.png')
# -------------------------------------------------------

running = True

#맵 위치
Width, Height = 1700, 2500

#자동차 현재 속도
curSpeed = 30

#자동차 현재 상태
status = 1
carCurrentImage = 1
carCrashImage = 0

#칼치기 변수
carMoveStatus = 0
carMoveCount = 0
moveLine = 10

#class--------------------------
road1 = Road1()
road2 = Road2()
road3 = Road3()

roads1 = [Road1() for i in range(100)]
roads2 = [Road2() for i in range(1)]
roads3 = [Road3() for i in range(1)]

#임시 변수----------------------
tempcount = 1
tempy = 1300
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

        tempy -= curSpeed

#충돌체크---------------------------------------------------------------------
    if( status == 1):

        if y + 40 < tempy - 200: # 첫번째코스
            if x + 25 > tempx + 100 or x - 25 > tempx + 100:  # 오른쪽면 충돌체크
                curSpeed = 0
                carCurrentImage = 6
            elif x - 25 < tempx - 100: # 왼쪽면
                curSpeed = 0
                carCurrentImage = 5

        if y + 40 > tempy and x < tempx + 100: #첫번째 코스 윗면 & 두번째코스 왼쪽면
            curSpeed = 0
            carCurrentImage = 4

        if y + 40 < tempy + 1000 and x + 25 > tempx + 300: #두번째코스 오른면
            curSpeed = 0
            carCurrentImage = 6

        if y + 40 > tempy + 1200 and x + 25 < tempx + 300: #두번째구간 첫째윗면
            curSpeed = 0
            carCurrentImage = 4

        if y + 40 > tempy + 1400 and x + 25 < tempx + 500: #두번째 코스 둘째윗면
            curSpeed = 0
            carCurrentImage = 4

        if y + 40 < tempy + 1200 and x + 25 > tempx + 500: #두번째코스 첫째오른옆면
            curSpeed = 0
            carCurrentImage = 6

        if y + 40 < tempy + 2000 and x + 25 > tempx + 700: #두번째코스 둘째오른옆면
            curSpeed = 0
            carCurrentImage = 6

        if y + 40 > tempy + 2200 and x + 25 < tempx + 700: #세번째코스 윗면
            curSpeed = 0
            carCurrentImage = 4

        if y + 40 > tempy + 2000 and x + 25 > tempx + 900: #세번째코스 옆면
            curSpeed = 0
            carCurrentImage = 6



# 칼치기-----------------------------------------------------------------------
        if(carMoveStatus == 1):
            x = x - moveLine
            carMoveCount = carMoveCount + 1

            if(carMoveCount > 8):
                moveLine = 0

        if(carMoveStatus == 2):
            x = x + moveLine
            carMoveCount = carMoveCount + 1

            if(carMoveCount > 8):
                moveLine = 0


    elif(status == 2):
        tempx = tempx - temp

 # 칼치기-----------------------------------------------------------------------
        if(carMoveStatus == 3):
            y = y + moveLine
            carMoveCount = carMoveCount + 1

            if(carMoveCount > 8):
                moveLine = 0

        if(carMoveStatus == 4):
            y = y - moveLine
            carMoveCount = carMoveCount + 1

            if(carMoveCount > 8):
                moveLine = 0

#충돌체크--------------------------------------------------------------------------
        if y + 40 < tempy - 200:  # 첫번째코스
            if x + 25 > tempx + 100 or x - 25 > tempx + 100:  # 오른쪽면 충돌체크
                temp = 0
                carCurrentImage = 6
            elif x - 25 < tempx - 100:  # 왼쪽면
                temp = 0
                carCurrentImage = 5

        if y + 40 > tempy and x < tempx + 100:  # 첫번째 코스 윗면 & 두번째코스 왼쪽면
            temp = 0
            carCurrentImage = 4

        if y + 40 < tempy + 1000 and x + 25 > tempx + 300:  # 두번째코스 오른면
            temp = 0
            carCurrentImage = 6

        if y + 40 > tempy + 1200 and x + 25 < tempx + 300:  # 두번째구간 첫째윗면
            temp = 0
            carCurrentImage = 4

        if y + 40 > tempy + 1400 and x + 25 < tempx + 500:  # 두번째 코스 둘째윗면
            temp = 0
            carCurrentImage = 4

        if y + 40 < tempy + 1200 and x + 25 > tempx + 500:  # 두번째코스 첫째오른옆면
            temp = 0
            carCurrentImage = 6

        if y + 40 < tempy + 2000 and x + 25 > tempx + 700:  # 두번째코스 둘째오른옆면
            temp = 0
            carCurrentImage = 6

        if y + 40 > tempy + 2200 and x + 25 < tempx + 700:  # 세번째코스 윗면
            temp = 0
            carCurrentImage = 4

        if y + 40 > tempy + 2000 and x + 25 > tempx + 900:  # 세번째코스 옆면
            temp = 0
            carCurrentImage = 6




#애니메이션------------------------------------------------------------------

    if(carCurrentImage == 1):
        car.draw(x,y)

    if(carCurrentImage == 2):
        carDriftRight.clip_draw(frame * 100, 0, 100, 100, x, y)
        if(frame < 5):
            frame = frame + 1

    if(carCurrentImage == 3):
        carDriftBack.clip_draw(frame * 100, 0, 100, 100, x, y)
        if(frame < 5):
            frame = frame + 1

    if carCurrentImage == 4:
        carCrash.clip_draw(frame1 * 100, 0, 100, 100, x, y + 50)
        if(frame1 < 7):
            frame1 = frame1 + 1


        life = 0

    if carCurrentImage == 5:
        carCrash.clip_draw(frame1 * 100, 0, 100, 100, x - 20, y)
        if(frame1 < 7):
            frame1 = frame1 + 1


        life = 0

    if carCurrentImage == 6:
        carCrash.clip_draw(frame1 * 100, 0, 100, 100, x + 20, y)
        if (frame1 < 7):
            frame1 = frame1 + 1


        life = 0

#------------------------------------------------------------------------------------------

    delay(0.005)

    update_canvas()
    handle_events()

close_canvas()

