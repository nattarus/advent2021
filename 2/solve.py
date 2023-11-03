with open('input2') as f:
    lines = f.readlines()
    # print(map(lambda x: x.strip(),lines))
    # print(int(lines[0].split(' ')[1]))
    pos = 0
    depth = 0
    aim = 0
    for l in lines:
        direction,value = l.split(' ')
        value = int(value)
        if(direction == 'forward'):
            pos += value
            depth += aim * value
        if(direction == 'up'):
            aim -= value
        if(direction == 'down'):
            aim += value

    print(pos*depth)
        
    

