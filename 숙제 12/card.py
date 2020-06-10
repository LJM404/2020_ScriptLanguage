import copy

NULL = 0
ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING = range(1, 14)
CLUBS, HEARTS, DIAMONDS, SPADES = range(1, 5)
SUITS = ["NULL", "Clubs", "Hearts", "Diamonds", "Spades"]

class Card:
    def __init__(self, num):
        self.value = num % 13 + 1
        self.suit = num // 13 + 1

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def filename(self):
        return SUITS[self.suit] + str(self.value) + ".png"


RoyalStraightFlush = 10 ** 13
BackStraightFlush  = 10 ** 12
StraightFlush      = 10 ** 11
FourCard           = 10 ** 10
FullHouse          = 10 **  9
Flush              = 10 **  8
Mountine           = 10 **  7
BackStraight       = 10 **  6
Straight           = 10 **  5
Triple             = 10 **  4
TwoPair            = 10 **  3
OnePair            = 10 **  2
NoPair             = 10 **  1


def getNoPair(cards):
    noPairValue = 0
    for card in cards:
        if card.getValue() == ACE:
            return ACE
        elif card.getValue() > noPairValue:
            noPairValue = card.getValue()
    return noPairValue


# One Pair: 같은 숫자의 카드가 2장인 패
# One Pair가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 가장 높은 우선순위의 숫자를 반환합니다.
def checkOnePair(cards):
    onePairValue = NULL
    for value in range(ACE, KING + 1):
        count = 0
        for card in cards:
            if card.getValue() == value:
                count += 1
        if 2 <= count:
            if value == ACE:
                return ACE
            elif onePairValue < value:
                onePairValue = value
    return onePairValue

# Two Pair: 같은 숫자의 카드가 2장과 또다른 같은 숫자의 카드가 2장인 패
# Two Pair가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 가장 높은 우선순위의 두 숫자를 반환합니다.
def checkTwoPair(cards):
    onePairValue = checkOnePair(cards)
    if onePairValue == NULL:
        return NULL, NULL
    newCards = []
    for card in cards:
        if card.getValue() != onePairValue:
            newCards.append(card)
    twoPairValue = checkOnePair(newCards)
    if twoPairValue == NULL:
        return NULL, NULL
    return onePairValue, twoPairValue

# Triple: 같은 숫자의 카드가 3장인 패
# Triple이 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 가장 높은 우선순위의 숫자를 반환합니다.
def checkTriple(cards):
    tripleValue = NULL
    for value in range(ACE, KING + 1):
        count = 0
        for card in cards:
            if card.getValue() == value:
                count += 1
        if 3 <= count:
            if value == ACE:
                return ACE
            elif tripleValue < value:
                tripleValue = value
    return tripleValue

# Straight: 카드의 숫자가 5장 연속되는 패
# Straight가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 첫번째 숫자를 반환합니다.
def checkStraight(cards):
    straightValue = NULL
    cardList = copy.deepcopy(cards)
    cardList.sort(key=lambda card: card.getValue())

    count = 0
    prevValue = 0
    for card in cardList:
        if card.getValue() == (prevValue + 1):
            prevValue = card.getValue()
            count += 1
        elif card.getValue() != prevValue:
            prevValue = card.getValue()
            count = 1
        
        if count >= 5:
            straightValue = prevValue - 4
    return straightValue

# Back Straight: 카드의 숫자 A, 2, 3, 4, 5가 연속되는 패
# Back Straight가 되는 카드가 없으면 NULL을 반환, 있으면 ACE를 반환합니다.
def checkBackStraight(cards):
    cardList = copy.deepcopy(cards)
    cardList.sort(key=lambda card: card.getValue())

    count = 0
    prevValue = 0
    for card in cardList:
        if card.getValue() == (prevValue + 1):
            prevValue = card.getValue()
            count += 1
        elif card.getValue() != prevValue:
            prevValue = card.getValue()
            count = 1
        
        if count >= 5:
            if (prevValue - 4) == ACE:
                return ACE
            else:
                return NULL
    return NULL


# Flush: 같은 무늬가 3장인 패
# Flush가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 무늬를 반환합니다.
def checkFlush(cards):
    flushSuit = NULL
    for suit in range(CLUBS, SPADES + 1):
        count = 0
        for card in cards:
            if card.getSuit() == suit:
                count += 1
        if (3 <= count) and (flushSuit < suit):
            flushSuit = suit
    return flushSuit

# Full House: 같은 숫자의 카드가 3장, 또다른 같은 숫자의 카드가 2장인 패
# Full House가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 가장 높은 우선순위의 두 숫자를 반환합니다.
def checkFullHouse(cards):
    tripleValue = checkTriple(cards)
    if tripleValue == NULL:
        return NULL, NULL
    newCards = []
    for card in cards:
        if card.getValue() != tripleValue:
            newCards.append(card)
    onePairValue = checkOnePair(newCards)
    if onePairValue == NULL:
        return NULL, NULL
    return tripleValue, onePairValue

# Four Card: 같은 숫자의 카드가 4장인 패
# Four Card가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 가장 높은 우선순위의 두 숫자를 반환합니다.
def checkFourCard(cards):
    fourCardValue = NULL
    for value in range(ACE, KING + 1):
        count = 0
        for card in cards:
            if card.getValue() == value:
                count += 1
        if 4 <= count:
            if value == ACE:
                fourCardValue = ACE
                break
            elif fourCardValue < value:
                fourCardValue = value
    
    if fourCardValue == NULL:
        return NULL, NULL

    newCards = []
    for card in cards:
        if card.getValue() != fourCardValue:
            newCards.append(card)
    return fourCardValue, max(newCards, key=lambda card: card.getValue()).getValue()

# Straight Flush: 무늬가 같은 카드의 숫자가 5장 연속되는 패
# Straight Flush가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 무늬와 첫번째 숫자를 반환합니다.
def checkStraightFlush(cards):
    straightFlushSuit = NULL
    straightFlushValue = NULL
    for suit in range(CLUBS, SPADES + 1):
        newCards = []
        for card in cards:
            if card.getSuit() == suit:
                newCards.append(card)
        straightValue = checkStraight(newCards)
        if straightFlushValue < straightValue:
            straightFlushSuit = suit
            straightFlushValue = straightValue
    return straightFlushSuit, straightFlushValue

# Back Straight Flush: 무늬가 같은 카드의 숫자 A, 2, 3, 4, 5가 연속되는 패
# Back Straight Flush가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 무늬와 ACE를 반환합니다.
def checkBackStraightFlush(cards):
    backStraightFlushSuit = NULL
    backStraightFlushValue = NULL
    for suit in range(CLUBS, SPADES + 1):
        newCards = []
        for card in cards:
            if card.getSuit() == suit:
                newCards.append(card)
        backStraightValue = checkBackStraight(newCards)
        if backStraightValue == ACE:
            backStraightFlushSuit = suit
            backStraightFlushValue = ACE
    return backStraightFlushSuit, backStraightFlushValue

# Royal Straight Flush: 무늬가 같은 카드의 숫자 10, J, Q, K, A가 연달아 있는 패
# Royal Straight Flush가 되는 카드가 없으면 NULL을 반환, 있으면 해당 카드의 무늬와 ACE를 반환합니다.
def checkRoyalStraightFlush(cards):
    royalStraightFlushSuit = NULL
    royalStraightFlushValue = NULL
    for suit in range(CLUBS, SPADES + 1):
        newCards = []
        for card in cards:
            if card.getSuit() == suit:
                newCards.append(card)
        count = 0
        for card in newCards:
            if card.getValue() == TEN:
                count += 1
            elif card.getValue() == JACK:
                count += 1
            elif card.getValue() == QUEEN:
                count += 1
            elif card.getValue() == KING:
                count += 1
            elif card.getValue() == ACE:
                count += 1
        if count == 5:
            royalStraightFlushSuit = suit
            royalStraightFlushValue = ACE
    return royalStraightFlushSuit, royalStraightFlushValue


def getPoint(cards):
    suit, value = checkRoyalStraightFlush(cards)
    if (suit != NULL) and (value != NULL):
        return RoyalStraightFlush + suit, "Royal Straight Flush"

    suit, value = checkBackStraightFlush(cards)
    if (suit != NULL) and (value != NULL):
        return BackStraightFlush + suit, "Back Straight Flush"
    
    suit, value = checkStraightFlush(cards)
    if (suit != NULL) and (value != NULL):
        return StraightFlush + suit * 100 + value, "Straight Flush"

    value, remain = checkFourCard(cards)
    if (value != NULL) and (remain != NULL):
        if value == ACE: value += KING
        if remain == ACE: remain += KING
        return FourCard + value * 100 + remain, "Four Card"
    
    triple, pair = checkFullHouse(cards)
    if (triple != NULL) and (pair != NULL):
        if triple == ACE: triple += KING
        if pair == ACE: pair += KING
        return FullHouse + triple * 100 + pair, "Full House"

    suit = checkFlush(cards)
    if suit != NULL:
        return Flush + suit, "Flush"

    value = checkBackStraight(cards)
    if value != NULL:
        return BackStraight, "Back Straight"

    value = checkStraight(cards)
    if value != NULL:
        return Straight + value, "Straight"

    value = checkTriple(cards)
    if value != NULL:
        if value == ACE: value += KING
        return Triple + value, "Triple"

    one, two = checkTwoPair(cards)
    if (one != NULL) and (two != NULL):
        if one == ACE: one += KING
        if two == ACE: two += KING
        return TwoPair + max(one, two), "Two Pair"

    value = checkOnePair(cards)
    if value != NULL:
        if value == ACE: value += KING
        return OnePair + value, "One Pair"

    return getNoPair(cards), "No Pair"