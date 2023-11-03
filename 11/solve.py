def open_parse():
    with open("./input") as f:
        input = f.read().strip()
        res = []
        for l in input.split('\n'):
            temp = []
            for o in l:
                temp.append(int(o))
            res.append(temp)
    return res

def plus_flash(x,y,input,sum):
    len_y = len(input[0])
    len_x = len(input)
    if(x < 0 or x > len_x - 1) :
        return input,sum
    if(y < 0 or y > len_y - 1) :
        return input,sum
    if(input[x][y] != 0):
        input[x][y] += 1




def flash(x,y,input,sum):
    len_y = len(input[0])
    len_x = len(input)
    if(x < 0 or x > len_x - 1) :
        return input,sum
    if(y < 0 or y > len_y - 1) :
        return input,sum

    if (input[x][y] == 0):
        return input,sum

    if(input[x][y] > 9):
        input[x][y] = 0
        sum += 1
        plus_flash(x+1,y+1,input,sum)
        input,sum  = flash(x+1,y+1,input,sum)
        plus_flash(x-1,y+1,input,sum)
        input,sum  = flash(x-1,y+1,input,sum)
        plus_flash(x,y+1,input,sum)
        input,sum  = flash(x,y+1,input,sum)
        plus_flash(x+1,y,input,sum)
        input,sum  = flash(x+1,y,input,sum)
        plus_flash(x-1,y,input,sum)
        input,sum  = flash(x-1,y,input,sum)
        plus_flash(x,y-1,input,sum)
        input,sum  = flash(x,y-1,input,sum)
        plus_flash(x+1,y-1,input,sum)
        input,sum  = flash(x+1,y-1,input,sum)
        plus_flash(x-1,y-1,input,sum)
        input,sum  = flash(x-1,y-1,input,sum)
        print('flash')


    return input,sum
        


def main():
    input = open_parse()
    print(input[0][0])
    sum = 0
    for step in range(1000):
        for i,l in enumerate(input):
            for j,o in enumerate(l):
                input[i][j] += 1
        for i,l in enumerate(input):
            for j,o in enumerate(l):
                if(o > 9):
                    input,sum = flash(i,j,input,sum)
        sum_input = 0
        for l in input:
            for o in l:
                sum_input += o
        if(sum_input == 0):
            print('all',step)
            return step
    print(sum)


main()


