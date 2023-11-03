parse_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_b(str):
    b = ""
    for c in str:
        b += parse_table[c]
    return b


# print(hex_to_b("8A004A801A8002F478"))


def b_to_dec(str):
    sum = 0
    for i, c in enumerate(str[::-1]):
        sum += (2 ** i) * int(c)
        # print(c, i)
    # print(sum)
    return sum


def cut_zero(str):
    while str[0] == "0":
        str = str[1:]
    return str


def read_sub_lit(str):
    while str[0] == "1":
        str, _ = read_literal(str[1:])
    str, _ = read_literal(str[1:])


def read_literal(str):
    val = ""
    while str[0] == "1":
        val = val + str[1:5]
        str = str[5:]

    val = val + str[1:5]
    str = str[5:]
    # print("read", str)
    # str = cut_zero(str)

    return str, val


def read_3(str, len):
    ver = b_to_dec(str[:len])
    return str[len:], ver


# assert b_to_dec("101") == 5


def product(temp_list):
    p = 1
    for i in temp_list:
        p *= i
    return p


def greater(temp_list):
    if temp_list[0] > temp_list[1]:
        return 1
    return 0


def lesser(temp_list):
    if temp_list[0] < temp_list[1]:
        return 1
    return 0


def equa(temp_list):
    if temp_list[0] == temp_list[1]:
        return 1
    return 0


oper_dict = {0: sum, 1: product, 2: min, 3: max, 5: greater, 6: lesser, 7: equa}


def parse_lit_package(str, vers):
    # print(str)
    if str == "":
        return str
    str, ver = read_3(str, 3)
    str, type = read_3(str, 3)
    vers.append(ver)
    # print(ver, type)
    value = 0

    if type == 4:
        str, literal = read_literal(str)
        print("ver:", ver, "type:", type, "literal", b_to_dec(literal))
        value = b_to_dec(literal)
        # print(str, ver, type, literal)
        # print(b_to_dec(literal))
    else:
        str, label = read_3(str, 1)
        if label == 0:
            str, len = read_3(str, 15)
            print("ver:", ver, "type:", type, len, "length")
            to_parse = str[:len]
            temp_list = []
            while to_parse != "":
                to_parse, temp = parse_lit_package(to_parse, vers)
                temp_list.append(temp)
            str = str[len:]
            value = oper_dict[type](temp_list)
        if label == 1:
            str, sub_p = read_3(str, 11)
            print("ver:", ver, "type:", type, sub_p, "packages")
            # print(str)
            # print(sub_p)
            temp_list = []
            for i in range(sub_p):
                str, temp = parse_lit_package(str, vers)
                temp_list.append(temp)
            value = oper_dict[type](temp_list)
            # print(str)
    return str, value


def read_file():
    with open("./input") as f:
        return f.read().strip()


def main():
    # test = hex_to_b("D2FE28")
    # test = hex_to_b("8A004A801A8002F478")
    # test = hex_to_b("620080001611562C8802118E34")
    # test = hex_to_b("C0015000016115A2E0802F182340")
    # test = hex_to_b("A0016C880162017C3686B18A3D4780")
    test = hex_to_b(read_file())
    # test = hex_to_b("9C0141080250320F1802104A08")
    # for _ in range(4):
    vers = []
    test, val = parse_lit_package(test, vers)
    print(val)
    # sum_ver = 0
    # for i in vers:
    #     sum_ver += i
    # print(sum_ver)


main()
