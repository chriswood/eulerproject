import math
import itertools
import functools

def is_prime(N):
    '''
    Check a number N and see if it is divisible by anything less than
    its square root evenly.
    '''
    # check quick values
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = math.ceil(math.sqrt(N))

    for n in range(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

def get_pfactors(n):
    try:
        vals = set(functools.reduce(list.__add__,
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    except TypeError:
        vals = []
    return list(filter(is_prime, vals))


search = 4
found = False
consec = 0
number = 5000
while not found:
    print(number)
    pfactors = get_pfactors(number)

    if len(pfactors) == search:
        consec += 1
        if consec == search:
            print("found.")
            found = True
            for i in range(number, number - search, -1):
                print(i)
    else:
        consec = 0
    number += 1
