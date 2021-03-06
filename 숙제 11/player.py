class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N
    
    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):    # ace는 1혹은 11로 모두 사용 가능, 일단 11로 계산한 후 21이 넘어가면 1로 정정
        s = 0
        aceExists = False
        for card in self.cards:
            if card.getValue() == 1:
                aceExists = True
                s += 11
            else:
                s += card.getValue()

        if (aceExists == True) and (s > 21):
            s = 0
            for card in self.cards:
                s += card.getValue()

        return s