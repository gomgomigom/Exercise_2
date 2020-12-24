numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers.reverse()
print(numbers)

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for left in range(int((len(numbers))/2)):
    right = len(numbers) - left - 1
    numbers[right], numbers[left] = numbers[left], numbers[right]
    print(numbers)

print("뒤집어진 리스트: " + str(numbers))