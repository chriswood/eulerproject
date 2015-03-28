from math import ceil, sqrt

def gen_is_pandigital(n, r):
    """ Generalized version of pandigital function.
        Still can't start with 0 """
    n = str(n)
    #return all(['0' not in n, len(n) == r, len(set(n)) == r])
    compa = "".join([str(i) for i in range(1, r + 1)]) #'1234'
    compb = "".join(sorted(n))
    return compa == compb

def is_prime(x):
    # check short values
    if x in (1,4):
        return False
    if x in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(x))

    for n in range(2, int(last_value) + 1):
        if (x%n == 0):
            return False
    return True

p = 0
limit = 987654321
sieve = filter(is_prime, range(11, limit))
highest = 0

while p <= limit:
    p = next(sieve)
    if gen_is_pandigital(p, len(str(p))):
        if p > highest:
            highest = p
            print("new highest pandigital prime: ", p)
