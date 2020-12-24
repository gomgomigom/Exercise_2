
with open('test_text.txt', 'r', encoding='UTF=8') as f:
    print(type(f))
    for line in f:
        print(line.strip())

# split

my_string = "1, 2, 3, 4, 5, 6, 7"
print(my_string.split(", "))

full_name = "Hong, GilDong"
print(full_name.split(', '))
print(full_name)
full_name = full_name.split(', ')
print(full_name)
first_name = full_name[1]
last_name = full_name[0]

print(first_name, last_name)

numbers = "           \n   \n  \t  2  \n  \t   5         \n 4 5 2 21  \n   ".split()
print(numbers)
print(numbers[0] + numbers[1])
print(int(numbers[0]) + int(numbers[1]))
print(numbers)

my_string = "1, 2, 3, 4, 5, 6, 7"
print(my_string)

with open('test_text.txt', 'r', encoding='UTF=8') as f:
    print(type(f))
    print(f)

