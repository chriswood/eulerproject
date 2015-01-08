
# file handling
def read_file_to_list(filename):
    l = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip("\n")
            l.append(map(int, line.split(" ")))
    return l

pyr = read_file_to_list('data18.txt')
print(pyr)



