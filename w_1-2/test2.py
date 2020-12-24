print(1 + 3)
print(1 * 5)
print(6 / 2)
print(6 % 4)
print(2 ** 10)
# floor division (버림 나눗셈)
print(7 // 2)

# round (반올림)
print(round(3.141592, 4))

print("코드잇")
print("Hello" * 3)
print("Hello\n" * 3)

print(int("7") + int("5"))
print(str(5) + str(7))
print(float(3.2) + float(2.2))
print(float("2.2") + float("1.2"))

# 오늘은 2019년 10월 29일 입니다.
def a_year(a):
    if a > 12:
        return year + 1
    else:
        return a


year = 2019
month = 5
day = 29
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day + 1))

print("오늘은 {}년 {}월 {}일 입니다.".format(year, str(month).zfill(2), day))
print("오늘은 {}년 {}월 {}일 입니다.".format(year, f'{month:02}', day))
print("오늘은 {0}년 {1}월 {2}일 입니다.".format(year, month, day))


n = 30
print(str(n).zfill(3))
print(f'{n:05}')

print(a_year(15))
