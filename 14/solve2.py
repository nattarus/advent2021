def read_parse():
    with open("./example") as f:
        input = f.read()
        init, seq = input.split("\n\n")
        seq = seq.splitlines()
        seq = list(map(lambda x: x.split(' -> '),seq))
        # print(init,seq)
        
        return init,seq
class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next
    def get_next(self):
        return self.next
    def get_two_char(self):
        if(self.next):
            return self.val + self.next.val

class SLinkedList:
   def __init__(self):
      self.headval = None

def print_node(node):
    result = []
    while(node.next):
        # print(node.get_two_char())
        result.append(node.val)
        node = node.get_next()
        # print(node.val)
    # print(node.val)
    # print(node.get_two_char())
    result.append(node.val)

    # print("".join(result),len(result))
    print(len(result))
    # le

def insert_char(node,c):
    new_node = Node(c,node.next)
    node.next = new_node
    return new_node

def step(node,pair):
    c_node = node
    while(c_node.next):
        for p in pair:
            formular , char = p
            if(c_node.get_two_char() == formular ):
                c_node = insert_char(c_node,char)
                break
        c_node = c_node.next

    return node
        
def main():
    init,seq = read_parse()
    node = Node("X",None)
    prev_node = None
    for c in list(init)[::-1]:
        if(not prev_node):
            node = Node(c,None)
        else:
            node = Node(c,prev_node)
        prev_node = node
    for loop in range(40):
        print(loop)
        node = step(node,seq)
    print_node(node)

    # last = Node('N',None)


    # print_node(node)
main()
