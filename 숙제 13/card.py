import copy


NULL, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN = range(10 + 1)

class Card:
    def __init__(self, num):
        self.suit = num // 4 + 1
        self.value = num % 4 + 1
    
    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def filename(self):
        return str(self.suit) + '.' + str(self.value) + ".gif"


def getRemainPoint(cards):
    cardList = copy.deepcopy(cards)
    cardList.sort(key=lambda card: card.getSuit())

    if (cardList[0].getSuit() == THREE) and (cardList[1].getSuit() == EIGHT):
        return 22, "38광떙"
    
    if (cardList[0].getSuit() == ONE) and (cardList[1].getSuit() == THREE):
        return 21, "13광땡"

    if (cardList[0].getSuit() == ONE) and (cardList[1].getSuit() == EIGHT):
        return 20, "18광땡"

    if (cardList[0].getSuit() == TEN) and (cardList[1].getSuit() == TEN):
        return 19, "장땡"

    if (cardList[0].getSuit() == NINE) and (cardList[1].getSuit() == NINE):
        return 18, "9땡"

    if (cardList[0].getSuit() == EIGHT) and (cardList[1].getSuit() == EIGHT):
        return 17, "8땡"

    if (cardList[0].getSuit() == SEVEN) and (cardList[1].getSuit() == SEVEN):
        return 16, "7땡"

    if (cardList[0].getSuit() == SIX) and (cardList[1].getSuit() == SIX):
        return 15, "6땡"

    if (cardList[0].getSuit() == FIVE) and (cardList[1].getSuit() == FIVE):
        return 14, "5땡"

    if (cardList[0].getSuit() == FOUR) and (cardList[1].getSuit() == FOUR):
        return 13, "4땡"

    if (cardList[0].getSuit() == THREE) and (cardList[1].getSuit() == THREE):
        return 12, "3땡"

    if (cardList[0].getSuit() == TWO) and (cardList[1].getSuit() == TWO):
        return 11, "2땡"

    if (cardList[0].getSuit() == ONE) and (cardList[1].getSuit() == ONE):
        return 10, "1땡"

    lastNumber = (cardList[0].getSuit() + cardList[1].getSuit()) % 10 
    if lastNumber != 0:
        return lastNumber, "{0}끗".format(lastNumber)
    else:
        return 0, "망통"


def getMade992Point(cards, suitCounts):
    if (2 <= suitCounts[8]) and (1 <= suitCounts[1]):
        madeCards = []
        remainCards = []
        cnt9, cnt2 = 0, 0
        for card in cards:
            if card.getSuit() == NINE:
                if cnt9 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt9 += 1
            elif card.getSuit() == TWO:
                if cnt2 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt2 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "구구리(9 9 2) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade884Point(cards, suitCounts):
    if (2 <= suitCounts[7]) and (1 <= suitCounts[3]):
        madeCards = []
        remainCards = []
        cnt8, cnt4 = 0, 0
        for card in cards:
            if card.getSuit() == EIGHT:
                if cnt8 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt8 += 1
            elif card.getSuit() == FOUR:
                if cnt4 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt4 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "팍팍싸(8 8 4) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade776Point(cards, suitCounts):
    if (2 <= suitCounts[6]) and (1 <= suitCounts[5]):
        madeCards = []
        remainCards = []
        cnt7, cnt6 = 0, 0
        for card in cards:
            if card.getSuit() == SEVEN:
                if cnt7 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt7 += 1
            elif card.getSuit() == SIX:
                if cnt6 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt6 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "철철육(7 7 6) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade668Point(cards, suitCounts):
    if (2 <= suitCounts[5]) and (1 <= suitCounts[7]):
        madeCards = []
        remainCards = []
        cnt6, cnt8 = 0, 0
        for card in cards:
            if card.getSuit() == SIX:
                if cnt6 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt6 += 1
            elif card.getSuit() == EIGHT:
                if cnt8 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt8 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "쭉쭉팔(6 6 8) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade578Point(cards, suitCounts):
    if (1 <= suitCounts[4]) and (1 <= suitCounts[6]) and (1 <= suitCounts[7]):
        madeCards = []
        remainCards = []
        cnt5, cnt7, cnt8 = 0, 0, 0
        for card in cards:
            if card.getSuit() == FIVE:
                if cnt5 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt5 += 1
            elif card.getSuit() == SEVEN:
                if cnt7 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt7 += 1
            elif card.getSuit() == EIGHT:
                if cnt8 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt8 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "오리발(5 7 8) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade569Point(cards, suitCounts):
    if (1 <= suitCounts[4]) and (1 <= suitCounts[5]) and (1 <= suitCounts[8]):
        madeCards = []
        remainCards = []
        cnt5, cnt6, cnt9 = 0, 0, 0
        for card in cards:
            if card.getSuit() == FIVE:
                if cnt5 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt5 += 1
            elif card.getSuit() == SIX:
                if cnt6 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt6 += 1
            elif card.getSuit() == NINE:
                if cnt9 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt9 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "오륙구(5 6 9) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade5510Point(cards, suitCounts):
    if (2 <= suitCounts[4]) and (1 <= suitCounts[9]):
        madeCards = []
        remainCards = []
        cnt5, cnt10 = 0, 0
        for card in cards:
            if card.getSuit() == FIVE:
                if cnt5 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt5 += 1
            elif card.getSuit() == TEN:
                if cnt10 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt10 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "꼬꼬장(5 5 10) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade479Point(cards, suitCounts):
    if (1 <= suitCounts[3]) and (1 <= suitCounts[6]) and (1 <= suitCounts[8]):
        madeCards = []
        remainCards = []
        cnt4, cnt7, cnt9 = 0, 0, 0
        for card in cards:
            if card.getSuit() == FOUR:
                if cnt4 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt4 += 1
            elif card.getSuit() == SEVEN:
                if cnt7 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt7 += 1
            elif card.getSuit() == NINE:
                if cnt9 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt9 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "사칠구(4 7 9) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade4610Point(cards, suitCounts):
    if (1 <= suitCounts[3]) and (1 <= suitCounts[5]) and (1 <= suitCounts[9]):
        madeCards = []
        remainCards = []
        cnt4, cnt6, cnt10 = 0, 0, 0
        for card in cards:
            if card.getSuit() == FOUR:
                if cnt4 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt4 += 1
            elif card.getSuit() == SIX:
                if cnt6 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt6 += 1
            elif card.getSuit() == TEN:
                if cnt10 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt10 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "사륙장(4 6 10) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade442Point(cards, suitCounts):
    if (2 <= suitCounts[3]) and (1 <= suitCounts[1]):
        madeCards = []
        remainCards = []
        cnt2, cnt4 = 0, 0
        for card in cards:
            if card.getSuit() == TWO:
                if cnt2 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt2 += 1
            elif card.getSuit() == FOUR:
                if cnt4 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt4 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "살살이(4 4 2) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade389Point(cards, suitCounts):
    if (1 <= suitCounts[2]) and (1 <= suitCounts[7]) and (1 <= suitCounts[8]):
        madeCards = []
        remainCards = []
        cnt3, cnt8, cnt9 = 0, 0, 0
        for card in cards:
            if card.getSuit() == THREE:
                if cnt3 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt3 += 1
            elif card.getSuit() == EIGHT:
                if cnt8 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt8 += 1
            elif card.getSuit() == NINE:
                if cnt9 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt9 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "삼빡구(3 8 9) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade3710Point(cards, suitCounts):
    if (1 <= suitCounts[2]) and (1 <= suitCounts[6]) and (1 <= suitCounts[9]):
        madeCards = []
        remainCards = []
        cnt3, cnt7, cnt10 = 0, 0, 0
        for card in cards:
            if card.getSuit() == THREE:
                if cnt3 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt3 += 1
            elif card.getSuit() == SEVEN:
                if cnt7 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt7 += 1
            elif card.getSuit() == TEN:
                if cnt10 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt10 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "삼칠장(3 7 10) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade334Point(cards, suitCounts):
    if (2 <= suitCounts[2]) and (1 <= suitCounts[3]):
        madeCards = []
        remainCards = []
        cnt3, cnt4 = 0, 0
        for card in cards:
            if card.getSuit() == THREE:
                if cnt3 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt3 += 1
            elif card.getSuit() == FOUR:
                if cnt4 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt4 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "심심새(3 3 4) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade2810Point(cards, suitCounts):
    if (1 <= suitCounts[1]) and (1 <= suitCounts[7]) and (1 <= suitCounts[9]):
        madeCards = []
        remainCards = []
        cnt2, cnt8, cnt10 = 0, 0, 0
        for card in cards:
            if card.getSuit() == TWO:
                if cnt2 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt2 += 1
            elif card.getSuit() == EIGHT:
                if cnt8 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt8 += 1
            elif card.getSuit() == TEN:
                if cnt10 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt10 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "이판장(2 8 10) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade235Point(cards, suitCounts):
    if (1 <= suitCounts[1]) and (1 <= suitCounts[2]) and (1 <= suitCounts[4]):
        madeCards = []
        remainCards = []
        cnt2, cnt3, cnt5 = 0, 0, 0
        for card in cards:
            if card.getSuit() == TWO:
                if cnt2 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt2 += 1
            elif card.getSuit() == THREE:
                if cnt3 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt3 += 1
            elif card.getSuit() == FIVE:
                if cnt5 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt5 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "이삼오(2 3 5) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade226Point(cards, suitCounts):
    if (2 <= suitCounts[1]) and (1 <= suitCounts[5]):
        madeCards = []
        remainCards = []
        cnt2, cnt6 = 0, 0
        for card in cards:
            if card.getSuit() == TWO:
                if cnt2 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt2 += 1
            elif card.getSuit() == SIX:
                if cnt6 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt6 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "니니육(2 2 6) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade1910Point(cards, suitCounts):
    if (1 <= suitCounts[0]) and (1 <= suitCounts[8]) and (1 <= suitCounts[9]):
        madeCards = []
        remainCards = []
        cnt1, cnt9, cnt10 = 0, 0, 0
        for card in cards:
            if card.getSuit() == ONE:
                if cnt1 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt1 += 1
            elif card.getSuit() == NINE:
                if cnt9 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt9 += 1
            elif card.getSuit() == TEN:
                if cnt10 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt10 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "삥구장(1 9 10) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade145Point(cards, suitCounts):
    if (1 <= suitCounts[0]) and (1 <= suitCounts[3]) and (1 <= suitCounts[4]):
        madeCards = []
        remainCards = []
        cnt1, cnt4, cnt5 = 0, 0, 0
        for card in cards:
            if card.getSuit() == ONE:
                if cnt1 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt1 += 1
            elif card.getSuit() == FOUR:
                if cnt4 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt4 += 1
            elif card.getSuit() == FIVE:
                if cnt5 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt5 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "빽새오(1 4 5) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade136Point(cards, suitCounts):
    if (1 <= suitCounts[0]) and (1 <= suitCounts[2]) and (1 <= suitCounts[5]):
        madeCards = []
        remainCards = []
        cnt1, cnt3, cnt6 = 0, 0, 0
        for card in cards:
            if card.getSuit() == ONE:
                if cnt1 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt1 += 1
            elif card.getSuit() == THREE:
                if cnt3 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt3 += 1
            elif card.getSuit() == SIX:
                if cnt6 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt6 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "몰삼육(1 3 6) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade127Point(cards, suitCounts):
    if (1 <= suitCounts[0]) and (1 <= suitCounts[1]) and (1 <= suitCounts[6]):
        madeCards = []
        remainCards = []
        cnt1, cnt2, cnt7 = 0, 0, 0
        for card in cards:
            if card.getSuit() == ONE:
                if cnt1 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt1 += 1
            elif card.getSuit() == TWO:
                if cnt2 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt2 += 1
            elif card.getSuit() == SEVEN:
                if cnt7 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt7 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "삐리칠(1 2 7) " + text
    else:
        return NULL, NULL, NULL, NULL


def getMade118Point(cards, suitCounts):
    if (2 <= suitCounts[0]) and (1 <= suitCounts[7]):
        madeCards = []
        remainCards = []
        cnt1, cnt8 = 0, 0
        for card in cards:
            if card.getSuit() == ONE:
                if cnt1 < 2: madeCards.append(card)
                else: remainCards.append(card)
                cnt1 += 1
            elif card.getSuit() == EIGHT:
                if cnt8 < 1: madeCards.append(card)
                else: remainCards.append(card)
                cnt8 += 1
            else: remainCards.append(card)
        point, text = getRemainPoint(remainCards)
        return point, madeCards, remainCards, "콩콩팔(1 1 8) " + text
    else:
        return NULL, NULL, NULL, NULL


def getPoint(cards):
    suitCounts = [0 for i in range(10)]
    for card in cards:
        suitCounts[card.getSuit() - 1] += 1

    point, madeCards, remainCards, text = NULL, NULL, NULL, "노메이드"

    p, m, r, t = getMade118Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade127Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade136Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade145Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade226Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade235Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade334Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade389Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade442Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade479Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade569Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade578Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade668Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade776Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t

    p, m, r, t = getMade884Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    
    p, m, r, t = getMade992Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    
    p, m, r, t = getMade1910Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    
    p, m, r, t = getMade2810Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    
    p, m, r, t = getMade3710Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    
    p, m, r, t = getMade4610Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    
    p, m, r, t = getMade5510Point(cards, suitCounts)
    if point < p: point, madeCards, remainCards, text = p, m, r, t
    return point, madeCards, remainCards, text