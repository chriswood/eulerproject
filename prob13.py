# file handling
def read_file_to_list(filename):
    l = []
    with open(filename, 'r') as f:
	    for line in f:
	        l.append(long(line.strip('\n')))
    return l

nums = read_file_to_list('data13.txt')
print(sum(nums))


