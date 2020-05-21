class Card:
    def __init__(self, temp): # 랜덤 넘버 0...51 값을 입력받아서 카드 객체 생성
        self.value = temp % 13 + 1  # 1...13
        self.x = temp // 13         # 0..3 카트 무늬 suit 결정

    def getValue(self): # 카트 값 JQK는 10으로 결정
        if self.value > 10:
            return 10
        else:
            return self.value
    
    def getSuit(self):
        if self.x == 0:
            self.suit = "Clubs"
        elif self.x == 1:
            self.suit = "Spades"
        elif self.x == 2:
            self.suit = "Hearts"
        else:
            self.suit = "Diamonds"
        return self.suit

    def filename(self):
        return self.getSuit() + str(self.value) + ".png"