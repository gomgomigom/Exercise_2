# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

kyj = 0
ksk = 0
cms = 0
for name in votes:
    if name == "김영자":
         kyj += 1
    elif name == "강승기":
         ksk += 1
    elif name == "최만수":
        cms += 1

vote_counter = {}
vote_counter['김영자'] = kyj
vote_counter['강승기'] = ksk
vote_counter['최만수'] = cms

print(vote_counter)
print(ksk)
print(kyj)
print(cms)
print(ksk + kyj + cms)
print(len(votes))

vote_counter_complete = {}

for name in votes:
    if name not in vote_counter_complete:
        vote_counter_complete[name] = 1
    else:
        vote_counter_complete[name] += 1

print(vote_counter_complete)

x = 5
y = x
y = 2
print(x)
print(y)

x = [2, 3, 5, 7, 11]
y = x
y[2] = 22
print(x)
print(y)

y = list(x)
y[2] = 78
print(x)
print(y)

alphabet_string = 'ABCDEFG'

print(alphabet_string[0:2])
print(alphabet_string[3:])
print(alphabet_string[:2])
print(alphabet_string[-2])

alphabet_list = ["A", "B", "C", "D", "E", "F", "G"]

print(alphabet_list[0:2])
print(alphabet_list[3:])
print(alphabet_list[:2])
print(alphabet_list[-2])

my_list = [2, 3, 5, 3, 2]

print(len(my_list))

my_string = "Hello World!"

print(len(my_string))

numbers = [1, 4, 5, 3, 22]
numbers[2] = 77
print(numbers)

name = 'codeit'
# name[0] = 'C' 문자열은 리스트와 달리 수정 안됨
print(name)

list_1 = [1, 3, 4, 3]
list_2 = [2, 3, 3, 1]
list_3 = list_1 + list_2
list_2 = list_1 + list_2
print(list_3)
print(list_2)

string_1 = "123"
string_2 = "456"
string_3 = string_1 + string_2
print(string_3)