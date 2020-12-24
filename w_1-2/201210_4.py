# numbers라는 빈 리스트를 만들고 리스트를 출력한다.
# append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
# numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
# numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
# numbers 리스트를 정렬한 후 출력한다.

# 빈 리스트 만들기
numbers = []
print(numbers)

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)


# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
        i -= 1
    i += 1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)
print(type(numbers))

for num in numbers:
    print(num)

for x in range(2, 10, 2):
    print(x)

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

print(range(len(numbers)))

for num in range(len(numbers)):
    print(f"{num} {numbers[num]}")

print(1,2)
print(1, 2)

for i in range(1,11):
    print(f'2^{i} = {2 ** i}')

i = 1
while i <= 10:
    print(f'2^{i} = {2 ** i}')
    i += 1

for i in range(11):
    print("2^{} = {}".format(i, 2 ** i))

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

i = 1
while i < 10:
    j = 1
    while j < 10:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1

for i in range(1,10):
  if i < 10 :
    a = 1
    print("{} * {} = {}".format(a, i, a * i))
    print("if문이 실행!")
  else :
    a += 1
    i = 1
    print("else문이 실행!")


for a in range(1,1001):
    for b in range(a,1001):
       c = 1000 - a - b
       if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000 and a < b < c:
           print(a * b * c)
print("완료")

