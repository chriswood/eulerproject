
class GridSearch:
    grid = []
    lproduct = 0

    def __init__(self, filename, search_size):
        '''
        read file into 2 dimension grid
        '''
        self.search_size = search_size
        with open(filename, 'r') as f:
            for row in f.readlines():
                line = row.rstrip('\n')
                line = line.split(' ')
                self.grid.append(map(int, line))
        f.closed
        self.x_range = len(self.grid[0])
        self.y_range = len(self.grid)

    def gprint(self):
        '''
        Display the grid lne by line
        '''
        for line in self.grid:
            print(line)

    def product(self, element_list):
        '''
        This takes four numbers and multiplies them.
        '''
        product = 1
        for item in element_list:
            product *= item
        return product

    def compare(self, sset):
        p = self.product(sset)
        self.lproduct = p if p > self.lproduct else self.lproduct

    def search_down(self, x, y):
        if (y + self.search_size) > self.y_range:
            return
        sset = []
        for n in range(y, y + self.search_size):
            sset.append(self.grid[n][x])
        print(sset)
        self.compare(sset)

    def search_diag(self, x, y):
        pass

# range 0, 19 end with 16
search = GridSearch('data11.txt', 4)
search.gprint()
for y in range(search.y_range):
    for x in range(search.x_range):
        search.search_down(x, y)
    

