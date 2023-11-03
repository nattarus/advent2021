def read_parse():
    with open("./input") as f:
        input = map(int,f.read().strip().split(','))
        return list(input)

def main():
    input = read_parse()
    sum = 0
    result = 0
    print(input)
    
    for x in range(min(input),max(input)+1):
        temp = 0
        for n in input:
            diff = abs(x-n)
            diff_sum = (diff * (diff + 1)) /2
            # for d in range(1,diff+1):
            #     print(d)
            #     diff_sum += d

            temp += diff_sum
        if (sum == 0) :
            sum = temp
            result = x
        if(temp < sum):
            sum = temp
            result = x
    print("res",result)
    print("sum",sum)


main()
