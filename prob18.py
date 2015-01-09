

class Tree:
    def __init__(self, data):
        self.tree = data
        self.height = len(data)
        self.nodelist = []

    def build_from_file(filename):
        l = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip("\n")
                l.append(map(int, line.split(" ")))
        return l

#    def node(self, level, position):
#        node = Node(level, position)

    def add_node(self, level, pos):
        self.nodelist.append((level, pos))

    def display(self):
        for n in self.nodelist:
            print(n)

class Node:
    tree = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    def __init__(self, level, position):
        self.level = level
        self.pos = position
        self.value = self.tree[level][position]
        self.l_value = self.tree[level + 1][position]
        self.r_value = self.tree[level + 1][position + 1]
        self.l_cost = self.value + self.l_value
        self.r_cost = self.value + self.r_value
        self.l = (self.level + 1, self.pos, self.l_cost)
        self.r = (self.level + 1, self.pos + 1, self.r_cost)




# nodes named nodelevel-pos
#   3
#  7 4
# 2 4 6
#8 5 9 3
#find best of the bottom two rows.
node = Node(2,0)
path = []
path.append((node.level, node.pos, node.value))
if node.l_cost > node.r_cost:
    path.append(node.l)
else:
    path.append(node.r)
print(path)




# breadth first traversal
#levelorder(root)
#  q = empty queue
#  q.enqueue(root)
#  while not q.empty do
#    node := q.dequeue()
#    visit(node)
#    if node.left ≠ null then
#      q.enqueue(node.left)
#    if node.right ≠ null then
#      q.enqueue(node.right)
