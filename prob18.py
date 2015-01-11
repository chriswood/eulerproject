#python3.4

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def spop(self):
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
        node.visit()

    def bottom(self, level):
        return(level == (len(data) - 1))

class Node:
    def __init__(self, nodedata): #(level, pos)
        self.level = nodedata[0]
        self.pos = nodedata[1]
        self.value = tree.tree[self.level][self.pos]
        self.visited = False
        if not tree.bottom(self.level):
            self.l = (self.level + 1, self.pos)
            self.r = (self.level + 1, self.pos + 1)
        else:
            self.l = None
            self.r = None

    def visit(self):
        self.visited = True

#   3
#  7 4
# 2 4 6
#8 5 9 3

data = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
tree = Tree(data)
root = Node((0, 0))
tree.visit(root)
s = Stack()
s.push(Node(root.l))
s.push(Node(root.r))
while not s.is_empty():
    node = s.spop()
    print(node.value)
    if node.l:
        lnode = Node(node.l)
        if not lnode.visited:
            tree.visit(lnode)
            s.push(lnode)
    if node.r:
        rnode = Node(node.r)
        if not rnode.visited:
            tree.visit(rnode)
            s.push(rnode)


#iterative DFS(Vertex v)
#    mark v visited
#    make an empty Stack S
#    push all vertices adjacent to v onto S
#    while S is not empty do
#        Vertex w is pop off S
#        for all Vertex u adjacent to w do
#            if u is not visited then
#                mark u visited
#                push u onto S



