import copy


def open_parse():
    # with open("./example.py") as f:
    with open("./input") as f:
        input = f.read()
        result = []
        for i, l in enumerate(input.splitlines()):
            result.append(list(map(int, list(l))))
        return result


def print_input(input):
    for i in input:
        print(i)
    print("---------")


def location(step, input):
    x_len = len(input) - 1
    y_len = len(input[0]) - 1

    l_l = []
    for x, y in zip(range(step), range(step)[::-1]):
        if x > x_len:
            continue
        if y > y_len:
            continue
        temp = [(x, y)]
        if x != 0:
            temp.append((x - 1, y))
        if y != 0:
            temp.append((x, y - 1))

        l_l.append((temp))
    return l_l


# def move(x,y,mem):
def reduce_input(input, l_l):

    # print(x_len, y_len)
    for i in l_l:
        min = float("inf")
        # min = float("inf")
        for x, y in i[1:3]:
            val = input[x][y]
            if val < min:
                min = val

        x, y = i[0]
        input[x][y] = input[x][y] + min

    return input


def walk2(x, y, risk, input, l_input):
    x_len = len(input) - 1
    y_len = len(input[0]) - 1

    if x < 0 or x > x_len:
        return risk
    if y < 0 or y > y_len:
        return risk
    if x == x_len and y == y_len:
        final = risk + input[x][y]
        if l_input[x][y] >= final:
            print("dang", risk + input[x][y])
        return risk

    lowest = l_input[x][y]
    if risk + input[x][y] > lowest:
        # print(x, y, input[x][y], risk, lowest)
        # print(x, y)
        return risk

    if risk + input[x][y] < lowest:
        print(
            "opti",
            (x, y),
            l_input[x][y],
            "-->",
            risk + input[x][y],
        )
        l_input[x][y] = risk + input[x][y]
        # print(x, y, input[x][y], risk, lowest)
        # return risk

    risk += input[x][y]

    risk = walk2(x + 1, y, risk, input, l_input)
    risk = walk2(x, y + 1, risk, input, l_input)
    # risk = walk2(x - 1, y, risk, input, l_input)
    # risk = walk2(x, y - 1, risk, input, l_input)

    risk = risk - input[x][y]
    return risk


def plus_arr(arr, num):
    temp = arr[:]
    for i, l in enumerate(temp):
        temp[i] = arr[i] + num
        if temp[i] > 9:
            temp[i] = temp[i] - 9
    return temp


def scale_map(input):
    for i, l in enumerate(input):
        temp = l[:]
        for j in range(4):
            input[i] += plus_arr(temp, j + 1)
    template = copy.deepcopy(input)
    for i in range(4):
        temp = copy.deepcopy(template)
        for x, l in enumerate(temp):
            for y, n in enumerate(l):
                temp[x][y] += i + 1
                if temp[x][y] > 9:
                    temp[x][y] -= 9

        input = input + temp
    return input


def opti_point(x, y, x_1, y_1, input, l_input):
    x_len = len(input)
    y_len = len(input[0])
    if x_1 < 0 or x_1 == x_len:
        return
    if y_1 < 0 or y_1 == y_len:
        return
    c_low = l_input[x][y]
    c_v = input[x][y]

    another = l_input[x_1][y_1]
    sum_risk = another + c_v
    if another + c_v < c_low:
        print("opti", c_low, "-->", sum_risk)
        l_input[x][y] = sum_risk
        return True
    return False


def opti_lower(input, l_input):
    x_len = len(input)
    y_len = len(input[0])
    is_opti = False

    for x in range(x_len):
        for y in range(y_len):
            # is_opti = opti_point(x, y, x + 1, y, input, l_input)
            is_opti = opti_point(x, y, x - 1, y, input, l_input)
            # is_opti = opti_point(x, y, x, y + 1, input, l_input)
            is_opti = opti_point(x, y, x, y - 1, input, l_input)
    return is_opti


def main():
    input = open_parse()
    input = scale_map(input)
    # input[0][0] = 0
    l_input = copy.deepcopy(input)
    # print_input(input)
    for i in range(len(input) * 2)[3:]:
        # print(i)
        temp = location(i, input)
        l_input = reduce_input(l_input, temp)
    # print_input(l_input)
    # print(len(input), len(input[0]))
    # temp = location(199, input)
    # print(temp)

    # print_input(l_input)
    # print(len(input), len(input[0]))
    # print(l_input[0][0])
    for i in range(1000):
        # print("loop", i)
        is_opti = opti_lower(input, l_input)
        if not is_opti:
            print(l_input[-1][-1])
            return

    # print("start walking")
    # risk = 0
    # risk = walk2(0, 0, risk, input, l_input)


# print(input)


main()
