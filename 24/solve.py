import math


def parse_intrc(str: str):
    intrc, v = str.split(" ", 1)
    if intrc == "inp":
        v1 = v
        return (intrc, v1, None)
    else:
        v1, v2 = v.split(" ")
        return (intrc, v1, v2)


def intp(instr, mem, inp_val):
    _, v, _ = instr
    mem[v] = int(inp_val)


def mul(instr, mem):
    _, v1, v2 = instr
    v0 = v1
    v1 = mem[v1]
    if v2 in mem.keys():
        v2 = mem[v2]
    mem[v0] = int(v2) * int(v1)


def div(instr, mem):
    _, v1, v2 = instr
    v0 = v1
    v1 = mem[v1]
    if v2 in mem.keys():
        v2 = mem[v2]
    mem[v0] = math.floor(int(v1) / int(v2))


def mod(instr, mem):
    _, v1, v2 = instr
    v0 = v1
    v1 = mem[v1]
    if v2 in mem.keys():
        v2 = mem[v2]
    mem[v0] = int(v1) % int(v2)


def add(instr, mem):
    _, v1, v2 = instr
    v0 = v1
    v1 = mem[v1]
    if v2 in mem.keys():
        v2 = mem[v2]
    mem[v0] = int(v1) + int(v2)


def eql(instr, mem):
    _, v1, v2 = instr
    v0 = v1
    v1 = mem[v1]
    if v2 in mem.keys():
        v2 = mem[v2]
    mem[v0] = 1 if int(v1) == int(v2) else 0


instr_set = {"inp": intp, "mul": mul, "div": div, "mod": mod, "add": add, "eql": eql}


def read():
    with open("./input") as f:
        f = f.read()
        f = f.splitlines()
        f = map(parse_intrc, f)
        f = list(f)
        return f


def section(f):
    res = []
    temp = []
    for line in f:
        if line[0] == "inp" and len(temp) > 0:
            res.append(temp)
            temp = []
        temp.append(line)
    res.append(temp)
    return res


def run(f, mem, inp_val):
    for line in f:
        intr, _, _ = line
        fn = instr_set[intr]
        # print(line, mem)
        if intr == "inp":
            fn(line, mem, inp_val)
        else:
            fn(line, mem)
        # if mem["z"] > 99999999:
        #     break
    return mem


def mem_to_tup(mem):
    return (mem["x"], mem["y"], mem["z"])


def tup_to_mem(tup):
    # print(tup)
    x, y, z = tup
    return {"x": x, "y": y, "z": z, "w": 0}


def run_one_to_ten(sec, init_mem, init_val):
    mems = {}
    for i in range(1, 10)[::-1]:
        # temp_mem = init_mem.copy()
        temp_mem = tup_to_mem(init_mem)
        run(sec, temp_mem, str(i))
        key = mem_to_tup(temp_mem)
        if init_val:
            mems[key] = init_val + [i]
        else:
            mems[key] = [i]

    return mems


def run_one_to_ten_from_list(sec, init_mems):
    temp = {}
    for mem in init_mems:
        init_val = init_mems[mem]
        mems = run_one_to_ten(sec, mem, init_val)
        temp = temp | mems
    return temp


def print_m(mems):
    for line in mems:
        print(line)


def filter_mems(mems, val):
    new_mems = {}
    for mem in mems:
        if mem[2] < val:
            new_mems[mem] = mems[mem]
    return new_mems


def filter_mems_with_0(mems):
    new_mems = {}
    for mem in mems:
        if mem[0] == 0 and mem[1] == 0:
            new_mems[mem] = mems[mem]
    return new_mems


def check_z(mems):
    for mem in mems:
        if mem[2] == 0:
            print("BINGO", mem, mems[mem])
            print("".join(map(str, mems[mem])))


def main():
    mem = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    f = read()
    secs = section(f)
    tup_mem = mem_to_tup(mem)
    init = {}
    init[tup_mem] = None
    mems = run_one_to_ten_from_list(secs[0], init)
    round = 4
    for i in range(1, round):
        mems = run_one_to_ten_from_list(secs[i], mems)

    # mems = filter_mems(mems, 1000)
    mems = filter_mems_with_0(mems)
    # print_m(mems)

    print(round)

    prev_round = round
    round = 8
    for i in range(prev_round, round):
        mems = run_one_to_ten_from_list(secs[i], mems)

    mems = filter_mems_with_0(mems)

    print(round)

    prev_round = round
    round = 10
    for i in range(prev_round, round):
        mems = run_one_to_ten_from_list(secs[i], mems)
    mems = filter_mems_with_0(mems)

    print(round)

    prev_round = round
    round = 12
    for i in range(prev_round, round):
        mems = run_one_to_ten_from_list(secs[i], mems)
    mems = filter_mems_with_0(mems)

    prev_round = round
    round = 14
    for i in range(prev_round, round):
        mems = run_one_to_ten_from_list(secs[i], mems)

    # mems = filter_mems(mems, 1000000)

    print_m(mems)
    check_z(mems)
    # for i in range(5, 7):
    #     mems = run_one_to_ten_from_list(secs[i], mems)
    # print_m(mems)


# def main2():
#     mem = {
#         "w": 2,
#         "x": 0,
#         "y": 0,
#         "z": 641,
#     }
#     f = read()
#     secs = section(f)
#     min = float("inf")
#     # for sec in secs[0:1]:
#     for i in range(1, 10):
#         temp_mem = mem.copy()
#         run(secs[4], temp_mem, str(i))
#         for j in range(1, 10):
#             temp_mem2 = temp_mem.copy()
#             run(secs[5], temp_mem2, str(j))
#             for k in range(1, 10):
#                 temp_mem3 = temp_mem2.copy()
#                 run(secs[6], temp_mem3, str(k))
#                 for l in range(1, 10):
#                     temp_mem4 = temp_mem3.copy()
#                     run(secs[7], temp_mem4, str(l))
#                     # print(temp_mem4)
#                     if temp_mem4["z"] < min:
#                         min = temp_mem4["z"]
#                         print(temp_mem4, i, j, k, l)

# print(sec)
# print(mem["z"])
# print(mem)


main()
