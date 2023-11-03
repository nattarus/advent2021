import re
def open_parse():
    with open('./input') as f:
        input = f.readlines()
        dis = []
        for i,l in enumerate(input) :
            # if(i % 2 == 1):
            # print(l)
            temp = l.strip().split(' ')
            dis.append(temp)
        return dis
            
        # input = re.split('\s\|\s',input)
        # return input
def diff(str1,str2):
    res = str1
    for s in str2 :
        res = res.replace(s,"")
    return res
def is_contain(str1,str2):
    is_con = True
    for s in str2:
        if s not in str1:
            is_con = False

    return is_con

def is_same(str1,str2):
    if(len(str1) != len(str2)):
        return False
    return is_contain(str1,str2)

        
def main():
    result = 0
    input = open_parse()
    # sum = 0
    len_dict = {
            "1" : 2,
            "2" : 5,
            "3" : 5,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 3,
            "8" : 7,
            "9" : 6,
            "0" : 6,
            }

    for l in input:
        val_map = {}
        # print(l[11:])
        for w in l:
            l_w = len(w)
            if(l_w == 2):
                val_map["1"] = w
            if(l_w == 4):
                val_map["4"] = w
            if(l_w == 3):
                val_map["7"] = w
            if(l_w == 7):
                val_map["8"] = w

        # val_map["a"] = diff(val_map["7"],val_map["1"])
        for w in l:
            l_w = len(w)
            if(l_w == 5):
                if(is_contain(w,val_map["1"])):
                    val_map["3"] = w
            if(l_w == 6):
                if(not is_contain(w,val_map["1"])):
                    val_map["6"] = w
                if(is_contain(w,val_map["4"])):
                    val_map["9"] = w

        for w in l:
            l_w = len(w)
            if(l_w == 5):
                if(is_contain(val_map["6"],w)):
                    val_map["5"] = w
                if(not is_contain(val_map["9"],w)):
                    val_map["2"] = w

            if(l_w == 6):
                if(not is_same(w ,val_map["6"]) and not is_same(w , val_map["9"])):
                    val_map["0"] = w

        
        sum = []
        print(l[11:])
        print(val_map)
        for num in l[11:]:
            for k in val_map:
                if(is_same(val_map[k] ,num)):
                    sum.append(k)
                    print(k,val_map[k])
        print(sum)
        result += int("".join(sum))





    print(result)




main()
