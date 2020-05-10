import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("틱택토")
root.geometry("240x210")
root.resizable(False, False)

# Constants 
CELL_O, CELL_X, CELL_NULL = range(3)
TURN_O = "플레이어 O의 차례입니다."
TURN_X = "플레이어 X의 차례입니다."
WIN_NULL = "비김! 게임이 끝났습니다."
WIN_O = "O승리! 게임이 끝났습니다."
WIN_X = "X승리! 게임이 끝났습니다."


# 이미지
o_image = PhotoImage(file="image/o.gif")
x_image = PhotoImage(file="image/x.gif")
null_image = PhotoImage(file="image/empty.gif")

# 셀과 이미지 데이터 테이블
state_table = {
    CELL_O : o_image,
    CELL_X : x_image,
    CELL_NULL : null_image
}

# 셀과 안내 문자 데이터 테이블
info_table = {
    CELL_O : TURN_O,
    CELL_X : TURN_X
}

# 셀과 종료 문자 데이터 테이블
exit_table = {
    CELL_O : WIN_O,
    CELL_X : WIN_X,
    CELL_NULL : WIN_NULL
}

# Globals
cells = []
count = 0
curr_player = random.randint(CELL_O, CELL_X)
winner = CELL_NULL

# 안내 문자
info_str = StringVar()
info_str.set(info_table[curr_player])
info_label = ttk.Label(root, textvariable=info_str)
info_label.place(x=60, y=190)

def checkGame():
    for i in range(3):
        if (cells[i * 3 + 0].state == cells[i * 3 + 1].state) and (cells[i * 3 + 1].state == cells[i * 3 + 2].state):
            if (cells[i * 3 + 0].state == CELL_O):
                return CELL_O
            elif (cells[i * 3 + 0].state == CELL_X):
                return CELL_X
        if (cells[0 * 3 + i].state == cells[1 * 3 + i].state) and (cells[1 * 3 + i].state == cells[2 * 3 + i].state):
            if (cells[0 * 3 + i].state == CELL_O):
                return CELL_O
            elif (cells[0 * 3 + i].state == CELL_X):
                return CELL_X

    if (cells[0].state == cells[4].state) and (cells[4].state == cells[8].state):
        if (cells[4].state == CELL_O):
            return CELL_O
        elif (cells[4].state == CELL_X):
            return CELL_X

    if (cells[2].state == cells[4].state) and (cells[4].state == cells[6].state):
        if (cells[4].state == CELL_O):
            return CELL_O
        elif (cells[4].state == CELL_X):
            return CELL_X

    return CELL_NULL

def changeTurn():
    global count, curr_player, winner
    winner = checkGame()
    count += 1
    if count < 9 and winner == CELL_NULL:
        curr_player = (curr_player + 1) % 2
        info_str.set(info_table[curr_player])
    else:
        info_str.set(exit_table[winner])

# 셀 클레스
class Cell:
    def __init__(self, root, x, y, state):
        self.root = root
        self.x = x
        self.y = y
        self.state = CELL_NULL
        self.label = ttk.Label(root, image=state_table[state])
        self.label.bind("<ButtonRelease-1>", lambda event : self.update())
        self.label.place(x=x, y=y)

    def update(self):
        if self.state == CELL_NULL and winner == CELL_NULL:
            self.state = curr_player
            self.label = ttk.Label(self.root, image=state_table[curr_player])
            self.label.place(x=self.x, y=self.y)
            changeTurn()


# 셀 초기화
for i in range(3):
    for j in range(3):
        cells.append(Cell(root, x=30+i*60, y=j*60, state=CELL_NULL))


# run
root.mainloop()