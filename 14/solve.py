def read_parse():
    with open("./input") as f:
        input = f.read()
        init, seq = input.split("\n\n")
        seq = seq.splitlines()
        seq = list(map(lambda x: x.split(' -> '),seq))
        # print(init,seq)
        
        return init,seq
def count(str):
    sum ={}
    for c in str:
        if(c not in sum):
            sum[c] = 1
        else:
            sum[c] += 1
    max = 0
    min = 99999
    for k in sum:
        if sum[k] > max :
            max = sum[k]
        if sum[k] < min :
            min = sum[k]
    print(max - min)

    return sum

def main():
    init,seq = read_parse()
    for loop in range(10):
        m_arr = []
        for s in seq:
            for i,c in enumerate(init):
                temp = init[i:i+2]
                if temp == s[0]:
                    m_arr.append((s[1],i))
                    

            # temp = re.findall(s[0],init)
            # if(temp):
            #     for m in temp:
            #         print(m)
            #         i = int(m.start())
            #         m_arr.append((s[1],i))
        m_arr.sort(key=lambda x: x[1])

        # print(m_arr,init)
        for j,pair in enumerate(m_arr) :
            c,i = pair
            idx = i + j + 1
            # if(idx < len(init)):
            init = init[:idx] + c + init[idx:]
            # else:
            #     init = init[:idx] + c + init[idx:]
            #     print('sdf')




        # print(loop+1,init,len(init))
    print(count(init))
main()
