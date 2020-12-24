x = 2


def t_1():
    global x
    x += 1
    print(x)


print(x)
t_1()
t_1()
x = 2


def t_2(x):
    x += 1
    return x


print(t_2(x))
print(t_2(x))

print("---------------")
x = 3


def t_3():
    print(x)


t_3()

PI = 3.14


def calculate_circle(r):
    return PI * r * r


r = 3
print(f"반지름이 {r}인 원의 넓이는 {calculate_circle(r):.2f}이다.")

r = 6
print("반지름이 {}이면, 넓이는 {:.2f}이다.".format(r, calculate_circle(r)))

r = 7
print(f"반지름이 {r}이면, 원의 넓이는 {calculate_circle(r):.2f}이다.")


def calculate_circle_p(r):
    print(f"반지름이 {r}이면, 원의 넓이는 {PI * r * r}이다.")


calculate_circle_p(11)


def is_evenly_divisible(number):
    return number % 2 == 0


print(is_evenly_divisible(2))

print(2 % 2 == 0)


def calculate_change(payment, cost):
    change = payment - cost  # 코드를 작성하세요.
    print(f"50000원 지폐: {int(change / 50000)}장")
    print(f"10000원 지폐: {int((change % 50000 / 10000))}장")
    print(f"5000원 지폐: {int((change % 50000 % 10000) / 5000)}장")
    print(f"1000원 지폐: {int((change % 50000 % 10000 % 5000) / 1000)}장")


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

print(42425 // 2000)


def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = change % 50000 // 10000  # 10,000원 지폐
    five_count = change % 10000 // 5000  # 5,000원 지폐
    one_count = change % 5000 // 1000  # 1,000원 지폐

    print(f"50000원 지폐: {fifty_count}장")
    print(f"10000원 지폐: {ten_count}장")
    print(f"5000원 지폐: {five_count}장")
    print(f"1000원 지폐: {one_count}장")


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

num_1 = 1

while num_1 < 3:
    num_1 += 1
    if num_1 >= 1:
        print("반복중 입니다")
    if num_1 >= 3:
        print("종료 합니다")

num_1 = 1
while num_1 <= 3:
    print("반복")
    num_1 += 1

num_1 = 1
while num_1 <= 2:
    num_1 += 1
    if num_1 <= 2:
        print("반복?")

num_1 = 1
while num_1 <= 2:
    if num_1 <= 2:
        print("반복!")
    num_1 += 1


even_number = 2
while even_number <= 100:
    print(even_number)
    even_number += 2

i = 100

while not i % 23 == 0:
    i += 1
    if i % 23 == 0:
        print(i)

print(115 % 23)


def print_grade(midterm_score, final_score):
    total = midterm_score + final_score  # 합산 점수

    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1

#  10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
#  while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.

i = 1
total = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)

i = 1
total = 0
while i <= 10:
    total += i
    i += 1

print(total)


i = 1
count = 0
while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print(count)


i = 1
count = 0
while i <= 120:
    if 120 % i == 0:
        count += 1
    i += 1

print(count)

i = 10
x = 10
y = 0.5
print("---")
while i <= 20:
    x *= y
    i += 1

