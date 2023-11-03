def read_parse():
    with open("./example") as f:
        input = f.read()
        init, seq = input.split("\n\n")
        seq = seq.splitlines()
        seq = list(map(lambda x: x.split(' -> '),seq))
        # print(init,seq)
        
        return init,seq

class Node:
    def __init__(self, data=None,next=None,is_new=False):
      self.data = data
      self.next = next
      self.is_new = is_new
    def __repr__(self):
        return self.data


class SLinkedList:
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(data=elem)
        node = node.next

  def __iter__(self):
      node = self.head
      while node is not None:
          yield node
          node = node.next
          if(node and node.is_new):
              node.is_new = False
              node = node.next
  def step(self,seq):
      for node in self:
          if(node.next):
            c_node_data = node.data
            n_node_data = node.next.data
            for s,c in seq:
                before,after = list(s)
                if(before == c_node_data and after == n_node_data):
                    new_node = Node(c,is_new=True)
                    new_node.next = node.next
                    node.next = new_node
                    


def main():
    # print('main')
    init,seq = read_parse()
    # first_node = Node("K")
    llist = SLinkedList(list(init))
    # p_node = llist.head
    # for c in init[1:]:
    #     c_node = Node(c)
    #     p_node.next = c_node
    #     p_node = c_node
        # c_node.next = Node(c)
    for i in range(40):
        print(i)
        llist.step(seq)
    # for node in llist:
    #     print(node)
    length = len(list(llist))
    print(length)


main()
