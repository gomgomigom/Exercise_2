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
# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(celsius_list))  # 섭씨 온도 출력

print(fahrenheit_to_celsius(temperature_list[1]))
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1


print("섭씨 온도 리스트: " + str(temperature_list))


# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000



# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 1000 / 8



# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))

# amounts를 원화(￦)에서 달러($)로 변환하기
i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i += 1


# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
i = 0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))

# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000



# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 1000 / 8



# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))

i = 0
j = 0
while i < len(amounts):
    while j < len(amounts):
        amounts[j] = krw_to_usd(amounts[j])
        j += 1
    amounts[i] = usd_to_jpy(amounts[i])
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))


