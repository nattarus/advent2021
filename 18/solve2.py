import math


def read_file():
    with open("./input") as f:
        file = f.read()
        return file


nums_range = list(map(str, range(10)))


def add(s1, s2):
    temp = []
    temp.append("[")
    temp += s1
    temp.append(",")
    temp += s2
    temp.append("]")
    # result = "[" + s1 + "," + s2 + "]"
    # print(temp)
    return temp


def explode(l, idx):
    left = l[idx + 1]
    right = l[idx + 3]
    print(left, right)
    # print(left, right)
    # print(l, left, idx)
    print_l(l)
    l = l[:idx] + [0] + l[idx + 5 :]
    print_l(l)

    for i in range(idx - 1, -1, -1):
        if type(l[i]) is int:
            l[i] = l[i] + left
            break

    for i, c in enumerate(l[idx + 1 :]):
        if type(c) is int:
            l[i + idx + 1] += right
            break
    print_l(l)
    return l


def split(l, idx):
    c = l[idx]
    temp = []
    left = int(math.floor(float(c) / 2))
    right = int(math.ceil(float(c) / 2))
    temp.append("[")
    temp.append(left)
    temp.append(",")
    temp.append(right)
    temp.append("]")
    l = l[:idx] + temp + l[idx + 1 :]
    return l


def check_action(l):
    level = 0

    for i, c in enumerate(l):
        if c == "[":
            level += 1
        if c == "]":
            level -= 1
        if level > 4:
            idx = i
            print("explode")
            l = explode(l, idx)
            return l

    for i, c in enumerate(l):
        if type(c) is int and c > 9:
            print("split")
            l = split(l, i)
            return l

    return l


def is_action(l):
    level = 0
    for i, c in enumerate(l):
        if c == "[":
            level += 1
        if c == "]":
            level -= 1
        if level > 4:
            return True

    for i, c in enumerate(l):
        if type(c) is int and c > 9:
            return True

    return False


def check_int(c):
    if c in nums_range:
        return int(c)
    return c


def s_to_l(s):
    temp = map(check_int, list(s))
    return list(temp)


def print_l(l):
    print("".join(map(str, l)))


def sum_bracket(l):
    print_l(l)
    for i in range(len(l)):
        if type(l[i]) is int and type(l[i + 2]) is int:
            left = l[i]
            right = l[i + 2]
            result = (3 * left) + (2 * right)
            l = l[: i - 1] + [result] + l[i + 4 :]
            return l


def main():
    f = read_file().splitlines()
    first = s_to_l(f[0])
    l = first[:]
    for line in f[1:]:
        temp = s_to_l(line)
        l = add(l, temp)
        while is_action(l):
            l = check_action(l)
    while "," in l:
        l = sum_bracket(l)
    print(l)
    print_l(l)

    # check()


def sum_2(l1, l2):
    l1 = s_to_l(l1)
    l2 = s_to_l(l2)
    l = add(l1, l2)
    while is_action(l):
        l = check_action(l)
    while "," in l:
        l = sum_bracket(l)
    print(l)
    print_l(l)
    return l[0]


def main2():
    max = 0
    f = read_file().splitlines()
    for i in range(len(f)):
        for j in range(len(f)):
            if j == i:
                continue
            sum = sum_2(f[i], f[j])
            if sum > max:
                max = sum

    print(max)


# main()
main2()
