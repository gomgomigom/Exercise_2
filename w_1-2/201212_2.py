import random

i = 4
correct_answer = random.randint(1,20)
while i > 0:
    digit = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    i -= 1
    if digit == correct_answer:
        victory = 4 - i
        print(f"축하합니다 {victory}번 만에 숫자를 맞히셨습니다.")
        break
    elif digit < correct_answer:
        print("Up")
    elif digit > correct_answer:
        print("Down")
    if i == 0:
        print(f"아쉽습니다. 정답은 {correct_answer}입니다.")
        break



