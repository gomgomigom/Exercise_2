# type 함수
print(type(3))
print(type(3.0))
print(type("3"))
print(type(print))

def xx():
    print("Hello World")

print(type(xx))
print(type(True))
print(type(print(3>1)))
print(type(3>1))

print(3>1)

print(int(3.5))
print(int(str(1) + str(2)))
print(type(4 / 2))

x = 5
x = x - 2
print(x)
x = 6
print(x)
x = x - 11
print(x)

def square(x):
    return x * x
print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

# return문의 역할 : 함수 즉시 종료하기, 값 돌려주기

def test_return(x):
    print("함수 호출 전")
    return x * x
    print("함수 호출 후") # dead code : return문에서 함수가 즉시 종료되기 때문

print(test_return(3))

print("-----------")
def get(x):
    print (x ** 3)
    return x ** 2

print(get(3))
print("---------------")
def test_return_1(x):
    return round(x, 1)

print(test_return_1(2.322))
print("---------------------------")

def function_print():
    print("I printed")

x1 = function_print

function_print()

x1()

def myself(name, age = "17", nationality = "한국"):
    print("내 이름은 {0}\n나이는 {1}살\n국적은 {2}".format(name, age, nationality))

myself("가나다")
print()
myself("가나", 11, "미국")

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
print(f"{num_1} 나누기 {num_2}은 {(num_1 / num_2):.2f}입니다")

n = 1
print(n)
print(f'{n:02}')
print(str(n).zfill(2))

print("-------------")

x = 5
print(x)
x /= 2
print(x)
x += 5
print(x)
x %= 4
print(int(x))
x *= 2
print(int(x))

def myself_1(name, age =  "11", nationally = "일본"):
    print("안녕하세요 제 이름은 {}\n나이는 {}살\n출생지는 {}입니다".format(name, age, nationally))

myself_1("개동", 12, "한국")
print()
def myself_2(name, age =  "11", nationally = "일본"):
    print(f"안녕하세요 제 이름은 {name}\n나이는 {age}살\n출생지는 {nationally}입니다")

myself_2("개동개")

n_1 = 1
n_2 = 2
print(f"{n_1}더하기 {n_2}는 {n_1 + n_2}이다.")

f = 2
print(f)
print("안녕")

