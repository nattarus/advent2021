def strip_input(s: str):
    r = s[2:]
    r1, r2 = r.split("..")
    return int(r1), int(r2)


def print_m(s):
    print("_______________")
    for i in s:
        print(i)


def is_inter(p1, p2):
    # if p1[0] <= p2[1] and p1[0] >= p2[0]:
    #     if p2[0] > p1[0]:
    #         return p1, p2, (0, -1)
    #     else:
    #         return (
    #             (p2[1] + 1, p1[1]),
    #             (p1[0], p2[1]),
    #             (p2[0], p1[0] - 1),
    #         )
    # if p1[1] >= p2[0] and p1[1] <= p2[1]:
    #     if p1[0] > p2[0]:
    #         return (0, -1), p1, p2
    #     else:
    #         return (p1[0], p2[0] - 1), (p2[0], p1[1]), (p1[1] + 1, p2[1])
    if p1[1] >= p2[0] and p1[1] <= p2[1]:
        if p1[0] <= p2[0]:
            return p2[0], p1[1]
        else:
            return p1[0], p1[1]
    if p2[1] >= p1[0] and p2[1] <= p1[1]:
        if p2[0] <= p1[0]:
            return p1[0], p2[1]
        else:
            return p2[0], p2[1]

    #
    # if p1[0] <= p2[1] and p1[0] >= p2[0]:
    #     if p1[1] >= p2[0]:
    #         return p1[0], p2[1]
    #     else:
    #         return p1[0], p1[1]
    #
    # if p2[0] <= p1[1] and p2[0] >= p1[0]:
    #     if p2[1] >= p1[0]:
    #         return p2[0], p1[1]
    #     else:
    #         return p2[0], p2[1]

    return False


def get_point(p1, p2):
    # print(p1, p2)
    temp = []
    if p1[0] <= (p2[0] - 1):
        temp.append((p1[0], p2[0] - 1))
    temp.append(p2)
    if (p2[1] + 1) <= p1[1]:
        temp.append((p2[1] + 1, p1[1]))
    # print(temp)

    return temp


def ext_cube(c, i_cube):
    x = get_point(c[0], i_cube[0])
    y = get_point(c[1], i_cube[1])
    z = get_point(c[2], i_cube[2])

    temp = []
    for i in x:
        for j in y:
            for k in z:
                if i_cube == (i, j, k):
                    continue
                temp.append((i, j, k))

    # print("Extract cube")
    # print(x, y, z)
    # print(c)
    # print(i_cube)
    # print_c(temp)
    return temp


def union_cube(c1, c2):
    x = is_inter(c1[0], c2[0])
    y = is_inter(c1[1], c2[1])
    z = is_inter(c1[2], c2[2])

    if x and y and z:
        i_cube = (x, y, z)
        # t1 = ext_cube(c1, i_cube)
        t2 = ext_cube(c2, i_cube)

        return t2
    return [c2]


def cut_cube2(c1, c2):
    x = is_inter(c1[0], c2[0])
    y = is_inter(c1[1], c2[1])
    z = is_inter(c1[2], c2[2])

    if x and y and z:
        i_cube = (x, y, z)
        t1 = ext_cube(c1, i_cube)
        # print(c1, "c1")
        # print(i_cube, "i_cue")
        # print_c(t1)

        return t1
    return [c1]


def im_cube(c):
    for i in c:
        if i[0] > i[1]:
            return True
    return False


def combine_cube(c1, c2):
    x1 = c1[0]
    y1 = c1[1]
    z1 = c1[2]
    x2 = c2[0]
    y2 = c2[1]
    z2 = c2[2]

    if (x1, y1) == (x2, y2):
        if z1[1] == z2[0]:
            return (x1, y2, (z1[0], z2[1]))
        if z2[1] == z1[0]:
            return (x1, y2, (z2[0], z1[1]))
    if (x1, z1) == (x2, z2):
        if y1[1] == y2[0]:
            return (x1, (y1[0], y2[1]), z1)
        if y2[1] == y1[0]:
            return (x1, (y2[0], y1[1]), z1)
    if (z1, y1) == (z2, y2):
        if x1[1] == x2[0]:
            return ((x1[0], x2[1]), y1, z1)
        if x2[1] == x1[0]:
            return ((x2[0], x1[1]), y1, z1)
    return False


def compress_state(s):
    for i in range(len(s)):
        for j in range(1, len(s)):
            com = combine_cube(s[i], s[j])
            if com:
                s.pop(i)
                s.pop(j)
                s.append(com)


def u_state(s, c2):
    temp = [c2]
    for c in s:
        t2 = union_cube(c2, c)
        temp = temp + t2

    return temp


def cut_state(s, c2):
    temp = []
    for c in s:
        res = cut_cube2(c, c2)
        for i in res:
            temp.append(i)
    return temp


def count_dot(c):
    x = c[0][1] - c[0][0] + 1
    y = c[1][1] - c[1][0] + 1
    z = c[2][1] - c[2][0] + 1

    return x * y * z


def print_c(s):
    print("----------------")
    for i in s:
        print(i, "-->", count_dot(i))
    print("---------------")


def count_state(s):
    sum = 0
    for i in s:
        sum += count_dot(i)
    return sum


def read_pares():
    with open("./input") as f:
        f = f.read()
        f = f.splitlines()
        result = []
        for l in f:
            m, t = l.split(" ")
            x, y, z = list(map(strip_input, t.split(",")))
            temp = (m, (x, y, z))
            result.append(temp)
        # print_m(result)
        return result


def main():
    f = read_pares()
    # c1 = f[0][1]
    # c2 = f[1][1]
    # c3 = f[2][1]
    # state = [c1]
    # test = union_cube(c1, c2)
    # c = count_state(test)
    # print(c)
    # print_c(test)
    # test = cut_state(test, c3)
    # print_c(test)
    # c = count_state(test)
    # print(c)
    state = [f[0][1]]
    for i in f[1:]:
        opt, cube = i
        # if cube[0][0] > 100 or cube[0][1] < -100:
        #     continue
        print(opt, cube)
        if opt == "on":
            state = u_state(state, cube)
        if opt == "off":
            state = cut_state(state, cube)
        print(len(state))

        c = count_state(state)
        print(c)

    # print_m(state)
    # state = u_state(state, c2)
    # print_m(state)
    # count = count_state(state)
    # print(count)
    # state = cut_state(state, c3)
    # print_c(state)
    # res = u_cube(c1, c2)
    # print_m(res)

    # count = count_state(state)
    # print(count)


main()
