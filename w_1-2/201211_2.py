# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    for i in range(len(num)):
        digit = str_num[i]
        total += int(digit)
    return total

print(sum_digit('255'))

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기

def sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in range(len(str(num))):
        total += int(str_num[digit])

    return total

total = 0

for i in range(1,1001):
    total += sum_digit(i)

print(total)


def sum_digit(num):
    total = 0
    num_str = str(num)

    for digit in range(len(num_str)):
        total += int(num_str[digit])

    return total

print(sum_digit(1252))

total_digit = 0

for i in range(1,1001):
    total_digit += sum_digit(i)

print(total_digit)


