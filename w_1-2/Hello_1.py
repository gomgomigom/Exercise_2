year = 1988
money = 50000000
interest_rate = 0.12
apart = 1100000000

while year < 2016:
    money = money + money*interest_rate
    year += 1

if money - apart > 0:
    print(f"{int(money - apart)}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(apart - money))
