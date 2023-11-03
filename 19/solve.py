def parse_scanner(s):
    r = s.split("\n")
    name = r[0]
    data = []
    for s in r[1:]:
        # print(s)
        temp1 = s.strip().split(",")
        # print(temp1)
        if len(temp1) == 3:
            temp1 = map(int, s.strip().split(","))
            data.append(temp1)
    return data


def point_diff(p1, p2):
    temp = [0, 0, 0]
    temp[0] = p1[0] - p2[0]
    temp[1] = p1[1] - p2[1]
    temp[2] = p1[2] - p2[2]
    return temp


def print_m(l):
    print("------")
    for i in l:
        print(i)


def compare_in_scaner(p, l):
    temp = []
    for temp_p in l:
        # if temp_p == p:
        #     continue
        temp.append(point_diff(temp_p, p))
    # print_m(temp)
    return temp


def check_same_point(p1, p2):
    mem = {}
    for i, d1 in enumerate(p1):
        for j, d2 in enumerate(p2):
            if abs(d1) == abs(d2):
                if d2 is not 0:
                    mem[i] = [j, d1 / d2]
                else:
                    mem[i] = [j, 0]
    if len(mem) == 3:
        return mem
    return False


def check_overlap(l1, l2):
    d = {}
    for i, p1 in enumerate(l1):
        for j, p2 in enumerate(l2):
            temp = check_same_point(p1, p2)
            if temp:
                d[(i, j)] = temp
    # print(d, len(d))
    if len(d) > 11:
        # print(d, len(d))
        return d
    else:
        return False


def compare(l1, l2):
    save_table = False
    for p1 in l1:
        diff_l1_p = compare_in_scaner(p1, l1)
        for p2 in l2:
            diff_l2_p = compare_in_scaner(p2, l2)
            overlap_table = check_overlap(diff_l1_p, diff_l2_p)
            if overlap_table:
                # if not save_table:
                #     save_table = overlap_table.copy()
                #     continue
                # if save_table == overlap_table:
                #     return overlap_table
                # else:
                #     print(overlap_table)
                #     save_table = overlap_table
                return overlap_table
    return False


def recon_overlap(l1, l2, o_table):
    d1 = []
    d2 = []
    for k in o_table:
        k1, k2 = k
        d1.append(l1[k1])
        d2.append(l2[k2])
    return d1, d2
    # print_m(d1)
    # print_m(d2)


def check_table(t):
    for k in t:
        v = t[k]
        if v[1] == 0:
            return False
    return True


def recon_overlap_convert(l1, l2, o_table):
    d1 = []
    d2 = []
    good_table = None
    count = 0
    for k in o_table:
        k1, k2 = k
        temp = [0, 0, 0]
        val = o_table[k]
        if not check_table(val):
            continue
        else:
            if not good_table:
                good_table = val
            else:
                if good_table != val:
                    count += 1
                    if count > 3:
                        good_table = val
                    continue
        for kk in val:
            vv = val[kk]
            temp[kk] = l2[k2][vv[0]] * vv[1]

        # for t_k in o_table[k]:
        #     if check_table(o_table[k]):
        #         good_table = o_table[k].copy()
        #     val = o_table[k][t_k]
        #     if val[1] is not 0:
        #         temp[t_k] = l2[k2][val[0]] * val[1]
        #         print(good_table, o_table[k])
        #         if good_table:
        #             if good_table != o_table[k]:
        #                 print(good_table, o_table[k])
        #                 # assert good_table == o_table[k]
        #                 # print("DAMMM")
        #         else:
        #             if check_table(o_table[k]):
        #                 good_table = o_table[k].copy()

        d1.append(l1[k1])
        d2.append(temp)
    assert len(d1) == len(d2)
    # print_m(d1)
    # print_m(d2)

    diff_scan = False
    count = 0
    for i in range(len(d2)):
        if diff_scan:
            if d1[i] == [0, 0, 0] or d2[i] == [0, 0, 0]:
                continue
            # print(d1[i], d2[i], diff_scan, diff_point(d1[i], d2[i]))
            temp = diff_point(d1[i], d2[i])
            # assert diff_scan == temp
            if diff_scan != temp:
                count += 1
                d1.pop(i)
                d2.pop(i)
                if count > 3:
                    diff_scan = temp
                continue
            else:
                diff_scan = temp
                # if diff_scan != diff_point(d1[i + 1], d2[i + 1]):
                #     diff_scan = temp
                # else:
                #     continue

        else:
            diff_scan = diff_point(d1[i], d2[i])

    # assert diff_scan is not [0, 0, 0]

    return good_table, diff_scan


def recon_scaner(table, diff, l):
    temp = []
    for p in l:
        temp_p = []
        for i in range(3):
            l_i = table[i][0]
            sign = table[i][1]
            val = (p[l_i] * sign) + diff[i]
            temp_p.append(val)
        temp.append(temp_p)
    # print(temp)
    return temp


def diff_point(p1, p2):
    temp = [0, 0, 0]
    for i in range(3):
        temp[i] = p1[i] - p2[i]
    # print(temp)
    return temp


def merge_scanner(l1, l2):
    temp = l1[:]
    for p2 in l2:
        reg = False
        for p1 in l1:
            if p1 == p2:
                reg = True
        if not reg:
            temp.append(p2)
    return temp


def parse_input():
    with open("./input") as f:
        f = f.read()
        f = f.split("\n\n")
        f = list(map(parse_scanner, f))
    # print_m(f[0])
    # print_m(f[4])
    ref_scanner = f[0]
    scanners = f[1:]
    # print_m(ref_scanner)
    # print(len(ref_scanner))

    mem = [ref_scanner]
    finish = []
    scan_pos = []
    scanner_len = len(f)
    while len(mem) < scanner_len:
        for j, m in enumerate(mem):
            to_pop = []
            for i, l in enumerate(scanners):
                print("loop", i)
                o_table = compare(m, l)
                if o_table:
                    table, diff_scan = recon_overlap_convert(m, l, o_table)
                    scan_pos.append(diff_scan)
                    final = recon_scaner(table, diff_scan, l)
                    # scanners[i] = final
                    # print("final")
                    print_m(final)

                    mem.append(final)
                    to_pop.append(i)
                    # scanners.pop(i)
            for i in to_pop[::-1]:
                scanners.pop(i)

                # ref_scanner = merge_scanner(ref_scanner, final)

    temp = []
    for i in mem:
        temp = merge_scanner(temp, i)

    print_m(temp)
    print(len(temp))
    print_m(scan_pos)
    print(len(scan_pos))
    manhat(scan_pos)

    # o_table = compare(f[0], f[1])
    # # print(o_table)
    # table, diff_scan = recon_overlap_convert(f[0], f[1], o_table)
    # # print(table, diff_scan)
    # final = recon_scaner(table, diff_scan, f[1])
    # print_m(final)
    # # print(l)
    # return f


def cal_manhat(p1, p2):
    sum = 0
    for i in range(3):
        sum += abs(p1[i] - p2[i])
    return sum


def manhat(scan_pos):
    max = 0
    for i, s in enumerate(scan_pos):
        for j in range(i, len(scan_pos)):
            print(i, j)
            left = s
            right = scan_pos[j]
            temp = cal_manhat(left, right)
            if temp > max:
                max = temp
    print(max)


# manhat()


# def find_start(d1, d2):
#     count = 0
#     prev_diff_table = None
#     for i, p1 in enumerate(d1):
#         p2 = d2[i]
#         diff_table = check_same_point(p1, p2)
#         if prev_diff_table == diff_table:
#             count += 1
#         else:
#
#         prev_diff_table = diff_table


def parse_input2():
    with open("./input") as f:
        f = f.read()
        f = f.split("\n\n")
        f = list(map(parse_scanner, f))
    # print_m(f[0])
    # print_m(f[4])
    ref_scanner = f[0]
    scanners = f[1:]
    # print_m(ref_scanner)
    # print(len(ref_scanner))

    mem = [ref_scanner]
    scanner_len = len(f)
    while len(mem) < scanner_len:
        for j, m in enumerate(mem):
            to_pop = []
            for i, l in enumerate(scanners):
                print("loop", i)
                o_table = compare(m, l)
                if o_table:
                    d1, d2 = recon_overlap(m, l, o_table)
                    # table, diff_scan = recon_overlap_convert(m, l, o_table)
                    # final = recon_scaner(table, diff_scan, l)
                    # scanners[i] = final
                    # print("final")
                    # print_m(final)

                    # mem.append(final)
                    to_pop.append(i)
                    # scanners.pop(i)
            for i in to_pop[::-1]:
                scanners.pop(i)

                # ref_scanner = merge_scanner(ref_scanner, final)

    temp = []
    for i in mem:
        temp = merge_scanner(temp, i)

    print_m(temp)
    print(len(temp))


# parse_input()
sc = [
    [0, 0, 0],
    [38, 1213, -102],
    [107, -1107, -103],
    [-39, 1336, -1209],
    [-12, -1098, 1067],
    [-59, -2331, -114],
    [-1221, 1246, -1298],
    [-1199, -1205, 1054],
    [-24, -2345, -1388],
    [1137, -2354, -185],
    [-1242, -2316, -20],
    [-2397, 1350, -1273],
    [-1234, -19, -1347],
    [-1147, 2470, -1367],
    [-1203, -2354, 1028],
    [-1155, -2289, -1267],
    [-11, -2328, -2513],
    [-1212, -1125, -1217],
    [-1247, 2471, -2553],
    [-1086, 3712, -1326],
    [-2342, -2258, -1213],
    [-1087, -2382, -2510],
    [99, -1188, -2466],
    [-2422, -1229, -1332],
    [-1112, -1126, -2573],
    [-58, 2432, -2497],
    [-2301, 3723, -1377],
    [-2299, -3615, -1274],
    [-1137, -2335, -3610],
    [-2386, -1133, -2447],
    [-1077, -1232, -3760],
    [-1226, 33, -3681],
]
manhat(sc)
