name = input("1~10 사이의 정수를 입력하세요: ")
i = 1
while i <= 1:
    if not (type(int(name))) == int:
        print("입력값이 올바르지 않습니다.")
        name = input("1~10 사이의 정수를 입력하세요")
    if not 1 <= int(name) <= 10:
        print("입력값이 올바르지 않습니다.")
        name = input("1~10 사이의 정수를 입력하세요: ")
    else:
        break

print(int(name))

test = input("아무거나: ")
print(type(test))
print(test)