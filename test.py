x = [
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 1]
]

def get_size(img):
    return [len(img),len(img[0])]

print(get_size(x))
height, width = get_size(x)
print(height)
print(width)

def empty_image(height, width):
    new_img = []
    for i in range(height):
        new_img.append([int(-1) for j in range(width)])
    return new_img

print(empty_image(height, width))


def horizontal_flip(img):
    height, width = get_size(img)
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = img[i][-j-1]
    return new_img

print(horizontal_flip(x))

def vertical_flip(img):
    height, width = get_size(img)
    new_img = empty_image(height, width)
    for i in range(height):
        new_img[i] = img[-i-1]
    return new_img

def display(img):
    height, width = get_size(img)
    for i in range(height):
        for j in range(width):
            print(img[i][j], end=' ')
        print()

print(x)
print(vertical_flip(x))

display(x)
print()
display(vertical_flip(x))