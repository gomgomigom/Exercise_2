def mask_security_number(security_number):
    blind = security_number[0:-4] + "****"
    return blind


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


def mask_security_number(security_number):
    security_number_list = []
    for i in range(len(security_number)):
        security_number_list.append(security_number[i])
    for i in range(len(security_number_list) - 4, len(security_number_list)):
        security_number_list[i] = "*"
    total_str = ""
    for i in range(len(security_number_list)):
        total_str += security_number_list[i]
    return total_str


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))

num_1 = "252214141511"
print(list(num_1))

unit = ["영어", "공부", "힘들다"]
units_to_string = ' '.join(unit)

print(units_to_string)

def mask_security_number(security_number):
    security_number_list = []
    for i in range(len(security_number)):
        security_number_list.append(security_number[i])
    for i in range(len(security_number_list) - 4, len(security_number_list)):
        security_number_list[i] = "*"
    security_number_list = "".join(security_number_list)
    return security_number_list

print(mask_security_number("8807201234567"))

num_1 = "252214141511"
num_1 = list(num_1)
print(num_1)
print()

def is_palindrome(word):
    list_word = list(word)
    list_reverse = []
    for i in range(int(len(word))):
        list_reverse.append(list_word[-i-1])
    list_reverse = "".join(list_reverse)
    if list_reverse == word:
        return True
    else:
        return False

# 코드를 입력하세요.


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

num_1 = "151641514"
list_num = list(num_1)
reversed_list = list_num[::-1]
print(reversed_list)
print("".join(reversed_list))


import calculator

print(calculator.subtract(5, 2))

import calculator as cal

print(cal.divide(6, 2))

from calculator import multiply

print(multiply(5, 12))

from calculator import *

print(subtract(7, 11))

import os

print(os.getlogin())
print(os.getcwd())

import math

print(math.log(100, 100))

import random

print(random.random())
print(random.randint(1,100))
print(random.randrange(0,11,2))
print(random.uniform(1,2))

import datetime

pi_day = datetime.datetime(2020, 12, 12)
print(pi_day)
print(type(pi_day))
pi_day = datetime.datetime(2020, 12, 12, 9, 8, 11)
print(pi_day)
pi_day = datetime.datetime.now()
print(pi_day)

today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 12, 5)
print(today - pi_day)
print(type(pi_day - today))
time_delta = datetime.timedelta(days=5, hours=3, minutes=1, seconds=21)
print(today - time_delta)
print(type(today - time_delta))

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)
print(today.microsecond)
for i in range(10):
    print(today.microsecond)

print(today.strftime("%A, %B, %a"))

name = input("이름을 입력하세요: ")
print(name)

test = int(input("숫자를 입력하세요: "))
print(test * 4)

name = int(input("1~10 사이의 정수를 입력하세요: "))
i = 1
while i in i <= 1:
    if not 1 <= name <= 10:
        print("입력값이 올바르지 않습니다.")
        name = input("1~10 사이의 정수를 입력하세요: ")
    else:
        break
