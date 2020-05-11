import random

# 원하는 단어를 넣으세요
words = ["write", "program", "that", "teacher", "student", "korea", "hangman"]

run = True
while run:
    word = words[random.randint(0, len(words) - 1)]
    result = ['*' for n in range(len(word))]
    failure_count = 0

    while word != ''.join(result):
        c = input("단어 %s 에 포함되는 문자를 입력하세요 > " % ''.join(result))

        if c in result:
            print("%s 은/는 이미 포함되어 있습니다." % (c))
        else:
            if c in word:
                for i in range(len(word)):
                    if c == word[i]:
                        result[i] = c
            else:
                print("%s 은/는 포함되어 있지 않습니다." % (c))
                failure_count += 1

    print("정답은 %s 입니다. %d 번 실패했습니다." % (word, failure_count))
    print()

    while True:
        c = input("다른 단어 맞추기를 하시겠습니까? y또는 n을 입력하세요. > ")
        if c == 'n' or c == 'N':
            run = False
            break
        elif c == 'y' or c == 'Y':
            run = True
            break