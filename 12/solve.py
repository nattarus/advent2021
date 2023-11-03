import time;
def open_parse():
    with open("./input") as f:
        input = f.read().strip()
        mem = {}
        for l in input.split('\n'):
            n1,n2 = l.split('-')
            if(n1 not in mem):
                mem[n1] = [n2]
            else:
                mem[n1].append(n2)
            if(n2 not in mem):
                mem[n2] = [n1]
            else:
                mem[n2].append(n1)
        return mem
def count_cave(mem,c):
    if( c not in mem):
        return False
    c = []
    for p in mem:
        if( p.islower() and p != 'start' and p != 'end'):
            if(p in c):
                # print('dang',p,'with',mem)
                return True
            else:
                c.append(p)
                # c[p] = 1
    # print('sdf',c)
    return False

def walk(c,input,mem,mem_list):
    # print('now',mem)
    # time.sleep(1)
    if(c == 'end'):
        mem.append('end')
        # print('to the end',mem_list)
        mem_list.append(mem[:])
        mem.pop()
        # print(mem)
        return mem_list,mem
    if(c.islower() and count_cave(mem,c) and c != 'start'):
        # print('to small cave again')
        # mem.pop()
        return mem_list,mem

    mem.append(c)
    # if(c in mem):
    #     return 
    
    ways = input[c]
    # print(ways)
    for w in ways:
        if(w != 'start'):
            mem_list,mem = walk(w,input,mem,mem_list)
    mem.pop()
        # print(ways)
        # print(mem)

    return mem_list,mem
    


def main():
    input = open_parse()
    # starts = input['start']
    # count = 0
    mem_list = []
    mem = []
    # print(input['HN'])
    mem_list,mem = walk('start',input,mem,mem_list)
    # for w in starts:
    #     mem = ['start',w]
    #     mem_list,mem = walk(w,input,mem,mem_list)
        # print(mem)
    # for l in mem_list:
    #     print(l)
    print(len(mem_list))
    

main()
