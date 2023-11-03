import re
def read_and_parse():
    with open("./input") as f :
        input = f.read()
        input = input.splitlines()
        input = map(lambda x : re.split(',|\s+->\s+',x),input)
        return list(input)

# print(read_and_parse())
def main():
    input = read_and_parse()
    rows, cols = (1000, 1000)
    # b = [[0]*cols]*rows
    b = [[0 for i in range(cols)] for j in range(rows)]
    # b[1][0] = 1
    # b[1][1] = 1
    # print(len(input))

    
    for l in input:
        x1 = int(l[0].strip())
        y1 = int(l[1].strip())
        x2 = int(l[2].strip())
        y2 = int(l[3].strip())


        print(x1,y1,x2,y2)
        if(x1 == x2):
            if(y1 < y2):
                for y in range(y1,y2+1) :
                    b[x1][y] += 1
            if(y1 > y2):
                for y in range(y2,y1+1) :
                    b[x1][y] = b[x1][y] + 1
        if(y1 == y2):
            if(x1 < x2):
                for x in range(x1,x2+1) :
                    b[x][y1] = b[x][y1] + 1
            if(x1 > x2):
                for x in range(x2,x1+1) :
                    b[x][y1] = b[x][y1] + 1
        if(x1-x2 == y1-y2):
            diff = x1 - x2
            if(diff > 0):
                for i in range(diff+1):
                    b[x2+i][y2+i] += 1
            else:
                for i in range(-diff+1):
                    b[x1+i][y1+i] += 1
        if(x1-x2 == -(y1-y2)):
            diff = x1 - x2
            if(diff > 0):
                for i in range(diff+1):
                    b[x2+i][y2-i] += 1
            else:
                for i in range(-diff+1):
                    b[x1+i][y1-i] += 1
                    
            


    sum = 0
    for row in b:
        for p in row:
            if(p > 1):
                sum = sum + 1
    # print(b)
    # print(range(12,40))
    print(sum)


main()

