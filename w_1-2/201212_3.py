import random

guess = -1
ANSWER = random.randint(1,20)
NUM_TRIES = 4
tries = 0

while guess != ANSWER and NUM_TRIES > tries:
    guess = int(input(f"기회가 {NUM_TRIES - tries}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    tries += 1

    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")
if guess == ANSWER:
    print(f"축하합니다. {tries}번 만에 숫자를 맞히셨습니다.")
else:
    print(f"아쉽습니다. 정답은 {ANSWER}입니다.")

