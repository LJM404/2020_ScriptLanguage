import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("사목게임")
root.geometry("280x280")
root.resizable(False, False)

# Constants
MAX_TURN_NUM = 7 * 6
VOID, RED, YELLOW = range(-1, 2)

# Data Table
player_name = {
    RED : "빨간색",
    YELLOW : "노란색"
}

# Globals
turn = None
winner = None
curr_player = None
tables = None

def updateTable(index):
    if (0 <= index) and (index < 7):
        for i in range(6):
            if tables[i][index].state == VOID:
                tables[i][index].state = curr_player
                tables[i][index].draw()
                return True
    return False

def checkTable():
# 가로 확인
    for i in range(6):
        count = 0
        color = VOID
        for j in range(7):
            if tables[i][j].state == color:       # 색깔이 같은 경우
                count += 1                      # 카운트를 1 증가 시킨다.
            else:                           # 색깔이 다른 경우
                if count == 4:                  # 카운트가 4일 경우
                    if color == RED:                # 색깔이 RED일 경우
                        return RED                      # RED를 반환
                    elif color == YELLOW:           # 색깔이 YELLOW일 경우
                        return YELLOW                   # YELLOW를 반환
                else:                           # 카운드가 4가 아닐 경우
                    count = 1                       # 카운트를 1로 
                    color = tables[i][j].state            # 색깔을 현재 테이블 색깔로
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
            if tables[i][j].state == color:       # 색깔이 같은 경우
                count += 1                      # 카운트를 1 증가 시킨다.
            else:                           # 색깔이 다른 경우
                if count == 4:                  # 카운트가 4일 경우
                    if color == RED:                # 색깔이 RED인 경우
                        return RED                      # RED를 반환
                    elif color == YELLOW:           # 색깔이 YELLOW인 경우
                        return YELLOW                   # YELLOW를 반환
                else:                           # 카운트가 4가 아닐 경우
                    count = 1                       # 카운트를 1로
                    color = tables[i][j].state            # 색깔을 현재 테이블 색깔로
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
            if tables[i][j].state == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    #색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1                           # 카운트를 1로
                    color = tables[i][j].state                # 색깔을 현재 테이블 색깔로
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
            if tables[i][j].state == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    #색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1                           # 카운트를 1로
                    color = tables[i][j].state                # 색깔을 현재 테이블 색깔로
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
            if tables[i][j].state== color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    # 색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1
                    color = tables[i][j].state
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
            if tables[i][j].state == color:           # 색깔이 같은 경우
                count += 1                          # 카운트를 1 증가시킨다.
            else:                               # 색깔이 다른 경우
                if count == 4:                      # 카운트가 4인 경우
                    if color == RED:                    # 색깔이 RED인 경우
                        return RED                          # RED를 반환
                    elif color == YELLOW:               # 색깔이 YELLOW인 경우
                        return YELLOW                       # YELLOW를 반환
                else:                               # 카운트가 4가 아닌 경우
                    count = 1
                    color = tables[i][j].state
            i -= 1
            j += 1
        if count == 4:          # 카운트 4일 경우
            if color == RED:        # 색깔이 RED인 경우
                return RED              # RED를 반환
            elif color == YELLOW:   # 색깔이 YELLOW인 경우
                return YELLOW           # YELLOW를 반환

    return VOID

def resultMessage():
    if winner == RED or winner == YELLOW:
        messagebox.showinfo(title="알림", message="%s 플레이어가 이겼습니다." % player_name[winner])
    else:
        messagebox.showinfo(title="알림", message="비겼습니다.")


# Class Cell
class Cell:
    def __init__(self, master, x, y, index, state):
        self.master = master
        self.x = x
        self.y = y
        self.index = index
        self.state = state
        self.canvas = Canvas(master, width=40, height=40, bg="white")
        self.canvas.bind("<ButtonRelease-1>", lambda event: self.update())
        self.draw()
        self.canvas.place(x=x, y=y)

    def draw(self):
        self.canvas.delete("all")
        if self.state == RED:
            self.canvas.create_oval(5, 5, 35, 35, fill="red")
        elif self.state == YELLOW:
            self.canvas.create_oval(5, 5, 35, 35, fill="yellow")
        else:
            self.canvas.create_oval(5, 5, 35, 35)
        self.canvas.update()

    def update(self):
        global turn, curr_player, winner
        if turn < MAX_TURN_NUM and winner == VOID:
            result = updateTable(self.index)
            winner = checkTable()

            if result:
                turn += 1
                curr_player = (curr_player + 1) % 2

                if turn >= MAX_TURN_NUM or winner != VOID:
                    resultMessage()


def createGame():
    global turn, winner, curr_player, tables
    turn = 0
    winner = VOID
    curr_player = RED
    tables = [ [] for n in range(6) ]
    for i in range(6):
        for j in range(7):
            tables[i].append(Cell(root, j * 40, 240 - 40 - i * 40, j, VOID))

reset_button = ttk.Button(root, text="새로시작", command=createGame)
reset_button.place(x=100, y=250)

# run
createGame()
root.mainloop()