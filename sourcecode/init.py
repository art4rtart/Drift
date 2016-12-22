import random

# -----------------------------------------------------------------------------------
car_x, car_y = 237, 130       # 차량 초기화
road_x, road_y = 280, 0       # 도로 초기화
angle_0, angle_1 = 0, 0     # 각도 초기화
PI = 3.14                   # 3.14 pi
# -----------------------------------------------------------------------------------
drift_state = 0             # 드리프트 상태
volume_state = 0            # 음향 상태
stealth_state = 0           # 스텔스 상태
clear_state = 0             # 스테이지 클리어 상태
carMoveStatus = 0           # 칼치기 상태
wasted_state = 0            # 종료 상태
# -----------------------------------------------------------------------------------
driftCount = 0              # 드리프트 횟수 카운트
mouseCount = 0              # 클릭 횟수 카운트
soundCount = 0              # 사운드 횟수 카운트
# -----------------------------------------------------------------------------------
life = 1                    # 목숨
stageEnd = 0                # 스테이지 종료
# -----------------------------------------------------------------------------------
ufoDirX, ufoDirY, ufoMoveX, ufoMoveY, ufoCount, questionMark = 1, 1, random.randint(100, 600), random.randint(500, 600), 0, 0
itemTime, itemDir = 1, 1
# -----------------------------------------------------------------------------------
boxCount, beerCount, cellCount, missileCount, stealthCount, tempS = 0, 0, 0, 0, 0, 1
# -----------------------------------------------------------------------------------
moveBack, carMoveLine, stealth_mode, tempRe = 0, 0, 0, 0
mileage, tempT, tempTime = 0, 0, 0
drunk_time = 0
drunk_dir = 1
drunk_count = 0

launch_update = 0
launchX, launchY = 800, 0
disX, disY = None, None

missile_crash = 0
