# 사전 (dictionary)
# key - value pair (키 - 값 쌍)
my_dictionary = {
    'ps4': 'mhw',
    'switch': 'animal'
}
print(type(my_dictionary))

print((my_dictionary['ps4']))

my_dictionary[9] = 11
print(my_dictionary)

my_family = {
    '아빠': '123',
    '엄마': '456',
    '형': '789',
    '나': '1011',
    '아내': '1213'
}

print(my_family)
print(my_family['아내'])
my_dictionary[9] = 15
print(my_dictionary)
my_dictionary[3] = [3, 4, 5, 6]
print(my_dictionary)
print(my_dictionary[3])

for i in range(len(my_dictionary[3])):
    print(i)



# 1. 단어장 만들기
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)


# 2. 새로운 단어들 추가
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)

print(vocab.values())
print('문명' in vocab.values())

for value in vocab.values():
    print(value)

for key in vocab.keys():
    value = vocab[key]
    print(key, value)

for key, value in vocab.items():
    print(key, value)

vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
    }
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    for key, value in vocab.items():
        new_dict[value] = key
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
    }

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

print(range(len(vocab)))

print(my_dictionary)
print(my_family.keys())
