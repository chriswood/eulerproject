

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes
# below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

# first get all primes less that a million....
from math import ceil, sqrt
import collections
from time import time

def is_prime(x):
    # check predefined values
    if x in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(x))

    for n in range(2, int(last_value) + 1):
        if (x%n == 0):
            return False
    return True

def rotate(n):
    d = collections.deque([c for c in str(n)])
    d.rotate(1)
    return int(''.join(d))

def check(p):
    if '0' in str(p):
        return False
    original = p
    p = rotate(p)
    while p != original:
        if p < limit:
            if p not in primes:
                return False
        else:
            if not is_prime(p):
                return False
        p = rotate(p)
    return True

t = time()
primes = []
circ_primes = set()
limit = 10**6
for i in range(2, limit):
    if is_prime(i):
        primes.append(i)

print("starting perms")
for p in primes:
    if check(p):
        print("found {0}".format(p))
        circ_primes.add(p)

print("time is {0}".format(time() - t))

print("********")

print(len(circ_primes))
