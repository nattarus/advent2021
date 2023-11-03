import time;
def open_parse():
    with open("./input") as f:
        input = f.read().strip()
        plot,fold = input.split('\n\n')
        rows, cols = (1600, 1600)
        arr = [[False for i in range(cols)] for j in range(rows)]

        for l in plot.split('\n'):
            x,y = l.strip().split(',')
            x = int(x)
            y = int(y)
            # print(x,y)
            arr[y][x] = True

        fold_arr = []

        for l in fold.split('\n'):
            direction = l[11]
            # print(direction,l[13:])
            fold_arr.append((direction,int(l[13:])))


        return arr,fold_arr
def count_dot(arr):
    sum = 0
    for x in arr:
        print(x)
        for y in x:
            if(y):
                sum += 1
    print(sum)
    return sum

def draw_dot(arr):
    # sum = 0
    for i,x in enumerate(arr):
        # print(x)
        for j,y in enumerate(x):
            if(y):
                arr[i][j] = 'x'
            else:
                arr[i][j] = ' '
    for x in arr:
        print(x)

                # sum += 1
    # print(sum)
    # return sum

def fold_y(arr,y):
    for i in range(y + 1):
        for j in range(len(arr[0])):
            arr[y - i][j] = arr[y - i][j] or arr[y + i][j]
    arr = arr[:y]

    # count_dot(arr)
    return arr

def fold_x(arr,x):
    # x = 5
    for i in range(x + 1):
        for j in range(len(arr)):
            arr[j][x - i] = arr[j][x + i] or arr[j][x - i]
    
    
    # arr = arr[:][:5]
    for l in range(len(arr)):
        arr[l] = arr[l][0:x]
    # print(arr)

    # count_dot(arr)
    return arr

    # for i,x in enumerate(arr):
    #     for j,y in enumerate(x):
    #         if( i < fold_y):
    #             
    #         fold_y 
    #         arr[i][j]


def main():
    input = open_parse()
    # input = fold_y(input,7)
    input = fold_x(input,7)
    count_dot(input)
    input = fold_y(input,5)
    count_dot(input)
    # print(input)

def main2():
    input,fold = open_parse()
    for l in fold:
        if(l[0] == 'x'):
            input = fold_x(input,l[1])
        if(l[0] == 'y'):
            input = fold_y(input,l[1])
            # print(l)
    # count_dot(input)
    draw_dot(input)
    # print(fold)
    # input = fold_y(input,655)



main2()

