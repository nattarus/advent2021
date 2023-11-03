with open('input3') as f:
    ori_lines = f.readlines()
    l = ori_lines[0]
    # for l in lines:
    #     print()

    bi_len = len(ori_lines[0].strip())

    lines = ori_lines

    for i in range(bi_len):
        one_count = 0
        zero_count = 0
        for l in lines:
            if(l[i] == "1") :
                one_count += 1
            if(l[i] == "0") :
                zero_count += 1
        
        if(one_count >= zero_count):
            # result.append(1)
            lines = list(filter(lambda x: x[i] == '1',lines))
        else:
            lines = list(filter(lambda x: x[i] == '0',lines))
            # result.append(0)
        # print(lines)
        if(len(lines) == 1):
            break
    print(lines)

    o2 = 0

    final = lines[0].strip()
# 
    for i,bin in enumerate(final):
        gamma_temp = int(bin) * (2 ** (bi_len - i - 1))
        o2 += gamma_temp
        # epp_temp = (1 - bin) * (2 ** (len_result - i - 1))
        # epp += epp_temp

    lines = ori_lines

    for i in range(bi_len):
        one_count = 0
        zero_count = 0
        for l in lines:
            if(l[i] == "1") :
                one_count += 1
            if(l[i] == "0") :
                zero_count += 1
        
        if(one_count >= zero_count):
            # result.append(1)
            lines = list(filter(lambda x: x[i] == '0',lines))
        else:
            lines = list(filter(lambda x: x[i] == '1',lines))
            # result.append(0)
        # print(lines)
        if(len(lines) == 1):
            break
    print(lines)

    co2 = 0

    final = lines[0].strip()
# 
    for i,bin in enumerate(final):
        gamma_temp = int(bin) * (2 ** (bi_len - i - 1))
        co2 += gamma_temp
        # epp_temp = (1 - bin) * (2 ** (len_result - i - 1))
        # epp += epp_temp

    print(o2,co2)
    print(o2*co2)
    




        
    
