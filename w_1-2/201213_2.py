
with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    dic = {}
    for line in f:
        data = line.strip().split(": ")
        dic[data[0]] = data[1]
        import random
    keys = list(dic.keys())


    while True:
        index = random.randint(0, len(keys) - 1)
        word_en = keys[index]
        word_kor = dic[word_en]
        answer = input(f'{word_kor}: ')
        if answer == word_en:
            print('맞았습니다!\n')
        elif answer == "q":
            break
        else:
            print(f'틀렸습니다. 정답은 {word_en}입니다.\n')

