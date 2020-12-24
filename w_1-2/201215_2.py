
def take_guess():
    new_guess = []
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    while len(new_guess) < 3:
            new_num = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: "))
        if new_num not in range(10):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess

take_guess()

