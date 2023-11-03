with open("./input") as f:
    input = f.read()
    result = 0
    for i,s in enumerate(input):
        if(s =="("):
            result += 1
        if(s ==")"):
            result += -1 
        if(result == -1):
            print(i+1)
            print(result)

