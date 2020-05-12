class Player:
    UPPER = 6 # upper category 6개
    LOWER = 7 # lower category 7개
    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER + self.LOWER)] # 13개 category 점수
        self.used = [False for i in range(self.UPPER + self.LOWER)] # 13개 category 사용 여부

    def setScore(self, score, index):
        self.scores[index] = score

    def setAtUsed(self, index):
        self.used[index] = True

    def getUpperScore(self):
        score = 0
        for i in range(0, self.UPPER):
            score += self.scores[i]
        return score

    def getLowerScore(self):
        score = 0
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            score += self.scores[i]
        return score

    def getUsed(self):
        return self.used

    def toString(self):
        return self.name

    def allLowerUsed(self): # lower category 7개 모두 사용되었는가?
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            if (self.used[i] == False):
                return False
        return True

    def allUpperUsed(self): # upper category 6개 모두 사용되었는가?
        for i in range(0, self.UPPER):
            if (self.used[i] == False):
                return False
        return True