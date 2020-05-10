import random

CELL_NULL, CELL_X, CELL_O = range(3)
WIN_NULL, WIN_X, WIN_O = range(3)

class Cell:
    def __init__(self, x, y, state=CELL_NULL):
        self.x = x
        self.y = y
        self.state = state


# initialize 
cells = []
for i in range(3):
    for j in range(3):
        cells.append(Cell(x=i, y=j))


def drawTable():
    print("\n-------------\n|", end='')
    for i in range(0, 3):
        if cells[i].state == CELL_NULL:
            print('   ', end='|')
        elif cells[i].state == CELL_O:
            print(' O ', end='|')
        elif cells[i].state == CELL_X:
            print(' X ', end='|')
    print("\n-------------\n|", end='')
    for i in range(3, 6):
        if cells[i].state == CELL_NULL:
            print('   ', end='|')
        elif cells[i].state == CELL_O:
            print(' O ', end='|')
        elif cells[i].state == CELL_X:
            print(' X ', end='|')
    print("\n-------------\n|", end='')
    for i in range(6, 9):
        if cells[i].state == CELL_NULL:
            print('   ', end='|')
        elif cells[i].state == CELL_O:
            print(' O ', end='|')
        elif cells[i].state == CELL_X:
            print(' X ', end='|')
    print("\n-------------\n")


def updateTable(x, y, player):
    if (0 <= x) and (x < 3) and (0 <= y) and (y < 3): 
        if cells[x * 3 + y].state == CELL_NULL:
            cells[x * 3 + y].state = player
            return True
    return False
    

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



count = 0
winer = CELL_NULL
curr_player = random.randint(1, 2)
drawTable()
while count < 9 and winer == CELL_NULL:
    print("%d번쨰 턴" % count)
    c = ' '
    if curr_player == CELL_O:
        c = 'O'
    elif curr_player == CELL_X:
        c = 'X'

    x = eval(input("플레이어 %s의 행(0, 1, 2)을 입력하세요: " % c))
    y = eval(input("플레이어 %s의 열(0, 1, 2)을 입력하세요: " % c))

    result = updateTable(x, y, curr_player)
    winer = checkGame()
    drawTable()

    if result == True:
        if curr_player == CELL_O:
            curr_player = CELL_X
        elif curr_player == CELL_X:
            curr_player = CELL_O
        count += 1

if winer == CELL_O:
    print("플레이어 O가 이겼습니다.")
elif winer == CELL_X:
    print("플레이어 X가 이겼습니다.")
else:
    print("플레이어 X와 O가 비겼습니다.")