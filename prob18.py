#python3.4

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def show(self):
        print([x.value for x in self.items])

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return(len(self.items) == 0)

class Tree:
    def __init__(self, data):
        self.tree = data

    def visit(self, node):
        print("noode", node.value, sep=' ')


class Node:
    def __init__(self, nodedata): #(level, pos)
        self.level = nodedata[0]
        self.pos = nodedata[1]
        self.value = tree.tree[self.level][self.pos]
        try:
            self.l_value = tree.tree[self.level + 1][self.pos]
            self.r_value = tree.tree[self.level + 1][self.pos + 1]
            self.l = Node((self.level + 1, self.pos))
            self.r = Node((self.level + 1, self.pos + 1))
        except(IndexError):
            self.l = None
            self.r = None
#   3
#  7 4
# 2 4 6
#8 5 9 3

data = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
tree = Tree(data)
root = Node((0, 0))
q = Queue()
q.enqueue(root)
while not q.is_empty():
    q.show()
    node = q.dequeue()
    if node.l:
        q.enqueue(node.l)
    if node.r:
        q.enqueue(node.r)



