def read_parse():
    with open("./input") as f:
        input = f.readlines()
        parse = []
        for l in input:
            temp = []
            for p in l.strip():
                temp.append(int(p))
            parse.append(temp)
        return parse
def is_lower(x,y,input ,val):
    input_x = len(input)
    input_y = len(input[0])
    if(x < 0 or x > input_x - 1):
        return True
    if(y < 0 or y > input_y - 1):
        return True
    if(val < input[x][y]):
        return True
    return False

def walk(x,y,input,prev):
    input_x = len(input)
    input_y = len(input[0])
    if(x < 0 or x > input_x - 1):
        return input
    if(y < 0 or y > input_y - 1):
        return input
    c_val = input[x][y]
    if(c_val == 9 ):
        return input
    if(prev > c_val):
        return input
    input[x][y] = -1
    input = walk(x+1,y,input,c_val)  
    input = walk(x-1,y,input,c_val)  
    input = walk(x,y+1,input,c_val)  
    input = walk(x,y-1,input,c_val)
    return input

def count(input):
    sum = 0
    for l in input:
        for p in l :
            if(p == -1):
                sum += 1
    return sum

def main():
    low_lo = []
    lowest = 0
    input = read_parse()
    for i,l in enumerate(input):
        for j,p in enumerate(l):
            # up = input[i-1][j-1]
            # down = input[i+1][j-1]
            # left = input[i-1][j+1]
            # right = input[i+1][j+1]
            if(is_lower(i,j+1,input,p) and is_lower(i,j-1,input,p) and
                    is_lower(i-1,j,input,p) and is_lower(i+1,j,input,p)):
                low_lo.append((i,j))
                print(i,j,p)
                lowest += p + 1
    prev_count = 0
    area = []
    for i,lo in enumerate(low_lo):
        clone_input = input[:]
        print(walk(lo[0],lo[1],clone_input,0))
        c = count(input)
        c_count = c - prev_count
        print(c_count)
        area.append(c_count)
        prev_count = c
    area.sort()
    print(area[-3::])
    result = 1
    for a in area[-3::]:
        result *= a
    print(result)








main()
    


