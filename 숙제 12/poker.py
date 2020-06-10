from tkinter import *
from tkinter import font
from winsound import *
from card import *
import random

# Texas Holdem Poker
# 각 플레이어가 2장의 카드를 받는다.
# 공통의 5장의 카드를 이용하여 높은 족보가 승리하는 게임
# 총 7장 중 5장만 선별해서 내 패를 구성함
# 처음 2장의 패를 받기전 블라인드라는 의무적으로 내야하는 돈이 있음
# 배팅 후 3장의 카드를 동시에 바닥에 깔음 (플랍)
# 플랍 이후 배팅 기회를 얻음
# 배팅 라운드 이후 또 1장의 카드를 바닥에 깔음 (턴)
# 턴 이후 배팅 기회를 얻음
# 배팅 라운드 이후 마지막 1장의 카드를 바닥에 깔음 (리버)
# 마지막 배팅 라운드 후 가장 좋은 패를 갖고 있는 사람이 돈을 가져옴

# Check: 베팅 안하고 차례를 넘김

PRE_FLOP, FLOP, TURN, RIVER = range(4)

class TexasHoldemPoker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem Poker")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle0 = font.Font(self.window, size=24, weight="bold", family="Consolas")
        self.fontstyle1 = font.Font(self.window, size=16, weight="bold", family="Consolas")
        self.setupButton()
        self.setupLabel()

        self.dealFunc = [self.preFlop, self.flop, self.turn, self.river]

        self.round = PRE_FLOP # 게임 라운드

        self.playerCards = [] # 플레이어 카드 목록
        self.playerCardNum = 0 # 플레이어 카드 개수
        self.playerCardLabels = [] # 플레이어 카드 라벨 목록

        self.npcCards = [] # npc 카드 목록
        self.npcCardNum = 0 # npc 카드 개수
        self.npcCardLabels = [] # npc 카드 라벨 목록

        self.communityCards = [] # community 카드 목록
        self.communityCardNum = 0 # community 카드 개수
        self.communityCardLabels = [] # community 카드 라벨 목록

        self.betMoney = 10 # 초기 베팅 금액
        self.playerMoney = 990 # 초기 플레이어 소유 금액
        self.window.mainloop()
        pass

    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle1, command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle1, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle1, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle1, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle1, command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"
        self.Again["state"] = "disabled"
        self.Again["bg"] = "gray"


    def setupLabel(self):
        self.betMoneyLabel = Label(text="$10", width=4, height=1, font=self.fontstyle0, bg="green", fg="orange")
        self.betMoneyLabel.place(x=200, y=450)
        self.playerMoneyLabel = Label(text="You have $990", width=15, height=1, font=self.fontstyle0, bg="green", fg="orange")
        self.playerMoneyLabel.place(x=500, y=450)
        self.playerResultLabel = Label(text="", width=15, height=1, font=self.fontstyle0, bg="green", fg="cyan")
        self.playerResultLabel.place(x=200, y=400)
        self.npcResultLabel = Label(text="", width=15, height=1, font=self.fontstyle0, bg="green", fg="cyan")
        self.npcResultLabel.place(x=200, y=100)
        self.gameResultLabel = Label(text="", width=15, height=1, font=self.fontstyle0, bg="green", fg="red")
        self.gameResultLabel.place(x=500, y=300)


    def pressedCheck(self):
        needMoney = self.betMoney * 0
        if needMoney <= self.playerMoney:
            self.betMoney += needMoney
            self.playerMoney -= needMoney
            self.betMoneyLabel.configure(text="$" + str(self.betMoney))
            self.playerMoneyLabel.configure(text="You have $" + str(self.playerMoney))

            self.Check["state"] = "disabled"
            self.Check["bg"] = "gray"
            self.Bx1["state"] = "disabled"
            self.Bx1["bg"] = "gray"
            self.Bx2["state"] = "disabled"
            self.Bx2["bg"] = "gray"
            
            if self.round <= RIVER:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"
                PlaySound("sounds/chip.wav", SND_FILENAME)
            else:
                self.Again["state"] = "active"
                self.Again["bg"] = "white"
                PlaySound("sounds/chip.wav", SND_FILENAME)
                self.checkWinner()



    def pressedBx1(self):
        needMoney = self.betMoney * 1
        if needMoney <= self.playerMoney:
            self.betMoney += needMoney
            self.playerMoney -= needMoney
            self.betMoneyLabel.configure(text="$" + str(self.betMoney))
            self.playerMoneyLabel.configure(text="You have $" + str(self.playerMoney))
            
            self.Check["state"] = "disabled"
            self.Check["bg"] = "gray"
            self.Bx1["state"] = "disabled"
            self.Bx1["bg"] = "gray"
            self.Bx2["state"] = "disabled"
            self.Bx2["bg"] = "gray"
            
            if self.round <= RIVER:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"
                PlaySound("sounds/chip.wav", SND_FILENAME)
            else:
                self.Again["state"] = "active"
                self.Again["bg"] = "white"
                PlaySound("sounds/chip.wav", SND_FILENAME)
                self.checkWinner()


    def pressedBx2(self):
        needMoney = self.betMoney * 2
        if needMoney <= self.playerMoney:
            self.betMoney += needMoney
            self.playerMoney -= needMoney
            self.betMoneyLabel.configure(text="$" + str(self.betMoney))
            self.playerMoneyLabel.configure(text="You have $" + str(self.playerMoney))

            self.Check["state"] = "disabled"
            self.Check["bg"] = "gray"
            self.Bx1["state"] = "disabled"
            self.Bx1["bg"] = "gray"
            self.Bx2["state"] = "disabled"
            self.Bx2["bg"] = "gray"
            
            if self.round <= RIVER:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"
                PlaySound("sounds/chip.wav", SND_FILENAME)
            else:
                self.Again["state"] = "active"
                self.Again["bg"] = "white"
                PlaySound("sounds/chip.wav", SND_FILENAME)
                self.checkWinner()


    def pressedDeal(self):
        self.dealFunc[self.round]()


    def pressedAgain(self):
        self.Again["state"] = "disabled"
        self.Again["bg"] = "gray"

        self.Check["state"] = "active"
        self.Check["bg"] = "white"
        self.Bx1["state"] = "active"
        self.Bx1["bg"] = "white"
        self.Bx2["state"] = "active"
        self.Bx2["bg"] = "white"

        for item in self.playerCardLabels:
            item.image = None
            item.destroy()
        
        for item in self.npcCardLabels:
            item.image = None
            item.destroy()

        for item in self.communityCardLabels:
            item.image = None
            item.destroy()
            
        self.playerCardLabels.clear()
        self.npcCardLabels.clear()
        self.communityCardLabels.clear()

        self.round = PRE_FLOP
        self.betMoney = 10
        self.playerMoney = max(self.playerMoney - 10, 0)

        self.playerResultLabel.configure(text="")
        self.npcResultLabel.configure(text="")
        self.gameResultLabel.configure(text="")
        self.playerMoneyLabel.configure(text="You have $" + str(self.playerMoney))
        self.betMoneyLabel.configure(text="$" + str(self.betMoney))
        PlaySound("sounds/ding.wav", SND_FILENAME)


    def preFlop(self):
        self.resetPlayerCard()
        self.resetNpcCard()
        self.resetCommunityCard()

        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)

        self.setPlayerCard(0)
        self.setNpcCard(0)
        self.setPlayerCard(1)
        self.setNpcCard(1)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.Check["state"] = "active"
        self.Check["bg"] = "white"
        self.Bx1["state"] = "active"
        self.Bx1["bg"] = "white"
        self.Bx2["state"] = "active"
        self.Bx2["bg"] = "white"

        self.round += 1


    def flop(self):
        self.setCommunityCard(0)
        self.setCommunityCard(1)
        self.setCommunityCard(2)
        
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.Check["state"] = "active"
        self.Check["bg"] = "white"
        self.Bx1["state"] = "active"
        self.Bx1["bg"] = "white"
        self.Bx2["state"] = "active"
        self.Bx2["bg"] = "white"

        self.round += 1


    def turn(self):
        self.setCommunityCard(3)
        
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.Check["state"] = "active"
        self.Check["bg"] = "white"
        self.Bx1["state"] = "active"
        self.Bx1["bg"] = "white"
        self.Bx2["state"] = "active"
        self.Bx2["bg"] = "white"

        self.round += 1


    def river(self):
        self.setCommunityCard(4)
        
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.Check["state"] = "active"
        self.Check["bg"] = "white"
        self.Bx1["state"] = "active"
        self.Bx1["bg"] = "white"
        self.Bx2["state"] = "active"
        self.Bx2["bg"] = "white"

        self.round += 1


    def checkWinner(self):
        p = PhotoImage(file="cards/" + self.npcCards[0].filename())
        self.npcCardLabels[0].configure(image=p)
        self.npcCardLabels[0].image = p

        p = PhotoImage(file="cards/" + self.npcCards[1].filename())
        self.npcCardLabels[1].configure(image=p)
        self.npcCardLabels[1].image = p 

        npcPoint, npcResult = getPoint(self.npcCards + self.communityCards)
        playerPoint, playerResult = getPoint(self.playerCards + self.communityCards)

        self.playerResultLabel.configure(text=playerResult)
        self.npcResultLabel.configure(text=npcResult)

        if playerPoint > npcPoint:
            self.gameResultLabel.configure(text="Win")
            self.playerMoney += self.betMoney * 2
            PlaySound("sounds/win.wav", SND_FILENAME)
        elif playerPoint == npcPoint:
            self.playerMoney += self.betMoney
            self.gameResultLabel.configure(text="Push")
        else:
            self.gameResultLabel.configure(text="Lose")
            PlaySound("sounds/wrong.wav", SND_FILENAME)

        self.betMoney = 0
        self.playerMoneyLabel.configure(text="You have $" + str(self.playerMoney))
        self.betMoneyLabel.configure(text="$" + str(self.betMoney))


    def setPlayerCard(self, num):
        newCard = Card(self.cardDeck.pop())
        self.addPlayerCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.playerCardLabels.append(Label(self.window, image=p))

        self.playerCardLabels[self.playerCardNum - 1].image = p
        self.playerCardLabels[self.playerCardNum - 1].place(x=50+num*80, y=350)
        PlaySound("sounds/cardFlip1.wav", SND_FILENAME)


    def setNpcCard(self, num):
        newCard = Card(self.cardDeck.pop())
        self.addNpcCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.npcCardLabels.append(Label(self.window, image=p))

        self.npcCardLabels[self.npcCardNum - 1].image = p
        self.npcCardLabels[self.npcCardNum - 1].place(x=50+num*80, y=50)


    def setCommunityCard(self, num):
        newCard = Card(self.cardDeck.pop())
        self.addCommunityCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.communityCardLabels.append(Label(self.window, image=p))

        self.communityCardLabels[self.communityCardNum - 1].image = p
        self.communityCardLabels[self.communityCardNum - 1].place(x=150+num*80, y=200)
        PlaySound("sounds/cardFlip1.wav", SND_FILENAME)


    def resetPlayerCard(self):
        self.playerCards.clear()
        self.playerCardNum = 0


    def resetNpcCard(self):
        self.npcCards.clear()
        self.npcCardNum = 0


    def resetCommunityCard(self):
        self.communityCards.clear()
        self.communityCardNum = 0

    
    def addPlayerCard(self, card):
        self.playerCards.append(card)
        self.playerCardNum += 1


    def addNpcCard(self, card):
        self.npcCards.append(card)
        self.npcCardNum += 1


    def addCommunityCard(self, card):
        self.communityCards.append(card)
        self.communityCardNum += 1