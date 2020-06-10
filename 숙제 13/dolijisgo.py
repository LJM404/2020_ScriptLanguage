from tkinter import *
from tkinter import font
from winsound import *
from card import *
import random


PLAYER_0, PLAYER_1, PLAYER_2 = range(3)

class Dolijisgo:
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle0 = font.Font(self.window, size=24, weight="bold", family="Consolas")
        self.fontstyle1 = font.Font(self.window, size=16, weight="bold", family="Consolas")
        self.fontstyle2 = font.Font(self.window, size=12, weight="bold", family="Consolas")
        self.setupButton()
        self.setupLabel()

        self.dealerCards = [] # 딜러가 가지고 있는 카드 목록
        self.dealerCardNum = 0 # 딜러가 가지고 있는 카드의 수
        self.dealerCardLabels = [] # 딜러가 가지고 있는 카드 라벨 목록
        self.dealerCardNumLabels = [] # 딜러가 가지고 있는 카드 숫자 라벨 목록

        self.player0Cards = [] # 플레이어 0번이 가지고 있는 카드 목록
        self.player0CardNum = 0 # 플레이어 0번이 가지고 있는 카드의 수
        self.player0CardLabels = [] # 플레이어 0번이 가지고 있는 카드 라벨 목록
        self.player0CardNumLabels = [] # 플레이어 0번이 가지고 있는 카드 숫자 라벨 목록

        self.player1Cards = [] # 플레이어 1번이 가지고 있는 카드 목록
        self.player1CardNum = 0 # 플레이어 1번이 가지고 있는 카드의 수
        self.player1CardLabels = [] # 플레이어 1번이 가지고 있는 카드 라벨 목록
        self.player1CardNumLabels = [] # 플레이어 1번이 가지고 있는 카드 숫자 라벨 목록
        
        self.player2Cards = [] # 플레이어 2번이 가지고 있는 카드 목록
        self.player2CardNum = 0 # 플레이어 2번이 가지고 있는 카드의 수
        self.player2CardLabels = [] # 플레이어 2번이 가지고 있는 카드 라벨 목록
        self.player2CardNumLabels = [] # 플레이어 2번이 가지고 있는 카드 숫자 라벨 목록

        self.playerCards = [[], [], []]
        self.playerCardNum = [0, 0, 0]
        self.playerCardLabels = [[], [], []]
        self.playerCardNumLabels = [[], [], []]

        self.round = 0
        self.totalMoney = 1000
        self.player0BetMoney = 0
        self.player1BetMoney = 0
        self.player2BetMoney = 0

        self.dealFunc = [self.firstRound, self.secondRound, self.thirdRound]
        self.playerBetMoney = [self.player0BetMoney, self.player1BetMoney, self.player2BetMoney]
        self.playerTextLabel = [self.player0TextLabel, self.player1TextLabel, self.player2TextLabel]
        self.playerResultLabel = [self.player0ResultLabel, self.player1ResultLabel, self.player2ResultLabel]
        self.playerBetMoneyLabel = [self.player0BetMoneyLabel, self.player1BetMoneyLabel, self.player2BetMoneyLabel]
        self.window.mainloop()


    def setupButton(self):
        self.Bet5Million0 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle1, command=lambda : self.pressed5Million(0))
        self.Bet5Million0.place(x=50, y=550)
        self.Bet1Million0 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle1, command=lambda : self.pressed1Million(0))
        self.Bet1Million0.place(x=130, y=550)
        self.Bet5Million1 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle1, command=lambda : self.pressed5Million(1))
        self.Bet5Million1.place(x=250, y=550)
        self.Bet1Million1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle1, command=lambda : self.pressed1Million(1))
        self.Bet1Million1.place(x=330, y=550)
        self.Bet5Million2 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle1, command=lambda : self.pressed5Million(2))
        self.Bet5Million2.place(x=450, y=550)
        self.Bet1Million2 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle1, command=lambda : self.pressed1Million(2))
        self.Bet1Million2.place(x=530, y=550)
        self.Deal = Button(self.window, text="Deal", width=5, height=1, font=self.fontstyle1, command=self.pressedDeal)
        self.Deal.place(x=620, y=550)
        self.Again = Button(self.window, text="Again", width=5, height=1, font=self.fontstyle1, command=self.pressedAgain)
        self.Again.place(x=700, y=550)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"
        self.Again["state"] = "disabled"
        self.Again["bg"] = "gray"


    def setupLabel(self):
        self.totalMoneyLabel = Label(text="1000만원", width=15, height=1, font=self.fontstyle0, bg="green", fg="blue")
        self.totalMoneyLabel.place(x=580, y=450)
        self.player0BetMoneyLabel = Label(text="0만", width=5, height=1, font=self.fontstyle0, bg="green", fg="cyan")
        self.player0BetMoneyLabel.place(x=100, y=500)
        self.player1BetMoneyLabel = Label(text="0만", width=5, height=1, font=self.fontstyle0, bg="green", fg="cyan")
        self.player1BetMoneyLabel.place(x=300, y=500)
        self.player2BetMoneyLabel = Label(text="0만", width=5, height=1, font=self.fontstyle0, bg="green", fg="cyan")
        self.player2BetMoneyLabel.place(x=500, y=500)

        self.player0ResultLabel = Label(text="", width=5, height=1, font=self.fontstyle0, bg="green", fg="red")
        self.player0ResultLabel.place(x=50, y=240)
        self.player1ResultLabel = Label(text="", width=5, height=1, font=self.fontstyle0, bg="green", fg="red")
        self.player1ResultLabel.place(x=250, y=240)
        self.player2ResultLabel = Label(text="", width=5, height=1, font=self.fontstyle0, bg="green", fg="red")
        self.player2ResultLabel.place(x=450, y=240)
        
        self.dealerTextLabel = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.dealerTextLabel.place(x=250, y=10)
        self.player0TextLabel = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.player0TextLabel.place(x=50, y=290)
        self.player1TextLabel = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.player1TextLabel.place(x=250, y=290)
        self.player2TextLabel = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="cyan")
        self.player2TextLabel.place(x=450, y=290)
        

    def firstRound(self):
        self.resetDealerCard()
        self.resetPlayerCard(PLAYER_0)
        self.resetPlayerCard(PLAYER_1)
        self.resetPlayerCard(PLAYER_2)

        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)

        self.setDealerCard(0)
        self.setPlayerCard(0, PLAYER_0)
        self.setPlayerCard(0, PLAYER_1)
        self.setPlayerCard(0, PLAYER_2)
        PlaySound("sounds/cardFlip1.wav", SND_FILENAME)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.round += 1


    def secondRound(self):
        for i in range(1, 3 + 1):
            self.setDealerCard(i)
            self.setPlayerCard(i, PLAYER_0)
            self.setPlayerCard(i, PLAYER_1)
            self.setPlayerCard(i, PLAYER_2)
        PlaySound("sounds/cardFlip1.wav", SND_FILENAME)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.round += 1


    def thirdRound(self):
        self.setDealerCard(4)
        self.setPlayerCard(4, PLAYER_0)
        self.setPlayerCard(4, PLAYER_1)
        self.setPlayerCard(4, PLAYER_2)
        PlaySound("sounds/win.wav", SND_FILENAME)

        self.checkWinner()

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"
        self.Again["state"] = "active"
        self.Again["bg"] = "white"
        self.Bet5Million0["state"] = "disabled"
        self.Bet5Million0["bg"] = "gray"
        self.Bet1Million0["state"] = "disabled"
        self.Bet1Million0["bg"] = "gray"
        self.Bet5Million1["state"] = "disabled"
        self.Bet5Million1["bg"] = "gray"
        self.Bet1Million1["state"] = "disabled"
        self.Bet1Million1["bg"] = "gray"
        self.Bet5Million2["state"] = "disabled"
        self.Bet5Million2["bg"] = "gray"
        self.Bet1Million2["state"] = "disabled"
        self.Bet1Million2["bg"] = "gray"

        self.round += 1


    def checkWinner(self):
        for i in range(self.dealerCardNum):
            p = PhotoImage(file="GodoriCards/" + self.dealerCards[i].filename())
            self.dealerCardLabels[i].configure(image=p)
            self.dealerCardLabels[i].image = p
            self.dealerCardNumLabels[i].configure(text=str(self.dealerCards[i].getSuit()))

        dealerPoint, dealerMadeCards, dealerRemainCards, dealerText = getPoint(self.dealerCards)
        player0Point, player0MadeCards, player0RemainCards, player0Text = getPoint(self.playerCards[PLAYER_0])
        player1Point, player1MadeCards, player1RemainCards, player1Text = getPoint(self.playerCards[PLAYER_1])
        player2Point, player2MadeCards, player2RemainCards, player2Text = getPoint(self.playerCards[PLAYER_2])

        if dealerPoint != NULL:
            for i in range(self.dealerCardNum):
                if self.dealerCards[i] in dealerMadeCards:
                    self.dealerCardNumLabels[i].configure(fg="orange")
                    self.dealerCardLabels[i].place(x=250+i*30, y=100)
        self.dealerTextLabel.config(text=dealerText)

        if player0Point != NULL:
            for i in range(self.playerCardNum[PLAYER_0]):
                if self.playerCards[PLAYER_0][i] in player0MadeCards:
                    self.playerCardNumLabels[PLAYER_0][i].configure(fg="orange")
                    self.playerCardLabels[PLAYER_0][i].place(x=50+i*30, y=380)
        self.playerTextLabel[PLAYER_0].configure(text=player0Text)

        if player1Point != NULL:
            for i in range(self.playerCardNum[PLAYER_1]):
                if self.playerCards[PLAYER_1][i] in player1MadeCards:
                    self.playerCardNumLabels[PLAYER_1][i].configure(fg="orange")
                    self.playerCardLabels[PLAYER_1][i].place(x=250+i*30, y=380)
        self.playerTextLabel[PLAYER_1].configure(text=player1Text)

        if player2Point != NULL:
            for i in range(self.playerCardNum[PLAYER_2]):
                if self.playerCards[PLAYER_2][i] in player2MadeCards:
                    self.playerCardNumLabels[PLAYER_2][i].configure(fg="orange")
                    self.playerCardLabels[PLAYER_2][i].place(x=450+i*30, y=380)
        self.playerTextLabel[PLAYER_2].configure(text=player2Text)

        if dealerPoint < player0Point:
            self.player0ResultLabel.configure(text="승")
            self.totalMoney += self.playerBetMoney[PLAYER_0] * 2
        else:
            self.player0ResultLabel.configure(text="패")

        if dealerPoint < player1Point:
            self.player1ResultLabel.configure(text="승")
            self.totalMoney += self.playerBetMoney[PLAYER_1] * 2
        else:
            self.player1ResultLabel.configure(text="패")

        if dealerPoint < player2Point:
            self.player2ResultLabel.configure(text="승")
            self.totalMoney += self.playerBetMoney[PLAYER_2] * 2
        else:
            self.player2ResultLabel.configure(text="패")

        self.totalMoneyLabel.configure(text=str(self.totalMoney) + "만원")


    def setDealerCard(self, num):
        newCard = Card(self.cardDeck.pop())
        self.addDealerCard(newCard)
        p = PhotoImage(file="GodoriCards/cardback.gif")
        self.dealerCardLabels.append(Label(self.window, image=p))

        self.dealerCardLabels[self.dealerCardNum - 1].image = p
        self.dealerCardLabels[self.dealerCardNum - 1].place(x=250+num*30, y=70)

        self.dealerCardNumLabels.append(Label(text="", width=2, height=1, font=self.fontstyle1, bg="green", fg="white"))
        self.dealerCardNumLabels[self.dealerCardNum - 1].place(x=250+20+num*30, y=30)


    def setPlayerCard(self, num, player):
        pos = [50, 250, 450]
        newCard = Card(self.cardDeck.pop())
        self.addPlayerCard(newCard, player)
        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.playerCardLabels[player].append(Label(self.window, image=p))

        self.playerCardLabels[player][self.playerCardNum[player] - 1].image = p
        self.playerCardLabels[player][self.playerCardNum[player] - 1].place(x=pos[player]+num*30, y=350)

        self.playerCardNumLabels[player].append(Label(text=str(newCard.getSuit()), width=2, height=1, font=self.fontstyle1, bg="green", fg="white"))
        self.playerCardNumLabels[player][self.playerCardNum[player] - 1].place(x=pos[player]+20+num*30, y=310)


    def pressedDeal(self):
        self.dealFunc[self.round]()


    def pressedAgain(self):
        self.Again["state"] = "disabled"
        self.Again["bg"] = "gray"

        self.Bet5Million0["state"] = "active"
        self.Bet5Million0["bg"] = "white"
        self.Bet1Million0["state"] = "active"
        self.Bet1Million0["bg"] = "white"
        self.Bet5Million1["state"] = "active"
        self.Bet5Million1["bg"] = "white"
        self.Bet1Million1["state"] = "active"
        self.Bet1Million1["bg"] = "white"
        self.Bet5Million2["state"] = "active"
        self.Bet5Million2["bg"] = "white"
        self.Bet1Million2["state"] = "active"
        self.Bet1Million2["bg"] = "white"

        self.resetDealer()
        self.resetPlayer(PLAYER_0)
        self.resetPlayer(PLAYER_1)
        self.resetPlayer(PLAYER_2)

        self.round = 0

        PlaySound("sounds/ding.wav", SND_FILENAME)
        

    def resetDealer(self):
        self.dealerTextLabel.configure(text="")
        self.resetDealerCard()
        for item in self.dealerCardNumLabels:
            item.destroy()
        self.dealerCardNumLabels.clear()
        for item in self.dealerCardLabels:
            item.image = None
            item.destroy()
        self.dealerCardLabels.clear()


    def resetPlayer(self, player):
        self.playerBetMoney[player] = 0
        self.playerTextLabel[player].configure(text="")
        self.playerResultLabel[player].configure(text="")
        self.playerBetMoneyLabel[player].configure(text="0만")
        self.resetPlayerCard(player)
        for item in self.playerCardNumLabels[player]:
            item.destroy()
        self.playerCardNumLabels[player].clear()
        for item in self.playerCardLabels[player]:
            item.image = None
            item.destroy()
        self.playerCardLabels[player].clear()


    def pressed5Million(self, player):
        betMoney = 5
        if betMoney <= self.totalMoney:
            self.totalMoney -= betMoney
            self.playerBetMoney[player] += betMoney
            self.totalMoneyLabel.configure(text=str(self.totalMoney) + "만원")
            self.playerBetMoneyLabel[player].configure(text=str(self.playerBetMoney[player]) + "만")
            
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound("sounds/chip.wav", SND_FILENAME)


    def pressed1Million(self, player):
        betMoney = 1
        if betMoney <= self.totalMoney:
            self.totalMoney -= betMoney
            self.playerBetMoney[player] += betMoney
            self.totalMoneyLabel.configure(text=str(self.totalMoney) + "만원")
            self.playerBetMoneyLabel[player].configure(text=str(self.playerBetMoney[player]) + "만")

            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound("sounds/chip.wav", SND_FILENAME)


    def addPlayerCard(self, card, player):
        self.playerCards[player].append(card)
        self.playerCardNum[player] += 1


    def addDealerCard(self, card):
        self.dealerCards.append(card)
        self.dealerCardNum += 1


    def resetPlayerCard(self, player):
        self.playerCards[player].clear()
        self.playerCardNum[player] = 0

    
    def resetDealerCard(self):
        self.dealerCards.clear()
        self.dealerCardNum = 0