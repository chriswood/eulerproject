

# file handling
#def read_file_to_list(filename):
#    l = []
#    with open(filename, 'r') as f:
#        for line in f.readlines():
#            line = line.strip("\n")
#            l.append(map(int, line.split(" ")))
#    return l

#pyr = read_file_to_list('data18.txt')


class Tree:
    def __init__(self, data):
        self.tree = data
        self.height = len(data)

class Node:
    def __init__(self, level, position):
        self.level = level
        self.pos = position

test = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
tree = Tree(test)
print(tree.tree)

#   3
#  7 4
# 2 4 6
#8 5 9 3



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
