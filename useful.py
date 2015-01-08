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

