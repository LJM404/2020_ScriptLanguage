from dice import *

class Configuration:

    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
    "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
    "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    @staticmethod
    def getConfigs():
        return Configuration.configs

    @staticmethod
    def score(row, d):
        if (row == 0):
            return Configuration.scoreUpper(d, 1)
        elif (row == 1):
            return Configuration.scoreUpper(d, 2)
        elif (row == 2):
            return Configuration.scoreUpper(d, 3)
        elif (row == 3):
            return Configuration.scoreUpper(d, 4)
        elif (row == 4):
            return Configuration.scoreUpper(d, 5)
        elif (row == 5):
            return Configuration.scoreUpper(d, 6)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row == 11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.sumDie(d)

    @staticmethod
    def scoreUpper(d, num):
        numbers = [d[i].getRoll() for i in range(5)]
        return num * numbers.count(num)

    @staticmethod
    def scoreThreeOfAKind(d):
        numbers = [d[i].getRoll() for i in range(5)]
        for num in range(6):
            if numbers.count(num + 1) == 3:
                return sum(numbers)
        return 0

    @staticmethod 
    def scoreFourOfAKind(d):
        numbers = [d[i].getRoll() for i in range(5)]
        for num in range(6):
            if numbers.count(num + 1) == 4:
                return sum(numbers)
        return 0

    @staticmethod
    def scoreFullHouse(d):
        numbers = [d[i].getRoll() for i in range(5)]
        for i in range(6):
            if numbers.count(i + 1) == 3:
                for j in range(6):
                    if numbers.count(j + 1) == 2:
                        return 25
        return 0

    @staticmethod
    def scoreSmallStraight(d):
        numbers = list(set([d[i].getRoll() for i in range(5)]))
        numbers.sort()
        count = 1
        for i in range(1, len(numbers)):
            if (numbers[i - 1] == numbers[i] - 1): count += 1
            else: count = 1
            if (count == 4): return 30
        return 0

    @staticmethod
    def scoreLargeStraight(d):
        numbers = list(set([d[i].getRoll() for i in range(5)]))
        numbers.sort()
        count = 1
        for i in range(1, len(numbers)):
            if (numbers[i - 1] == numbers[i] - 1): count += 1
            else: count = 1
            if (count == 5): return 40
        return 0

    @staticmethod
    def scoreYahtzee(d):
        numbers = [d[i].getRoll() for i in range(5)]
        for num in range(6):
            if numbers.count(num + 1) == 5:
                return 50
        return 0

    @staticmethod
    def sumDie(d):
        return sum([d[i].getRoll() for i in range(5)])