#python3.4

# file handling
def read_file_to_list(filename):
    l = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip("\n")
            l.append([int(x) for x in line.split(" ")])
        return l

class Tree:
    def __init__(self, data):
        self.tree = data
        self.length = len(data)
        self.high_cost = 0
        self.high_path = ''

    def visit(self, node):
        node.visit()

    def bottom(self, level):
        return(level == (len(data) - 1))

    def traverse(self, path):
        print("Path: ", path)
        clevel = 0
        cpos = 0
        cost = self.tree[clevel][cpos]
        for c in path:
            new_level = clevel + 1
            if c == '0':
                cost += self.tree[new_level][cpos]
            elif c == '1':
                new_pos = cpos + 1
                cost += self.tree[new_level][new_pos]
                cpos = new_pos
            clevel = new_level
        if cost > self.high_cost:
            self.high_cost = cost
            self.high_path = path
            
data = read_file_to_list('data18.txt')
print(data)
tree = Tree(data)
pathcount = pow(2, tree.length - 1)
for n in range(pathcount):
    path = bin(n) #binary string
    path = path[2:] #remove 'b' notation
    path = path.zfill(tree.length - 1)
    tree.traverse(path)
    if n >= pathcount:
        break
print("Cost: ", tree.high_cost)
print("Path: ", tree.high_path)


