# # utils 모듈의 'read_image' 함수와 'display' 함수를 임포트해 주세요
# from cil.utils import read_image, display
# # processing 모듈의 'invert' 함수를 'inv'로 임포트하고 'merge' 함수를 'mrg'로 임포트해 주세요
# from cil.processing import invert as inv
# from cil.processing import merge as mrg
#
# logo = read_image('codeit_logo')
# inverted_logo = inv(logo)
# merged_img = mrg(logo, inverted_logo)
#
# print('원본 이미지:')
# display(logo)
# print('\n색상 반전 이미지:')
# display(inverted_logo)
# print('\n합성 이미지:')
# display(merged_img)
#
# # 채점 코드
# print()
# dir_list = dir()
# key_names = ['read_image', 'display', 'inv', 'mrg']
# print(all(x in dir_list for x in key_names))
# print('save_image' not in dir_list)


import cil


logo = cil.read_image('codeit_logo')
text = cil.read_image('codeit_text')

print('코드잇 로고:')
# logo를 디스플래이해 주세요
cil.display(logo)
### 코드를 작성해 주세요 ###
print('\n코드잇 텍스트:')
cil.display(text)
# text를 디스플래이해 주세요
### 코드를 작성해 주세요 ###

# text를 색상 반전해서 inverted_text에 저장해 주세요
cil.save_image(cil.invert(text), 'inverted_text')
### 코드를 작성해 주세요 ###
# logo와 text를 합성한 이미지를 merged_img에 저장해 주세요
cil.save_image(cil.merge(logo, text), 'merged_img')
### 코드를 작성해 주세요 ###

print('\n색상 반전 텍스트:')
# inverted_text를 디스플래이해 주세요
cil.display(cil.read_image('inverted_text'))
### 코드를 작성해 주세요 ###
print('\n합성 이미지:')
cil.display(cil.read_image('merged_img'))
# merged_img를 디스플래이해 주세요
### 코드를 작성해 주세요 ###

# 채점 코드
print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(cil) for x in key_functions))
print(not any(x in dir(cil) for x in non_key_functions))