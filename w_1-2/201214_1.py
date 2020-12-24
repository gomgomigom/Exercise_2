import random

def count_matching_numbers(list_1, list_2):
    i = 0
    for j in range(len(list_1)):
        if list_1[j] in list_2:
            i += 1

    return i


print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))


def check(numbers_list, winning_number_test):
    i = count_matching_numbers(numbers_list, winning_number_test)
    if i == 6 and numbers_list[0:6] == winning_number_test[0:6]:
        return "600,000,000"
    elif i == 6:
        return "50,000,000"
    elif i == 5:
        return "1,000,000"
    elif i == 4:
        return "50,000"
    elif i == 3:
        return "5,000"
    else:
        return "꽝"

print(check([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))

def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        ran = random.randint(1, 45)
        if ran not in numbers:
            numbers.append(ran)

    return numbers


print(generate_numbers(6))

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

print(draw_winning_numbers())

i = [1, 3, 5, 7]
print(i)
print(i[:1] + i[2:])
print(i[:1])

def count_matching_numbers(list_1, list_2):
    i = 0
    for num in list_1:
        if num in list_2:
            i += 1

    return i


print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))


def count_matching_numbers(list_1, list_2):
    same_numbers = list(set(list_1).intersection(list_2))
    return len(same_numbers)


print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))

def check(numbers_list, winning_number_test):
    i = count_matching_numbers(numbers_list, winning_number_test[:6])
    bonus_count = count_matching_numbers(numbers_list, winning_number_test[6:])
    if i == 6:
        return "600,000,000"
    elif i == 5 and bonus_count == 1:
        return "50,000,000"
    elif i == 5:
        return "1,000,000"
    elif i == 4:
        return "50,000"
    elif i == 3:
        return "5,000"
    else:
        return "꽝"


print(check([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
