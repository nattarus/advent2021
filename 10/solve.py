import math
def open_parse():
    with open('./input') as f:
        input = f.readlines()
        for l in input:
            print(l)
        return input

def reverse_and_sum(mem):
    value = {
            "(" : 1,
            "[":2,
            "{":3,
            "<":4
            }
    result = 0
    for c in mem[::-1]:
        val = value[c]
        print(value[c])
        result = (result * 5) + val
    return result



def check_err(str):
    expect = {
            "{":"}",
            "<":">",
            "(":")",
            "[":"]",
            }
    open = ["{","(","[","<"]
    close = ["}",")","]",">"]

    value = {
            ")":3,
            "]":57,
            "}":1197,
            ">":25137
            }
    mem = []
    for c in str:
        if(c in open):
            mem.append(c)
        if(c in close):
            latest = mem.pop()
            if(c != expect[latest]):
                # print(latest,c,value[c])
                # return value[c]
                return 0
                
    print(mem)
    cal = reverse_and_sum(mem)
    print(reverse_and_sum(mem))
    return cal
    # return mem
        
        


def main():
    input = open_parse()
    sum = 0
    final = []
    for l in input:
        temp = check_err(l)
        if(temp):
            final.append(temp)
    final.sort()
    fi_len = int(math.ceil(len(final) / 2))
    print(final[fi_len])



main()

