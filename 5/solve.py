def read_file():
    with open('./input') as f:
        input =  f.read()
        return input


def main():
    input = read_file()
    # print(input)
    init_fishes = list(map(lambda x: int(x),input.split(',')))

    days = 256

    f_dict = {
            0:0,
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            }
    for f in init_fishes:
            f_dict[f] += 1

    print(f_dict)
    print(len(init_fishes))

    for _ in range(days):
        old_dict = dict(f_dict)
        f_dict[0] = old_dict[1]
        f_dict[1] = old_dict[2]
        f_dict[2] = old_dict[3]
        f_dict[3] = old_dict[4]
        f_dict[4] = old_dict[5]
        f_dict[5] = old_dict[6]
        f_dict[6] = old_dict[0] + old_dict[7]
        f_dict[7] = old_dict[8]
        f_dict[8] = old_dict[0]

    print(f_dict)
    sum = 0
    for i in f_dict:
        sum += f_dict[i]

    print(sum)



#     fishes = [8]
# 
#     for d in range(days):
#         print(d)
#         for i in range(len(fishes)) :
#             fishes[i] -= 1
#             if(fishes[i] < 0):
#                 fishes[i] = 6
#                 fishes.append(8)
#         print(len(fishes))
#             
# 
#     print(fishes)

main()

