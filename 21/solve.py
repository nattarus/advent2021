import sys

sys.setrecursionlimit(10000000)
print(sys.getrecursionlimit())


def read_parse():
    with open("./example") as f:
        f = f.read()
        return f


# while True:
#     pos = [4, 8]
#     sc = [0, 0]
#     c = [0, 0]
#     for i in range(1, 4):
#         print(i)


def roll2(d, pos, sc):
    temp_pos = (pos + d) % 10
    if temp_pos == 0:
        temp_sc = sc + 10
    else:
        temp_sc = sc + temp_pos
    return temp_pos, temp_sc


def playing():
    state = {((10, 0), (4, 0)): 1}
    # pos = [4, 8]
    win = [0, 0]
    # sc = [0, 0]
    turn = 0

    for i in range(20):
        next_state = {}
        for s in state:
            v = state[s]
            pos = s[turn][0]
            score = s[turn][1]
            for d1 in range(1, 4):
                for d2 in range(1, 4):
                    for d3 in range(1, 4):
                        dice = d1 + d2 + d3
                        temp_pos, temp_sc = roll2(dice, pos, score)
                        if temp_sc > 20:
                            win[turn] += v
                        else:
                            if turn == 0:
                                temp = ((temp_pos, temp_sc), s[1])
                            else:
                                temp = (s[0], (temp_pos, temp_sc))
                            if temp not in next_state:
                                next_state[temp] = v
                            else:
                                next_state[temp] += v
                            # temp = s.copy()
                            # temp[0 + turn] = temp_pos
                            # temp[2 + turn] = temp_sc
                            # next_state.append(temp)

        state = next_state

        if turn == 0:
            turn = 1
        else:
            turn = 0
        print(win)
        print(len(state))
        print(win[0] > win[1])
        # print(state)


playing()
# if temp_sc > 20:
#     print(c)
#     c[pla] = c[pla] + 1
#     return pos, sc, c
# pos[pla] = temp_pos
# sc[pla] = temp_sc


def roll(d1, d2, d3, pla, pos, sc, c):
    score = d1 + d2 + d3
    # print("turn:", pla + 1, score)
    # print(pos, sc, c)
    if score != 0:

        temp_pos = (pos[pla] + score) % 10
        if temp_pos == 0:
            temp_sc = sc[pla] + 10
        else:
            temp_sc = sc[pla] + pos[pla]

        if temp_sc > 20:
            print(c)
            c[pla] = c[pla] + 1
            return pos, sc, c
        pos[pla] = temp_pos
        sc[pla] = temp_sc

    if pla == 0:
        p = 1
    else:
        p = 0

    for i in range(1, 4):
        # for j in range(1, 4):
        #     for k in range(1, 4):
        prev_p = pos[p]
        prev_sc = sc[p]
        roll(i, 0, 0, p, pos, sc, c)
        pos[p] = prev_p
        sc[p] = prev_sc
        # score = i
        # pos[p] = abs(pos[p] - score) % 10
        # if pos[p] == 0:
        #     sc[p] = sc[p] - 10
        # else:
        #     sc[p] = sc[p] - pos[p]
    # print(c)

    return pos, sc, c

    # roll(2, 1, 1, p, pos, sc, c)
    # roll(3, 1, 1, p, pos, sc, c)


def main2():
    pos = [4, 8]
    sc = [0, 0]
    c = [0, 0]
    roll(0, 0, 0, 1, pos, sc, c)
    print(sc, c, pos)


# main2()


def main():
    start1 = 4
    start2 = 8
    sc1 = 0
    sc2 = 0
    dice = 0
    count = 0
    while True:
        count += 3
        r = 0
        for _ in range(3):
            dice += 1
            r += dice
        t_c = (start1 + r) % 10
        start1 = t_c
        if t_c == 0:
            t_c = 10
        sc1 += t_c

        if sc1 >= 21:
            print(count)
            print(sc1)
            print(sc2 * count)
            break

        count += 3
        r = 0
        for _ in range(3):
            dice += 1
            r += dice
        t_c = (start2 + r) % 10
        start2 = t_c
        if t_c == 0:
            t_c = 10
        sc2 += t_c

        if sc2 >= 21:
            print(count)
            print(sc1 * count)
            print(sc2)

            break


# main()
