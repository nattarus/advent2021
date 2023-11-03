def read_parse():
    with open("./input") as f:
        f = f.read()
        f = f.splitlines()

        temp = []
        temp.append(f[1][1])
        temp.append(f[1][2])
        temp.append((f[2][3], f[3][3], f[4][3], f[5][3]))
        temp.append(f[1][4])
        temp.append((f[2][5], f[3][5], f[4][5], f[5][5]))
        temp.append(f[1][6])
        temp.append((f[2][7], f[3][7], f[4][7], f[5][7]))
        temp.append(f[1][8])
        temp.append((f[2][9], f[3][9], f[4][9], f[5][9]))
        temp.append(f[1][10])
        temp.append(f[1][11])

        return tuple(temp)


ambi_room = {"A": 2, "B": 4, "C": 6, "D": 8}
ambi_val = {"A": 1, "B": 10, "C": 100, "D": 1000}

rooms_val = {2: "A", 4: "B", 6: "C", 8: "D"}


def room_first_ambi(room, ambi):
    com = True
    for i, v in enumerate(room):
        if v != "." and v != ambi:
            com = False

    if com:
        return False

    for i, v in enumerate(room):
        if v != ".":
            return i, v
    return False


def room_move_out(room):
    r = list(room)
    for i, v in enumerate(room):
        if v != ".":
            r[i] = "."
            break
    return tuple(r)


def can_move_in_v(ambi, diag):
    num = ambi_room[ambi]
    room = diag[num]
    for i in room:
        if i in ambi_val.keys() and i != ambi:
            return False
    for i, v in enumerate(diag[num]):
        if v != ".":
            return i
    return 4


def can_move_in_h(i, ambi, diag):
    num = ambi_room[ambi]
    if num < i:
        for d in list(diag)[num:i]:
            if d in ambi_val.keys():
                return False
    if i < num:
        for d in list(diag)[i + 1 : num]:
            if d in ambi_val.keys():
                return False
    # print(i, ambi, num)
    return abs(num - i)


def room_move_in(room, ambi, i):
    # print(room, i)
    room = list(room)
    room[i] = ambi
    return tuple(room)


def move_in(i, diag, sums):
    ambi = diag[i]
    # assert isinstance(ambi, str)
    num = ambi_room[ambi]
    move_v = can_move_in_v(ambi, diag)
    move_h = can_move_in_h(i, ambi, diag)
    if move_v and move_h:
        temp = list(diag)
        ener = sums[diag][0] + ((move_v + move_h) * ambi_val[ambi])
        temp[i] = "."
        temp[num] = room_move_in(temp[num], ambi, move_v - 1)
        his = sums[diag][1][:] + [tuple(temp)]
        return tuple(temp), ener, his
    return False


def move_out(i, j, diag: tuple, sums):
    ambi = diag[i][j]
    halls = []
    for k, v in enumerate(diag):
        if v == ".":
            halls.append(k)
        if v in ambi_val.keys():
            if i > k:
                halls = []
            if k > i:
                break

    r = []
    for k in halls:
        x_diff = abs(i - k)
        y_diff = j + 1
        ener = sums[diag][0] + ((x_diff + y_diff) * ambi_val[ambi])
        temp = list(diag)
        temp[i] = room_move_out(temp[i])
        temp[k] = ambi
        # print(sums[diag][1])
        if len(sums[diag][1]) == 0:
            his = [tuple(temp)]
        else:
            his = sums[diag][1][:] + [tuple(temp)]
        r.append((tuple(temp), ener, his))
    return r


def check_room(room, ambi):
    for a in room:
        if a != ambi:
            return False
    return True


def check_rooms(diag):
    a = check_room(diag[2], "A")
    b = check_room(diag[4], "B")
    c = check_room(diag[6], "C")
    d = check_room(diag[8], "D")
    if a and b and c and d:
        # print("GOD")
        return True
    return False


def turn(diags):
    r = {}
    for diag in diags:
        for i, v in enumerate(diag):
            if v in ambi_val.keys():
                mi = move_in(i, diag, diags)
                if mi:
                    d, ener, his = mi
                    # print_d(d)
                    if check_rooms(d):
                        NotImplemented
                        # print(ener)
                        # for l in his:
                        #     print_d(l)
                    if d in r:
                        if r[d][0] > ener:
                            r[d] = (ener, his)
                    else:
                        r[d] = (ener, his)
            if isinstance(v, tuple):
                ambi = rooms_val[i]
                room = room_first_ambi(v, ambi)
                if room:
                    j, ambi = room
                    results = move_out(i, j, diag, diags)
                    for d, ener, his in results:
                        if d in r:
                            if r[d][0] > ener:
                                r[d] = (ener, his)
                        else:
                            r[d] = (ener, his)
    return r


def tuple_to_str(x):
    if isinstance(x, tuple):
        return "."
    return x


def print_d(diag):
    d = list(diag)
    hall = list(map(tuple_to_str, d))
    print("#" * 13)
    print("#" + "".join(hall) + "#")

    print("##" + "#" + d[2][0] + "#" + d[4][0] + "#" + d[6][0] + "#" + d[8][0] + "###")
    for j in range(1, 4):
        print(
            "  " + "#" + d[2][j] + "#" + d[4][j] + "#" + d[6][j] + "#" + d[8][j] + "#"
        )


def main():
    f = read_parse()
    # print_d(f)
    init = {}
    init[f] = (0, [])
    mem = turn(init)
    # mem = turn(mem)
    # for l in mem:
    #     print_d(l)
    # print(len(mem))
    while len(mem) > 0:
        mem = turn(mem)
        #     if len(mem) < 20:
        #         for l in mem:
        #             print_d(l)
        # print(len(mem))
    # print(mem)
    # for l in mem:
    #     print_d(l)
    #     print(mem[l])
    # mem = {}
    # mem[f] = 0
    # print(mem)


main()
# print(read_parse())
