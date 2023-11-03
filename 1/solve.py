with open('input') as f:
    lines = f.readlines()

    prev_depth = 999999900

    window_1 = lines[:-2]
    window_2 = lines[1:-1]
    window_3 = lines[2:]
    zip(lines,lines,lines)
    sum_windows = [int(a) + int(b) + int(c) for a ,b ,c in zip(window_1,window_2,window_3)]

    # print(sum_windows)
    
    count = 0
    for l in sum_windows:
        depth = int(l)
        if depth > prev_depth:
            count += 1
            pass
        prev_depth = depth
    print(count)


