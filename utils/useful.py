from math import hypot, sqrt, ceil, factorial

def is_pyth(sides):
    '''
    Tests for a 3-4-5 right triangle (Pythagorean triplet)
    '''
    return hypot(sides[0], sides[1]) == float(sides[2])

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def coprime(a, b):
    return gcd(a, b) == 1

def is_prime(N):
    '''
    Check a number N and see if it is divisible by anything less than
    it's square root evenly.
    '''
    # check predefined values
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(N))

    for n in xrange(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

# file handling
def read_file_to_string(filename):
    str_num = ''
    with open(filename, 'r') as f:
	    for line in f:
	        str_num += line
	    str_num = "".join(str_num.split('\n'))
    f.closed
    return str_num

def read_file_to_list(filename):
    l = []
    with open(filename, 'r') as f:
	    for line in f:
	        l.append(long(line.strip('\n')))
    return l

def product(l):
    '''Multiply numbers in a list'''
    p = 1
    for el in l:
        p *= el
    return p

def choose(a,b):
    '''implement choose notation'''
    return (factorial(a)/(factorial(b) * factorial(a - b)))

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
        self.length = len(data)
        self.high_cost = 0
        self.high_path = ''

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

import collections
def rotate(n):
    d = collections.deque([c for c in str(n)])
    d.rotate(1)
    return int(''.join(d))

def is_pandigital(n):
    """ can't start with 0 """
    n = str(n)
    return all(['0' not in n, len(n) == 9, len(set(n)) == 9])

def ccat(x, y, z):
    return ''.join([str(i) for i in [x,y,z]])
