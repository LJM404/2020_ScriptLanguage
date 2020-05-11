import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("행맨")
root.geometry("500x400")
root.resizable(False, False)

fp = open("hangman.txt")
words = fp.read().split()
fp.close()

MAX_COUNT_NUM = 7

word = None
result = None
canvas = None
running = None
draw_func = None
failure_count = None
failure_words = None
info_str = "단어 추측: %s"

def createGame():
    global word, result, running, failure_count, failure_words
    word = words[random.randint(0, len(words) - 1)]
    result = ['*' for n in range(len(word))]
    running = True
    failure_count = 0
    failure_words = []

def draw():
    canvas.delete("all")
    # 틀린 횟수별 그림
    for i in range(failure_count + 1):
        draw_func[i]()
        
    # 문자열 출력
    if running:
        canvas.create_text(250, 300, text=(info_str % ''.join(result)))
        if failure_count > 0:
            canvas.create_text(250, 350, text=("틀린 글자: %s" % ''.join(failure_words)))
    else:
        if failure_count < MAX_COUNT_NUM:
            canvas.create_text(250, 250, text="승리!")
        else:
            canvas.create_text(250, 250, text="패배!")
        canvas.create_text(250, 300, text=("정답: %s" % word))
        canvas.create_text(250, 350, text="게임을 계속하려면 ENTER를 누르세요.")
    canvas.update()

def keyInput(event):
    global failure_count, failure_words, running
    if running:
        if (ord('A') <= event.keycode) and (event.keycode < ord('z')):
            c = event.char
            if not (c in result):
                if c in word:
                    for i in range(len(word)):
                        if c == word[i]:
                            result[i] = c
                else:
                    failure_count += 1
                    failure_words.append(c)
                    failure_words = list(set(failure_words))

        if word == ''.join(result) or failure_count == MAX_COUNT_NUM:
            running = False
        draw()
    else:
        if event.keycode == 13:
            createGame()
            draw()

def drawLevel0():
    canvas.create_line(100, 30, 100, 250)
    canvas.create_line(100, 30, 250, 30)
    canvas.create_arc(50, 250, 150, 300, start=0, extent=180)

def drawLevel1():
    canvas.create_line(250, 30, 250, 50)

def drawLevel2():
    canvas.create_oval(220, 50, 280, 110)

def drawLevel3():
    canvas.create_line(230, 100, 150, 180)

def drawLevel4():
    canvas.create_line(270, 100, 350, 180)

def drawLevel5():
    canvas.create_line(250, 110, 250, 210)

def drawLevel6():
    canvas.create_line(250, 210, 200, 260)

def drawLevel7():
    canvas.create_line(250, 210, 300, 260)

draw_func = [drawLevel0, drawLevel1, drawLevel2, drawLevel3, drawLevel4, drawLevel5, drawLevel6, drawLevel7]

root.bind("<Key>", keyInput)
root.bind("<Return>", keyInput)

canvas = Canvas(root, width=500, height=400, bg="white")
canvas.place(x=0, y=0)

createGame()
draw()

# run
root.mainloop()