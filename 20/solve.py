def read_pares():
    with open("./input") as f:
        f = f.read()
        algo, img = f.split("\n\n")
        img = list(map(list, img.splitlines()))
        for i in range(len(img)):
            for j in range(len(img[0])):
                img[i][j] = to_int(img[i][j])
        return algo, img


def to_int(s):
    if s == "#":
        return 1
    if s == ".":
        return 0


def print_m(img):
    print("-----")
    for line in img:
        temp = []
        for d in line:
            if d == 1:
                temp.append("#")
            if d == 0:
                temp.append(".")

        print("".join(temp))
    print("-----")


def wrap(img):
    for i in range(len(img)):
        img[i].insert(0, 0)
        img[i].append(0)
    img.insert(0, [0 for _ in range(len(img[0]))])
    img.append([0 for _ in range(len(img[0]))])
    return img


def wrap1(img):
    for i in range(len(img)):
        img[i] = [0] + img[i] + [0]
    blank_line = [0 for _ in range(len(img) + 2)]
    img = [blank_line[:]] + img + [blank_line[:]]
    return img


def bi_to_dec(bi):
    sum = 0
    for i, n in enumerate(bi[::-1]):
        sum += (2 ** i) * n
    return sum


def read_algo(algo, code):
    sum = bi_to_dec(code)
    pix = algo[sum]
    if pix == ".":
        return 0
    else:
        return 1


def eval_pixel(img, y, x):
    temp = []
    temp.append(img[y - 1][x - 1])
    temp.append(img[y - 1][x])
    temp.append(img[y - 1][x + 1])
    temp.append(img[y][x - 1])
    temp.append(img[y][x])
    temp.append(img[y][x + 1])
    temp.append(img[y + 1][x - 1])
    temp.append(img[y + 1][x])
    temp.append(img[y + 1][x + 1])

    return temp


def count_dot(img):
    sum = 0
    for i in img:
        for j in i:
            sum += j
    print("sum", sum)


def enchanc(img1, algo):

    # print_m(img)

    img1 = wrap(img1)
    print(len(img1), len(img1[0]))
    # temp = [[0] * len(img1) for _ in range(len(img1))]
    temp = [[0 for i in range(len(img1))] for j in range(len(img1))]
    # temp = list(list(0 for i in range(len(img1))) for j in range(len(img1[0])))

    for i in range(1, len(img1) - 1):
        for j in range(1, len(img1[0]) - 1):
            code = eval_pixel(img1, i, j)
            pix = read_algo(algo, code)
            assert len(algo) == 512
            temp[i][j] = pix

    # print_m(temp)

    return temp


def cut(img):
    for i in range(len(img)):
        img[i] = img[i][5:-5]
    img = img[5:-5]
    return img


def main():
    algo, img = read_pares()
    print(algo)
    print_m(img)
    for _ in range(50):
        img = wrap(img)

    for i in range(50):

        img = enchanc(img, algo)
        print_m(img)
        if i % 2 == 1:
            img = cut(img)
            for _ in range(5):
                img = wrap(img)
        print_m(img)
        count_dot(img)
        # img = wrap1(img)

    img = cut(img)
    count_dot(img)
    # img[0][0] = 1
    # print_m(img)

    # img = enchanc(img, algo)
    # print_m(img)
    # img = enchanc(img, algo)
    # print_m(img)
    # print(img)

    # for i,y in enumerate(img):
    #     for j,x in enumerate(x):


main()
