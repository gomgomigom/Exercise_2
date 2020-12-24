from random import randint

print("\n\n규칙\n컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. \n\n"
      "예를 들어서 컴퓨터가 5, 2, 3을 뽑을 수도 있고 6, 7, 4를 뽑을 수도 있는 거죠.\n\n"
      "사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야 합니다.\n\n"
      "컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.\n\n"
      "숫자의 값과 위치가 모두 일치하면 S입니다.\n\n숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.\n\n"
      "예를 들어 컴퓨터가 1, 2, 3을 뽑았다고 가정합시다. \n\n"
      "사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.\n\n"
      "기회는 무제한입니다. 하지만 몇 번의 시도 끝에 맞췄는지 기록됩니다.\n\n"
      "3S(숫자 3개의 값과 위치를 모두 맞춘 경우)가 나오면 게임이 끝납니다.\n\n")


def com_numbers_select():
    numbers_com = []
    while len(numbers_com) < 3:
        strike_number = randint(0, 9)
        if strike_number not in numbers_com:
            numbers_com.append(strike_number)

    return numbers_com

numbers_com = com_numbers_select()
print(numbers_com)
print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")


def user_numbers_select():
    numbers_user = []
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    while True:
        user_1 = int(input("1번째 숫자를 입력하세요: "))
        if user_1 not in range(10):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            numbers_user.append(user_1)
            break

    while True:
        user_2 = int(input("2번째 숫자를 입력하세요: "))
        if user_2 not in range(10):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif user_2 in numbers_user:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            numbers_user.append(user_2)
            break

    while True:
        user_3 = int(input("3번째 숫자를 입력하세요: "))
        if user_3 not in range(10):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif user_3 in numbers_user:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            numbers_user.append(user_3)
            break

    return numbers_user


def decipher():
    s = 0
    i = 0
    for num in numbers_com:
        if num == numbers_user[i]:
            s += 1
        i += 1

    b = 0
    i = 0
    while i < 3:
        if numbers_user[i] in numbers_com:
            b += 1
        i += 1

    return print(f"{s}S {b - s}B\n")


count = 1
while True:
    numbers_user = user_numbers_select()
    s = 0
    i = 0
    for num in numbers_com:
        if num == numbers_user[i]:
            s += 1
        i += 1

    b = 0
    i = 0
    while i < 3:
        if numbers_user[i] in numbers_com:
            b += 1
        i += 1

    print(f"{s}S {b - s}B\n")

    if s != 3:
        count += 1

    else:
        print(f'축하합니다. {count}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.')
        break

end = input("\nEnter를 누르면 종료됩니다.")
