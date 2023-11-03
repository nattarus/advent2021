def read():
    with open("./input") as f:
        f = f.read()
        f = f.splitlines()
        f = map(list, f)
        f = list(f)
        return f


def print_c(sea):
    print("-------")
    for line in sea:
        print("".join(line))
    print("-------")


def get_e_cu(sea):
    w = len(sea[0]) - 1
    temp = {}
    for i, x in enumerate(sea):
        for j, y in enumerate(x):
            if y == ">":
                if j == w:
                    if sea[i][0] == ".":
                        temp[(i, j)] = (i, 0)
                else:
                    if sea[i][j + 1] == ".":
                        temp[(i, j)] = (i, j + 1)

    return temp


def get_s_cu(sea):
    h = len(sea) - 1
    temp = {}
    for i, x in enumerate(sea):
        for j, y in enumerate(x):
            if y == "v":
                if i == h:
                    if sea[0][j] == ".":
                        temp[(i, j)] = (0, j)
                else:
                    if sea[i + 1][j] == ".":
                        temp[(i, j)] = (i + 1, j)

    return temp


def move_s_cu(sea):
    cucums = get_s_cu(sea)
    for k, c in cucums.items():
        sea[k[0]][k[1]] = "."
        sea[c[0]][c[1]] = "v"
    return sea, cucums


def move_e_cu(sea):
    cucums = get_e_cu(sea)
    for k, c in cucums.items():
        sea[k[0]][k[1]] = "."
        sea[c[0]][c[1]] = ">"
    return sea, cucums


def turn(sea):
    sea, e_cu = move_e_cu(sea)
    sea, s_cu = move_s_cu(sea)
    if len(e_cu) == 0 and len(s_cu) == 0:
        return False
    return True


# def can_move_sount(cus):
#     NotImplemented


def main():
    sea = read()
    print_c(sea)
    step = 1
    while turn(sea):
        print(step)
        step += 1
    print(step)
    print_c(sea)


main()
