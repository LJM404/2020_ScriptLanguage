import random

# Constants
MAX_TURN_NUM = 7 * 6
VOID, RED, YELLOW = range(-1, 2)

# Data Table
player_name = {
    RED : "빨간색",
    YELLOW : "노란색"
}


turn = 0
winner = VOID
curr_player = random.randint(RED, YELLOW) 
tables = [ [VOID for i in range(7)] for n in range(6) ]


def updateTable(num):
    if (0 <= num) and (num < 7):
        for i in range(6):
            if tables[i][num] == VOID:
                tables[i][num] = curr_player
                return True
    return False

def checkTable():
    # 가로 확인
    for i in range(6):
        count = 0
        color = VOID
        for j in range(7):
            if tables[i][j] == color:       # 색깔이 같은 경우
                count += 1                      # 카운트를 1 증가 시킨다.
            else:                           # 색깔이 다른 경우
                if count == 4:                  # 카운트가 4일 경우
                    if color == RED:                # 색깔이 RED일 경우
                        return RED                      # RED를 반환
                    elif color == YELLOW:           # 색깔이 YELLOW일 경우
                        return YELLOW                   # YELLOW를 반환
                else:                           # 카운드가 4가 아닐 경우
                    count = 1                       # 카운트를 1로 
                    color = tables[i][j]            # 색깔을 현재 테이블 색깔로
        if count == 4:              # 카운트가 4일 경우
            if color == RED:            # 색깔이 RED일 경우
                return RED                  # RED를 반환
            elif color == YELLOW:       # 색깔이 YELLOW일 경우
                return YELLOW               # YELLOW를 반환

    # 세로 확인
    for j in range(7):
        count = 0
        color = VOID
        for i in range(6):
            if tables[i][j] == color:       # 색깔이 같은 경우
                count += 1                      # 카운트를 1 증가 시킨다.
            else:                           # 색깔이 다른 경우
                if count == 4:                  # 카운트가 4일 경우
                    if color == RED:                # 색깔이 RED인 경우
                        return RED                      # RED를 반환
                    elif color == YELLOW:           # 색깔이 YELLOW인 경우
                        return YELLOW                   # YELLOW를 반환
                else:                           # 카운트가 4가 아닐 경우
                    count = 1                       # 카운트를 1로
                    color = tables[i][j]            # 색깔을 현재 테이블 색깔로
        if count == 4:              # 카운트가 4일 경우
            if color == RED:            # 색깔이 RED일 경우
                return RED                  # RED를 반환
            elif color == YELLOW:       # 색깔이 YELLOW일 경우
                return YELLOW               # YELLOW를 반환

    # 오름 대각선 확인 - 0
    for n in range(6):
        i, j = n, 0
        count = 0
        color = VOID
        while ((0 <= i) and (i < 6)) and ((0 <= j) and (j < 7)):
            if tables[i][j] == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    #색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1                           # 카운트를 1로
                    color = tables[i][j]                # 색깔을 현재 테이블 색깔로
            i += 1
            j += 1
        if count == 4:          # 카운트 4일 경우
            if color == RED:        # 색깔이 RED인 경우
                return RED              # RED를 반환
            elif color == YELLOW:   # 색깔이 YELLOW인 경우
                return YELLOW           # YELLOW를 반환
    
    # 오름 대각선 확인 - 1
    for n in range(7):
        i, j = 0, n
        count = 0
        color = VOID
        while ((0 <= i) and (i < 6)) and ((0 <= j) and (j < 7)):
            if tables[i][j] == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    #색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1                           # 카운트를 1로
                    color = tables[i][j]                # 색깔을 현재 테이블 색깔로
            i += 1
            j += 1
        if count == 4:          # 카운트 4일 경우
            if color == RED:        # 색깔이 RED인 경우
                return RED              # RED를 반환
            elif color == YELLOW:   # 색깔이 YELLOW인 경우
                return YELLOW           # YELLOW를 반환

    # 내림 대각선 확인 - 0
    for n in range(7):
        i, j = 5, n
        count = 0
        color = VOID
        while ((0 <= i) and (i < 6)) and ((0 <= j) and (j < 7)):
            if tables[i][j] == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    # 색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1
                    color = tables[i][j]
            i -= 1
            j += 1
        if count == 4:          # 카운트 4일 경우
            if color == RED:        # 색깔이 RED인 경우
                return RED              # RED를 반환
            elif color == YELLOW:   # 색깔이 YELLOW인 경우
                return YELLOW           # YELLOW를 반환


    # 내림 대각선 확인 - 1
    for n in range(6):
        i, j = n, 0
        count = 0
        color = VOID
        while ((0 <= i) and (i < 6)) and ((0 <= j) and (j < 7)):
            if tables[i][j] == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    # 색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1
                    color = tables[i][j]
            i -= 1
            j += 1
        if count == 4:          # 카운트 4일 경우
            if color == RED:        # 색깔이 RED인 경우
                return RED              # RED를 반환
            elif color == YELLOW:   # 색깔이 YELLOW인 경우
                return YELLOW           # YELLOW를 반환

    return VOID

def drawTable():
    for i in range(5, -1, -1):
        print("|", end='')
        for j in range(7):
            if tables[i][j] == RED:
                print(" R ", end='')
            elif tables[i][j] == YELLOW:
                print(" Y ", end='')
            else:
                print("   ", end='')
            print("|", end='')
        print()
    print("-----------------------------")

# main loop
drawTable()
while turn < MAX_TURN_NUM and winner == VOID:
    num = eval(input("열 0~6에 %s 디스크를 떨어뜨리세요: " % player_name[curr_player]))
    result = updateTable(num)
    winner = checkTable()
    drawTable()

    if result:
        turn += 1
        curr_player = (curr_player + 1) % 2

# result infomation 
if winner == RED:
    print("%s 플레이어가 이겼습니다." % player_name[winner])
elif winner == YELLOW:
    print("%s 플레이어가 이겼습니다." % player_name[winner])
else:
    print("비겼습니다.")