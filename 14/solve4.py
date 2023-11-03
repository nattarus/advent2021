def read_parse():
    with open("./input") as f:
        input = f.read()
        init, seq = input.split("\n\n")
        seq = seq.splitlines()
        seq = list(map(lambda x: x.split(' -> '),seq))
        # print(init,seq)
        
        return init,seq
def main():
    init,seq = read_parse()
    dict = {}
    for c,n_c in zip(init[:-1],init[1:]):
        str = "".join([c,n_c])
        if(str in dict):
            dict[str] +=  1
        else:
            dict[str] = 1



    l_dict = {}
    for s in seq:
        patt,c = s
        before = "".join([patt[0],c])
        after = "".join([c,patt[1]])
        l_dict[patt] = [before,after]
    # print(dict)
    # for l in l_dict:
    #     print(l,l_dict[l])
    # print(l_dict)
    assert(len(l_dict)==len(seq))

    for _ in range(40):
        old_d = dict.copy()
        for k in l_dict:
            if(k in old_d ):
                count = old_d[k]
                vals = l_dict[k]
                # print(k,'dang',vals)
                for v in vals :
                    if v not in dict:
                        dict[v] = count
                    else:
                        dict[v] += count
                dict[k] -= count


    c_dict = {}
    sum = 0
    for k in dict:
        count = dict[k]
        for c in list(k):
            if c in c_dict:
                c_dict[c] += count
            else:
                c_dict[c] = count
        sum += count
    print(init,init[-1],init[0],sum)

    c_dict[init[0]] += 1
    c_dict[init[-1]] += 1

    for k in c_dict:
        c_dict[k] = c_dict[k] / 2
        # c_dict[k] = c_dict[k] 


    min = c_dict[init[0]]
    max = c_dict[init[0]]

    for k in c_dict:
        val = c_dict[k]
        if(val > max):
            max = val
        if(val < min):
            min = val
    # print(dict,sum)
    print('diff',max - min)
    print(max)
    print(min)
    print('sdf')
    # for k in dict:
    #     print(dict[k], k)


    print(c_dict,max,min)

                

main()
