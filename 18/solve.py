nums_range = list(map(str, range(10)))
import math
import re


def split(s):
    left = int(math.floor(float(s) / 2))
    right = int(math.ceil(float(s) / 2))
    result = "[" + str(left) + "," + str(right) + "]"
    return result


def explode(s, i):
    target = s[i : i + 5]
    left_num = s[i + 1]
    if left_num not in nums_range:
        print(s)
        print(left_num, s[i:])
    left_num = int(left_num)
    right_num = int(s[i + 3])
    left_to_sum = 0
    right_to_sum = 0

    s = s[:i] + str(0) + s[i + 5 :]
    # print(s, left_num, right_num)

    for j, c in enumerate(s[i + 1 :]):
        if c in nums_range:
            right_to_sum = j + 1 + i
            # print("right", j, c, s[i + j + 1])
            break

    if right_to_sum is not 0:
        sum = int(s[right_to_sum]) + right_num
        if sum > 9:
            sum = split(sum)
        else:
            sum = str(sum)
        s = s[:right_to_sum] + sum + s[right_to_sum + 1 :]

        # print("right", s)

    for j, c in enumerate(s[:i]):
        if c in nums_range:
            left_to_sum = j

    if left_to_sum is not 0:
        sum = int(s[left_to_sum]) + left_num
        if sum > 9:
            sum = split(sum)
        else:
            sum = str(sum)
        s = s[:left_to_sum] + sum + s[left_to_sum + 1 :]

    # print(s)
    return s

    # print(left_num, right_num)


def add(s1, s2):
    result = "[" + s1 + "," + s2 + "]"
    print(result)
    return result


def parse_nest(s):
    level = 0
    max = 0
    idx = 0
    # ma = re.match(r"^\[.*?\[.*?\[.*?\[.*?(\[\d,\d\]).*?\].*?\].*?\].*?\]$", s)
    # if ma:
    #     print(s)
    #     print("h", ma.group(1))
    #     idx = ma.start(1)
    #     # print("ma", s[idx])
    #     return explode(s, idx)

    for i, c in enumerate(s):
        if c == "[":
            level += 1
        if c == "]":
            level -= 1
        if level > 4:
            idx = i
            # while s[idx + 1] not in nums_range:
            #     idx += 1
            return explode(s, idx)

    return False


def is_explde(str):
    level = 0
    for i, c in enumerate(str):
        if c == "[":
            level += 1
        if c == "]":
            level -= 1
        if level > 4:
            return True
    return False


def main():
    with open("./example") as f:
        input = f.read().splitlines()
        s = input[0]
        for l in input[1:]:
            print(l)
            s = add(s, l)
            while is_explde(s):
                s = parse_nest(s)
                # print("result", s)


main()
# s = add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]")
# s = parse_nest(s)
# s = parse_nest("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
# parse_nest("[7,[6,[5,[4,[3,2]]]]]")
# s = parse_nest(s)
# s = parse_nest(s)
# s = parse_nest(s)
# parse_nest(s)
