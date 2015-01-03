
class GridSearch:
	grid = []

	def __init__(self, filename):
		'''
		read file into 2 dimension grid
		'''
		with open(filename, 'r') as f:
		    for row in f.readlines():
		        line = row.rstrip('\n')
		        line = line.split(' ')
		        self.grid.append(map(int, line))
		f.closed

	def product(self, element_list):
	    '''
	    This takes four numbers and multiplies them.
	    '''
	    product = 1
	    for item in element_list:
	        product *= item
	    return product

search = GridSearch('data11.txt')
print(search.grid)

# for each element
#     search up
# 	search down
# 	search diagonal
