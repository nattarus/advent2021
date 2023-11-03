def get_seq(x,y):
    start = (1,y+x-1)
    end = (start[1]-1,1)
    end_seq = get_sum(end[0])
    order = end_seq + x - 1
    return order

def get_sum(y):
    result = 0
    for x in range(y+1):
        result += x
    return result


def main(x,y):
    seed = 20151125
    for _ in range(get_seq(x,y)):
        seed = (seed * 252533) % 33554393
    print(seed)
        

# main(2981,3075)
main(3075,2981)
# main(3,4)
# print(get_sum(2000))

