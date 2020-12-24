total = 0
day = 0
with open('chicken.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])
        total += revenue
        day += 1
    print(total / day)

with open('new_file.txt', 'w') as g:
    g.write('Hello World\n')
    g.write('My name is...\n')


with open('vocabulary.txt', 'a', encoding='UTF-8') as h:
    i = 0
    while i == 0:
        word_en = input("영어 단어를 입력하세요: ")
        if word_en == "q":
            break
        word_kor = input("한국어 뜻을 입력하세요: ")
        h.write(f"{word_en}: {word_kor}\n")

