with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(": ")
        answer = input(f"{data[0]}: ")
        if answer == data[1]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {data[1]}입니다.")