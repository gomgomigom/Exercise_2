i = 1
while i <= 9:
    i_1 = 1
    while i_1 <= 9:
        print(f"{i} * {i_1} = {i * i_1}")
        i_1 += 1
    i += 1


i = 100
while True:
    if i % 23 == 0:
        break
    i += 1

print(i)


i = 0
while i < 7:
    i += 1
    if i % 2 !=0:
        continue
    print(i)

i = 100
while i >= 100:
    i += 1
    if i % 123 == 0:
        break

print(i)

# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 14]
names = ["가위", "바위", "보", "참새", "쨱짹"]

print(numbers[5])
print(numbers)
print(names)
print(names[-2])
num_1 = numbers[3]
print()
print(num_1)
print(numbers[1:2])
print(numbers[2:-1])
print(numbers[3:])

new_list = names[-2:6]
print(new_list)

numbers[2] = numbers[1] + numbers[-1]
print(numbers)

print('---')
numbers = [1, 3 ,4, 5, 31, 14, 13]
numbers.append(211)
print(numbers)
del numbers[1:3]
print(numbers)
print(len(numbers))
numbers.insert(-1, 5515)
print(numbers)
print('---')
numbers.insert(2, 1111)
print(numbers)
numbers.extend([1,3,4])
print(numbers)
print(len(numbers))
print()
new_num = sorted(numbers)
print(new_num)
new_num = sorted(new_num, reverse=True)
print(new_num)
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print('---')

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

# 코드를 작성하세요.
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1


# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

celsius_list = []
i = 0
while i < len(temperature_list):
    celsius_list.append(round(fahrenheit_to_celsius(temperature_list[i]),1))
    i += 1

print("섭씨 온도 리스트: " + str(celsius_list))  # 섭씨 온도 출력

print(fahrenheit_to_celsius(temperature_list[1]))

while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]),1)
    i += 1

print("섭씨 온도 리스트: " + str(temperature_list))

