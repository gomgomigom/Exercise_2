# 이미지를 파일에서 읽어오는 함수
def read_image(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])
    return img

def read_img(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])